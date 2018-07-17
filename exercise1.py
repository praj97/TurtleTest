import turtle 

def moveTurt():
    turt.forward(50)
    turt.left(135)
    turt.forward(50)
    turt.forward(100)
def backTurt():
    turt.backward(50)    
    turt.left(180)

wn=turtle.Screen()
turt=turtle.Turtle()
turt.shape("turtle")
turt.speed(0)
turt.right(135)
for i in range(10,350):
        turt.forward(i)
        turt.left(90)
turt.color('red')
turt.penup()
turt.right(315)
turt.forward(250)
turt.pendown()
for i in range(10,150):
        turt.forward(i)
        turt.left(225)          
    
turt.hideturtle()
wn.mainloop()