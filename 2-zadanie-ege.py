"""print('x y z ')
for x in range(2):
    for y in range(2):
        for z in range(2):
            f = (x or y) <= (z==x)
            if f ==0:
                print(x,y,z,f)""" 


"""
print("x,y,z")
for x in range(2):
    for y in range(2):
        for z in range(2):
            f = (x or y) <= (z==x)
            if f == 0:
                print(x,y,z)"""

"""
print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = ((not x) == z)<=(y==(w or x))
                if f == 0:
                    print(x,y,z,w)"""



# from itertools import *
# def f(x,y,z,w):
#     return w and ((y<=x)<=z)

# for i in product([0,1], repeat=5):
#     table = [(i[0], i[1], 0, 1), (0, i[2],i[3], 0), (0, 1, i[4], 1)]

#     for p in permutations('xyzw'):
#         if [f(**dict(zip(p,r))) for r in table] == [1,1,0]:
#             print(p)
     
