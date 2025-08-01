def algorithm1(A):
    # Brute force algorithm O(m*n^2))
    # Input: matrix A(m x n) representing stock prices
    # initialize variables
    # m represents number of stocks
    # n represents number of days
    # Output: return tuple (bestStock, bestBuyDay, bestSellDay, maxProfit)
    m = len(A)
    n = len(A[0])
    maxProfit = 0
    bestStock = 0
    bestBuyDay = 0
    bestSellDay = 0

    # iterate through each stock index
    for i in range(m):
        # iterate through each day to get the best buy and sell days
        for j in range(n-1):
            # sell day must be after buy day 
            for j2 in range(j + 1, n):
                # calculate profit sell day - buy day
                profit = A[i][j2] - A[i][j]
                if profit > maxProfit:
                    # update max profit, best stock, buy day, sell day | 1-based index
                    maxProfit = profit
                    bestStock = i + 1
                    bestBuyDay = j + 1
                    bestSellDay = j2 + 1

    # if profit is 0 return 0
    if maxProfit == 0:
        return (0, 0, 0, 0)  
    else:
        # return the best transaction found
        return (bestStock, bestBuyDay, bestSellDay, maxProfit)
