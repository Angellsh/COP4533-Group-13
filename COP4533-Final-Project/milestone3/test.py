import random
import numpy as np
from algorithm_task1 import algorithm1
from algorithm_task3 import algorithm3
from algorithm_task2 import algorithm2

def generate_matrix(stocks, days, upper_cost, gaussian=False):
    matrix  = [[0 for i in range(days)] for j in range(stocks)]

    #normal distribution - more realistic beahviour
    if gaussian==True:
        matrix  = np.random.normal(loc=upper_cost//2, scale=3, size = (stocks, days ) )
    
    #else random behaviour
    for i in range(stocks):
        for j in range(days):
            matrix[i][j] =  random.randint(0, upper_cost)
    return matrix


if __name__ == '__main__':
    n=1000 #upper limit
    upper_cost = 100000 #10^5

    for i in range(n): 
        stocks = random.randint(1, n)
        days = random.randint(5, n)

    matrix = generate_matrix(stocks, days, upper_cost)

    for row in matrix:
        print(row)
   
    solution3 = algorithm3(matrix)
    solution1 = algorithm1(matrix)
    solution2 = algorithm2(matrix)
    
    #best_stock, min_opt, i, stock_max
    print("solution 1", solution1)
    print("solution 3", solution3) 
    print("solution 2", solution2)

    assert solution2==solution3==solution1




