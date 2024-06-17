/**
 * @param {number[]} candyType
 * @return {number}
 */
var distributeCandies = function(candyType) {
    let unique_num = new Set(candyType)
    let max_num = candyType.length;
    let final = max_num / 2;
    return Math.min(unique_num.size, final)
};