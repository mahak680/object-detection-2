#find the maximum profit from buying and selling a stock on given days

def max_profit(prices):
    max_profit = 0

    # Iterate through the prices array
    for i in range(1, len(prices)):
        # If the price on the current day is higher than the previous day,
        # add the difference to max_profit
        if prices[i] > prices[i - 1]:
            max_profit += prices[i] - prices[i - 1]
  
    return max_profit    

arr = [100,180,260,310,40,535,695]
print(max_profit(arr))