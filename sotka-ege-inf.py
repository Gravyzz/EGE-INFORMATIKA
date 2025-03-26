###Решение с ip адресом №13

"""from ipaddress import * 

for mask in range(33):
    net = ip_network(f'111.81.88.168/{mask}', 0)
    print(net, net.netmask)"""

"""from ipaddress import *

net = ip_network('202.75.38.152/255.255.255.248')
for i in net:
    ip = f'{i:b}' or ip = bin(int(i))[2:].zfill(32)
    
    print(ip)"""


"""from ipaddress import *
net = ip_network('158.132.161.128/255.255.255.128')
count =0
for i in net:
    ip = f'{i:b}'
    if "1" in ip[-1]:
        count +=1 
print(count)
"""

"""from ipaddress import *
net = ip_network('115.198.0.0/255.254.0.0')
count = 0
c = 0
for i in net:
    ip = f'{i:b}'
    if ip.count("1") % 5==0:
        count +=1
        
print(count)"""

"""
from ipaddress import *
for mask in range(33):
    net = ip_network(f'111.81.208.27/{mask}', 0)
    print(net, net.netmask)

"""

"""from ipaddress import *
for mask in range(33):
    net = ip_network(f'215.181.200.27/{mask}', 0)
    print(net, net.netmask)

"""
"""for n in range(2, 10000):
    s = bin(n)[2:] # перевод в двоичную систему
    s = s.replace('0','2')
    s = s.replace('1','0')
    s = s.replace('2','1')
    s.lstrip("0")
    s=int(s,2)
    if n-s == 979:
        print(n)
        break""" 


"""c = 0
ans = []
f = open("17-352.txt")
lst = [int(x) for x in f]
l = [x for x in lst if x%73==0]
for i in range(0, len(lst)-1):
    if lst[i]>=8249 and lst[i+1]>=8249:
        c +=1
        ans.append(lst[i] +lst[i+1])
print(c, max(ans))
"""

"""f = open("17-354.txt")
lst = [int(x) for x in f]
l = []
sum = 0
for i in range(len(lst)-1):
    if (abs(lst[i])%10 == (abs(lst[i+1])%100)//10 or abs(lst[i+1])%10 == (abs(lst[i])%100)//10 ) and ((abs(lst[i])%11==0 and abs(lst[i+1])%11!=0) or (abs(lst[i+1])%11==0 and abs(lst[i])%11==0)) and ((lst[i]**2 + lst[i+1]**2)>= 177218):
        l.append(lst[i]**2 + lst[i+1]**2)
print(len(l), max(l))

"""


"""print("x y z w f")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = ((x<=y)<=z) or not w
                if f ==0:
                    print(x,y,z,w,f)"""


"""x = int(input())
y = int(input())
k = int(input())
l = int(input())



lst1 = []
ls1 = []

s = abs(y-x)
if y > x:
    for i in range(x, y+1):
        lst1.append(i)
for i in range(len(lst1)):
    if abs(lst1[i])%k==0:
        ls1.append(lst1[i])

if y > x:
    for i in range(len(lst1)):
        count = 0
        first_pos = ls1[0]
        last_pos = ls1[-1]
        current = first_pos
        while current-l<y:
            count +=1
            current += k

print(count)

if x > y:
    for i in range(x, y-1, -1):
        lst2.append(i)
for i in range(len(lst2)):
    if abs(lst2[i])%k==0:
        ls2.append(lst2[i])

if x > y:
    for i in range(len(lst2)):
        count = 0
        first_pos = ls2[0]
        last_pos= ls2[-1]
        current = first_pos
        while current-l>y:
            count +=1
            current += k

print(count)"""

"""c = 0
f = open('ege-variant-reshal.txt')
for i in f:
    l = [int(x) for x in i.split()]
    chet = [x for x in l if x%2==0]
    nechet = [x for x in l if x%2!=0]
    if sum(nechet) > sum(chet):
        c+=1
print(c)"""

