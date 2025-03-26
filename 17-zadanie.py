"""lst = []
for i in range(1016, 7938):
    if i %3 == 0 and i %7 != 0 and i %17 != 0 and i %19 != 0 and i %27 != 0:
        lst.append(i)
print(len(lst), max(lst))
"""
"""
f = open('text-17zadanie/17-345.txt')
lst = []
for i in f:
    lst.append(int(i))
print(sum(lst))  """

"""f = open('text-17zadanie/17-345.txt')
lst = [int(x) for x in f if int(x)%3==0]
print(sum(lst))"""

"""f = open('text-17zadanie/17-4-2.txt')
lst = [int(x) for x in f if int(x)%3 == 0 and int(x) %7 != 0 and int(x) %17 != 0 and int(x)%19 != 0 and int(x) %27 != 0]
print(len(lst), max(lst))"""

"""f = open('text-17zadanie/17-345.txt')
lst = [int(x) for x in f]
c = 0
for i in range(0,len(lst)-1):
    if lst[i] % 10 == 0 or lst[i+1] % 10 == 0:
        c +=1
print(c)"""

"""f = open('text-17zadanie/17-257.txt')
lst = [int(x) for x in f]
l11 = [a for a in lst if a%11==0]
l17 = [d for d in lst if d%17==0]

if len(l11) > len(l17):
    print(len(l11), min(l11))
else:
    print(len(l17), max(l17))
"""

"""
lst = []
for i in range(3712,8433):
    if (i %2== i % 4) and i%13==0  and i%14 ==0 and i%15 ==0:
        lst.append(i)
print(len(lst), min(lst))
"""

"""f = open('text-17zadanie/17-257.txt')
lst = [int(x) for x in f]
chet = [x for x in lst if x%2==0]
nechet = [x for x in lst if x%2!=0]
if max(chet) > max(nechet):
    print(len(chet), min(chet))
else:
    print(len(nechet), min(nechet))"""

"""c = 0
summ = []
f = open('text-17zadanie/17-1.txt')
lst = [int(x) for x in f]
for i in range(0, len(lst)-1):
    if (lst[i] % 7 == 0 and lst[i+1] %17 != 0 ) or (lst[i+1] % 7 == 0 and lst[i] %17 != 0 ):
        c +=1
        summ.append(lst[i]+lst[i+1])
print(c, min(summ))"""

"""
f = open('text-17zadanie/17-336.txt')
lst = [int(x) for x in f]
mx = max([x for x in lst if x%37==0])
m = []
for i in range(len(lst)-1):
    if lst[i] % 89762==0 or lst[i+1] % 89762==0:
        m.append(lst[i]+lst[i+1])
print(len(m), min(m))"""

"""
f = open('text-17zadanie/17-(1).txt')
lst = [int(x) for x in f]
ls =[]
for i in range(0,len(lst)-1):
    a,b = lst[i], lst[i+1]
    if (a+b)%126==0:
        ls.append(a+b)
print(len(ls), max(ls))


from itertools import *
ls1 = []
for j in combinations(lst,2):
    if( j[0]+j[1])%126==0:
        ls1.append(j[0]+j[1])
print(len(ls1), max(ls1))"""

"""
from itertools import *
f = open('text-17zadanie/17-(2).txt')
lst = [int(x) for x in f]
ls = []
for i in combinations(lst, 2):
    if ((i[0] +i[1]) %80==0) and (i[0] %50 ==0 or i[1] %50 ==0):
        ls.append(i[0] +i[1])
print(len(ls), max(ls))"""

"""f = open('text-17zadanie/17-(3).txt')
lst = [int(x) for x in f]
ls = []
for i in range(0, len(lst)-1):
    a, b = lst[i], lst[i+1]
    if a*b%15==0 and (a+b)%7==0:
        ls.append(a+b)
print(len(ls), max(ls))
"""

"""f = open('text-17zadanie/17-1.txt')
lst = [int(x) for x in f]
ls = []
ls1 = []
for i in range(len(lst)-1):
    if lst[i+1] > lst[i]:
        ls.append(lst[i+1])
for j in range(len(ls)-1):
    ls1.append(abs(ls[j+1]-ls[j]))
print(len(ls), min(ls1))"""


