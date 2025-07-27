def algorithm2(A): #MaxProfitGreedy
#Input: matrix A(m × n) representing stock prices
#Output: tuple (i, j₁, j₂, profit) representing the best stock and days to buy/sell and max profit
    m = len(A)
    n = len(A[0])
    maxProfit = 0
    bestStock = 0
    bestBuyDay = 0
    bestSellDay = 0

    for i in range(m):
        minPrice = A[i][0]
        minDay = 0

        for j in range(1, n):
            if A[i][j] - minPrice > maxProfit:
                maxProfit = A[i][j] - minPrice
                bestStock = i + 1          
                bestBuyDay = minDay + 1     
                bestSellDay = j + 1         

            if A[i][j] < minPrice:
                minPrice = A[i][j]
                minDay = j

    if maxProfit == 0:
        return (0, 0, 0, 0)
    else:
        return (bestStock, bestBuyDay, bestSellDay, maxProfit)
