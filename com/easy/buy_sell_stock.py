# Input: [7, 1, 5, 3, 6, 4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5.
# Not 7-1 = 6, as selling price needs to be larger than buying price.

def max_profit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit

print(max_profit([7, 1, 5, 3, 6, 4])) # 5