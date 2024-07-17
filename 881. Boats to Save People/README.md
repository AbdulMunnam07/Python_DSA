# Minimum Number of Boats

## Problem Statement

You are given an array `people` where `people[i]` is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of `limit`. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most `limit`.

Return the minimum number of boats to carry every given person.

## Examples

### Example 1

**Input**: 
- `people = [1,2]`
- `limit = 3`

**Output**: 
- `1`

**Explanation**:
1 boat carrying the people with weights 1 and 2.

### Example 2

**Input**: 
- `people = [3,2,2,1]`
- `limit = 3`

**Output**: 
- `3`

**Explanation**:
3 boats:
- 1 boat carrying people with weights 1 and 2.
- 1 boat carrying the person with weight 2.
- 1 boat carrying the person with weight 3.

### Example 3

**Input**: 
- `people = [3,5,3,4]`
- `limit = 5`

**Output**: 
- `4`

**Explanation**:
4 boats, each carrying one person:
- 1 boat carrying the person with weight 3.
- 1 boat carrying the person with weight 5.
- 1 boat carrying the person with weight 3.
- 1 boat carrying the person with weight 4.

## Constraints

- `1 <= people.length <= 5 * 10^4`
- `1 <= people[i] <= limit <= 3 * 10^4`