"""lst = []
for n in range(9900,10000):
    s = "1" + n*'2'
    while '12' in s or '322' in s or '222' in s:
        if '12' in s:
            s = s.replace('12', '2', 1)
        if '322' in s:
            s = s.replace('322', '21', 1)
        if '222' in s:
            s = s.replace('222', '3', 1)
        c = 0
        for i in range(len(str(s))):
            c += int(s[i])
        
        lst.append(c)
print(max(lst))
"""
"""s = ''
x = 4*8**3032+3*16*1956+870

while x !=0:
    
    s +=str(x%7)
    x//=7
s = s[::-1]
print(s.count('3')*3 - s.count('1'))"""

# 15
"""k = 0
for n in range(1, 1000):
    for A in range(1, 1000):
        if ((A + n <123) <= (n%5==0 <=  (not(n%7==0)))) == True:
            k+=1
        if A+n< 123:
            print(A)
"""

# 16
"""import sys
sys.setrecursionlimit(10**4)

def F(n):
    if n >= 2025:
        return n
    else:
        return F(n+1) - F(n+2) +7
print(F(15)-F(24))"""

#17
"""k = 0
minsum = []
f = open('17-378.txt')
lst = [int(x) for x in f]
m = [x for x in lst if abs(x)%1001==0]
for i in range(len(lst)-1):
    a, b = lst[i], lst[i+1]
    if (99<a<1000 or 99<b<1000) and (a+b)>1001:
        k+=1
        minsum.append(a+b)
print(k, min(minsum))"""

#23
"""def f(x,y):
    if x<y:
        return 0
    if x == y:
        return 1
    else:
        return f(x - 2, y) + f(x // 2, y)
print(f(28, 10)* f(10, 1))"""


#24 ???
"""c = ''
k = 0
lst = []
f = open('24-1.txt').readline()
for i in range(len(f)):
    c +=f[i]
    if f[i] == 'A' or f[i] == 'B' or f[i] == 'X':
        k+=1
    if k == 5:
        lst.append(c)
        c = ''
print(lst)"""


"""from turtle import *

screensize(100000, 100000)
tracer(0)
k = 50
down()
for i in range(6):
    rt(36)
    fd(10*k)
    rt(36)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*k, y*k)
        dot(5, 'black')
exitonclick()

import math
counter = 0
for x in range(30):
    for y in range(-15, 15):
        if ((y < x*math.tan(3*math.pi/10)) and (y > -x*math.tan(3*math.pi/10)) \
        and (y < -x*math.tan(math.pi/10) + 5 + math.tan(math.pi/10)*10*(math.cos(3*math.pi/10)+math.cos(math.pi/10))) \
        and (y > x*math.tan(math.pi/10) - 5 - math.tan(math.pi/10)*10*(math.cos(3*math.pi/10)+math.cos(math.pi/10))) \
        and (x < 10*(math.cos(3*math.pi/10)+math.cos(math.pi/10)))):
            counter += 1
print(counter)"""

'''lst = []
from itertools import *
for i in product("ABCX", repeat=5):
    s = ''.join(i)
    if (s.count("X") == 1 and s[-1]=="X" )or (s.count("X") == 0):
        lst.append(s)
print(lst)
print(len(lst))'''


"""count = m = 0
f = open('111.txt')
l = [int(i) for i in f]
for i in range(len(l) - 1):
    for j in range(i+1, len(l)):
        if (l[i] - l[j]) % 80 == 0:
            count += 1
            m = max(m, abs(l[i] - l[j]))
print(count, m)"""

"""def f(s,n):
    if s>40: return n%2==0
    if n==0: return 0
    h = [f(s+1, n-1), f(s+4, n-1),f(s*3, n-1)]
    return any(h) if (n-1)%2==0 else all (h)
print([s for s in range(1, 41) if not f(s,2) and f(s, 4)])
"""

# def f(n,fn):
#     if n==fn: return 1
#     if n>fn: return 0
#     return f(n+1, fn) + f(n+3, fn) + f(n*3, fn)
# print(f(4,10)*f(10,17)*f(17,23))

# f = open('text-24zadanie/t4.txt').readline()
# k = 1
# m = 0
# for i in range(len(f)-1):
#     if f[i] != f[i+1]:
#         k += 1
#         m = max(m, k)
#     else:
#         k = 1
# print(m)


# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f = ((z and (w <= y)) and (not x))
#                 if f==1:
#                     print(x,y,z,w,f)


