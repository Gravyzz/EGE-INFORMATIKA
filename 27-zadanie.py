# f = open('text-27zadanie/1b.txt')
# N = int(f.readline())
# msum = 0
# dmin=[]
# for i in range(N):
#     a,b = map(int, f.readline().split())
#     msum+=max(a,b)
#     if abs(a-b)%3!=0:
#         dmin.append(abs(a-b))
# if msum%3!=0:
#     print(msum)
# else:
#     print(msum-min(dmin))


# f = open('text-27zadanie/3b.txt')
# n= int(f.readline())
# msum = 0
# dmin=[]
# for i in range(n):
#     a,b,c= sorted([int(x) for x in f.readline().split()])
#     msum+= c
#     if (c-a)%109!=0: dmin.append(c-a)
#     elif (c-b)%109!=0: dmin.append(c-b)
# if msum%109!=0:
#     print(msum)
# else:
#     print(msum-min(dmin))





# clasterA = [[],[]]
# for i in open('text-27zadanie/1a.txt'):
#     x,y=[float(k) for k in i.split()]
#     if x<2:
#         clasterA[0].append([x,y])
#     else:
#         clasterA[1].append([x,y])

# #Меняем условие
# clasterB = [[],[],[]]
# for i in open('text-27zadanie/1b.txt'):
#     x,y=[float(k) for k in i.split()]
#     if x>4:
#         clasterB[0].append([x,y])
#     elif y>2:
#         clasterB[1].append([x,y])
#     else:
#         clasterB[2].append([x,y])

# #Шаблон
# def dist(p1,p2):
#     x1,y1= p1
#     x2,y2= p2
#     return ((x2-x1)**2+(y2-y1)**2)**0.5

# def center(cl):
#     lst = []
#     for p in cl:
#         s = sum([dist(p,p1) for p1 in cl])
#         lst.append([s,p])
#     return min(lst)[1]

# #Выводим
# centerA = [center(cl) for cl in clasterA ]
# pxA = sum([x[0] for x in centerA])/2*10000
# pyA = sum([x[1] for x in centerA])/2*10000
# print(int(pxA),int (pyA))


# centerB = [center(cl) for cl in clasterB]
# pxB = sum([x[0] for x in centerB])/3*10000
# pyB = sum([x[1] for x in centerB])/3*10000
# print(int(pxB),int (pyB))






# clasterA = [[],[]]
# for i in open('text-27zadanie/2a.txt'):
#     x,y=[float(k) for k in i.split()]
#     if y<-1:
#         clasterA[0].append([x,y])
#     else:
#         clasterA[1].append([x,y])

# #Меняем условие
# clasterB = [[],[],[]]
# for i in open('text-27zadanie/1b.txt'):
#     x,y=[float(k) for k in i.split()]
#     if y>-0.9:
#         clasterB[0].append([x,y])
#     elif x<3:
#         clasterB[1].append([x,y])
#     else:
#         clasterB[2].append([x,y])

# #Шаблон
# def dist(p1,p2):
#     x1,y1= p1
#     x2,y2= p2
#     return ((x2-x1)**2+(y2-y1)**2)**0.5

# def center(cl):
#     lst = []
#     for p in cl:
#         s = sum([dist(p,p1) for p1 in cl])
#         lst.append([s,p])
#     return min(lst)[1]

# #Выводим
# centerA = [center(cl) for cl in clasterA ]
# pxA = sum([x[0] for x in centerA])/2*10000
# pyA = sum([x[1] for x in centerA])/2*10000
# print(int(pxA),int (pyA))


# centerB = [center(cl) for cl in clasterB]
# pxB = sum([x[0] for x in centerB])/3*10000
# pyB = sum([x[1] for x in centerB])/3*10000
# print(int(pxB),int (pyB))





# clasterA = [[], []]
# for i in open('text-27zadanie/1a.txt'):
#     x,y = [float(k) for k in i.split()]
#     if y>1.25*x+0.75:
#         clasterA[0].append([x,y])
#     else:
#         clasterA[1].append([x,y])

# clasterB = [[], [], []]
# for i in open('text-27zadanie/1b.txt'):
#     x,y = [float(k) for k in i.split()]
#     if y<-x+8:
#         clasterB[0].append([x,y])
#     elif y<x-2:
#         clasterB[1].append([x,y])
#     else:
#         clasterB[2].append([x,y])

# def dist(p1,p2):
#     x1,y1 = p1
#     x2,y2 = p2
#     return ((x1-x2)**2+(y1-y2)**2)**0.5
# def center(cl):
#     m = []
#     for p in cl:
#         s = sum([dist(p, p1) for p1 in cl])
#         m.append([s,p])
#     return min(m)[1]

    
# centerA = [center(x) for x in clasterA]
# pxA = sum([x[0] for x in centerA])/2*100000
# pyA = sum([x[1] for x in centerA])/2*100000
# print(int(pxA),int(pyA))

# centerB = [center(x) for x in clasterB]
# pxB = sum([x[0] for x in centerB])/3*100000
# pyB = sum([x[1] for x in centerB])/3*100000
# print(int(pxB),int(pyB))


