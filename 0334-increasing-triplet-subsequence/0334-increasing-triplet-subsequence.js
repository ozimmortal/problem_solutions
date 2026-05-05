/**
 * @param {number[]} nums
 * @return {boolean}
 */
var increasingTriplet = function(nums) {
    
    let first = Infinity , second = Infinity;

    for(let x of nums){
        if(x > second) return true;
        if(x > first) second = Math.min(second , x);
        first = Math.min(first ,x);
        
    }
    return false

};