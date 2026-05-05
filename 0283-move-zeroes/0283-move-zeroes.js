/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {

    let p1 = 0;
    for(let p2=0; p2<nums.length; p2++){
        if(nums[p2] != 0 ){
            [nums[p2] , nums[p1]] = [nums[p1], nums[p2]]
            p1++;
        }
    }  
};