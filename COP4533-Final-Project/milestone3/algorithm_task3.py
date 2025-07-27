

def algorithm3 (stocks): 

    opt = [ [0 for _ in range(len(stocks[0]))] for _ in range(len(stocks)) ] 
   #stock_max = 0
   # min_opt = -1
   # best_stock = -1
    s = len(stocks)
    d = len(stocks[0])

    for m in range(s):
       min_ind = 0 

       for n in range(1, d):
            if m>0:
                opt[m][n] = max(opt[m][n-1], opt[m-1][n], stocks[m][n] - stocks[m][min_ind])
            else:
                 opt[m][n] = max(opt[m][n-1], stocks[m][n] - stocks[m][min_ind])

               
            if stocks[m][min_ind] >= stocks[m][n]:
               min_ind = n


    if opt[s-1][d-1] == 0:
        return (0,0,0,0)

    m = s-1
    n = d-1
    stock =0
    sell = n
    buy = 0
    profit = opt[m][n]
    
    while(n>0):
    
       if(m>0 and opt[m][n] == opt[m-1][n]):
           m=m-1
       elif( opt[m][n]==opt[m][n-1]):
            n=n-1
       else:
           print("m, n", m, n)
           stock = m
           sell = n
           for i in range(sell-1, -1, -1):

               if(stocks[m][sell]- stocks[m][ i] == profit):
                   buy = i
                   break
           break
        
       
    return (stock+1, buy+1, sell+1, profit)
