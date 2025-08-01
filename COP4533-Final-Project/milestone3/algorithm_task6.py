
# Task 6 Code Algorithm Implementation 
# Run time O(m*n^2)

# Input is a matrix and a cooldown period c 

def bestProfit(A, c):
    m = len(A)
    n = len(A[0]) 

    dp = [0] * n
    transactions = [None] * n 
    results = []
    currDay = n - 1

    # if the array is empty, or there are no stocks, or no days, return 0
    if A.empty() or m == 0 or n ==0:
        return(0,0,0)
    
    # else get pairs of profit (j1,j2)
    for i in range(m):
        for j1 in range(0, n - 2):
            for j2 in range(j1 + 1, n - 1):
                # calculate profit 
                profit = A[i][j2] - A[i][j1]
                if profit < 0:
                    continue # skip profit

                prevDay = j1 - c - 1
                if prevDay >= 0:
                    totalProfit = profit + dp[prevDay]
                else:
                    totalProfit = profit
                
                if totalProfit > dp[j2]:
                    dp[j2] = totalProfit
                    # store the transaction
                    transactions[j2] = (j1, j2)

                else:
                    dp[j2] = max(dp[j2], dp[j2-1])
                
    # backtrack to get best sequence
    while currDay >= 0:
        if transactions[currDay] is not None:
            i, j1, j2 = transactions[currDay]
            results.append((i+1, j1+ 1, j2 + 1))
            currDay = j1 - c - 1
        else:
            # skip to previous day
            currDay -= 1

    # need to sort the results output correctly
    return results





