
def procedure (stocks , kval):
    profit = -1
    s =  len(stocks)
    d =  len(stocks[0])

    opt = [[[0 for _ in range(kval)] for _ in range(d)] for _ in range(s)]
    cmax = [float('-inf')] * kval
    buy = [[0 for _ in range(kval)] for _ in range(s)]

    for n in range(1, d):

        for m in range(s):

            for k in range( kval):
                cmax[k] = max(cmax[k], stocks[m][n] - stocks[m][buy[m][k]])

                if(k==0 and m==0):
                     opt[m][n][k]  = cmax[k]

                elif(k==0):
                     opt[m][n][k]  = max( opt[m-1][n][k],
                                     cmax[k])

                elif(m==0):  
                    opt[m][n][k]  = max( opt[m][n-1][k], 
                                    opt[m][n-1][k-1] + cmax[k])

                else:
                    opt[m][n][k]  = max( opt[m-1][n][k],
                                    opt[m][n-1][k], 
                                    opt[m][n-1][k-1] + cmax[k])
                    
                if k==0 and stocks[m][n] <= stocks[m][buy[m][k]]:
                    buy[m][k] = n
                    break

                if( stocks[m][n] <= stocks[m][buy[m][k]]) :
                    buy[m][k] = n

                elif(opt[m][n][k] ==  opt[m][n-1][k-1] + cmax[k] ):
                    buy[m][k] = n 
                    cmax[k] = 0
    k=-1
    profit = 0
    for i in range(kval):
        if (opt[s-1][d-1][i] > profit):
            profit = opt[s-1][d-1][i]
            k = i
    if k==-1:
        return (0, 0, 0, 0)


    sell = d-1
    m = s -1
    transactions = []
    while sell>0:
        if m>0 and opt[m][sell][k] == opt[m-1][sell][k]:
            m-=1
        elif (opt[m][sell][k] == opt[m][sell-1][k]):
            sell-=1
        else:
            diff = opt[m][sell][k] - opt[m][sell-1][k-1]
            gap = float('INF')
            cstock = -1
            cbuy = -1
            for i  in range(m, -1, -1):
                for  j in range(sell, -1, -1):
                    if (diff == stocks[i][sell] - stocks[i][j]) and (sell-j < gap):
                        gap= sell-j
                        cstock = i
                        cbuy = j
                        
            if cstock==-1 :
                break
            transactions.append((cstock, cbuy, sell))
            sell = cbuy
            k-=1

    transactions = transactions.reverse() 
    return transactions
  