from algorithm_task7 import bestTrades

def main():

    #test 1. 1x1 matrix
    #returns empty array
    A=[[2]]
    print(bestTrades(A,1))

    #test 2 1X1000 matrix
    #return one array with one tuple
    A=[[0 for m in range(1000)]]
    A[0][999]=2
    print(bestTrades(A,1))

    #test 3 1000x1 matrix
    #return empty array
    A=[[0] for m in range(1000)]
    print(bestTrades(A,1))

    #test 4 1000X1000 matrix
    #return empty array
    A=[[0 for m in range(1000)] for m in range(1000)]
    print(bestTrades(A,1))

    #test 5 1x4 matrix 3 day cooldown
    #returns only one tuple
    A=[[0,10,0,10]]
    print(bestTrades(A,3))

    #test 6 1x10 matrix 3 day cooldown
    #returns two tuples same stock
    A=[[0,10,0,0,0,0,0,0,0,10]]
    print(bestTrades(A,3))

    #test 7 2x10 matrix 3 day cooldown
    #return two tuples different stocks
    A=[[0,10,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,10]]
    print(bestTrades(A,3))

    #test 8 2x10 matrix 3 day cooldown
    #return two tuple different or same stocks
    #has overlapping profitable trades
    A=[[0,10,0,0,0,0,0,0,0,10],[0,0,0,10,0,0,0,0,0,10]]
    print(bestTrades(A,3))



    return

if __name__ == '__main__':
    main()