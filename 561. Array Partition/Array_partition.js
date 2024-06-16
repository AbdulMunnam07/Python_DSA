/**
 * @param {number[]} nums
 * @return {number}
 */
var arrayPairSum = function(nums) {
    nums.sort();
    max = 0;

    for (let i = 0; i < nums.length; i += 2) {
        max += nums[i];
    }
    return max;
};