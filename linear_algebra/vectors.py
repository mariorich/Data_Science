from functools import reduce
import math

def add_vectors(v1,v2):
# v1 and v2 are vectors
    sum = [x + y
        for x, y in zip(v1, v2)]
    return sum

def sub_vectors(v1,v2):
# v1 and v2 are vectors
    sum = [x - y
        for x, y in zip(v1, v2)]
    return sum

def vector_sum(vectors):
    # vectors is a list of vectors
    return reduce(add_vectors, vectors)

def scalar_multiply(c,v):
    # c is a number,v is a vector
    return [c * x for x in v]

def vector_mean(vectors):
    # vectors is a list of vectors
    l = len(vectors)
    return scalar_multiply(1/l, vector_sum(vectors))

def dot(v1,v2):
    # v1 and v2 are vectors
    return sum([x * y for x, y in zip(v1, v2)])

def sum_of_squares(v):
    #v_1*v_1 + v_2*v_2 + ...
    return dot(v,v)

def magnitude(v):
    return math.sqrt(sum_of_squares(v))

def squared_distance(v, w):
    return sum_of_squares(vector_subtract(v, w))

def distance(v, w):
    return magnitude(vector_subtract(v, w))



# TESTS

v1 = [2,2]
v2 = [3,3]
v3 = [5,5]
vectors = [v1,v2,v3]
v4 =[3,4]


print(add_vectors(v1,v2))
# prints [5,5] 

print(sub_vectors(v2,v1))
# prints [1,1]

print(vector_sum(vectors))
# prints [10,10]

print(magnitude(v4))
# prints 5.0