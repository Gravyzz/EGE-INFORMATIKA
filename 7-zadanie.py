"""f = open('1.txt') #Шаблон решения
for i in f:
    lst = [int(x) for x in i.split()]
    a,b,c = lst[0],lst[1],lst[2]
    #Или можно просто написать так a,b,c = map(int, i.split())
    Условие if"""

"""f = open('test7.txt')
cout = 0
for i in f:
    a,b,c,d,e = map(int, i.split())
    maxi = max(a,b,c,d,e)
    mini = min(a,b,c,d,e)
    sum_ost = a**2+b**2+c**2+d**2+e**2-mini**2-maxi**2
    if (maxi+mini)**2 > sum_ost:
        cout += 1
print(cout)"""


"""f = open('test7.txt')
cout = 0
for i in f:
    l= sorted([int(x) for x in i.split()])
    if (max(l)+min(l))**2 >(l[1]**2+l[2]**2+l[3]**2):
        cout += 1 
print(cout)"""

"""
f = open('text-7zadanie/text7-1.txt')
cout = 0
for i in f:
    l = sorted([int(x) for x in i.split()])
    if (max(l) - min(l)) >= 50 and (l[1]*l[2]) <= 1000:
        cout +=1
print(cout)"""

"""
f = open('text-7zadanie/text7-2.txt')
cout = 0
for i in f:
    l = sorted([int(x) for x in i.split()])
    if max(l)**3>=(2*l[0]*l[1]*l[2]) and ( l[0] > 10 and l[1] > 10 and l[2] > 10 and l[3] > 10 ):
        cout +=1
print(cout)"""

"""f = open('text-7zadanie/text7-3.txt')
cout = 0 
for i in f:
    l = [int(x) for x in i.split()]
    chet = [x for  x in l if x%2==0]
    nechet = [x for x in l if x%2!=0]
    if sum(nechet) > sum(chet):
            cout +=1 
print(cout)
     """

"""f = open('text-7zadanie/text7-4.txt')
cout = 0
for i in f:
    l = sorted([int(x) for x in i.split()])
    if l[0] != l[1] != l[2] != l[3]:
        if max(l)+min(l)>(l[1]+l[2]):
            cout+=1
print(cout)"""

