/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
var kidsWithCandies = function(candies, extraCandies) {
    let maxCan = Math.max(...candies);
    let res = Array(candies.length).fill(false);

    for(let i=0; i<candies.length; i++){
        if (candies[i] + extraCandies >= maxCan){
            res[i] = true
        }
    }
    return res
};