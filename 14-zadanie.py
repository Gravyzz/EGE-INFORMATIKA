"""lst = []
base = 7
n = (77+7**77)*7**77+77+7**7
while n>0:
    lst.append(n%base)
    n = n//base
lst = lst[::-1]
print(lst.count(1))"""

"""lst = []
n = 2**51+2**40+2**35+2**17-2**5
base = 16
while n>0:
    lst.append(n%base)
    n = n//base
lst = lst[::-1]
print(lst)"""

"""lst = []
n = 256**2+4096**16-15
base = 16
while n>0:
    lst.append(n%base)
    n = n//base
print(lst.count(15))"""

"""for x in range(0,10):
    a = f'4c{x}4'
    b = f'{x}62a'
    r = int(a,15)+int(b,13)
    if r%121==0:
        print(r/121)"""

"""
lst = []
n = 7**103+6*7**104-3*7**57
base = 7
while n>0:
    lst.append(n%base)
    n = n//base
print(sum(lst))"""

