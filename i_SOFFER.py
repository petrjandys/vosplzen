import turtle as t

def vykresli(x, y, n):
    t.penup()
    t.goto(x, y)
    t.pensize(3)
    t.pencolor("blue")    
    t.pendown()
    
    #"J"
    t.forward(15)
    t.backward(30)
    t.forward(15)
    t.right(90)
    t.forward(50)
    t.circle(-10,200)
    t.penup()

    t.goto(x + 40, y)
    t.left(270)
    t.pendown()

    #"S"
    t.forward(5)
    t.backward(5)
    t.circle(-15, -185)
    t.circle(15, -250)


    side_length = 100 / (n)  
    angle = 360 / n  

    t.penup()
    t.goto(x + 70, y - 25)
    t.pencolor("red")  
    t.pendown()

    for _ in range(n):
        t.forward(side_length)
        t.left(angle)

    t.hideturtle()
    t.done()

vykresli(-100, 100, 5)  