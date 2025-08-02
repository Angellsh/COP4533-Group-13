import random
import numpy as np
from algorithm_task1 import algorithm1
from algorithm_task3 import algorithm3
from algorithm_task2 import algorithm2
from algorithm_task6 import algorithm6

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


# make test cases for algorithm_task6.py
def test_algorithm6():
    A = [
        [7, 1, 5, 3, 6, 8, 9],
        [2, 4, 3, 7, 9, 1, 8],
        [5, 8, 9, 1, 2, 3, 10],
        [9, 3, 4, 8, 7, 4, 1],
        [3, 1, 5, 8, 9, 6, 4]
    ]
    c = 2
    expectedProfit = 11
    result = algorithm6(A, c)
    

    def totalProfit(transactions):
        return sum(A[i][j2] - A[i][j1] for i, j1, j2 in transactions)
    
    if totalProfit(result) == expectedProfit:
        print("Test passed")
    else:
        print("test Failed")
        print("result:", result)
        print("total profit:", totalProfit(result))



if __name__ == "__main__":
    test_algorithm6()
    # You can add more test cases here
    # e.g., test_algorithm6() with different inputs