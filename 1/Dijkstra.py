from time import clock
import Array
import Input
# function for find least path
def Dijkstra():

    # array for path start to goal
    dist = []

    matrix , row , column , w = Array.array_kind()
    # max weight array
    infinity = w*w*w

    # order why start to start = infinity
    for i in range(0,column):
        matrix[i][i] = infinity

    true = True
    # order why get number for start and goal
    while(true):
        start = Input.get_number_start() 
        if(start > row and start > column):
            print("Error : Please Enter number less than row or column")
        else:
            while(true):
                goal = Input.get_number_goal() 
                if(goal > row and goal > column):
                    print("Error : Please Enter number less than row or column")
                else:
                    true = False

    # function why compulation clock
    clock()

    start -= 1
    goal -= 1
    if (start == goal):
        print("The reason why start equal goal least path is zero.( Distance == 0 )")
        input("End.")
    elif(w <= 1):
        print("The reason why not to exist path least path is zero.( Distance == 0 )")
        input("End.")
    # start compute least path
    elif( start != goal or w > 1):
        for i in range (0,column):    
            for j in range (0,row):
                if(matrix[j][i]==0):
                    matrix[j][i]= infinity
        for k in range(0,row):                
            print(matrix[k])
        min_path = 0
        Min = []
        number = 0
        true = True
        while(true):   
            for i in range (0,column):
                dist.append( min_path + matrix[start][i] )
            if(number == column*10):
                true = False
            number += 1
            min_path = min(dist)
            place = dist.index(min_path)
            start = place % column
            if(dist[place] != infinity ):
                dist[place] = infinity
                if( start == goal ):
                    Min.append(min_path) 
        if(Min != []):
            print("Shortest Path is : ",min(Min))
        else:
            print("Dont Path between start and goal.")
        print("Shortest paths is --->  ",Min)
    clock()

    # use file for save information
    time_pro = clock()
    str_time = str(time_pro)
    str_n = str(column)
    str_w = str(w)
    Time = open("Time.txt","a")
    Time.write("Time : "+str_time+"\t"+"Number of lenght : "+str_n+"\t"+"Weight : "+str_w+"\n")
    Time.close()
    input("End.")