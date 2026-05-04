/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
  
  let prefix = [nums[0]];
  for(let i=1; i<nums.length; i++){
    prefix[i] = prefix[i - 1] * nums[i]
  }

  let suffix = Array(nums.length).fill(0)
  suffix[nums.length - 1] = nums[nums.length - 1]
  for(let i = nums.length - 2; i>=0; i--){
    suffix[i] = suffix[i + 1] * nums[i]
  }

  nums[0] = suffix[1]
  nums[nums.length - 1] = prefix[nums.length - 2 ]

  for(let i=1; i <nums.length-1; i++){
    nums[i] = prefix[i - 1] * suffix[i + 1]
  }
  return nums

};