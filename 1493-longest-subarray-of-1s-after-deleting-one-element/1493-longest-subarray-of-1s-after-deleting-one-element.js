/**
 * @param {number[]} nums
 * @return {number}
 */
var longestSubarray = function(nums) {
    let count = 0, l = 0;
    let ans = 0;

    for(let r=0; r<nums.length; r++){
        count += nums[r] === 0 ? 1 : 0;

        while (count > 1){
            count -= nums[l] === 0 ? 1 : 0;
            l++;
        }

        ans = Math.max(ans , r - l + 1)
    }
    return ans - 1
};