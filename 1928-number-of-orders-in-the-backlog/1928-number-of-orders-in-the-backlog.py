class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        #[price, amount, order type]
        #use a min heap to store prices for sell orders
        #use a max heap to store prices for buy orders
        #the same security is traded so can only store 2 heaps

        sell_heap = [] #min heap, store as (price, amount)
        buy_heap = [] #max heap, store as (price, amount)

        for price, amount, order_type in orders:
            if order_type == 0: #buy order
                #check the sell orders
                while amount > 0 and sell_heap and sell_heap[0][0] <= price:
                    root = heapq.heappop(sell_heap)
                    sell_price = root[0]
                    sell_amount = root[1]

                    if amount >= sell_amount:
                        amount -= sell_amount
                    else:
                        heapq.heappush(sell_heap, [sell_price, sell_amount - amount])    
                        amount = 0
                if amount > 0:
                    heapq.heappush(buy_heap, [-price, amount])

            elif order_type == 1:
                while amount > 0 and buy_heap and -buy_heap[0][0] >= price:
                    root = heapq.heappop(buy_heap)
                    buy_price = -root[0]
                    buy_amount = root[1]
                    
                    if amount >= buy_amount:
                        amount -= buy_amount
                    else:
                        heapq.heappush(buy_heap, [-buy_price, buy_amount - amount])
                        amount = 0
                if amount > 0:
                    heapq.heappush(sell_heap, [price, amount])
        
        total = 0 
        for price, amount in sell_heap:
            total += amount
        for price, amount in buy_heap:
            total += amount 
        return total % (10**9 + 7)

