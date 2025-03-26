# #Два  хода +1 и *2, нужно получить из 2 - 35, при том должно быть 15 и не быть 31.
# def f(n, finish):
#     if n == finish: return 1
#     if n>finish or n== 31: return 0 
#     return f(n+1, finish)+f(n*2, finish)
# print(f(2,15)*f(15,35)) # Если есть вершина которая должна быть, то сначала идем до нее, а потом от нее до конечной и перемножаем эти два значения

# def f(n,fn):
#     if n == fn: return 1
#     if n>fn or n == 14: return 0
#     return f(n+1, fn)+f(n+2, fn)
# print(f(2,9)*f(9,18))

# def f(n,fn):
#     if n == fn: return 1
#     if n>fn or n == 17: return 0
#     return f(n+1,fn)+f(n*2,fn)
# print(f(1,10)*f(10,21))

# def f(n,fn):
#     if n== fn: return 1
#     if n>fn or n == 16: return 0
#     return f(n+1, fn)+f(n*2, fn)
# print(f(1,10)*f(10,21))

# def f(n,fn):
#     if n == fn: return 1
#     if n>fn or n==11: return 0
#     return f(n+1, fn)+f(n*2,fn)+f(n+5,fn)
# print(f(1,9)*f(9,18))

# def f(n, fn):
#     if n == fn: return 1
#     if n>fn or n==8: return 0
#     return f(n+1, fn)+f(n+2, fn)
# print(f(3,13))

# def f(n, fn):
#     if n == fn: return 1
#     if n>fn or n == 10 or n == 15: return 0
#     return f(n+1, fn)+f(n+2, fn)+ f(n+3,fn)
# print(f(5,11)*f(11,18))

# def f(n, fn):
#     if n == fn: return 1
#     if n<fn: return 0
#     return f(n-8, fn)+f(n//2, fn)
# print(f(102, 43)*f(43,5))

# def f(n,fn):
#     if n == fn: return 1
#     if n>fn or n == 12: return 0
#     return f(n+1, fn)+f(n+3, fn)+f(n*2, fn)
# print(f(3,8)*f(8,21))

# def f(n,fn):
#     if n == fn: return 1
#     if n>fn: return   0
#     return f(n*2, fn)+f(n*3, fn)
# print(f(8,96)*f(96,3456))

# Другое немного
# lst = []
# def f(n, step):
#     if step == 5: lst.append(n)
#     else:
#         f(n+2, step+1)
#         f(n+3, step+1)
#         f(n*2, step+1)
# f(10,0)
# print(len(set(lst)))

# def f(n,fn):
#     if n == fn: return 1
#     if n>fn or n == 14: return 0
#     return f(n+1, fn)+f(n*2, fn)+f(n*3, fn)
# print(f(1,12)*f(12,40))

# def f(n,fn):
#     if n == fn: return 1
#     if n>fn: return 0
#     return f(n+1, fn)+f(n*2, fn)
# print(f(2,11)*f(11,25)*f(25,50))

# def f(n,fn):
#     if n == fn: return 1
#     if n>fn or n == 30: return 0
#     return f(n+1, fn)+ f(n*2, fn)+f(n*3, fn)
# print(f(2,13)*f(13,39))

# def f(n,fn):
#     if n== fn: return 1
#     if n<fn: return 0
#     return f(n-8, fn)+f(n//2,fn)
# print(f(102,43)*f(43,5))

