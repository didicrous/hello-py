import json
import math
from contextlib import redirect_stdout
from io import StringIO
from typing import Any, Callable, TypedDict

from anthropic import Anthropic
from anthropic.types import MessageParam, ToolUnionParam


class PythonExpressionToolResult(TypedDict):
    result: Any
    error: str | None


class SubmitAnswerToolResult(TypedDict):
    answer: Any
    submitted: bool


def python_expression_tool(expression: str) -> PythonExpressionToolResult:
    """
    Tool that evaluates Python expressions using eval.
    """
    try:
        # Make common modules available
        safe_globals = {
            "__builtins__": {},
            "math": math,
            "abs": abs,
            "min": min,
            "max": max,
            "sum": sum,
            "len": len,
            "range": range,
            "round": round,
            "int": int,
            "float": float,
            "str": str,
            "list": list,
            "dict": dict,
            "tuple": tuple,
            "set": set,
            "print": print,
        }
        stdout = StringIO()
        with redirect_stdout(stdout):
            exec(expression, safe_globals, {})
        return {"result": stdout.getvalue(), "error": None}
    except KeyboardInterrupt:
        raise
    except Exception as e:
        return {"result": None, "error": str(e)}


def submit_answer_tool(answer: Any) -> SubmitAnswerToolResult:
    """
    Tool for submitting the final answer.
    """
    return {"answer": answer, "submitted": True}


def run_agent_loop(
    prompt: str,
    tools: list[ToolUnionParam],
    tool_handlers: dict[str, Callable],
    max_steps: int = 5,
    model: str = "claude-3-5-haiku-latest",
    verbose: bool = True,
) -> Any | None:
    """
    Runs an agent loop with the given prompt and tools.

    Args:
        prompt: The initial prompt for the agent
        tools: List of tool definitions for Anthropic API
        tool_handlers: Dictionary mapping tool names to their handler functions
        max_steps: Maximum number of steps before stopping (default 5)
        model: The Anthropic model to use
        verbose: Whether to print detailed output (default True)

    Returns:
        The submitted answer if submit_answer was called, otherwise None
    """
    client = Anthropic()
    messages: list[MessageParam] = [{"role": "user", "content": prompt}]

    for step in range(max_steps):
        if verbose:
            print(f"\n=== Step {step + 1}/{max_steps} ===")

        response = client.messages.create(
            model=model, max_tokens=1000, tools=tools, messages=messages
        )

        # Track if we need to continue
        has_tool_use = False
        tool_results = []
        submitted_answer = None

        # Process the response
        for content in response.content:
            if content.type == "text":
                if verbose:
                    print(f"Assistant: {content.text}")
            elif content.type == "tool_use":
                has_tool_use = True
                tool_name = content.name

                if tool_name in tool_handlers:
                    if verbose:
                        print(f"Using tool: {tool_name}")

                    # Extract arguments based on tool
                    handler = tool_handlers[tool_name]
                    tool_input = content.input

                    # Call the appropriate tool handler
                    if tool_name == "python_expression":
                        assert (
                            isinstance(tool_input, dict) and "expression" in tool_input
                        )
                        if verbose:
                            print("\nInput:")
                            print("```")
                            for line in tool_input["expression"].split("\n"):
                                print(f"{line}")
                            print("```")
                        result = handler(tool_input["expression"])
                        if verbose:
                            print("\nOutput:")
                            print("```")
                            print(result)
                            print("```")
                    elif tool_name == "submit_answer":
                        assert isinstance(tool_input, dict) and "answer" in tool_input
                        result = handler(tool_input["answer"])
                        submitted_answer = result["answer"]
                    else:
                        # Generic handler call
                        result = (
                            handler(**tool_input)
                            if isinstance(tool_input, dict)
                            else handler(tool_input)
                        )

                    tool_results.append(
                        {
                            "type": "tool_result",
                            "tool_use_id": content.id,
                            "content": json.dumps(result),
                        }
                    )

        # If we have tool uses, add them to the conversation
        if has_tool_use:
            messages.append({"role": "assistant", "content": response.content})

            messages.append({"role": "user", "content": tool_results})

            # If an answer was submitted, return it
            if submitted_answer is not None:
                if verbose:
                    print(f"\nAgent submitted answer: {submitted_answer}")
                return submitted_answer
        else:
            # No tool use, conversation might be complete
            if verbose:
                print("\nNo tool use in response, ending loop.")
            break

    if verbose:
        print(f"\nReached maximum steps ({max_steps}) without submitting answer.")
    return None

