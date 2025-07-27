import random
import numpy as np
from TASK3 import algorithm3
from TASK5 import algorithm5

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
    n=20
    upper_cost = 10000

    for i in range(n): 
        stocks = random.randint(1, n)
        days = random.randint(5, n)

    matrix = generate_matrix(stocks, days, upper_cost)

    for row in matrix:
        print(row)

    solution3 = algorithm3(matrix)
    print(solution3) #best_stock, min_opt, i, stock_max


#cases we need to account for

