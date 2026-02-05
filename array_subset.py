#User function Template for python3
from collections import Counter
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        c_a  = Counter(a)
        c_b = Counter(b)
        
        
        for k in c_b:
            if not c_a[k]:
                return False
            elif c_b[k] > c_a[k]:
                return False
        return True
        
        
        
        
    
    
    
    