# ==============================================================
# CUSTOM EVALUATION LOOP (Didi Crous)
# ==============================================================
def evaluate(prompt, expected_answer, tools, tool_handlers):
    
    # Run the test 30 times and track success rate
    num_runs = 30
    successes = 0

    print(f"Running {num_runs} test iterations...")
    print("=" * 60)

    for i in range(num_runs):
        print(f"\n\n{'=' * 20} RUN {i + 1}/{num_runs} {'=' * 20}")

        result = run_agent_loop(
            prompt=prompt,
            tools=tools,
            tool_handlers=tool_handlers,
            max_steps=7,
            verbose=False,  # Set to False for cleaner output during multiple runs
        )

    # Casting to a string here to normalize outputs (the model may return lists, strings, etc.).
    # In a production setting I would replace this with a dedicated grader function to 
    # handle output types more robustly. 

        if str(result) == expected_answer:
            print(f"✓ Run {i + 1}: SUCCESS - Got {result}")
            successes += 1
        else:
            print(f"✗ Run {i + 1}: FAILURE - Got {result}, expected {expected_answer}")

    # Calculate and display pass rate
    pass_rate = (successes / num_runs) * 100
    print(f"\n{'=' * 60}")
    print("Test Results:")
    print(f"  Passed: {successes}/{num_runs}")
    print(f"  Failed: {num_runs - successes}/{num_runs}")
    print(f"  Pass Rate: {pass_rate:.1f}%")
    print(f"{'=' * 60}")



def main():
    tools: list[ToolUnionParam] = [
        {
            "name": "python_expression",
            "description": "Evaluates a Python expression",
            "input_schema": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "Will be passed to exec(). Use print() to output something. Returns stdout. ",
                    }
                },
                "required": ["expression"],
            },
        },
        {
            "name": "submit_answer",
            "description": "Submit the final answer",
            "input_schema": {
                "type": "object",
                "properties": {"answer": {"description": "The final answer to submit"}},
                "required": ["answer"],
            },
        },
    ]

    tool_handlers = {
        "python_expression": python_expression_tool,
        "submit_answer": submit_answer_tool,
    }

    # Run the test 10 times and track success rate
    # num_runs = 10
    # expected_answer = 8769
    # successes = 0

    # print(f"Running {num_runs} test iterations...")
    # print("=" * 60)

    # for i in range(num_runs):
    #     print(f"\n\n{'=' * 20} RUN {i + 1}/{num_runs} {'=' * 20}")

    #     result = run_agent_loop(
    #         prompt="Calculate (2^10 + 3^5) * 7 - 100. Use the python_expression tool and then submit the answer.",
    #         tools=tools,
    #         tool_handlers=tool_handlers,
    #         max_steps=5,
    #         verbose=False,  # Set to False for cleaner output during multiple runs
    #     )

    #     if result == expected_answer:
    #         print(f"✓ Run {i + 1}: SUCCESS - Got {result}")
    #         successes += 1
    #     else:
    #         print(f"✗ Run {i + 1}: FAILURE - Got {result}, expected {expected_answer}")

    # # Calculate and display pass rate
    # pass_rate = (successes / num_runs) * 100
    # print(f"\n{'=' * 60}")
    # print("Test Results:")
    # print(f"  Passed: {successes}/{num_runs}")
    # print(f"  Failed: {num_runs - successes}/{num_runs}")
    # print(f"  Pass Rate: {pass_rate:.1f}%")
    # print(f"{'=' * 60}") 
    # End example code  

