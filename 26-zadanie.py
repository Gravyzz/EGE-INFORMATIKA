# f = open('text-26zadanie/1_26.txt')
# K = int(f.readline())
# N = int(f.readline())
# lst = []
# for i in range(N):
#     a = [int(x) for x in f.readline().split()]
#     lst.append(a)
# lst.sort()
# c = 0
# cam = K * [0]
# for i in range(N):
#     st, fin = lst[i][0], lst[i][1]
#     for j in range(K):
#         if st > cam[j]:
#             cam[j] = fin
#             c+=1
#             last = j+1
#             break
# print(c, last)

# f = open('text-26zadanie/26.txt')
# N = int(f.readline())
# lst = [int(x) for x in f]
# lst.sort(reverse=True)
# a = [lst[0]]

# for i in range(1,len(lst)):
#     if (a[-1]-lst[i])>=3:
#         a.append(lst[i])
        
# print(len(a), a[-1])
    
# f = open('text-26zadanie/26_6759.txt')
# N = int(f.readline())
# sum1 = 0
# sum2 = 0
# lst = [int(x) for x in f]
# for i in range(len(lst)-3):
#     a,b,c = lst[i],lst[i+1],lst[i+2]
#     maxi = max(a,b,c)
#     mini = min(a,b,c)
#     sum1 =a+b+c-maxi
#     sum2 = a+b+c-mini
# print(sum1, sum2)