# for n in range(1, 100):
#     ccc = n
#     n = bin(n)[2:]
#     if n.count('1')%2==0:
#         n+='0'
#         n = '1' + n[2:]
#     else:
#         n+='1'
#         n = '11' + n[2:]
#     r = int(n,2)
#     print(ccc, r)


# from itertools import *
# c = 1
# for i in product('АЕКМНЬ', repeat=6):
#     s = ''.join(i)
#     c+=1
#     if s[0] != 'Ь' and s.count('М') == 2 and s.count('А') == 1:
#         print(s,c)


# s = '3'*116
# while '333' in s or '7777' in s:
#     if '333' in s:
#         s = s.replace('333', '77', 1)
#     else:
#         s = s.replace('7777', '3', 1)
# print(s)

# n = 5*216**1225+4*36**1256-4*6**1257-2023
# s = ''
# while n>0:
#     s += str(n%6)
#     n //=16
# print(s.count('5'))

# def f(n):
#     if n<3: return 1
#     if n>2 and n%2==0: return f(n-1)+n
#     if n>2 and n%2!=0: return f(n-2)+2*n
# print(f(22)-f(20))


# f = open('text-17zadanie/17-17.txt')
# l = [int(x) for x in f]
# lst = []
# for i in range(len(l)-1):
#     a,b = l[i], l[i+1]
#     if (a%10==7 or b%10==7) and (a-b)**2>257**2:
#         lst.append(a+b)
# print(len(lst), max(lst), lst)


# def f(n,fn):
#     if n ==fn: return 1
#     if n>fn or n==24: return 0
#     return f(n+1, fn)+f(n*2,fn)
# print(f(1,11)*f(11,33))

# from itertools import *
# c = 0
# for i in product('АЕКМНЬ', repeat=6):
#     s = ''.join(i)
#     c+=1
#     if s[0] != 'Ь' and s.count('М') == 2 and s.count("А") <= 1:
#         print(s,c)
        

 

# n = 5*216**1255 + 4*36**1256 - 4*6**1257 - 2023
# s = ''
# while n>0:
#     s += str(n%6)
#     n //=6
# print(s.count('5'))


# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f =  (((x<=y)<=z) or (not w))
#                 if f == 0:
#                     print(x,y,z,w,f)


# def f(n,fn):
#     c = ''
#     c+=str(n)
#     m1 = [int(x) for x in c.split() if int(x)%2==0]
#     aa = 0

#     if n==fn: return 1; aa+=1
#     if n>fn: return 0
   
#     else: 
#         if len(m1)>aa:
#             return f(n+2,fn)+f(n+3,fn)+f(n*4,fn)
#         else:0
# print(f(1,50))

# chet = 0
# for a in range(10):
#     for b in range(10):
#         for c in range(10):
#             if a!=b and b!=c and c!=a:
#                 print(a,b,c)
#                 chet+=1
# print(1000-chet)


# for n in range(1, 100):
#     a = n
#     n = bin(n)[2:]
#     if n.count('1')%2==0:
#         n +='0'
#         n = '10'+n[2:]
#     else:
#         n+='1'
#         n = '11'+n[2:]
#     r = int(n,2)
#     if r<20:
#         print(a)

# c= 1
# f = open('9-zadanie.txt')
# for i in f:
#     x1,x2,x3,x4 = i.split()
#     if (int(max(x1,x2,x3,x4))>int(x1)+int(x2)+int(x3)+int(x4)- int(max(x1,x2,x3,x4))) and x1!=x2!=x3!=x4:
#         print(x1,x2,x3,x4)
#         c+=1
# print(c)
        
# s = '7' *108
# while '33333' in s or '777' in s:
#     if '33333' in s:
#         s = s.replace('33333', '7', 1)
#     else:
#         s = s.replace('777', '3', 1)
# print(s)


# from ipaddress import *
# net = ip_network('106.184.0.0/255.248.0.0', 0)
# cnt = 0
# for ip in net:
#     s = f'{ip:b}'
#     if s.count('1') % 2 != 0:
#         cnt += 1
# print(cnt)



# for x in range(2000):
#     n = 3**100 - x
#     s = ''
#     while n>0:
#         s+=str(n%3)
#         n //=3

#     if s.count('0') == 2:
#         print(x,s)
#         break


