class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool: 
        
        cnt_s1 = Counter(s1)
        cnt_s2  = defaultdict(int)
        
        m , n = len(s1) , len(s2)
        if m > n: return False

        matches = 0
        for i in range(m):
            cnt_s2[s2[i]] += 1
            if cnt_s2[s2[i]] == cnt_s1[s2[i]]:
                matches += 1
            
            if matches == len(cnt_s1):
                return True
        for i in range(m , n):
            l = i - m
            if cnt_s2[s2[l]] == cnt_s1[s2[l]]:
                matches -= 1
                
            cnt_s2[s2[l]] -= 1

            cnt_s2[s2[i]] += 1
            if cnt_s2[s2[i]] == cnt_s1[s2[i]]:
                matches += 1

            if matches == len(cnt_s1):
                return True


        return False
