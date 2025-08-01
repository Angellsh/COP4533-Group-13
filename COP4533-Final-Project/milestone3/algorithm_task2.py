def algorithm2(A): #MaxProfitGreedy
#Input: matrix A(m × n) representing stock prices
# m represents number of stocks
# n represents number of days
#Output: tuple (bestStock, bestBuyDay, bestSellDay, maxProfit) representing the best stock and days to buy/sell and max profit
    m = len(A)
    n = len(A[0])
    maxProfit = 0
    bestStock = 0
    bestBuyDay = 0
    bestSellDay = 0

    # iterate through each stock index
    for i in range(m):
        # initialize minPrice and minDay for this stock
        minPrice = A[i][0]
        minDay = 0

        # iterate through each day for current stock
        for j in range(1, n):
            # if selling gives a better profit than maxProfit, update best transaction
            if A[i][j] - minPrice > maxProfit:
                maxProfit = A[i][j] - minPrice
                # add 1 for 1-based index
                bestStock = i + 1          
                bestBuyDay = minDay + 1     
                bestSellDay = j + 1         

            # if current price is lower than minPrice we update 
            # minPrice and minDay to current day and price
            if A[i][j] < minPrice:
                minPrice = A[i][j]
                minDay = j

    # if profit is 0 then there is no profitable transaction made
    if maxProfit == 0:
        return (0, 0, 0, 0)
    else:
        # returns best transaction found
        return (bestStock, bestBuyDay, bestSellDay, maxProfit)
