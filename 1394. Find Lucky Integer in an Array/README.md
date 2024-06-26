# Largest Lucky Integer

## Problem Description

Given an array of integers `arr`, a lucky integer is an integer that has a frequency in the array equal to its value.

Return the largest lucky integer in the array. If there is no lucky integer, return -1.

### Examples

**Example 1:**

Input: arr = [2,2,3,4] <br>
Output: 2 <br>
Explanation: The only lucky number in the array is 2 because frequency[2] == 2.

**Example 2:**

Input: arr = [1,2,2,3,3,3] <br>
Output: 3 <br>
Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.

**Example 3:**

Input: arr = [2,2,2,3,3] <br>
Output: -1 <br>
Explanation: There are no lucky numbers in the array.

### Constraints

- 1 <= arr.length <= 500
- 1 <= arr[i] <= 500