# def f(A,x):
#     return x%2<=(not(x%5)) or(x+A>=70)
# for A in range(300):
#     if all(f(A,x) for x in range(300)):
#         print(A)
#         break

# import sys
# sys.setrecursionlimit(10000)

# def f(n):
#     if n==1: return 1
#     if n>1: return 2*n*f(n-1)
# print((f(2024) -4*f(2023))/f(2022))

# f = open('text-17zadanie/17-111.txt')
# lst = [int(x) for x in f]
# mimimum = min(lst)
# ans = []
# for i in range(len(lst)-1):
#     a,b = lst[i],lst[i+1]
#     if a%18+b%18==mimimum:
#         ans.append(a+b)
# print(len(ans), max(ans))


# def f(x,y):
#     if x<y: return 0
#     if x == y: return 1
#     else: return f(x-2,y)+f(x//2,y)
# print(f(30,14)*f(14,1))

# f = open('text-24zadanie/t6.txt').readline()
# lst = []
# c = 0
# ans = []
# for i in f:
   
#     lst.append(i)
#     if i == "*":
#         c+=1
#     if c==140:
#         ans.append(len(lst))
#         lst = []
#         c = 0
# print(max(ans))
# def f(ch):
#     lst = []
#     for i in range(1,int(ch**0.5)):
#         if ch%i==0 and i[-1] =="7":
#             lst.append(i)
#             lst.append(ch//i)
#     return lst



# for i in range(600000, 1000000):
#     if f(i) 








# import math
# import turtle

# def xt(t):
#     return 16*math.sin(t)**3

# def yt(t):
#     return 13*math.cos(t)-5*\
#     math.cos(2*t)-2*\
#     math.cos(3*t)-\
#     math.cos(4*t)\
    
# t =turtle.Turtle()
# t.speed(500)
# turtle.bgcolor('white')
# for i in range(2550):
#     t.goto((xt(i)*20, yt(i)*20))
#     t.pencolor('red')
#     t.goto(0,0)

# lst = []
# for n in range(1, 100):
#     n = bin(n)[2:]
#     if n.count('1')>n.count('0'):
#         n+='1'
#     else:
#         n+='0'
#     if n.count('1')>n.count('0'):
#         n+='1'
#     else:
#         n+='0'
#     r = int(n,2)
#     if r<57:
#         lst.append(r)
# print(max(lst))

# from itertools import *
# def f(x,y,z,w):
#     return (y <= (not(x<=z))) or w

# for i in product([0,1], repeat=7):
#     table = [(i[0], 0, i[1], i[2]), (0, 1, i[3], i[4]), (1, i[5], i[6], 0)]
#     for p in permutations('xyzw'):
#         if [f(**dict(zip(p,r))) for r in table] == [0,0,0]:
#             print(p)
     

# from itertools import *
# c = 1
# for i in product('КОСУФ', repeat=5):
#     s = ''.join(i)
#     if s.count("Ф") ==0 and s.count("У") == 2:
#         print(c)
#     c+=1

# c= 0
# f = open('text-9zadanie/1.txt')
# for i in f:
#     a = [int(x) for x in i.split()]
#     pov = [x for x in a if a.count(x)==3]
#     nepov = [x for x in a if a.count(x)==1]
#     if len(pov) == 3 and len(nepov) == 3:
#         if sum(pov)>sum(nepov):
#             c+=1

# print(c)

 

# for A in range(1,1000):
#    flag = True
#    for x in range(1,1000):
#        f = (x % A == 0) or ((70<=x<=90) <= (x % 27 != 0))
#        if f == 0:
#            flag = False
#    if flag:
#        print(A)

# from sys import *
# setrecursionlimit(6000)

# def f(n):
#     if n==1: return 1
#     if n>1: return 2*n*f(n-1)
# print((f(2024) - 3 * f(2023)) // f(2022))

# f = open('text-17zadanie/17-1211.txt')
# l = [int(x) for x in f]
# krat = [x for x in l if x%32==0]
# lst = []
# for i in range(len(l)-1):
#     a,b = l[i],l[i+1]
#     if (a<0 or b<0) and (a+b)<245:
#         lst.append(a+b)
# print(len(lst), max(lst))



# def f(s,n):
#     if s>=43: return n%2==0
#     if n == 0: return 0
#     h = [f(s+1,n-1),f(s+4,n-1),f(s*3,n-1)]
#     return any(h) if (n-1)%2==0 else all(h)
        
