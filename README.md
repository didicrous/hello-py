
hello-py
===

Setup instructions:

1. Clone the repository:
   ```
   git clone https://github.com/preferencemodel/hello-py.git
   ```

2. Navigate to the project directory:
   ```
   cd hello-py
   ```

3. Set up `ANTHROPIC_API_KEY` environment variable:
   ```
   export ANTHROPIC_API_KEY=your_api_key_here
   ```

4. Run the agent:
   ```
   uv run main.py
   ```
==============================================================================

Each task was evaluated over the course of 30 runs because I quickly found that 
the variance among 10 runs to be rather high. Across all 30-run evaluations, **pass
rates consistently fell within the required 10-40% band**. 

It should be noted that in this implementation, I cast model outputs to strings 
before comparison. This keeps the evaluation loop simple, since the model may 
sometimes return different types. In a production setting, however, I would instead
implement a dedicated grader function to normalize and evaluate outputs more robustly.
For the purposes of this assessment, string normalization was sufficient and allowed me
to focus on task design.


A summary of the tasks and results can be found here: 

| **Task** | **Description**                 | **Expected Answer**                                         | **Pass Rate (30 runs)** |
| -------- | ------------------------------- | ----------------------------------------------------------- | ----------------------- |
| Task 1   | Review sentiment classification | `positive`                                                  | 30%                     |
| Task 2   | Phone number validity           | `['valid', 'valid', 'invalid']`                             | 26.7%                   |
| Task 3   | Multi-step math reasoning       | `"9"`                                                       | 16.7%                   |
| Task 4   | JSON validity classification    | `['invalid', 'valid', 'invalid', 'invalid']`                | 23.3%                   |
| Task 5   | Cuisine classification          | `['South African', 'American', 'Chinese', 'Dutch', 'Thai']` | 26.7%                  |



## Terminal Output:

```
didi@Didis-MacBook-Pro hello-py % uv run main.py
Beginning of take home assignment submission:
PROMPT 1
Running 30 test iterations...
=====================================================


==================== RUN 1/30 ====================
✗ Run 1: FAILURE - Got negative, expected positive


==================== RUN 2/30 ====================
✗ Run 2: FAILURE - Got negative, expected positive


==================== RUN 3/30 ====================
✓ Run 3: SUCCESS - Got positive


==================== RUN 4/30 ====================
✗ Run 4: FAILURE - Got negative, expected positive


==================== RUN 5/30 ====================
✗ Run 5: FAILURE - Got negative, expected positive


==================== RUN 6/30 ====================
✗ Run 6: FAILURE - Got negative, expected positive


==================== RUN 7/30 ====================
✗ Run 7: FAILURE - Got negative, expected positive


==================== RUN 8/30 ====================
✗ Run 8: FAILURE - Got negative, expected positive


==================== RUN 9/30 ====================
✗ Run 9: FAILURE - Got negative, expected positive


==================== RUN 10/30 ====================
✓ Run 10: SUCCESS - Got positive


==================== RUN 11/30 ====================
✗ Run 11: FAILURE - Got negative, expected positive


==================== RUN 12/30 ====================
✗ Run 12: FAILURE - Got negative, expected positive


==================== RUN 13/30 ====================
✗ Run 13: FAILURE - Got negative, expected positive


==================== RUN 14/30 ====================
✗ Run 14: FAILURE - Got negative, expected positive


==================== RUN 15/30 ====================
✗ Run 15: FAILURE - Got negative, expected positive


==================== RUN 16/30 ====================
✓ Run 16: SUCCESS - Got positive


==================== RUN 17/30 ====================
✗ Run 17: FAILURE - Got negative, expected positive


==================== RUN 18/30 ====================
✗ Run 18: FAILURE - Got negative, expected positive


==================== RUN 19/30 ====================
✓ Run 19: SUCCESS - Got positive


==================== RUN 20/30 ====================
✓ Run 20: SUCCESS - Got positive


==================== RUN 21/30 ====================
✗ Run 21: FAILURE - Got negative, expected positive


==================== RUN 22/30 ====================
✓ Run 22: SUCCESS - Got positive


==================== RUN 23/30 ====================
✓ Run 23: SUCCESS - Got positive


==================== RUN 24/30 ====================
✗ Run 24: FAILURE - Got negative, expected positive


==================== RUN 25/30 ====================
✗ Run 25: FAILURE - Got negative, expected positive


==================== RUN 26/30 ====================
✓ Run 26: SUCCESS - Got positive


==================== RUN 27/30 ====================
✗ Run 27: FAILURE - Got negative, expected positive


==================== RUN 28/30 ====================
✗ Run 28: FAILURE - Got negative, expected positive


==================== RUN 29/30 ====================
✓ Run 29: SUCCESS - Got positive


==================== RUN 30/30 ====================
✗ Run 30: FAILURE - Got negative, expected positive

============================================================
Test Results:
  Passed: 9/30
  Failed: 21/30
  Pass Rate: 30.0%
============================================================
PROMPT 2
Running 30 test iterations...
============================================================


==================== RUN 1/30 ====================
✗ Run 1: FAILURE - Got ['invalid', 'invalid', 'invalid', 'valid'], expected ['invalid', 'valid', 'invalid', 'valid']


==================== RUN 2/30 ====================
✓ Run 2: SUCCESS - Got ['invalid', 'valid', 'invalid', 'valid']


==================== RUN 3/30 ====================
✗ Run 3: FAILURE - Got ['invalid', 'invalid', 'invalid', 'valid'], expected ['invalid', 'valid', 'invalid', 'valid']


==================== RUN 4/30 ====================
✓ Run 4: SUCCESS - Got ['invalid', 'valid', 'invalid', 'valid']


==================== RUN 5/30 ====================
✗ Run 5: FAILURE - Got ['invalid', 'invalid', 'invalid', 'valid'], expected ['invalid', 'valid', 'invalid', 'valid']


==================== RUN 6/30 ====================
✓ Run 6: SUCCESS - Got ['invalid', 'valid', 'invalid', 'valid']


==================== RUN 7/30 ====================
✗ Run 7: FAILURE - Got ['invalid', 'invalid', 'invalid', 'valid'], expected ['invalid', 'valid', 'invalid', 'valid']


==================== RUN 8/30 ====================
✓ Run 8: SUCCESS - Got ['invalid', 'valid', 'invalid', 'valid']


==================== RUN 9/30 ====================
✗ Run 9: FAILURE - Got ['valid', 'valid', 'invalid', 'valid'], expected ['invalid', 'valid', 'invalid', 'valid']


==================== RUN 10/30 ====================
✓ Run 10: SUCCESS - Got ['invalid', 'valid', 'invalid', 'valid']


==================== RUN 11/30 ====================
✗ Run 11: FAILURE - Got ['valid', 'valid', 'invalid', 'valid'], expected ['invalid', 'valid', 'invalid', 'valid']


==================== RUN 12/30 ====================
✗ Run 12: FAILURE - Got ['invalid', 'invalid', 'invalid', 'valid'], expected ['invalid', 'valid', 'invalid', 'valid']


==================== RUN 13/30 ====================
✗ Run 13: FAILURE - Got ['invalid', 'invalid', 'invalid', 'valid'], expected ['invalid', 'valid', 'invalid', 'valid']


==================== RUN 14/30 ====================
✗ Run 14: FAILURE - Got ['valid', 'valid', 'valid', 'valid'], expected ['invalid', 'valid', 'invalid', 'valid']


==================== RUN 15/30 ====================
✗ Run 15: FAILURE - Got ['valid', 'valid', 'invalid', 'valid'], expected ['invalid', 'valid', 'invalid', 'valid']


==================== RUN 16/30 ====================
✓ Run 16: SUCCESS - Got ['invalid', 'valid', 'invalid', 'valid']


==================== RUN 17/30 ====================
✓ Run 17: SUCCESS - Got ['invalid', 'valid', 'invalid', 'valid']


==================== RUN 18/30 ====================
✓ Run 18: SUCCESS - Got ['invalid', 'valid', 'invalid', 'valid']


==================== RUN 19/30 ====================
✗ Run 19: FAILURE - Got ['invalid', 'invalid', 'invalid', 'valid'], expected ['invalid', 'valid', 'invalid', 'valid']


==================== RUN 20/30 ====================
✗ Run 20: FAILURE - Got ['valid', 'invalid', 'valid', 'valid'], expected ['invalid', 'valid', 'invalid', 'valid']


==================== RUN 21/30 ====================
✗ Run 21: FAILURE - Got ['invalid', 'invalid', 'invalid', 'valid'], expected ['invalid', 'valid', 'invalid', 'valid']


==================== RUN 22/30 ====================
✗ Run 22: FAILURE - Got ['valid', 'valid', 'valid', 'valid'], expected ['invalid', 'valid', 'invalid', 'valid']


==================== RUN 23/30 ====================
✗ Run 23: FAILURE - Got ['valid', 'invalid', 'valid', 'valid'], expected ['invalid', 'valid', 'invalid', 'valid']


==================== RUN 24/30 ====================
✗ Run 24: FAILURE - Got ['invalid', 'valid', 'invalid', 'invalid'], expected ['invalid', 'valid', 'invalid', 'valid']


==================== RUN 25/30 ====================
✗ Run 25: FAILURE - Got ['valid', 'valid', 'valid', 'valid'], expected ['invalid', 'valid', 'invalid', 'valid']


==================== RUN 26/30 ====================
✗ Run 26: FAILURE - Got ['invalid', 'invalid', 'invalid', 'valid'], expected ['invalid', 'valid', 'invalid', 'valid']


==================== RUN 27/30 ====================
✗ Run 27: FAILURE - Got ['valid', 'invalid', 'valid', 'valid'], expected ['invalid', 'valid', 'invalid', 'valid']


==================== RUN 28/30 ====================
✗ Run 28: FAILURE - Got ['valid', 'valid', 'valid', 'valid'], expected ['invalid', 'valid', 'invalid', 'valid']


==================== RUN 29/30 ====================
✗ Run 29: FAILURE - Got ['invalid', 'invalid', 'invalid', 'valid'], expected ['invalid', 'valid', 'invalid', 'valid']


==================== RUN 30/30 ====================
✗ Run 30: FAILURE - Got ['invalid', 'invalid', 'invalid', 'valid'], expected ['invalid', 'valid', 'invalid', 'valid']

============================================================
Test Results:
  Passed: 8/30
  Failed: 22/30
  Pass Rate: 26.7%
============================================================
PROMPT 3
Running 30 test iterations...
============================================================


==================== RUN 1/30 ====================
✗ Run 1: FAILURE - Got None, expected 9


==================== RUN 2/30 ====================
✗ Run 2: FAILURE - Got None, expected 9


==================== RUN 3/30 ====================
✗ Run 3: FAILURE - Got 11, expected 9


==================== RUN 4/30 ====================
✗ Run 4: FAILURE - Got None, expected 9


==================== RUN 5/30 ====================
✗ Run 5: FAILURE - Got 10, expected 9


==================== RUN 6/30 ====================
✗ Run 6: FAILURE - Got None, expected 9


==================== RUN 7/30 ====================
✗ Run 7: FAILURE - Got None, expected 9


==================== RUN 8/30 ====================
✗ Run 8: FAILURE - Got 16, expected 9


==================== RUN 9/30 ====================
✗ Run 9: FAILURE - Got 10, expected 9


==================== RUN 10/30 ====================
✗ Run 10: FAILURE - Got 10, expected 9


==================== RUN 11/30 ====================
✗ Run 11: FAILURE - Got 16, expected 9


==================== RUN 12/30 ====================
✗ Run 12: FAILURE - Got 10, expected 9


==================== RUN 13/30 ====================
✓ Run 13: SUCCESS - Got 9


==================== RUN 14/30 ====================
✗ Run 14: FAILURE - Got 10, expected 9


==================== RUN 15/30 ====================
✗ Run 15: FAILURE - Got 11, expected 9


==================== RUN 16/30 ====================
✗ Run 16: FAILURE - Got None, expected 9


==================== RUN 17/30 ====================
✗ Run 17: FAILURE - Got 10, expected 9


==================== RUN 18/30 ====================
✗ Run 18: FAILURE - Got 10, expected 9


==================== RUN 19/30 ====================
✗ Run 19: FAILURE - Got 4, expected 9


==================== RUN 20/30 ====================
✗ Run 20: FAILURE - Got 10, expected 9


==================== RUN 21/30 ====================
✓ Run 21: SUCCESS - Got 9


==================== RUN 22/30 ====================
✓ Run 22: SUCCESS - Got 9


==================== RUN 23/30 ====================
✗ Run 23: FAILURE - Got None, expected 9


==================== RUN 24/30 ====================
✗ Run 24: FAILURE - Got 10, expected 9


==================== RUN 25/30 ====================
✓ Run 25: SUCCESS - Got 9


==================== RUN 26/30 ====================
✗ Run 26: FAILURE - Got 10, expected 9


==================== RUN 27/30 ====================
✓ Run 27: SUCCESS - Got 9


==================== RUN 28/30 ====================
✗ Run 28: FAILURE - Got 10, expected 9


==================== RUN 29/30 ====================
✗ Run 29: FAILURE - Got 10, expected 9


==================== RUN 30/30 ====================
✗ Run 30: FAILURE - Got 10, expected 9

============================================================
Test Results:
  Passed: 5/30
  Failed: 25/30
  Pass Rate: 16.7%
============================================================
PROMPT 4
Running 30 test iterations...
============================================================


==================== RUN 1/30 ====================
✗ Run 1: FAILURE - Got ['valid', 'valid', 'invalid', 'valid'], expected ['invalid', 'valid', 'invalid', 'invalid']


==================== RUN 2/30 ====================
✗ Run 2: FAILURE - Got ['invalid', 'valid', 'valid', 'invalid'], expected ['invalid', 'valid', 'invalid', 'invalid']


==================== RUN 3/30 ====================
✗ Run 3: FAILURE - Got ['invalid', 'valid', 'valid', 'invalid'], expected ['invalid', 'valid', 'invalid', 'invalid']


==================== RUN 4/30 ====================
✓ Run 4: SUCCESS - Got ['invalid', 'valid', 'invalid', 'invalid']


==================== RUN 5/30 ====================
✗ Run 5: FAILURE - Got ['invalid', 'valid', 'valid', 'invalid'], expected ['invalid', 'valid', 'invalid', 'invalid']


==================== RUN 6/30 ====================
✗ Run 6: FAILURE - Got ['invalid', 'valid', 'valid', 'invalid'], expected ['invalid', 'valid', 'invalid', 'invalid']


==================== RUN 7/30 ====================
✗ Run 7: FAILURE - Got ['invalid', 'valid', 'valid', 'invalid'], expected ['invalid', 'valid', 'invalid', 'invalid']


==================== RUN 8/30 ====================
✗ Run 8: FAILURE - Got ['invalid', 'valid', 'valid', 'invalid'], expected ['invalid', 'valid', 'invalid', 'invalid']


==================== RUN 9/30 ====================
✓ Run 9: SUCCESS - Got ['invalid', 'valid', 'invalid', 'invalid']


==================== RUN 10/30 ====================
✗ Run 10: FAILURE - Got ['invalid', 'invalid', 'invalid', 'invalid'], expected ['invalid', 'valid', 'invalid', 'invalid']


==================== RUN 11/30 ====================
✗ Run 11: FAILURE - Got ['invalid', 'valid', 'valid', 'invalid'], expected ['invalid', 'valid', 'invalid', 'invalid']


==================== RUN 12/30 ====================
✓ Run 12: SUCCESS - Got ['invalid', 'valid', 'invalid', 'invalid']


==================== RUN 13/30 ====================
✗ Run 13: FAILURE - Got ['invalid', 'invalid', 'invalid', 'invalid'], expected ['invalid', 'valid', 'invalid', 'invalid']


==================== RUN 14/30 ====================
✗ Run 14: FAILURE - Got ['invalid', 'valid', 'invalid', 'valid'], expected ['invalid', 'valid', 'invalid', 'invalid']


==================== RUN 15/30 ====================
✓ Run 15: SUCCESS - Got ['invalid', 'valid', 'invalid', 'invalid']


==================== RUN 16/30 ====================
✗ Run 16: FAILURE - Got ['invalid', 'valid', 'valid', 'invalid'], expected ['invalid', 'valid', 'invalid', 'invalid']


==================== RUN 17/30 ====================
✗ Run 17: FAILURE - Got ['invalid', 'invalid', 'invalid', 'invalid'], expected ['invalid', 'valid', 'invalid', 'invalid']


==================== RUN 18/30 ====================
✓ Run 18: SUCCESS - Got ['invalid', 'valid', 'invalid', 'invalid']


==================== RUN 19/30 ====================
✗ Run 19: FAILURE - Got ['invalid', 'valid', 'valid', 'invalid'], expected ['invalid', 'valid', 'invalid', 'invalid']


==================== RUN 20/30 ====================
✗ Run 20: FAILURE - Got ['invalid', 'invalid', 'invalid', 'invalid'], expected ['invalid', 'valid', 'invalid', 'invalid']


==================== RUN 21/30 ====================
✓ Run 21: SUCCESS - Got ['invalid', 'valid', 'invalid', 'invalid']


==================== RUN 22/30 ====================
✗ Run 22: FAILURE - Got ['invalid', 'invalid', 'invalid', 'invalid'], expected ['invalid', 'valid', 'invalid', 'invalid']


==================== RUN 23/30 ====================
✗ Run 23: FAILURE - Got ['invalid', 'valid', 'valid', 'invalid'], expected ['invalid', 'valid', 'invalid', 'invalid']


==================== RUN 24/30 ====================
✓ Run 24: SUCCESS - Got ['invalid', 'valid', 'invalid', 'invalid']


==================== RUN 25/30 ====================
✗ Run 25: FAILURE - Got ['invalid', 'invalid', 'invalid', 'invalid'], expected ['invalid', 'valid', 'invalid', 'invalid']


==================== RUN 26/30 ====================
✗ Run 26: FAILURE - Got ['invalid', 'valid', 'valid', 'invalid'], expected ['invalid', 'valid', 'invalid', 'invalid']


==================== RUN 27/30 ====================
✗ Run 27: FAILURE - Got ['invalid', 'valid', 'valid', 'invalid'], expected ['invalid', 'valid', 'invalid', 'invalid']


==================== RUN 28/30 ====================
✗ Run 28: FAILURE - Got ['valid', 'valid', 'valid', 'valid'], expected ['invalid', 'valid', 'invalid', 'invalid']


==================== RUN 29/30 ====================
✗ Run 29: FAILURE - Got ['invalid', 'valid', 'valid', 'invalid'], expected ['invalid', 'valid', 'invalid', 'invalid']


==================== RUN 30/30 ====================
✗ Run 30: FAILURE - Got ['invalid', 'valid', 'valid', 'invalid'], expected ['invalid', 'valid', 'invalid', 'invalid']

============================================================
Test Results:
  Passed: 7/30
  Failed: 23/30
  Pass Rate: 23.3%
============================================================
PROMPT 5
Running 30 test iterations...
============================================================


==================== RUN 1/30 ====================
✗ Run 1: FAILURE - Got ['Dutch', 'American', 'Chinese', 'Dutch', 'Thai'], expected ['South African', 'American', 'Chinese', 'Dutch', 'Thai']


==================== RUN 2/30 ====================
✓ Run 2: SUCCESS - Got ['South African', 'American', 'Chinese', 'Dutch', 'Thai']


==================== RUN 3/30 ====================
✗ Run 3: FAILURE - Got ['Dutch', 'American', 'Chinese', 'Dutch', 'Thai'], expected ['South African', 'American', 'Chinese', 'Dutch', 'Thai']


==================== RUN 4/30 ====================
✗ Run 4: FAILURE - Got ['Dutch', 'American', 'Chinese', 'Dutch', 'Thai'], expected ['South African', 'American', 'Chinese', 'Dutch', 'Thai']


==================== RUN 5/30 ====================
✗ Run 5: FAILURE - Got ['Dutch', 'American', 'Chinese', 'Dutch', 'Thai'], expected ['South African', 'American', 'Chinese', 'Dutch', 'Thai']


==================== RUN 6/30 ====================
✓ Run 6: SUCCESS - Got ['South African', 'American', 'Chinese', 'Dutch', 'Thai']


==================== RUN 7/30 ====================
✗ Run 7: FAILURE - Got ['Dutch', 'American', 'Chinese', 'Dutch', 'Thai'], expected ['South African', 'American', 'Chinese', 'Dutch', 'Thai']


==================== RUN 8/30 ====================
✗ Run 8: FAILURE - Got ['Dutch', 'American', 'Chinese', 'Dutch', 'Thai'], expected ['South African', 'American', 'Chinese', 'Dutch', 'Thai']


==================== RUN 9/30 ====================
✗ Run 9: FAILURE - Got ['Dutch', 'Mexican', 'Chinese', 'Dutch', 'Thai'], expected ['South African', 'American', 'Chinese', 'Dutch', 'Thai']


==================== RUN 10/30 ====================
✗ Run 10: FAILURE - Got ['Dutch', 'Mexican', 'Chinese', 'Dutch', 'Thai'], expected ['South African', 'American', 'Chinese', 'Dutch', 'Thai']


==================== RUN 11/30 ====================
✗ Run 11: FAILURE - Got ['Dutch', 'American', 'Chinese', 'Dutch', 'Thai'], expected ['South African', 'American', 'Chinese', 'Dutch', 'Thai']


==================== RUN 12/30 ====================
✗ Run 12: FAILURE - Got ['Dutch', 'American', 'Chinese', 'Dutch', 'Thai'], expected ['South African', 'American', 'Chinese', 'Dutch', 'Thai']


==================== RUN 13/30 ====================
✗ Run 13: FAILURE - Got ['Dutch', 'American', 'Chinese', 'Dutch', 'Thai'], expected ['South African', 'American', 'Chinese', 'Dutch', 'Thai']


==================== RUN 14/30 ====================
✗ Run 14: FAILURE - Got ['Dutch', 'American', 'Chinese', 'Dutch', 'Thai'], expected ['South African', 'American', 'Chinese', 'Dutch', 'Thai']


==================== RUN 15/30 ====================
✗ Run 15: FAILURE - Got ['South African', 'Mexican', 'Chinese', 'Dutch', 'Thai'], expected ['South African', 'American', 'Chinese', 'Dutch', 'Thai']


==================== RUN 16/30 ====================
✓ Run 16: SUCCESS - Got ['South African', 'American', 'Chinese', 'Dutch', 'Thai']


==================== RUN 17/30 ====================
✓ Run 17: SUCCESS - Got ['South African', 'American', 'Chinese', 'Dutch', 'Thai']


==================== RUN 18/30 ====================
✓ Run 18: SUCCESS - Got ['South African', 'American', 'Chinese', 'Dutch', 'Thai']


==================== RUN 19/30 ====================
✗ Run 19: FAILURE - Got ['Dutch', 'American', 'Chinese', 'Dutch', 'Thai'], expected ['South African', 'American', 'Chinese', 'Dutch', 'Thai']


==================== RUN 20/30 ====================
✓ Run 20: SUCCESS - Got ['South African', 'American', 'Chinese', 'Dutch', 'Thai']


==================== RUN 21/30 ====================
✗ Run 21: FAILURE - Got ['South African', 'Mexican', 'Chinese', 'Dutch', 'Thai'], expected ['South African', 'American', 'Chinese', 'Dutch', 'Thai']


==================== RUN 22/30 ====================
✗ Run 22: FAILURE - Got ['Dutch', 'Mexican', 'Chinese', 'Dutch', 'Thai'], expected ['South African', 'American', 'Chinese', 'Dutch', 'Thai']


==================== RUN 23/30 ====================
✗ Run 23: FAILURE - Got ['Dutch', 'American', 'Chinese', 'Dutch', 'Thai'], expected ['South African', 'American', 'Chinese', 'Dutch', 'Thai']


==================== RUN 24/30 ====================
✗ Run 24: FAILURE - Got ['South African', 'Mexican', 'Chinese', 'Dutch', 'Thai'], expected ['South African', 'American', 'Chinese', 'Dutch', 'Thai']


==================== RUN 25/30 ====================
✗ Run 25: FAILURE - Got ['South African', 'Mexican', 'Chinese', 'Dutch', 'Thai'], expected ['South African', 'American', 'Chinese', 'Dutch', 'Thai']


==================== RUN 26/30 ====================
✗ Run 26: FAILURE - Got ['Dutch', 'Mexican', 'Chinese', 'Dutch', 'Thai'], expected ['South African', 'American', 'Chinese', 'Dutch', 'Thai']


==================== RUN 27/30 ====================
✓ Run 27: SUCCESS - Got ['South African', 'American', 'Chinese', 'Dutch', 'Thai']


==================== RUN 28/30 ====================
✗ Run 28: FAILURE - Got ['Dutch', 'American', 'Chinese', 'Dutch', 'Thai'], expected ['South African', 'American', 'Chinese', 'Dutch', 'Thai']


==================== RUN 29/30 ====================
✗ Run 29: FAILURE - Got ['Dutch', 'American', 'Chinese', 'Dutch', 'Thai'], expected ['South African', 'American', 'Chinese', 'Dutch', 'Thai']


==================== RUN 30/30 ====================
✓ Run 30: SUCCESS - Got ['South African', 'American', 'Chinese', 'Dutch', 'Thai']

============================================================
Test Results:
  Passed: 8/30
  Failed: 22/30
  Pass Rate: 26.7%
============================================================