# ==============================================================
# BEGIN TAKE-HOME ASSIGNMENT SUBMISSION (Didi Crous)
# ==============================================================
    
    # The Rules section normalizes output upfront 
    print("Beginning of take home assignment submission:")

    prompt_1 = """Analyze the following restaurant review and determine whether the review should
                be classified as positive or negative. The result should be either "positive" or 
                "negative" and nothing else.
                
                Here is the review:
                "Finding the entrance of the restaurant felt nearly impossible so my party and I 
                arrived already frustrated. Then on top of that the service was slow so we were 
                cranky by the time we got it.
                
                I have to say though that the food quality was good and our waiter tried her best 
                so I'll give them a pass. If I'm in the area I'd go again..  Please fix your signage 
                though!! We were miserable when we arrived and it almost wasn't worth it!"
                """
    expected_answer = "positive"
    print("PROMPT 1")
    evaluate(prompt_1, expected_answer, tools, tool_handlers)    
    
    
    prompt_2 = """You will be given a list of phone numbers. 
                For each item in the list, determine if it is a valid U.S. phone number. 

                Rules:
                - Each result must be exactly one of: "valid" or "invalid". 
                - Valid separators are spaces, dashes (-), dots (.), or parentheses (() and ())).                
                - Do not return anything else.

                Example:
                Input: ["(123)456-7890", "1-800-GOT-JUNK", "123!456!7890"]
                Output: ["valid", "valid", "invalid"]

                Now classify this list:
                ["817,742,0078", "1-800-FLOWERS", "817*742*0078", "817-123-4567"]
               """
    expected_answer = "['invalid', 'valid', 'invalid', 'valid']"
    print("PROMPT 2")
    evaluate(prompt_2, expected_answer, tools, tool_handlers) 


    
    prompt_3 = """Evaluate the following series of expressions using the python_expression tool:

                1) Add two cubed and three raised to the power of four.
                2) Add the sum of the prime digits of the result to the result. Then add 1.
                3) If the result is greater than or equal to 90, halve it; otherwise subtract 5.
                4) Add one third of the result to itself. Round to the nearest integer (ties go up).
                5) Divide the result by 7, then round to the nearest integer (ties go up).

                After you finish, call the tool named submit_answer with only the final number. 
                """
    expected_answer = "9"
    print("PROMPT 3")
    evaluate(prompt_3, expected_answer, tools, tool_handlers)  


    prompt_4 = """You will be given a list of JSON objects. 
                For each item in the list, determine if the JSON is valid. 

                Rules:
                - Return only the list of results, in the same order as the input. 
                - Each result must be exactly one of: "valid" or "invalid". 
                - Do not return anything else.

                Example:
                Input: [{"id": 123, "active": true}, {"name": 'Jane',"age": 22}, {"id": 123, "active": true}]
                Output: ["valid", "invalid", "valid"]

                   Now classify this list:
                [
                    {"name": Bob, "age": 25},
                    {"name": "Jacob", "age": 65},                    
                    {'name': 'Carol', 'age': 30},
                    {"name": "Alice"; "age": 65}
                ]"""
    
    expected_answer = "['invalid', 'valid', 'invalid', 'invalid']"
    print("PROMPT 4")
    evaluate(prompt_4, expected_answer, tools, tool_handlers) 

   
    prompt_5 = """You will be given a list of strings containing food items.
                For each item in the list, determine the correct cuisine type. 

                Rules:
                - Return only the list of results, in the same order as the input. 
                - Each result must be exactly one of: "Thai", "Mexican", "Chinese",
                "South African", "American", "Dutch". 
                - Tex-Mex dishes should be classified as American, not Mexican.
                - Do not return anything else.

                Example:
                Input: ["Shrimp Pad Thai", "Grilled Cheese", "Quesadillas"]
                Output: ["Thai", "American", "Mexican"]

                Now classify this list:
                ["Pannekoeke (Afrikaans style)", "Fajitas", "Orange Chicken", "Stroopwafel", "Massaman Curry"]
                """
    
    expected_answer = "['South African', 'American', 'Chinese', 'Dutch', 'Thai']"
    print("PROMPT 5")
    evaluate(prompt_5, expected_answer, tools, tool_handlers)      

# ==============================================================
# END TAKE-HOME ASSIGNMENT SUBMISSION
# ==============================================================    

if __name__ == "__main__":
    main()