# print([s for s in range(1,43) if not f(s,2) and f(s,4)])



# d= {}
# s = "ABFDJADFKBLADFLJKBADKLFBJKADFBJLKADFLKBAKLDFBJAKLDLJKADFBLJKAFDJKBAJLKBFLKADLFKBKLDFBLKDALFKBJKLADKBFLJLKDFBALJKADLKFBLKADLJKFBLAKDJFLKBLKADFBJLKADFBJLKADFJKBADGKJBADJKLGBJKLADFBLKJAJLKJLKAKLJBADFBLJKALDKJFBJKAFDBARGNBLKYRPJOYKEPTOYJKOIJBAFIJBADFBADFBAIFOPRJIEYOIARPHJDAFBADCVACXXBACSBACXBAXCBADFOPIBERJIJWRIHYTTISSFOOOOOOOOIIIISDFHGKSDFJHNPIADFJIHDAPHIJFAP'NBADJBKLA;DFBKJADFOIBADJFGOIARJTBIOTRQ[IBSDJFBLKA;DGBKLADFJBADOIBJEQATIGB[OGBKLSF;GBJADKLFBJDAFBTERIHJSDFSDDSBGSDBASBVBVBBVIBJFDGHIJSGHJFSGHKL;FSJGHSOKLGLJHADFHAKDGH;LFGH'SFGH"
# for c in s:
#     if c in d:
#         d[c] +=1
#     else:
#         d[c]=1
# print(max(d))


# print('x y z w f')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f  = (x and (not y)) or (x == z) or w
#                 if f == 0:
#                     print(x,y,z,w,f)


# def sic(n):
#     s = ''
#     while n>0:
#         s+=str(n%3)
#         n//=3
#     return s[::-1]

# lst = []
# for n in range(1, 400):
#     a = n
#     n = sic(n)
#     if a%3==0: n = n+n[-2:]
#     else: n = n+ sic(a%3*5)
#     r = int(n,3)
#     if r<242:
#         lst.append(r)
# print(max(lst))

# c = 1
# from itertools import *
# for i in product('АГМНСТУ', repeat=6):
#     s = ''.join(i)
#     if s[0] != 'А' and s.count('М') == 2 and s.count('У')<=1:
#         print(c)
#         break
#     c+=1

# c= 0 
# f = open('text-9zadanie/2.txt')
# for i in f:
#     a = [int(x) for x in i.split()]
#     pov = [x for x in a if a.count(x) == 3]
#     nepov = [x for x in a if a.count(x) == 1]
#     if len(pov)>1 and len(nepov)==4:
#         if pov[0] >= sum(nepov)/4:
#             c+=1
#             print(pov, nepov, pov[0], sum(nepov)/4 )
# print(c)

# lst = []
# for n in range(3, 10001):
#     s = '5'+n*'2'
#     while '72' in s or '522' in s or '2222' in s:
#         if '72' in s:
#             s = s.replace('72', '2', 1)
#         if '522' in s:
#             s = s.replace('522', '27', 1)
#         if '2222' in s:
#             s = s.replace('2222', '5', 1)
#     if s.count('2')*2+s.count('5')*5+s.count('7')*7==63:
#         lst.append(n)

# print(min(lst))


# for x in range(0, 19):
#     x = str(x)
#     if (int('98'+ x +'79641')+int('36'+x+'14')+int('73' +x+'4'))%18==0:
#         print(x)

# for x in range(0,19):
#     a = f'98{x}79641'
#     b = f'36{x}14'
#     c = f'73{x}4'
#     r = int(a,19)+int(b,19)+int(c, 19)
#     if r%18==0:
#         print(r/18)


# def f(s,n):
#     if s >=88: return n%2==0
#     if n==0: return 0
#     h = [f(s+1, n-1), f(s+4,n-1), f(s*3,n-1)]
#     return any(h) if (n-1)%2==0 else all(h)

# print([s for s in range(1, 88) if not f(s, 2) and f(s,4)])

# f = open('text-26zadanie/hz.txt').readlines()
# lst = []
# for i in f:
#     l = [int(x) for x in i.split()]
#     lst.append(l)
# print(sorted(lst)[1])


