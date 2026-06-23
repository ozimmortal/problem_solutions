class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        group = []
        curr , curr_size = [] , 0

        for word in words:
            if curr_size + len(word) + len(curr) <= maxWidth:
                curr_size += len(word)
            else:
                group.append(curr)
                curr_size = len(word)
                curr = []
            curr.append(word)
        group.append(curr)
        
        res  = []
        for sen in group[:-1]:
            l = (len(sen) -1 if len(sen) > 1 else len(sen))
            t = 0
            for word in sen:
                t += len(word)
            
            i = 0
            while t < maxWidth:
                sen[i] += " "
                i = (i + 1) % l
                t += 1
            
            
            res.append("".join(sen))

        last = " ".join(group[-1])
        left = maxWidth - len(last)
        last += " " * left
        res.append(last)
        
        return res
        
        
        