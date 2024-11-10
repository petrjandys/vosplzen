import turtle

def vykresli(x, y, n):
    drawer = turtle.Turtle()
    drawer.speed(3)
    drawer.pensize(3)
    
    drawer.penup()
    drawer.goto(x, y)
    drawer.pendown()
    drawer.setheading(-60)  
    drawer.forward(85)      
    drawer.setheading(60)
    drawer.forward(85)
    
    drawer.penup()
    drawer.goto(x + 90, y)
    drawer.setheading(-90)  
    drawer.pendown()
    
    drawer.forward(60)
    drawer.circle(20, 180)  
    drawer.forward(60)
    
    side_length = 30  
    angle = 360 / n  
    
    drawer.penup()
    drawer.goto(x + 160, y - 10)  
    drawer.setheading(0)
    drawer.pendown()
    
    for _ in range(n):
        drawer.forward(side_length)
        drawer.right(angle)
    
    drawer.hideturtle()
    turtle.done()

screen = turtle.Screen()
screen.setup(width=500, height=400)  

vykresli(-125, 20, 7)
