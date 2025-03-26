from turtle import *

#Команды основные
"""
forward() - fd() вперед
right() - rt() вправо
left() - lt() влево
down() - хвост опущен
"""


#Первая программа
"""
screensize(10000,10000)
tracer(0)
k = 50
down()
for i in range(5):
    fd(9*k)
    rt(120)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*k,y*k)
        dot(3, 'red')
exitonclick()"""

# №2
"""from turtle import *
screensize(10000,10000)
tracer(0)
k = 50
down()
for i in range(4):
    fd(5*k)
    rt(90)
    fd(10*k)
    rt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*k,y*k)
        dot(3, 'red')
exitonclick()"""

# №3

"""from turtle import *
screensize(10000,10000)
tracer(0)
k = 50
down()
for i in range(2):
    fd(6*k)
    rt(90)
    fd(12*k)
    rt(90)
up()
fd(1*k)
rt(90)
fd(3*k)
lt(90)
down()
for i in range(2):
    fd(77*k)
    rt(90)
    fd(45*k)
    rt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*k,y*k)
        dot(3, 'red')
exitonclick()"""

# №4
"""from turtle import *
screensize(10000, 10000)
tracer(0)
k = 50
down()
for i in range(7):
    fd(10*k)
    rt(120)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*k, y*k)
        dot(5, 'black')
exitonclick()"""

# №5

"""from turtle import *
screensize(10000, 10000)
tracer(0)
k = 50
down()
for i in range(4):
    fd(28*k)
    rt(90)
    fd(26*k)
    rt(90)
up()
fd(8*k)
rt(90)
fd(7*k)
rt(90)
down()
for i in range(4):
    fd(67*k)
    rt(90)
    fd(98*k)
    rt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*k, y*k)
        dot(5, 'black')
exitonclick()"""