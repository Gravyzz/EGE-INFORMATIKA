#Одна куча
"""def f(s,n):
    if s>=74: return n%2 == 0
    if n ==0: return 0
    h = [f(s+1, n-1), f(s+2, n-1), f(s*3,n-1)]
    return any(h) if (n-1)%2==0 else all (h)

print([s for s in range(1, 74) if f(s,2)])
print([s for s in range(1,74) if not f(s,1) and f(s,3)])
print([s for s in range(1,74) if not f(s,2) and f(s,4)])"""


"""def f(s,n):
    if s>=25: return n%2==0
    if n==0:return 0
    h = [f(s+2,n-1), f(s*2, n-1)]
    return any(h) if (n-1)%2==0 else all(h)

print([s for s in range(1, 25) if f(s,2)])
print([s for s in range(1, 25) if not f(s,1) and f(s,3)])
print([s for s in range(1, 25) if not f(s,2) and f(s,4)])
"""

"""def f(s,n):
    if s>=50: return n%2==0
    if n==0:return 0
    h = [f(s+2,n-1), f(s*3, n-1)]
    return any(h) if (n-1)%2==0 else all(h)

print([s for s in range(1, 50) if f(s,2)])
print([s for s in range(1, 50) if not f(s,1) and f(s,3)])
print([s for s in range(1, 50) if not f(s,2) and f(s,4)])"""

"""def f(s,n):
    if s>=1000: return n%2==0
    if n==0:return 0
    h = [f(s+100,n-1), f(s*2, n-1)]
    return any(h) if (n-1)%2==0 else all(h)

print(len([s for s in range(1, 1000) if f(s,2)]))
print(len([s for s in range(1, 1000) if f(s,3)]))
print(min([s for s in range(1, 1000) if  f(s,2) or  f(s,4)]))"""

#Две кучи

"""def f(a,s,n):
    if a+s>=45: return n%2==0
    if n==0: return 0
    h = [f(a+1,s,n-1),f(a,s+1,n-1),f(a*3,s,n-1),f(a,s*3,n-1)]
    return any(h) if (n-1)%2==0 else all(h)

print([s for s in range(1,41) if f(4,s,2)])
print([s for s in range(1,41) if not f(4,s,1) and f(4,s,3)])
print([s for s in range(1,41) if not f(4,s,2) and f(4,s,4)])
"""

"""def f(a,s,n):
    if a+s>=77: return n%2==0
    if n ==0: return 0
    h = [f(a+1,s,n-1),f(a,s+1,n-1),f(a*2,s,n-1),f(a,s*2,n-1)]
    return any(h) if (n-1) % 2 == 0 else all(h)

print([s for s in range(1,70) if f(7,s,2)])
print([s for s in range(1,70) if not f(7,s,1) and f(7,s,3)])
print([s for s in range(1,70) if not f(7,s,2) and f(7,s,4)])"""


#дз два условия для куч(усложнение)
"""def f(a,s,n):
    if 60<=a+s<=79: return n%2 == 0 
    if a+s>79: return n%2 != 0
    if n==0: return 0
    h = [f(a+1, s,n-1),f(a,s+1,n-1),f(a*3, s,n-1),f(a, s*3,n-1)]
    return any(h) if (n-1)%2==0 else all(h)

print([s for s in range(1,52) if f(8,s,2)])
print([s for s in range(1,52) if not f(8,s,1) and f(8,s,3)])
print([s for s in range(1,52) if not f(8,s,2) and f(8,s,4)])"""

