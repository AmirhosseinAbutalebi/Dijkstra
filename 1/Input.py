# function for get number matrix n*n and return
def get_number_matrix():
    true = True
    while(true):
        n = input("Enter a number for lenght  matrix : ")# order for get input with print sentence think
        if(str.isnumeric(n)):
            n = int(n)
            if(n>0):
                true = False
            else:
                print("Error: You Do number > 0.")
        else : 
            print("Error: You Do Enter a number.")
    return n

# function for get number weight graf and return
def get_number_weight():
    true = True
    while(true):
        w = input("Enter a number for max weight matrix : ")# order for get input with print sentence think
        if(str.isnumeric(w)):
            w = int(w)
            if(w>0):
                true = False
            else:
                print("Dont path and you Enter number > 0.")
        else:
            print("Error: You Do Enter a number.")
    return w

# function for get number start point and return
def get_number_start():
    true = True
    while(true):
        start = input("Enter a number for start point matrix : (less than row or column)\n")# order for get input with print sentence think
        if(str.isnumeric(start)):
            start = int(start)
            if(start > 0):
                true = False
            else:
                print("Error:number > 0 .")
        else:
            print("Error: You Do Enter a number .")
    return start
    
# function for get number goal point and return
def get_number_goal():
    true = True
    while(true):
        goal = input("Enter a number for goal point matrix : (less than row or column)\n")# order for get input with print sentence think
        if(str.isnumeric(goal)):
            goal = int(goal)
            if(goal > 0):
                true = False
            else:
                print("Error:number > 0 .")
        else:
            print("Error: You Do Enter a number .")
    return goal