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

def bresenham(x1, y1, x2, y2):
    # Store original coordinates for labeling
    orig_x1, orig_y1, orig_x2, orig_y2 = x1, y1, x2, y2
    
    # Setup screen and turtle
    screen = turtle.Screen()
    screen.setup(800, 800)
    
    t = turtle.Turtle()
    t.speed(0)
    
    # Draw axes first
    draw_axes(t, 300, 300)
    
    # Draw start point
    t.penup()
    t.goto(x1, y1)
    t.dot(8, "blue")
    t.penup()
    t.goto(x1 + 10, y1 + 10)
    t.write(f"({orig_x1}, {orig_y1})", font=("Arial", 10, "normal"))

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1

    err = dx - dy

    # Draw line using Bresenham
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.color("red")
    t.pensize(2)
    
    while True:
        t.goto(x1, y1)
        t.dot(3)

        if x1 == x2 and y1 == y2:
            break

        e2 = 2 * err

        if e2 > -dy:
            err -= dy
            x1 += sx

        if e2 < dx:
            err += dx
            y1 += sy

    # Draw end point
    t.penup()
    t.goto(x2, y2)
    t.dot(8, "green")
    t.penup()
    t.goto(x2 + 10, y2 + 10)
    t.write(f"({orig_x2}, {orig_y2})", font=("Arial", 10, "normal"))
    
    t.penup()
    t.goto(0, -320)
    t.write(f"Bresenham Line from ({orig_x1}, {orig_y1}) to ({orig_x2}, {orig_y2})", font=("Arial", 12, "normal"))

    turtle.done()


# Input
x1 = int(float(input("Enter x1: ")))
y1 = int(float(input("Enter y1: ")))
x2 = int(float(input("Enter x2: ")))
y2 = int(float(input("Enter y2: ")))

bresenham(x1, y1, x2, y2)