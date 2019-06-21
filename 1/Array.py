import random
import Input
# function for define kind array
def array_kind():
    n = Input.get_number_matrix()
    w = Input.get_number_weight()
    row = n
    column = n
    matrix = matrix_square(n,w)
    return matrix,row,column,w

# function for create and return matrix square
def matrix_square(n,w):
    matrix_s = [[random.randrange(w)for i in range(0,n)]for j in range(0,n)]
    return matrix_s
    
# function for create and return matrix dream
def matrix_dream(row,column,w):
    matrix_d = [[random.randrange(w)for i in range(0,column)]for j in range(0,row)]
    return matrix_d