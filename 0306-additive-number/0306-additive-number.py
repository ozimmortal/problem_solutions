class Solution:
    def isAdditiveNumber(self, num: str) -> bool:

        

        def backtrack(path , st):

            if st == len(num) and len(path) >= 3:
                return True
            
            for i in range(st , len(num)):
                
                n = num[st : i + 1]

                if len(n) > 1 and n[0] == '0':
                    break
                

                if len(path) >= 2:
                    if int(n) < path[-1] + path[-2]:
                        continue
                    elif int(n) > path[-1] + path[-2]:
                        break
                path.append(int(n))
                if backtrack(path , i + 1):
                    return True
                path.pop()
            return False
       
        return  backtrack([]  , 0)

            