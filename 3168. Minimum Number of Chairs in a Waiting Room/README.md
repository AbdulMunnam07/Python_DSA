# Minimum Number of Chairs Needed

## Problem Description

You are given a string `s`. Simulate events at each second `i`:

- If `s[i] == 'E'`, a person enters the waiting room and takes one of the chairs in it.
- If `s[i] == 'L'`, a person leaves the waiting room, freeing up a chair.

Return the minimum number of chairs needed so that a chair is available for every person who enters the waiting room given that it is initially empty.

### Examples

**Example 1:**

Input: s = "EEEEEEE" <br>
Output: 7 <br>
Explanation: After each second, a person enters the waiting room and no person leaves it. Therefore, a minimum of 7 chairs is needed.


### Constraints

- The string `s` consists only of characters 'E' and 'L'.
- The length of `s` is between 1 and `10^5`.
