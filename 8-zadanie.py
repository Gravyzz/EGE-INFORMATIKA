from itertools import *

"""for i in product("НРТУ", repeat = 4):
    s = ''.join(i)
    print(s)"""

"""c = 0
for i in product("МЕТРО", repeat=4):
    s = ''.join(i)
    if s[0] in "ЕО" and s[3] in "МТР":
        c+=1
print(c)"""

"""c = 0
for i in product("ГОД", repeat=6):
    s = ''.join(i)
    if s[0] in "ГД" and s[-1] in "ГД":
        c+=1
    print(c, s)"""

"""c = 0
for i in product("ABCX", repeat=5):
    s = ''.join(i)
    if (s[0] in "X"  and s.count("X") == 1 ) or (s.count("X") == 0):
        c +=1
        print(s, c, s.count("X"))"""

"""lst = []
for i in permutations("ТИКТОК"):
    s = ''.join(i)
    if s[0]!=s[1]!=s[2]!=s[3]!=s[4]!=s[5]:
        lst.append(s)
print(len(set(lst)))"""

"""lst = []
for i in permutations("КЛАБХАУС"):
    s = ''.join(i)
    if s[0] != s[1] != s[2] != s[3] != s[4] !=s [5] != s[6] != s[7]:
        lst.append(s) 
print(set(lst), len(set(lst)))"""

"""
lst = []
for i in product("ABX", repeat=6):
    s = "".join(i)
    if s.count("X") == 1 and (s.count("A") >=1 or s.count("A") ==0) and (s.count("B") >=1 or s.count("B") ==0):
        lst.append(s)
print(lst, len(lst))"""

"""lst = []
for i in product("ABCDEF", repeat = 5):
    s = ''.join(i)
    if s[0] != "F" and s[-1] != "A":
        lst.append(s)
print(lst, len(lst))"""

"""
lst = []
for i in product(range(12), repeat=5):
    if i[0] != 0 and i.count(7) == 1  and (i.count(9)+i.count(10)+i.count(1)) <= 3:
        lst.append(i)
print(lst, len(lst))"""

"""
lst = []
for i in product(range(14), repeat = 5):
    if i[0] != 0 and i.count(9) == 1 and sorted(i)[-4]<=10:
        lst.append(i)
print(lst, len(lst))"""


"""c = 1
for i in product("АМУХ", repeat = 4):
    s = ''.join(i)
    if s == "ХУХХ":
        print(s, c)
    c +=1"""

"""from itertools import * 
c = 1 
for i in product('ВИНТ', repeat=5): 
    s = ''.join(i)
    if s == "ИТТВТ":
        print(c, s) 
    c += 1"""


# from itertools import *
# c= 0
# for i in product('ШКОЛА', repeat= 3):
#     s = ''.join(i)
#     if s.count('К')==1:
#         c+=1
# print(c) 

# from itertools import *

# c=0
# for i in product('АВСХ', repeat=5):
#     s = ''.join(i)
#     if (s[0]=='Х' and s.count("Х")==1 ) or s.count("Х")==0:
#         c+=1
# print(c)


# from itertools import *
# c = 0
# for i in product(range(16), repeat=5):
#     if i[0] !=1 and i[-1]%2!=0 and i[0] !=0:
#         c+=1
# print(c)


# from itertools import *
# c =0
# for i in permutations(range(8), r=5):
#     if i.count(1)==0 and i[0] != 0:
#         if i[0]%2!=i[1]%2!=i[2]%2!=i[3]%2!=i[4]%2:
#             c+=1
# print(c)




