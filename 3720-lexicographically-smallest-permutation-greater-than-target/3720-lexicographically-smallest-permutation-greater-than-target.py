class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        
        def can_take(cnt , tar):
            max_s ="".join(chr(k + ord('a')) * cnt[k] for k in range(25 ,-1, -1))
            return max_s > tar

        res = []
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1
        
        for i in range(len(target)):
            t = ord(target[i]) - ord('a')
            
            if cnt[t] > 0:
                cnt[t] -= 1
                if can_take(cnt , target[i+1:]):
                    res.append(target[i])
                    continue
                cnt[t] += 1

            for j in range(t + 1 , 26):
                if cnt[j] > 0:
                    cnt[j] -= 1
                    res.append(chr(j + ord('a')))
                    return"".join(res) +  "".join( chr(k + ord('a')) * cnt[k] for k in range(26))
                
            return ""
        
        return ""




