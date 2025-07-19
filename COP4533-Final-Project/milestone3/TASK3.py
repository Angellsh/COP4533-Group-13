

def TASK3 (stocks): 

   opt = [ [0 for _ in range(len(stocks[0]))] for _ in range(len(stocks)) ] 
   stock_max = 0
   min_opt = -1
   best_stock = -1
   s = len(stocks)
   d = len(stocks[0])

   for m in range(s):
       min_ind = 0 

       for n in range(1, d):
           opt[m][n] = max(opt[m][n-1], stocks[m][n] - stocks[m][min_ind])
           if stocks[m][min_ind] > stocks[m][n]:
               min_ind = n


       if opt[m][d - 1] > stock_max:
            stock_max = opt[m][d - 1]
            best_stock = m
            min_opt = min_ind



   for i in range(min_opt+1, d):
       if(stocks[best_stock][i] - stocks[best_stock][min_opt]  == stock_max):
           return best_stock, min_opt, i, stock_max
       
   return (0,0,0,0)
