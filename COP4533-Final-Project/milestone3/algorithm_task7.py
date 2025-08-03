

def bestTrades(A,c):

    #Here we grab height and width of the matrix
    m=len(A)
    n=len(A[0])

    #This block instatiates the various arrays we'll
    #be using
    profitByDay=[0 for i in range(n)]
    profitByStock=[None for i in range(m)]
    decision=[None]*n
    purchases=[None]*m

    #i and j are reversed in the following loops
    #This differs from the pseudocode simply due to the fact
    #that working with i in the first loop and then j is more
    #comfortable for me after all these years
    for i in range(n):

        for j in range(m):

            #If we come to a new day it makes sure bring over the last days profit
            if i>0:

                profitByDay[i]=max(profitByDay[i], profitByDay[i-1])

            #We intatiated the array with None so this just makes sure we're
            #no longer in the first day. So we have something to compare
            if profitByStock[j] != None:

                #grabbing a temp variable to make comparisons and assignments
                temp=A[j][i]+profitByStock[j]

                #If it is larger than historical profit
                #We reassign profits and start our process of 
                #acculmulating various decisions
                if temp>profitByDay[i]:

                    profitByDay[i]=temp
                    decision[i]=(j,purchases[j][0],i)
                    purchases[j]=None
                    profitByStock[j]=None
        
            #This following if else block does two things
            #first to checks if we're past a certain number of days
            #then checks back to see what the stock price would have been and 
            #assigns it if its better than holding

            #The second portion is just how we first approach the problem if we're not a
            #certain number of days out
            if i-c-1>=0:

                profit = profitByDay[i-c-1]-A[j][i]

                if profitByStock[j] == None or profitByStock[j]<profit:
                    profitByStock[j]=profit
                    purchases[j]=(i,A[j][i])

            elif i-c-1 < 0:
                profit = -A[j][i]
                if profitByStock[j] == None or profitByStock[j]<profit:
                    profitByStock[j]=profit
                    purchases[j]=(i,A[j][i])

    
    #This creates the array we're actually going to return
    tuplesToReturn=[]
    i=n-1

    #We run backwards in time through the decision array. jumping backward over the cooldown period because 
    #we are grabbing everything in the main algorithm and need to keep that mind
    while i>=0:
        #print(n)
        #print(i,decision[i])
        if decision[i] != None:
            tuplesToReturn.append((decision[i][0],decision[i][1],decision[i][2]))
            i=decision[i][1]-c-1
        else:
            i=i-1


    #return the tuples
    return tuplesToReturn
