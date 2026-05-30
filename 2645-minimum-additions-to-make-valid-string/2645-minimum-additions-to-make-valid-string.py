class Solution:
    def addMinimum(self, word: str) -> int:
        n = len(word)

        counter = 0
        i = 0
        while i < n:
            s = word[i]
            if s == "a":
                if i + 1 < n:
                    if word[i + 1] == "b":
                        if i + 2 < n and word[i + 2] == "c":
                            i += 3
                        else:
                            i += 2
                            counter += 1
                    elif  word[i + 1] == "c":
                        i += 2
                        counter += 1
                    else:
                        i += 1
                        counter += 2
                else:
                    i += 1
                    counter += 2
            elif s == "b":
                if i + 1 < n and word[i + 1]  == "c":
                    i += 2
                    counter += 1
                else:
                    i += 1
                    counter += 2
            else:
                i += 1
                counter += 2
            
        return counter
                