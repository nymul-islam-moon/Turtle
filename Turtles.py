from turtle import *
from random import randint
#=============================
#forward(100)
#=============================

#==========================================
#write(0)
#forward(100)
#write(5)
#============================================

#===========================================
#write(0)
#forward(20)
#write(1)
#forward(20)
#write(2)
#forward(20)
#write(3)
#forward(20)
#write(4)
#forward(20)
#write(5)
#forward(20)
#===============================================

#================================================
speed(10)
penup()
goto(-140, 140)

for step in range(21):
    write(step)
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)


#==================================================creating turtles
ada = Turtle()
ada.color('red')
ada.shape('turtle')

ada.penup()
ada.goto(-160, 100)
ada.pendown()

#for turn in range(100):
 #   ada.forward(randint(1,7))

bob = Turtle()
bob.color('blue')
bob.shape('turtle')

bob.penup()
bob.goto(-160, 70)
bob.pendown()

dob = Turtle()
dob.color('yellow')
dob.shape('turtle')

dob.penup()
dob.goto(-160, 40)
dob.pendown()

cob = Turtle()
cob.color('pink')
cob.shape('turtle')

cob.penup()
cob.goto(-160, 10)
cob.pendown()

#===================================================

for turn in range(100):
    ada.forward(randint(1,7))
    bob.forward(randint(1,7))
    dob.forward(randint(1,7))
    cob.forward(randint(1,7))