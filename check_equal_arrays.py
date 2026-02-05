from collections import Counter
class Solution:
    def checkEqual(self, a, b) -> bool:
        #code here
        c_a = Counter(a)
        c_b = Counter(b)
        
        if len(c_a) != len(c_b):
            return False
        
        for k in c_a:
            if not c_b[k]:
                return False
            elif  c_a[k] != c_b[k]:
                return False
        return True
                
        