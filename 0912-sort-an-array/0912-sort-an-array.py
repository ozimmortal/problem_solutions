class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(left_arr , right_arr):
            
            p1 , p2 = 0 , 0
            output = []
            while p1 < len(left_arr) and p2 < len(right_arr):

                if left_arr[p1] <= right_arr[p2]:
                    output.append(left_arr[p1])
                    p1 +=1
                else:
                    output.append(right_arr[p2])
                    p2 +=1
            output.extend(left_arr[p1:])
            output.extend(right_arr[p2:])

            return output
        
        def merge_sort(left , right ,arr):
            if left == right:
                return [arr[left]]

            mid = left + (right - left) // 2
            left_half = merge_sort(left , mid ,arr)
            right_half = merge_sort(mid + 1 , right , arr)

            return merge(left_half, right_half)
        
        return merge_sort(0 , len(nums)-1 , nums)
        