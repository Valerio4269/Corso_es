import turtle

# Funzione per disegnare una griglia bianca
def draw_white_grid():
    turtle.penup()
    turtle.goto(-300, -300)
    turtle.pendown()
    turtle.color("white")
    turtle.pensize(5)
    
    for _ in range(24):
        for _ in range(24):
            turtle.forward(20)
            turtle.right(90)
            turtle.forward(20)
            turtle.left(90)
        turtle.penup()
        turtle.goto(turtle.xcor(), turtle.ycor() + 20)
        turtle.setheading(180)
        turtle.pendown()

# Funzione per controllare se la turtle è sopra una casella bianca
def check_intersection():
    # Posizione attuale della turtle
    x, y = turtle.position()
    
    # Colore del pixel sotto la turtle
    color = turtle.getcanvas().getpixel((int(x), int(y)))
    print(color)
    # Restituisci True se il colore è bianco, altrimenti False
    return color == (255, 255, 255)

# Inizializzazione della turtle
turtle.speed(0)
turtle.penup()

# Disegno di una griglia bianca
draw_white_grid()

# Aggiunta della funzione check_intersection come callback per il movimento della turtle
turtle.ondrag(check_intersection)

# Avvio del ciclo di ascolto degli eventi della turtle
turtle.mainloop()
