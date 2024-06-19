# Count Good Pairs

## Problem Description

Given an array of integers `nums`, return the number of good pairs.

A pair `(i, j)` is called good if `nums[i] == nums[j]` and `i < j`.

### Examples

**Example 1:**

Input: nums = [1,2,3,1,1,3] <br>
Output: 4 <br>
Explanation: There are 4 good pairs: (0,3), (0,4), (3,4), (2,5) (0-indexed).



**Example 2:**

Input: nums = [1,1,1,1] <br> 
Output: 6 <br>
Explanation: Each pair in the array is good.



### Constraints

- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 100`


