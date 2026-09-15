func rotate(nums []int, k int)  {
    
    reverseArr := func(arr []int, i , j int ){
        for i < j{
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        }
    }
    n := len(nums)
    rot := k % n
    if rot == 0 {
        return 
    }
    
    reverseArr(nums, 0, n - 1);
    reverseArr(nums, rot , n - 1);
    reverseArr(nums, 0 , rot-1);

    
}