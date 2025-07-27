def algorithm1(A):
    m = len(A)
    n = len(A[0])
    maxProfit = 0
    bestStock = 0
    bestBuyDay = 0
    bestSellDay = 0

    for i in range(m):

        for j in range(n-1):

            for j2 in range(j + 1, n):
            
                profit = A[i][j2] - A[i][j]
                if profit > maxProfit:
                    maxProfit = profit
                    bestStock = i + 1
                    bestBuyDay = j + 1
                    bestSellDay = j2 + 1

    if maxProfit == 0:
        return (0, 0, 0, 0)  # no profitable transaction
    else:
        return (bestStock, bestBuyDay, bestSellDay, maxProfit)
