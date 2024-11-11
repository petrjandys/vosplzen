import turtle

prijmeni = "Janda"
#vykreslení bude provedeno funkcí jejímž vstupem budou souřadnice levého horního rohu vykreslované oblasti
def vykresli(x, y, n): 
    screen = turtle.Screen()
    #velikost vykreslené plochy bude max 100*100px
    screen.setup(width=100, height=100)  
    #turtle má souřadnice 0,0 uprostřed obrazovky
    screen.setworldcoordinates(x, y - 100, x + 100, y)  
    
    t = turtle.Turtle()
    t.penup()    

    t.goto(x-75, y-25)
    t.write("PJ", font=("Arial", 30, "normal"))      
 
    t.goto(x, y - 30) 
    t.pendown()    
  
    n = len(prijmeni) # prijmeni = pocet uhlu
    angle = 360 / n
    t.pencolor("red")
    for _ in range(n):
        t.forward(50)  
        t.left(angle)
      
    t.hideturtle()       
    turtle.done()

vykresli(-100, 100, prijmeni)