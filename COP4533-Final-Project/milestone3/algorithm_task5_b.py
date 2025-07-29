
def algorithm5 (stocks , kval): 
    s =  len(stocks)
    d =  len(stocks[0])
    opt = [[[0 for _ in range(kval)] for _ in range(d)] for _ in range(s)]
    buy = [[0 for _ in range(kval)]  for _ in range(s)]
    sums = [[[0 for _ in range(d)] for _ in range(d)] for _ in range(s)]
    sell = [[0 for _ in range(kval)]for _ in range(s)]


    
    for m in range(s):
        for  i in range(d):
            min_val = float('INF')
            for  j in range( i+1, d):
                min_val  = min(min_val, stocks[m][j-1] )
                sums[m][i][j] = stocks[m][j] - min_val
                if (m > 0 and  sums[m-1][i][j] > stocks[m][j] - min_val ):
                      sums[m][i][j] = sums[m-1][i][j] 

    for  n in range(1, d):

        for  m in range (s):
            improvement=-1

            for  k in range(0, kval): 
                print(f"at val {m}, {n}, {k}")
                
        
                buyday = buy[m][k]
                sellday = sell[m][k]

                if(k>0):
                    buyday = max(buy[m][k-1], buy[m][k])
                    print('previous buyday', buy[m][k-1])
                print(f'current buyday= {buyday}')
  
             #   print(f'buyday for {m}, {n}, {k} =', buyday)

                if(k==0 and m==0):
                     opt[m][n][k]  = max(opt[m][n-1][k], sums[m][buyday][n])

                elif(k==0):
                     print(type(opt[m-1][n][k]))
                     opt[m][n][k]  = max(  opt[m][n-1][k], sums[m][buyday][n], opt[m-1][n][k])

                elif(m==0):   
                    opt[m][n][k]  = max( opt[m][n-1][k], 
                                    opt[m][n-1][k-1] + sums[m][buyday][n])

                else:
                    opt[m][n][k]  = max( opt[m-1][n][k],
                                    opt[m][n-1][k], 
                                    opt[m][buyday][k-1] + sums[m][buyday][n], #or s[current] - s[buyday] - the same
                                    opt[m][sellday][k-1] +sums[m][sellday][n],
                                    opt[m][n][k-1]
                                    )      
                    print(f' else: max between {opt[m-1][n][k]}, {opt[m][n-1][k]} , { opt[m][buyday][k-1]} + {sums[m][buyday][n]}, {opt[m][sellday][k-1]} +{sums[m][sellday][k]}\n')


                    print(f"diff for opt[{m}][{n}][{k}] is [sums[{m}][{buyday}][{n}]] = {sums[m][buyday][n]} where buyday is {buyday}")


                print(f"opt[{m}][{n}][{k}] = ", opt[m][n][k])
                print("-----")


                if( stocks[m][n] <= stocks[m][buyday]) :
                    buy[m][k] = n

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
                sell[m][improvement+1] = n

              

    # Find maximum profit and corresponding transaction count k

    for k in range(kval):
        for m in range(s):
            for n in range(d):
                print(opt[m][n][k], sep = "")
        print()

    print("profit", opt[s-1][d-1][kval-1])

    for m in range(kval):
        for i in range(d):
            for j in range(i, d):
                print(f"The greatest sum between {i} and {j} up to {m}: {sums[m][i][j]}\n")

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

