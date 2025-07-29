def algorithm5 (stocks , kval): # stocks is a 2d array, kval is max allowed transactions
    s =  len(stocks)
    d =  len(stocks[0])
    opt = [[[0 for _ in range(kval)] for _ in range(d)] for _ in range(s)]
    buy = [[0 for _ in range(kval)]for _ in range(s)]
    profit = [0] * kval

    for  n in range(1, d):
        print(n)
        print()

        for  m in range(s):
            #Index k starts at 0 but represents the 1st transaction
            improvement = -1
            for  k in range(kval): 
              #  print("at index m = ", m, ", n = ",  n, ", k = ",  k)
                if(k>0):
                 #   print("buy[m][k]", buy[m][n][k])
                 #   print("buy[m][k-1]", buy[m][n][k-1])
                    buyday = max(buy[m][k-1], buy[m][k])

                else:
                    buyday = buy[m][k]
                    current_profit = stocks[m][n] - stocks[m][buyday]
                print(f"buyday[{m}][{k}] at index [{m}][{n}][{k}]", buyday)

               
                #Recurrence relations for different cases
                if(k==0 and m==0):
                     opt[m][n][k] =  max(opt[m][n-1][k], current_profit) 

                elif(k==0):
                     opt[m][n][k] = max( opt[m][n-1][k], opt[m-1][n][k], current_profit )

                elif(m==0):   
                    current_profit = stocks[m][n] - stocks[m][buyday]
                    opt[m][n][k] = max( opt[m][n-1][k], 
                                        opt[m][buyday][k-1] + current_profit, )

                else:

                    current_profit = stocks[m][n] - stocks[m][buyday]
                    earlier_profit= opt[m-1][n][k] - opt[m-1][buyday][k-1]  #guaranteed to be one transaction
                    opt[m][n][k]  = max( opt[m-1][n][k],
                                        opt[m][n-1][k], 
                                        opt[m][buyday][k-1] + current_profit,
                                        opt[m][buyday][k-1] + earlier_profit)      

           #     print( f'opt[{m}][{n}][{k}]={opt[m][n][k]}')
            
            # Propagate current buy day to the next day   
              #  buy[m][n+1][k] = buy[m][n][k] #propagate current minimum 

                # Update buy day if today's price is lower or equal to previous buy
                if( stocks[m][n] <= stocks[m][buyday]) :
                    buy[m][k] = n

                      
                # If no new transaction occurred (profit reused), skip further updates
                #very unsafe 
                if((opt[m][n][k] == opt[m][n-1][k])  \
                    or (m>0 and opt[m][n][k] == opt[m-1][n][k] ) \
                    or (k>0 and opt[m][n][k] == opt[m][n][k-1])):
                   #   print("continue")
                      continue
                else:
                    if improvement==-1:
                        improvement = k 

                # If a new transaction has been made, update the buy day for the next transaction
               # if k < kval-1 and n<d-1: 
                #    print(f"buy[{m}][{k+1}] becomes", n)
                 #  buy[m][k+1] = n
            if improvement!=-1 and improvement<kval-1:
                buy[m][improvement+1] = n


    for k in range(kval):
        for m in range(s):
            for n in range(d):
                print(opt[m][n][k], sep = "")
        print()
    print("profit", opt[s-1][d-1][kval-1])
    # Find the maximum profit and the number of transactions used
    k=-1
    profit = 0
    for  i in range(kval):
        if (opt[s-1][d-1][i] > profit):
            profit = opt[s-1][d-1][i]
            k = i

    if k==-1:
        return (0, 0, 0)

    sell = d- 1
    stock = s-1


  # Find last sell day (where the optimal values are reused)
    transactions = []
    while sell>0:

        # Same profit without using current stock, move up
        if stock >0 and opt[stock][sell][k] == opt[stock -1][sell][k]:
            stock -=1

        # Same profit as on the previous day, move left
        elif opt[stock][sell][k] == opt[stock][sell-1][k]:
            sell-=1

        else:
        
# A new transaction has been used: find the stock i and buy day j
# such that selling at day 'sell' gives the profit 'diff',
# and the interval [j, sell] is the shortest

            diff = opt[stock][sell][k] - opt[stock][sell-1][k-1]
            gap = float('INF') 
            cstock = -1
            cbuy = -1
            for  i in range(stock, -1, -1):
                for  j in range(sell, -1, -1):

                    if diff == stocks[i][sell] - stocks[i][j] and sell-j < gap:
                        gap= sell-j
                        cstock = i #current stock
                        cbuy = j #current buy
                        
            if cstock==-1 :
                break
            transactions.append((cstock+1, cbuy+1, sell+1))
            sell = cbuy
            k-=1

        
    return reversed(transactions)




