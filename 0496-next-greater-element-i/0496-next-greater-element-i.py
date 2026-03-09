class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hashmap = {}

        for  n in nums2:
            while stack and stack[-1] < n:
                hashmap[stack.pop()] = n
            stack.append(n)
        
        return [hashmap.get(n,-1) for n in nums1]

        