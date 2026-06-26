class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        mapper = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}

        def str_to_int(num):
            res  = 0 
            for n in num:
                res =res * 10 +  mapper[n]
            return res

        return str(str_to_int(num1) * str_to_int(num2))