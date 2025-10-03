class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid_idx = set()
        transactionMap = defaultdict(list) #name -> (city, time, amount)

        for i, transaction in enumerate(transactions):
            name,time,amount,city = transaction.split(',')
            if int(amount) > 1000:
                invalid_idx.add(i)
                
            
            for prevCity, prevTime, prevAmount, prevIdx in transactionMap[name]:
                if abs(int(prevTime) - int(time)) <= 60 and prevCity != city:
                    invalid_idx.add(i)
                    invalid_idx.add(prevIdx)
                    
            transactionMap[name].append((city, time, amount,i))

        return [transactions[i] for i in range(len(transactions)) if i in invalid_idx]
