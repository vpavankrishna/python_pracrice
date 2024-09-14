import turtle as t

def rectangle(horizontal, vertical, color):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()

def draw_robot():
    t.speed("slow")
    t.bgcolor("Dodger blue")

    # Feet
    t.goto(-100, -150)
    rectangle(50, 20, 'blue')
    t.goto(-30, -150)
    rectangle(50, 20, 'blue')

    # Legs
    t.goto(-25, -50)
    rectangle(15, 100, 'grey')
    t.goto(-55, -50)
    rectangle(15, 100, 'grey')

    # Body
    t.goto(-90, 100)
    rectangle(100, 150, 'red')

    # Arms
    t.goto(-150, 70)
    rectangle(60, 15, 'grey')
    t.goto(-150, 110)
    rectangle(15, 40, 'grey')

    t.goto(10, 70)
    rectangle(60, 15, 'grey')
    t.goto(55, 110)
    rectangle(15, 40, 'grey')

    # Neck
    t.goto(-50, 120)
    rectangle(15, 20, 'grey')

    # Head
    t.goto(-85, 170)
    rectangle(80, 50, 'red')

    # Eyes
    t.goto(-60, 160)
    rectangle(30, 10, 'white')
    t.goto(-55, 155)
    rectangle(5, 5, 'black')
    t.goto(-40, 155)
    rectangle(5, 5, 'black')

    # Mouth
    t.goto(-65, 135)
    rectangle(40, 5, 'black')

    t.hideturtle()

# Run the drawing function
draw_robot()

# Close the turtle graphics window when clicked
t.exitonclick()