# print("x y z w f")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f = (x or y or (not z))<= (x and z and w)
#                 if f == 1:
#                     print(x,y,z,w,f)


# def zap(n, base):
#     s =  ''
#     while n>0:
#         s += str(n%base)
#         n //=base
#     return s[::-1]

# lst = []
# for n in range(1, 150):
#     a = n
#     n = zap(n, 3)
#     if a%3==0:
#         n =n+n[-3:]
#     else:
#         n = n+zap(((a%3)*5), 3)
#     r = int(n, 3)
#     if r>288:
#         lst.append(a)
# print(min(lst))

# c = 1
# chet = 0
# from itertools import *
# for i in product("АГИЛМОРТ", repeat=5):
#     s = ''.join(i)
#     if c%2==0 and s[0] == 'Л' and s.count('И') >= 2:
#         chet+=1

#     c+=1
# print(chet)

# lst = []
# for n in range(3, 10000):
#     s = '5' + n*'2'
#     while '72' in s or '522' in s or '2222' in s:
#         if '72' in s:
#             s = s.replace('72', '2', 1)
#         if '522' in s:
#             s = s.replace('522', '27', 1)
#         if '2222' in s:
#             s = s.replace('2222', '5', 1)
    
#     if (s.count('2')*2+s.count('5')*5+s.count('7')*7)==63:
#         lst.append(n)
#         break
# print(min(lst))



# srok = int(input("Введите срок кредита в месяцах:"))
# stavka = int(input("Введите ставку кредита:"))
# summa = int(input("Введите сумму кредита:"))
# nach = summa
# for i in range(srok):
#     summa += summa * (stavka/100)/12
# print(summa-nach )

# print('x y z w f')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f = (x or (not y)) and (not(x==z)) and (not w)
#                 if f == 1:
#                     print(x,y,z,w,f)


# from itertools import *
# for i in product('')

# def sc(n):
#     a = 0
#     while n>0:
#         a+=n%10
#         n//=10
#     return a


# chet = 0
# for n in range(100_000_000, 200_000_000):
#     sumraz = sc(n)
#     bb = bin(n)[2:]
#     if bb.count('1')%2==0:
#         bb = '1' + bb + '00'
#     else:
#         bb = '10' + bb+'1'
#     r = int(bb, 2)
#     if r == 21:
#         chet+=1
# print(chet)


# c = 0
# from itertools import *
# for i in permutations('ГЛУБИНА'):
#     s = ''.join(i)
#     l = [x for x in s]
#     g = 0
#     a = 0
#     for i in range(len(l)):
#         if l[i] == "Г":
#             g = i
#         if l[i] == 'А':
#             a = i
#     if g>a and 'АГ' not in s:
#         c+=1
# print(c)



# c = 0
# f = open('text-9zadanie/3.txt')
# for i in f:
#     l =[int(x) for x in i.split()]
#     pov = [x for x in l if l.count(x) == 2]
#     nepov = [x for x in l if l.count(x)==1]
#     if (len(pov)==2 and len(nepov)==4) and ((max(l)+min(l))/2 > (sum(l)-max(l)-min(l))/4):
#         c+=1
# print(c)


# def pros(a):
#     lst = []
#     for i in range(1, int(a**0.5)+1):
#         if a%i==0:
#             lst.append(i)
#             lst.append(a//i)
#     return len(set(lst))

# for n in range(0, 100):
#     s = '>'+39*'0'+n*'1'+39*'2'
#     while '>1' in s or '>2' in s or '>0' in s:
#         if '>1' in s:
#             s = s.replace('>1','22>', 1)
#         if '>2' in s:
#             s = s.replace('>2', '2>', 1)
#         if '>0' in s:
#             s = s.replace('>0', '1>', 1)
#     if pros((s.count('1') + s.count('2')*2)) == 2:
#         print(n, (s.count('1') + s.count('2')*2))

# def f(x,base):
#     s = ''
#     while x>0:
#         s+=str(x%base)
#         x //=base
#     return s

# for x in range(1 ,3000):
#     a = 7**100-x
#     b = f(a,7)
#     if b.count('0')==2:
#         print(x)


# def f(a,x,y):
#     return (11<=y) or (7*y <x) or (a>x*y)

