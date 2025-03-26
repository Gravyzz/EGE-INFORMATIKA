from sys import *
setrecursionlimit(10000)
from functools import *
@lru_cache


# def f(n):
#     if n<=1: return 1
#     if n>1 and n%2 == 0: return n + f(n-1)
#     if n>1 and n%2 != 0: return n*n + f(n-2)

# print(f(82))

# def f(n):
#     if n<=1: return 1
#     if n>1 and n%2==0: return n*f(n-1)
#     if n>1 and n%2!=0: return n+f(n-2)
# print(f(84))

# c = 0
# for n in range(1, 101):
#     def f(n):
#         if n<=3: return n
#         if n>3 and n%2==0: return 2*n+f(n-1)
#         if n>3 and n%2!=0: return n*n+f(n-2)
#     if f(n)%3==0:
#         c +=1
# print(c) 

# def f(n):
#     if n<=10: return n
#     if 10<n<=36: return n//4+f(n-10)
#     if n>36: return 2*f(n-5)

# print(f(100))

 
# def f(n):
#     if n == 1: return 1
#     if n>=2: return f(n-1) +3*g(n-1)

# def g(n):
#     if n == 1: return 1
#     if n >=2: return f(n-1) - 2*g(n-1)

# print(f(18))

# from functools import *
# @lru_cache
# def f(n):
#     if n==1: return 1
#     if n>=2: return f(n-1)-2*g(n-1)
# def g(n):
#     if n==1: return 1
#     if n>=2: return f(n-1)+g(n-1)+n

# print(g(36)) 

# def f(n):
#     if n<2: return 1
#     if n>=2 and n%2==0: return f(n/2)+1
#     if n>=2 and n%2!=0: return f(n-3)+3
# c = 0
# for n in range(1, 10001):
#     if f(n) ==12:
#         c+=1
# print(c)


# from sys import *
# setrecursionlimit(10000)
# def f(n):
#     if n==1: return 1
#     if n>1: return (3*n+5)*f(n-1)
# print(f(2073)/f(2070))
