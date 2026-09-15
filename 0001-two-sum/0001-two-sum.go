func twoSum(nums []int, target int) []int {
    n := len(nums)
    
    cnt := map[int]int{}
    for i := 0 ; i < n; i ++{
        t := target - nums[i]
        if j, ok := cnt[t]; ok{
            return []int{j, i}
        }
        cnt[nums[i]] = i
    }

    return nil

}