# for a in range(0, 1000):
#     if all(f(a,x,y) for x in range(0, 1000) for y in range(0, 1000)):
#             print(a)
#             break


# def f(n):
#     return g(n-1)

# def g(n):
#     if n<10: return n
#     if n>=10: return g(n-2)
# lst = []
# for i in range(1, 101):
#     lst.append(f(i))
# print(lst.count(9))


# f = open('text-17zadanie/17-prob.txt')
# l = [int(x) for x in f]
# lst = []
# for i in range(len(l)-1):
#     a,b = l[i], l[i+1]
#     if a%36==0 or b%36==0:
#         lst.append(a+b)
# print(len(lst), max(lst))

# def f(x,y):
#     if x==y: return 1
#     if x>y or x == 20: return 0
#     return f(x+1,y)+f(x+3,y)+f(x**2,y)
# print(f(2,15)*f(15,35))

# f = open('text-24zadanie/t7.txt').readline()
# lst = []
# for i in range(len(f)-1):
#     a,b = f[i], f[i+1]
#     if (a in '0123456789' and b not in '0123456789') or (b in '0123456789' and a not in '0123456789'):
#         lst.append(i)

# ans = []
# maxi = 0
# for j in range(len(lst)-1):
    
#     a,b = lst[j], lst[j+1]
#     if b-a==1:
#         maxi+=1
#     ans.append(maxi)
#     if b-a>1:
#         maxi = 0
# print(max(ans))

# def f(a,n):
#     if a<0: return n%2==0
#     if n<0: return 0
#     h = [f(a-5, n-1), f(n//3, n-1)]
#     return any(h) if (n-1) % 2 == 0 else all(h)
# print([a for a in range(1,100) if f(a,4)])

# print('x y z w f')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f = not(z<=x) or (y==w) or y
#                 if f == 0:
#                     print(x,y,z,w,f)

# for n in range(1, 100):
#     a =n
#     n = bin(n)[2:]
#     if a%2==0:
#         n = '10'+n
#     else:
#         n='1'+n+'01'
#     r = int(n,2)
#     if r>516:
#         print(a)
#         break

# from itertools import *
# c= 0
# for i in product('АПРСУ', repeat=5):
#     s = ''.join(i)
#     c+=1
#     if s.count("У") <= 1 and "АА" not in s:
#         print(c)

# c = 0
# for i in open('text-9zadanie/4.txt'):
#     l = [int(x) for x in i.split()]
#     l.sort()
#     if l[3]<(l[0]+l[1]+l[2]):
#         if (l[0]+l[3])==(l[1]+l[2]):
#             c+=1
# print(c)

# s = 82*'8'
# while '1111' in s or '8888' in s:
#     if '1111' in s:
#         s = s.replace('1111', '8', 1)
#     else:
#         s = s.replace('8888', '11', 1)
# print(s)

# from ipaddress import *
# c= 0
# net = ip_network('122.159.136.144/255.255.255.248')
# for i in net:
#     ip = bin(int(i))[2:].zfill(32)
#     if ip.count('1')%4!=0:
#         c+=1
# print(c)

# def d(n,m):
#     return n%m==0
# def f(x, a):
#     return (not(d(x,a))) <= (d(x,14)<=(not (d(x,4))))

# for a in range(1, 50):
#     if all(f(x,a) for x in range(1, 50)):
#         print(a)

# from sys import *
# setrecursionlimit(100000)
# def f(n):
#     if n==1: return 1
#     if n>1: return n*f(n-1)
# print((f(2024)-f(2023))/f(2022))


# def f(a, s, n):
#     if a+s>=59: return n%2==0
#     if n ==0: return 0
#     h = [f(a+1,s,n-1),f(a,s+1,n-1),f(a*2,s,n-1),f(a,s*2,n-1)]
#     return any(h) if (n-1)%2==0 else all(h)
# print([s for s in range(1,54) if not f(5, s, 2) and f(5,s,4)])


# def f(x,y):
#     if x == y: return 1
#     if x>y: return 0
#     return f(x+1,y)+f(x+2,y)+f(x*2,y)
# print(f(4,11)*f(11,13)*f(13,15))


# print('x y z w f')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f = (not x and not y) or (y == z) or (not w)
#                 if f ==0:
#                     print(x,y,z,w,f)


