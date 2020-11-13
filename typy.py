from functools import reduce
#signicher = lambda x,y,z: x * x * y +z


print(reduce(lambda x,y: x+y,[1,2,3,4,5]))