class Solution:
    def intToRoman(self, num: int) -> str:
        ONES = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
        TENS = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        HUNDS = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        THOUS = ["","M","MM","MMM"]

        return THOUS[num//1000] + HUNDS[(num % 1000)//100] + TENS[(num%100)//10] + ONES[num%10]
