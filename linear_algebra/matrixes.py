A = [[1, 2, 3], # A has 2 rows and 3 columns
     [4, 5, 6]]

B = [[1, 2], # B has 3 rows and 2 columns
     [3, 4],
     [5, 6]]

def shape(M):
    num_rows = len(M)
    num_cols = len(M[0]) if M else 0
    return num_rows, num_cols

def get_row(A,i):
    return A[i]

def get_column(A,j):
    return [A_i[j] for A_i in A]

def make_matrix(rows,cols,entry_fn):
    return [[entry_fn(i,j)
             for j in range(cols)]
            for i in range(rows)]

def is_diagonal(i,j):
    return 1 if i == j else 0
 
identity_matrix = make_matrix(5,5,is_diagonal)

friendships =  [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0], # user 0
                [1, 0, 1, 1, 0, 0, 0, 0, 0, 0], # user 1
                [1, 1, 0, 1, 0, 0, 0, 0, 0, 0], # user 2
                [0, 1, 1, 0, 1, 0, 0, 0, 0, 0], # user 3
                [0, 0, 0, 1, 0, 1, 0, 0, 0, 0], # user 4
                [0, 0, 0, 0, 1, 0, 1, 1, 0, 0], # user 5
                [0, 0, 0, 0, 0, 1, 0, 0, 1, 0], # user 6
                [0, 0, 0, 0, 0, 1, 0, 0, 1, 0], # user 7
                [0, 0, 0, 0, 0, 0, 1, 1, 0, 1], # user 8
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]] # user 9

print(identity_matrix)
#print(shape(A))


