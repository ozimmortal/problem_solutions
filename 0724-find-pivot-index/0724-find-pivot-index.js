/**
 * @param {number[]} nums
 * @return {number}
 */
var pivotIndex = function(nums) {
    let prefix = [nums[0]];
    for(let i=1; i<nums.length; i++){
        prefix[i] = prefix[i-1] + nums[i];
    }

    let suffix = Array(nums.length).fill(0);
    suffix[nums.length - 1] = nums[nums.length - 1];
    for(let i=nums.length - 2; i>=0; i--){
        suffix[i] = suffix[i+1] + nums[i];
    }

    if(suffix[1] === 0 || nums.length === 1) return 0

    for(let i=1; i<nums.length-1; i++){
        if(suffix[i + 1] === prefix[i - 1]) return i
    }

    if(prefix[nums.length - 2] === 0) return nums.length - 1

    return -1
};