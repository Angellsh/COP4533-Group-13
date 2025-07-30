
def algorithm5 (stocks , kval): 

    s =  len(stocks) # number of stocks
    d =  len(stocks[0])  #number of days 
    # 3d DP array to store optimal profits where each index(day) represents a potential sell day for the current stock and transaction count k
    opt = [[[0 for _ in range(kval)] for _ in range(d)] for _ in range(s)]
    # 2d array to track minimum price day (best day to buy) for each stock and transaction count k
    buy = [[0 for _ in range(kval)]  for _ in range(s)]

    # 3d array with precomputed profits for each stock, buyday, and sellday
    sums = [[[0 for _ in range(d)] for _ in range(d)] for _ in range(s)]

    #2d array to track best sell day for each stock and transaction
    sell = [[0 for _ in range(kval)]for _ in range(s)]


    # Precompute max profit for each buy-sell day, where actual buy day is any day in the range [buy, sell-1] that produces the highest profit if sold on sell day
    for m in range(s):
        for  i in range(d):
            min_val = float('INF')
            for  j in range( i+1, d):
                min_val  = min(min_val, stocks[m][j-1] )
                sums[m][i][j] = stocks[m][j] - min_val
                if (m > 0 and  sums[m-1][i][j] > stocks[m][j] - min_val ):
                      sums[m][i][j] = sums[m-1][i][j] 

    #Build a DP array opt
    for  n in range(1, d): # days

        for  m in range (s): # stocks
            improvement=-1 # track whether adding a new k-th transaction improves the global profit

            for  k in range(0, kval): #transaction count
                
        
                buyday = buy[m][k] #current buyday
                sellday = sell[m][k] #the last sell day from k-1 transaction 

                # Propagate the minimum buy day from the previous k-th transaction.
                # If a better (either lower-priced or newly chosen due to adding one more transaction)
                #  buy day was found at transaction k-1,
                # it should be propagated to all future transactions (k+i) where k+1 < kval.
                if(k>0):
                    buyday = max(buy[m][k-1], buy[m][k])
         
                # Case 1: first stock and first transaction. Can reuse a previous optimal or sell today.
                if(k==0 and m==0):
                     opt[m][n][k]  = max(opt[m][n-1][k], sums[m][buyday][n])

                # Case 2: first transaction. Can reuse a previous optimal, upper row optimal, or sell today.
                elif(k==0):
                     print(type(opt[m-1][n][k]))
                     opt[m][n][k]  = max(  opt[m][n-1][k], sums[m][buyday][n], opt[m-1][n][k])

               # Case 3:  First row (m == 0), multiple transactions.
               #We can either reuse a previous optimal, or add the best profit to the optimal profit for k-1 for the current k-th transaction for mth row.
                elif(m==0):   
                    opt[m][n][k]  = max( opt[m][n-1][k], 
                                    opt[m][n-1][k-1] + sums[m][buyday][n])

                # Case 4: No restrictions.
                # We can either reuse a previous optimal, or add the best profit to the optimal profit for k-1 for the current k-th transaction.
                # The profit comes from any buy-sell pair where the buy day is meanimum day after the k-1th sell day.
                # This logic is already handled via the precomputed sums array and the tracked sellday for each k.
                else:
                    opt[m][n][k]  = max( opt[m-1][n][k],
                                    opt[m][n-1][k], 
                                    opt[m][buyday][k-1] + sums[m][buyday][n], #or s[current] - s[buyday] - it's the same
                                    opt[m][sellday][k-1] +sums[m][sellday][n],
                                    opt[m][n][k-1]
                                    )      
                  

                # If the current day's price is lower than the currently tracked minimum for stock m,
                # update the buy day and propagate it forward for all upcoming days and stocks.
                if( stocks[m][n] <= stocks[m][buyday]) :
                    buy[m][k] = n

                # A previous result has been reused — selling on the current day gives no improvement.
                # Skip executing the next block and continue.
                if((opt[m][n][k] == opt[m][n-1][k])  \
                    or (m>0 and opt[m][n][k] == opt[m-1][n][k] ) \
                    or (k>0 and opt[m][n][k] == opt[m][n][k-1])):
                      continue
                # The first improvement has occurred — mark the transaction count index (k), where the first meaningful profit increase happened
                else:
                   if improvement==-1:
                        improvement = k 
             
     

                # If selling on the current day results in an improved global profit for transaction k (improvement == k),
                # then for the next day and the next transaction (n+1, k+1), we should start tracking from this day
                # as the new potential(minimum price) buy point
            if improvement!=-1 and improvement<kval-1:
                buy[m][improvement+1] = n
                sell[m][improvement+1] = n

              
    # Find the maximum profit and the number of transactions used
    k=-1
    profit = 0
    # Find the minimum number of transactions (from 0 to k) needed to achieve the maximum profit
    for  i in range(kval):
        if (opt[s-1][d-1][i] > profit):
            profit = opt[s-1][d-1][i]
            k = i

    #Return early if no profit is possible
    if k==-1:
        return (0, 0, 0)

    #Initialize current sell day and stock number
    sell = d- 1
    stock = s-1


  # Find last sell day (where the optimal values are reused)
    transactions = []
    while sell>0 and k>-1:

        # Same profit without using current stock, move up
        if stock >0 and opt[stock][sell][k] == opt[stock -1][sell][k]:
            stock -=1

        # Same profit as on the previous day, move left
        elif opt[stock][sell][k] == opt[stock][sell-1][k]:
            sell-=1

        #Same profit with fewer transactions
        elif k>0 and opt[stock][sell][k] == opt[stock][sell][k-1]:
            k-=1
        # A sale has occured on the current candidate sell day
        else:
            
# A new transaction has been used: find the stock i and buy day j
# such that selling at day 'sell' gives the maximum added profit in this range and is consistent with opt array

            cstock = -1
            cbuy = -1
            found = False
            for  i in range(stock, -1, -1): #  iterate over all stocks up to this point
                for  j in range(sell, -1, -1): # iterate over all buy days up to the current day
                    current = j

                   # Case 1: If k > 0, the current optimal is formed by:
                    # the previous optimal from the k-1th transaction + the profit from the best k-th transaction (selling on "sell" day)
                    if k>0:
                        diff = opt[m][sell][k]  - opt[m][current][k-1] 
                     
                    # When k = 0 (zero-based), the current optimal corresponds to a single transaction starting from 0
                    else:  
                        diff = opt[m][sell][k] 

                    # If the values in the opt array logically match the stock price differences,
                    # we have found the correct buy day index
                    if diff == stocks[i][sell]- stocks[i][current]:
                            cstock = i #current stock
                            cbuy = current #current buy
                            found = True 
                            break
                    if found == True:
                        break
                         
            # Add the current transaction tuple to the list
            transactions.append((cstock+1, cbuy+1, sell+1))
            sell = cbuy
            stock=s-1
            k-=1

# Reverse the order since we backtracked from the end of the array
    transactions = list(reversed(transactions))

        
    return transactions

