# for i in range(10):
#     for j in range(10):
#         n = (int('12345' + str(i)+"7"+str(j)+'8'))
#         if n%23==0:
#             print(n,n//23)


# def f(n): Поиск делителий числа
#     lst = []
#     for i in range(1, n//2+1):
#         if n%i ==0:
#             lst.append(i)
#     lst.append(n)
#     return lst

# def f(n): # Поиск делителий числа универсальная программа которая работает очень быстро
#     lst = []
#     for i in range(2, int(n**0.5)+1):
#         if n%i==0:
#             lst.append(i)
#             lst.append(n//i)
#     return sorted(set(lst))

# for i in range(174457, 174506):
#     if len(f(i))==2:
#         print(f(i))


# def f(n):
#     lst = []
#     for i in range(2, int(n**0.5)+1):
#         if n%i==0:
#             lst.append(i)
#             lst.append(n//i)
#     return sorted(set(lst))

# for i in range(210235, 210301):
#     n = f(i)
#     if len(n)==4:
#         print(n)


# def f(n):
#     lst = []
#     for i in range(1, int(n**0.5)+1):
#         if n%i==0:
#             lst.append(i)
#             lst.append(n//i)
#     return sorted(set(lst))
# for i in range(312614, 312652):
#     n = f(i)
#     if len(n) == 6:
#         print(n)

# def f(n):
#     lst = []
#     for i in range(1, int(n**0.5)+1):
#         if n%i==0:
#             lst.append(i)
#             lst.append(n//i)
#     return sorted(set(lst))
# for i in range(110203, 110246):
#     n =f(i)
#     chet = [x for x in n if x%2==0]
#     if len(chet) == 4:
#         print(chet)

#Определяет простое или нет число
# def  isPrime(n):
#     for i in range(2, int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True
# c = 1
# for i in range(3614033, 3614117):
#     if isPrime(i):
#         print(c, i)
#     c+=1


#fnmatch("число", " маска")
# from fnmatch import *
# for i in range(17, 10**9+1, 17):
#     if fnmatch(str(i), '1?34567?9'):
#         print(i, i//17)


# from fnmatch import *
# for i in range(2025, 10**8+1, 2025):
#     if fnmatch(str(i), '123*4?5'):
#         print(i, i//2025)

# from fnmatch import *
# def isPrime(n):
#     for i in range(2, int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True

# for i in range(2627, 10**9, 2627):
#     s = sum([int(x) for x in str(i)])
#     if fnmatch(str(i),'7*53?3*1') and isPrime(s):
#         print(i,  i//2627)


# def f(n):
#     lst = []
#     for i in range(2, int(n**0.5)+1):
#         if n%i==0:
#             lst.append(i)
#             lst.append(n//i)
#     return sorted(set(lst))

# for i in range(350001, 350221):
#     n = f(i)
#     if len(n)>0:
#         m = max(n)-min(n)
#         if m%23==9:
#             print(i,m)


"""def f(n):
    lst = []
    for i in range(1, int(n**0.5)+1):
        if n%i==0:
            lst.append(i)
            lst.append(n//i)
    return sorted(set(lst))

for i in range(201455, 201471):
    n = f(i)
    if len(n)==4:
        print(n)"""