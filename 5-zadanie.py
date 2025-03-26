"""N = int(input())
n = bin(N)[2:]
if n.count("1") % 2 != 0:
    n = n+"1"
else:
    n = n+"0"

if n.count("1") % 2 != 0:
    n = n+"1"
else:
    n = n+"0"
r = int(n, 2)
print(r)"""

"""for N in range(100, 1000):
    n1, n2, n3 = int(str(N)[0]), int(str(N)[1]), int(str(N)[2])
    s1, s2 = n1+n2, n2+n3
    ans = str(max(s1,s2))+str(min(s1,s2))
    if ans == "1412":
        print(N)
"""

"""for N in range(1, 1000):
    n = bin(N)[2:]
    n = n +str(n.count("1")%2)
    n = n +str(n.count("1")%2)
    r = int(n, 2)
    if r > 77:
        print(N)
        break"""

"""for N in range(1, 9):
    n = bin(N)[2:]
    if N%2==0:
        n = "10"+n
    else:
        n = "1"+n+"01"
    r = int(n,2)
    print(r, N)
"""

"""for N in range(1, 1000):
    n = bin(N)[2:]
    if n.count("1")%2==0:
        n = n+"0"
        n = "10"+n[2:]
    else:
        n = n +"1"
        n = "11"+n[2:]
    r = int(n, 2)
    print(r, N)""" 

"""for N in range(10, 100):
    n = bin(N)[2:]
    if N%2!=0:
        n = n+"0"
    else:
        n = "1" + n
    if n.count("1") %2 ==0:
        n = n +"1"
    else:
        n = n +"0"
    r = int(n, 2)
    if r >228:
        print(N, r)"""

"""### Перевод числа в любую систему счисдения, где n - число, base - система счисления 
def f(n, base):
    s = ''
    while n !=0:
        s = str(n%base)+s
        n = n// base
    return s
### print(f(n, base))
lst = []
for N in range(1, 1000):
    n = f(N, 3)
    if N %3 ==0:
        n = n + n[-2:]
    else:
       n =  n + f(N % 3 * 5, 3)
    r = int(n, 3)
    if r > 133:
        lst.append(r)
print(min(lst))"""

"""for N in range(128, 256):
    n = bin(N)[2:].zfill(8) #добивает число в 2 записи чтобы было 8 цифр, например 1 в двоичной записи 1, а с zfill(8) 1= 00000001
    n1 = ''
    for i in n:
        if i == "1":
            n1 += "0"
        else:
            n1 += "1"
    r = int(n1, 2)
    ans = N-r
    if ans == 105:
        print(N)
"""


"""for N in range(1, 100):
    n= bin(N)[2:]
    if N%2==0:
        n = n+'0'+'1'
    else:
        n = n+'1'+'0'
    r = int(n,2)
    if r>102:
        print(r)
        break"""

"""for N in range(1, 10000):
    n= bin(N)[2:-1]
    if N%2!=0:
        n = n +'10'
    else:
        n = n +'01'
    r = int(n, 2)
    if r == 2017:
        print(N)
"""

"""for N in range(0, 256):
    n = bin(N)[2:].zfill(8)
    n1 = ''
    for i in n:
        if i == "1":
            n1 += "0"
        else:
            n1 += "1"
    r = int(n1, 2)
    if r-N==111:
        print(N)

   """

"""for N in range(1, 100):
    n = bin(N)[2:]
    if n.count('1') > n.count('0'):
        n = n +'1'
    else:
        n = n +'0'
    r = int(n,2)
    if r>100:
        print(r)
        break"""

"""for N in range(1, 100):
    n = bin(N)[2:]
    n = n + str(n.count('1')%2)
    n = n + str(n.count('1')%2)
    r =int(n,2)
    if r<50:
        print(r,N)"""

"""lst = []
for N in range(1000, 10000):
    s1,s2 = int(str(N)[0])+int(str(N)[1]), int(str(N)[2])+int(str(N)[3])
    s = str(max(s1,s2))+str(min(s1,s2))
    if s == '1311':
        lst.append(N)
print(min(lst))"""

"""for N in range(1, 1000):
    N = N-N%4
    n = bin(N)[2:]
    n = n + str(n.count('1')%2)
    n = n + str(n.count('1')%2)
    r = int(n,2)
    if r < 47:
        print(N, r)"""