# for n in range(100, 1000):
#     q = n
#     n = str(n)
#     a1 = int(n[0])+int(n[1])
#     a2 = int(n[1])+int(n[2])
#     a = str(max(a1,a2))+str(min(a1,a2))
#     if a == '1712':
#         print(q)
#         break

# c =0
# from itertools import *
# for i in permutations(range(8), r=5):
#     if i[0] != 0 and i[0]%2!=i[1]%2!=i[2]%2!=i[3]%2!=i[4]%2:
#         c+=1
# print(c)


# def f(x):
#   s = ''
#   while x>0:
#     s+=str(x%3)
#     x//=3
#   return(s[::-1])

# for n in range(1, 100):
#   a = f(n)
#   a =a+f(a.count('2'))
#   a = a+f(a.count('1'))
#   if a.count('0')==0:
#     a = a+'0'
#   else:
#     a = a+f(a.count('0'))
#   r = int(a,3)
#   if r<1000:
#     print(n)
    
# print('x y z w f')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f = ((w <= y)<=x) or (not z)
#                 if f==0: print(x,y,z,w,f)

# l = []
# for n in range(1,12):
#     a = n
#     n = bin(n)[2:]

#     if a%2==0:
#         n = '10'+n
#     else:
#         n = '1'+n+'01'

#     r = int(n,2)
#     l.append(r)
# print(max(l))


# from itertools import *
# chet = 0
# for i in product(range(12), repeat=5):
#     if i.count(7)==1 and i[0] != 0:
#         c = 0
#         for j in range(len(i)):
#             if i[j]>8:
#                 c+=1
#         if c <=3:
#             chet +=1
# print(chet)
            
# f = open('text-9zadanie/5.txt')
# ans = []
# for i in f:
#     l = [int(x) for x in i.split()]
#     pov = [x for x in l if l.count(x)==3]
#     nepov = [x for x in l if l.count(x)==1]
#     if len(pov)==3 and len(nepov)==3:
#         if (pov[0]+pov[1]+pov[2])**2>(nepov[0]+nepov[1]+nepov[2])**2:
#             ans.append(sum(pov))
# print(len(ans))

# s = 81*'1'
# while '11111' in s or '888' in s:
#     if '11111' in s:
#         s = s.replace('11111', '88', 1)
#     else:
#         s = s.replace('888', '8', 1)
# print(s)

# from ipaddress import *
# c = 0 
# net = ip_network('172.16.168.0/255.255.248.0')
# for i in net:
#     ip = bin(int(i))[2:].zfill(32)
#     if ip.count('1')%5!=0:
#         c+=1
# print(c)

# for x in '0123456789ABCDEFGHI':
#     s = int('98897' + x + '21', 19) + int('2' + x + '923', 19)
#     if s%18==0:
#         a = s//18
#         print(a)

# for x in '0123456789ABCDEFGHI':
#     r = int('98897' + x + '21', 19) + int('2' + x + '923', 19)
#     if r % 18 == 0:
#         print(r // 18)


# def f(a,p,q):
#     return (p <= ((q and (not a))<=(not p)))
# for a in range(1, 1000):
#     if all(f(a,p,q) for p in range(15,40) for q in range(15,40)):
#         print(a)

# from sys import *
# setrecursionlimit(10000000)
# def f(n):
#     if n==1: return 1
#     if n>1: return (n-1)*f(n-1)

# print((f(2024)+2*f(2023))/f(2022))

# f = open('text-17zadanie/1717.txt')
# l = [int(x) for x in f]
# ans = []
# for i in range(len(l)-1):
#     a,b=l[i],l[i+1]
#     if a%16==8 or b%16==8:
#         ans.append(a+b)

# print(len(ans), max(ans))


# def f(s,n):
#     if s<=19: return n%2==0
#     if n==0: return 0
#     h = [f(s-2, n-1),f(s-5, n-1),f(s//3, n-1)]
#     return any(h) if (n-1)%2==0 else all(h)
# print([s for s in range(20,100) if not f(s,2) and f(s,4)])

# def f(x,y):
#     if x==y: return 1
#     if x<y: return 0
#     return f(x-2,y)+f(x//2,y)
# print(f(38,16)*f(16,2))

