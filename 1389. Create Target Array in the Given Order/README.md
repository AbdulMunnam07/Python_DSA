# Create Target Array in the Given Order

## Problem Description

Given two arrays of integers `nums` and `index`, your task is to create a `target` array under the following rules:

1. Initially, the `target` array is empty.
2. From left to right, read `nums[i]` and `index[i]`, then insert the value `nums[i]` at the position `index[i]` in the `target` array.
3. Repeat the previous step until there are no elements to read in `nums` and `index`.
4. Return the `target` array.

It is guaranteed that the insertion operations will be valid.

### Examples

**Example 1:**

Input: nums = [0,1,2,3,4], index = [0,1,2,2,1] <br>
Output: [0,4,1,3,2] <br>
Explanation:
nums index target <br>
0 0 [0] <br>
1 1 [0,1] <br>
2 2 [0,1,2] <br>
3 2 [0,1,3,2] <br>
4 1 [0,4,1,3,2]


**Example 2:**

Input: nums = [1], index = [0] <br>
Output: [1]

### Constraints

- `1 <= nums.length, index.length <= 100`
- `nums.length == index.length`
- `0 <= nums[i] <= 100`
- `0 <= index[i] <= i`

