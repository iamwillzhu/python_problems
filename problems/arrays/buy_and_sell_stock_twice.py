from typing import List

def buy_and_sell_stock_twice(prices: List[int]) -> int:
    min_price_so_far: int
    max_price_so_far: int
    max_total_profit: int = 0
    max_first_profit_so_far: List[int] = [0 for i in range(len(prices))]
    
    if len(prices) == 0:
        return max_total_profit
    
    min_price_so_far = prices[0]
    for index, price in enumerate(prices):
        min_price_so_far = min(min_price_so_far, price) 
        max_total_profit = max(max_total_profit, price - min_price_so_far)
        max_first_profit_so_far[index] = max_total_profit
 
    max_price_so_far = prices[-1]
    for index, price in reversed(list(enumerate(prices[1:], 1))):
        max_price_so_far = max(max_price_so_far, price)
        max_total_profit = max(max_total_profit, max_price_so_far - price +  max_first_profit_so_far[index - 1])

    return max_total_profit