# clasterA=[[], []]
# for i in open('text-27zadanie/3a.txt'):
#     x,y = [float(k) for k in i.split()]
#     if (y<-3 and x<1) or (y>5 and x>5):
#         pass
#     elif x<2 or y>5:
#         clasterA[0].append([x,y])
#     else:
#         clasterA[1].append([x,y])

# clasterB = [[],[],[]]
# for i in open('text-27zadanie/3b.txt'):
#     x,y = [float(k) for k in i.split()]
#     if( x<1.5 and y<1) or (y>9 and x>7):
#         pass
#     elif (y>1 and x<=3) or y>7.5:
#         clasterB[0].append([x,y])
#     elif (x>6.5 and y<5) or y<1:
#         clasterB[1].append([x,y])
#     else:
#         clasterB[2].append([x,y])


# def dist(p1,p2):
#     x1,y1 =p1
#     x2,y2=p2
#     return ((x1-x2)**2+(y1-y2)**2)**0.5
# def center(cl):
#     m = []
#     for p in cl:
#         s = sum([dist(p,p1) for p1 in cl])
#         m.append([s,p])
#     return min(m)[1]
    
# centerA = [center(x) for x in clasterA]
# pxA = sum([x[0] for x in centerA])/2*100000
# pyA = sum([x[1] for x in centerA])/2*100000
# print(int(pxA),int(pyA))
# centerB = [center(x) for x in clasterB]
# pxB = sum([x[0] for x in centerB])/3*100000
# pyB = sum([x[1] for x in centerB])/3*100000
# print(int(pxB),int(pyB))


# clasterA = [[],[]]
# for i in open('text-27zadanie/dz1a.txt'):
#     x,y = [float(x) for x in i.split()]
#     if ( x>-20 and x<20 and y>0 and y<40):
#         clasterA[0].append([x,y])
#     elif y<-40 and x>40:
#         clasterA[1].append([x,y])
#     else:
#         pass

# clasterB= [[],[],[]]
# for i in open('text-27zadanie/dz1b.txt'):
#     x,y = [float(k) for k in i.split()]
#     if (y<0 and y>-40 and x>-40 and x<0):
#         clasterB[0].append([x,y])
#     elif (y<-40 and x>-80 and x<-60):
#         clasterB[1].append([x,y])
#     elif (y<-60 and x>-20 and x<0):
#         clasterB[2].append([x,y])
#     else:
#         pass

# def dist(p1,p2):
#     x1,y1 = p1
#     x2,y2 = p2
#     return ((x1-x2)**2+(y1-y2)**2)**0.5
# def center(cl):
#     m = []
#     for p in cl:
#         s = sum([dist(p, p1) for p1 in cl])
#         m.append([s,p])
#     return min(m)[1]
# centerA = [center(x) for x in clasterA]
# pxA = sum([x[0] for x in centerA])/2*100
# pyA = sum([x[1] for x in centerA])/2*100
# print(int(pxA),int(pyA))

# centerB = [center(x) for x in clasterB]
# pxB = sum([x[0] for x in centerB])/3*100
# pyB = sum([x[1] for x in centerB])/3*100
# print(int(pxB), int(pyB))





# clasterA = [[],[],[],[],[]]
# for i in open('text-27zadanie/dz2a.txt'):
#     x,y = [float(k) for k in i.split()]
#     if (x<-5 and y<-5):
#         clasterA[0].append([x,y])
#     elif (y>-4.5 and x<0 and y<4):
#         clasterA[1].append([x,y])
#     elif (y>4 and y<10 and x<0) :
#         clasterA[2].append([x,y])
#     elif (x>0 and x<5 and y<10):
#         clasterA[3].append([x,y])
#     elif (x>5 and x<10 and y>0 and y<10):
#         clasterA[4].append([x,y])
#     else:
#         pass



# clasterB = [[],[],[],[]]
# for i in open('text-27zadanie/dz2b.txt'):
#     x,y = [float(k) for k in i.split()]
#     if -19<x<-8 and -26<y<-14:
#         clasterB[0].append([x,y])
#     elif -6<x<5 and 2<y<14:
#         clasterB[1].append([x,y])
#     elif x>5 and y>0:
#         clasterB[2].append([x,y])
#     elif -14<x<-3 and -11<y<2:
#         clasterB[3].append([x,y])
#     else:
#         pass


# def dist(p1,p2):
#     x1,y1 = p1
#     x2,y2 = p2
#     return ((x1-x2)**2+(y1-y2)**2)**0.5


# def center(cl):
#     m = []
#     for p in cl:
#         s = sum([dist(p, p1) for p1 in cl])
#         m.append([s,p])
#     return min(m)[1]

# centerA = [center(i) for i in clasterA]
# pxA = sum([x[0] for x in centerA])/5*100
# pyA = sum([x[1] for x in centerA])/5*100
# print(int(pxA), int(pyA))

# centerB = [center(i) for i in clasterA]
# pxB = sum([x[0] for x in centerB])/4*100
# pyB = sum([x[1] for x in centerB])/4*100
# print(int(pxB),int(pyB))

# c = 1
# from itertools import *
# for i in product('012345678', repeat=6):
#     s = ''.join(i)
    
#     if int(s)>99999:
#         if s[0] !="1" and s[0] !="3"  and s[0] !="5" and s[0] !="7"  :
#             if s[-1] != '2' and s[-1] != '3' and s.count('1')>=2:
#                 print(s, c)
#                 c+=1

