class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words= s.split(' ')
        
        if len(words) != len(pattern): return False

        ptos, stop= {},{}
        
        for i in range(len(pattern)):
            if ( pattern[i] in ptos and ptos[pattern[i]] != words[i]) or ( words[i] in stop and stop[words[i]] != pattern[i]):
                return False
            
            ptos[pattern[i]] = words[i]
            stop[words[i]] = pattern[i]

        return True
        
        
        
        