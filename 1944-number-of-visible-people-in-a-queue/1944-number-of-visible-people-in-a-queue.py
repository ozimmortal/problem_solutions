class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        ans = [0] * len(heights)
        stack = []

        for i in range(len(heights) -1 , -1 , -1):
            v = 0
            while stack and stack[-1] < heights[i]:
                stack.pop()
                v += 1
            
            if stack and stack[-1] > heights[i]:
                v +=1

            ans[i] = v

            stack.append(heights[i])
        return ans





        