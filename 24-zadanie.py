# f = open('24.txt').read()
# c = 1
# lst = []
# for i in range(0, len(f)-1):
#     if f[i] != f[i+1]:
#         c+=1
#     else:
#         lst.append(c)
#         c = 1
# print(max(lst))


# f = open("").readline()
# c = 1
# lst = []
# for i in range(0, len(f)-1):
#     if f[i] != f[i+1]: 
#         c+=1
#     else:
#         lst.append(c)
#         c = 1
# print(max(lst))

# f = open('').readline()
# f = f.replace('B', 'A')
# f = f.replace('C', 'A')
# for i in range(1, 10000):
#     if i*'A' in f:
#         print(i)

# f = open('').readline()
# print(f.count('SOCKS'))

# from statistics import *
# f = open('').readline()
# lst = []
# for i in range(1, len(f)-1):
#     if f[i-1]==f[i+1]:
#         lst.append(f[i])
# print(multimode(lst))
# print(lst.count('W'))

# lst = []
# f = open('').readlines()
# for i in f:
#     s = i
#     s = s.replace('XYZ', "*")
#     for j in range(1,1000):
#         if j*'*' in s:
#             lst.append(i)
# print(max(lst)*3)

# f = open('text-24zadanie/t1.txt').readline()
# c = 1
# for i in range(0, len(f)-1):
#     if f[i]==f[i+1]=='B':
#         c+=1
# print(c)

# f = open('text-24zadanie/t2.txt').readline()
# qq = 1
# for i in range(0, len(f)-1):
#     if f[i]==f[i+1]=='C':
#         qq+=1
# print(qq)

# lst = []
# f = open('text-24zadanie/t2.txt').readline()
# for i in range(1, 1000):
#     if i*'AB' in f:
#         lst.append(i)
# print(max(lst))

#Сложные прототипы

# pos = []
# f = open("").readline()
# for i in range(0,len(f)):
#     if f[i]=='T':
#         pos.append(i)
# ans = []
# for i in range(99, len(pos)):
#     ans.append(pos[i]-pos[i-99]+1)
# print(min(ans))

# from statistics import *
# f = open('').readlines()
# ans = []
# for i in f:
#     lst = []
#     for j in range(0, len(i)-1):
#         if i[j]=='T':
#             lst.append(i[j+1])
#     ans = ans + multimode(lst)
# print(multimode(ans)) 