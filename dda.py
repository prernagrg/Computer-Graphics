import turtle

def draw_axes(t, width=400, height=400):
    """Draw x and y axes"""
    t.penup()
    t.goto(-width, 0)
    t.pendown()
    t.goto(width, 0)
    
    # Draw y axis
    t.penup()
    t.goto(0, -height)
    t.pendown()
    t.goto(0, height)
    
    # Draw arrow heads and labels
    t.penup()
    t.goto(width - 10, -10)
    t.write("X", font=("Arial", 12, "normal"))
    
    t.goto(10, height - 10)
    t.write("Y", font=("Arial", 12, "normal"))
    
    # Draw tick marks
    t.penup()
    for i in range(-width, width, 50):
        t.goto(i, -5)
        t.pendown()
        t.goto(i, 5)
        t.penup()
    
    for i in range(-height, height, 50):
        t.goto(-5, i)
        t.pendown()
        t.goto(5, i)
        t.penup()

def DDA(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    # Determine steps
    steps = int(max(abs(dx), abs(dy)))
    if steps == 0:
        steps = 1  # To avoid division by zero

    # Calculate increment
    xinc = dx / steps
    yinc = dy / steps

    x = x1
    y = y1

    # Setup turtle and screen
    screen = turtle.Screen()
    screen.setup(800, 800)
    
    t = turtle.Turtle()
    t.speed(0)
    
    # Draw axes first
    draw_axes(t, 300, 300)
    
    # Draw the line
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("red")
    t.pensize(2)
    
    # Draw start point
    t.penup()
    t.goto(x1, y1)
    t.dot(8, "blue")
    t.penup()
    t.goto(x1 + 10, y1 + 10)
    t.write(f"({x1:.1f}, {y1:.1f})", font=("Arial", 10, "normal"))
    
    # Draw line using DDA
    t.penup()
    t.goto(x, y)
    t.pendown()
    for i in range(steps):
        x += xinc
        y += yinc
        t.goto(round(x), round(y))
    
    # Draw end point
    t.penup()
    t.goto(x2, y2)
    t.dot(8, "green")
    t.penup()
    t.goto(x2 + 10, y2 + 10)
    t.write(f"({x2:.1f}, {y2:.1f})", font=("Arial", 10, "normal"))
    
    t.penup()
    t.goto(0, -320)
    t.write(f"Line from ({x1:.1f}, {y1:.1f}) to ({x2:.1f}, {y2:.1f})", font=("Arial", 12, "normal"))

    turtle.done()


# Input from user
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

DDA(x1, y1, x2, y2)