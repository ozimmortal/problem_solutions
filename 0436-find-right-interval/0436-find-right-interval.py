class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        arr = [[start , i] for i , (start , _) in enumerate(intervals)]
        arr.sort()

        def search(target):
            left , right = 0 , len(arr) - 1
            ans = len(arr)
            while left <= right:
                mid = (left + right) // 2
                if arr[mid][0] >= target:
                    right = mid - 1
                    ans = arr[mid][1]
                else:
                    left = mid + 1
            return ans if ans != len(arr) else -1
        
        res = []
        for start, end in intervals:
            res.append(search(end))
        
        return res

