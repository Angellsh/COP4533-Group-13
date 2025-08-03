"""
Task 6 Code Implementation
DP Solution approach for stock trading with a cool-down period c
Input: 2D matrix A and c representing the cool-down period
Output: We return a list of tuples representing the best transactions made for max profit
Run time O(m*n^2) where m is the number of stocks and n is the number of days
"""

def algorithm6(A, c):
    # if the array is empty, or there are no stocks, or no days, return empty list []
    if not A or len(A) == 0 or len(A[0]) == 0:
        return []

    m = len(A)
    n = len(A[0]) 
    
    #if m == 0 or n == 0:
    #   return []

    # store best profit up to the each day 
    dp = [0] * n
    # store transactions that give best profit of day
    transactions = [None] * n 

    # intialize results to store optimal transaction sequence
    results = []
    # initialize current day to the last day for backtracking 
    currDay = n - 1

    # go through all buy and sell day pairs
    for j1 in range(0, n - 1):
        for j2 in range(j1 + 1, n):
            # iterate through each stock
            for i in range(m):
                # calculate profit sell day - buy day
                profit = A[i][j2] - A[i][j1]
                if profit < 0:
                    # skip transaction if there is no profit
                    continue 
                
                # check for previous day after cool-down
                prevDay = j1 - c -  1
                if prevDay >= 0:
                    totalProfit = profit + dp[prevDay]
                else:
                    totalProfit = profit

                # update best profit and store transaction
                if totalProfit > dp[j2]:
                    dp[j2] = totalProfit
                    transactions[j2] = (i, j1, j2, prevDay)

    # Check skipped days with best profits 
    for skippedDays in range(1,n):
        if dp[skippedDays-1] > dp[skippedDays]:
            dp[skippedDays] = dp[skippedDays-1]
            # only get transaction if current one is none existent
            if transactions[skippedDays] is None:
                transactions[skippedDays] = transactions[skippedDays-1]

 
    # backtrack to get best sequence
    while currDay >= 0:
        if transactions[currDay] is not None:
            i, j1, j2, prevDay = transactions[currDay]
            # Get 1-based index for output
            results.append((i+1, j1+ 1, j2 + 1))
            # go to the previous transaction day
            currDay = prevDay
        else:
            # go to previous day
            currDay -= 1

    # reverse to get correct order output earliest transaction first
    results.reverse()
    return results



"""******** Test Cases for Algorithm 6 ********"""

# Base case for empty array

def emptyArray():
    print("Running base case empty array")
    empty_result = algorithm6([], 2)
    expectedOutput = []
    if empty_result == expectedOutput:
        print("Test case 1 passed.")
    else:
        print(f"Test case 1 failed. Results:{empty_result}")

# Base case for no available sell days

def noSellDays():
    A = [
        [10],
        [100],
        [1000]
    ]

    noSellDaysResults = algorithm6(A, 2)
    expectedOutput = []
    if noSellDaysResults == expectedOutput:
        print("Test case 2 passed.")
    else:
        print(f"Test case 2 failed. Results: {noSellDaysResults}")

# Problem Statement 3 Example from Final Project Project Description page 4

def example():
    A = [
        [2,9,8,4,5,0,7],
        [6,7,3,9,1,0,8],
        [1,7,9,6,4,9,11],
        [7,8,3,1,8,5,2],
        [1,8,4,0,9,2,1]
    ]
    c = 2
    exampleResults = algorithm6(A, c)
    def total_profit(A, transactions):
        return sum(A[i-1][j2-1] - A[i-1][j1-1] for (i, j1, j2) in transactions)

    profit = 16
    if profit == total_profit(A, exampleResults):
        print(f"Test case 4 passed. Max profit is: {profit}")
    else:
        print("Test case 4 failed. Profit calculation is incorrect.")
    
    print("Expected Output: [(3,1,3), (2,6,7)] Results: ", exampleResults)

# Problem 3 from Final Project Milestone 1 page 6
def problem3():
    A = [
        [7,1,5,3,6,8,9],
        [2,4,3,7,9,1,8],
        [5,8,9,1,2,3,10],
        [9,3,4,8,7,4,1],
        [3,1,5,8,9,6,4]
    ]
    c = 2
    problem3Results = algorithm6(A,c)

    def total_profit(A, transactions):
        return sum(A[i-1][j2-1] - A[i-1][j1-1] for (i,j1,j2) in transactions)

    profit3 = 11
    if profit3 == total_profit(A, problem3Results):
        print(f"Test case 5 passed. Max profit is: {profit3}")
    else:
        print("Test case 5 failed. Profit calculation is incorrect.")
    
    print("Expected: [(3,1,3), (3,6,7)] or [(3,1,2), (3,5,7)] Results: ", problem3Results)

# Test for no profits available

def noProfit():
    A = [
        [100,90,80,70,60],
        [90,80,30,20,10],
        [25,15,10,5,0]
    ]
    c = 2
    noProfitResults = algorithm6(A,c)
    expectedOutput = []
    if noProfitResults == expectedOutput:
        print("Test case 3 passed. No profit can be made.")
    else:
        print("Test case 3 failed. Expected no profit but got results.")
  

if __name__ == "__main__":
    emptyArray()
    noSellDays()
    noProfit()
    example()
    problem3()
  