"""def f(A,x,y):
    return ((x<=9)<=(x*x<=A)) and ((y*y<=A)<=(y<=9))

for A in range(0,500):
    ok = True
    for x in range(0,1000):
        for y in range(0,1000):
            if f(A,x,y)==False:
                ok = False
                break
    if ok == True:
        print(A)"""

"""def f(A,x,y):
    return ((x<=9)<=(x*x<=A)) and ((y*y<=A) <= (y<=9))
for A in range(-1000, 1000):
    if all(f(A,x,y) for x in range(0,500) for y in range(0,500)):
        print(A)""" 



# 1 prototip
"""def f(A,x,y):
    return ((x<6)<=(x**2<A)) and ((y**2<=A) <= (y<=6))
cnt = 0
for A in range(-300, 300):
    if all(f(A,x,y)  for x in range(0,300) for y in range(0,300)):
        cnt+=1
print(cnt)"""

"""def f(A,x,y):
     return (2*x +3*y <A) or (x>y) or (y>24)
for A in range(0,1000):
     if all(f(A,x,y) for x in range(1000) for y in range(1000)):
          print(A)"""


# 2 prototip
"""
def f(A, x):
    return (x&29 !=0) <= ((x&17==0) <=( x&A !=0))

for A in range(0,300):
    if all(f(A,x) for x in range(0, 300)):
        print(A)

        break"""

# 3 prototip
"""
def d(n,m):
    return n%m==0

def f(A,x):
    return (not d(x,A))<=(d(x,6)<=(not d(x,4)))
for A in range(1, 300):
    if all(f(A,x) for x in range(1, 300)):
        print(A)"""

"""
def d(n,m):
    return n%m==0

def f(A,x):
    return d(70,A) and ((not d(x,A)) <= (d(x,35)<= (not d(x,63))))
for A in range(1, 300):
    if all(f(A,x) for x in range(1, 300)):
        print(A)"""


# otrezki 
"""
a = 0 #если ищем наибольший отрезок, то а=1, иначе а=0
f_usl = 1 #чему должна быть равна функция (истина или ложь)
for x in [k*0.25 for k in range(-10000, 10000)]:
    p = 130 <= x <= 171
    q = 150<=x<= 185
    f = p <= ((q and (not a)) <= (not p))
    if f != f_usl: # Если ищем наибольший отрезок то ==, иначе !=
        print(x)"""

# a = 0
# f_usl = 1
# for x in [k*0.25 for k in range(-10000, 10000)]:
#     p = 4 <= x <= 15
#     q = 12<=x<=20
#     f=(p and q) <= a
#     if f != f_usl:
#         print(x)

# a = 0
# f_usl = 1
# for x in [k*0.25 for k in range(-10000, 10000)]:
#     p = 130<=x<=171
#     q = 150<= x<=185
#     f = p<=((q and (not a)) <= (not p))
#     if f != f_usl:
#         print(x)

# a = 1
# f_usl = 1
# for x in [k*0.25 for k in range(-10000, 10000)]:
#     p = 5<=x<=30
#     q = 14<=x<=23
#     f = (p==q)<=(not a)
#     if f == f_usl:
#         print(x) 

