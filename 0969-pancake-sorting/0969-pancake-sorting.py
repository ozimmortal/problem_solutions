class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        output = []
        
        def flip(end):
            start = 0
            while start < end:
                arr[start] , arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
        
        def max_index(k):
            idx = 0
            for  i in range(1,k + 1):
                if arr[i] > arr[idx]:
                    idx = i
            return idx

        n = len(arr)

        for  i in range(n - 1 , -1 , -1):
            maxidx = max_index(i)

            if i != maxidx:
                flip(maxidx)
                flip(i)

                output.append(maxidx + 1)
                output.append(i + 1)
        return output
