class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        
        m , n = len(img1) , len(img1[0])
        pts1 = [(x , y) for x in range(m) for y in range(n) if img1[x][y]]
        pts2 = [(x , y) for x in range(m) for y in range(n) if img2[x][y]]

        if not pts1 or not pts2: return 0
        cnt = Counter()
        for x1 , y1 in pts1:
            for x2, y2 in pts2:
                diff = (x2 - x1 , y2 - y1)
                cnt[diff] += 1
        
        return max(cnt.values())
