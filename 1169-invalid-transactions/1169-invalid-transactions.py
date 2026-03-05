class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        c = defaultdict(list)
        res =set()
        for i, tr in enumerate(transactions):
            name,mi,price,city  = tr.split(",")
            c[name].append([mi , price ,city, i])
            
            if int(price) > 1000:
                res.add(i)
            
            for v in c[name]:
                pmi , pprice, pcity , j = v
                if abs(int(mi) - int(pmi)) <= 60 and pcity != city:
                    res.add(i) 
                    res.add(j)
                
                
        return [transactions[i] for i in res] 