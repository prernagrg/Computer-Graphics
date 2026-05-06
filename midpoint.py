import turtle
import time

GRID_STEP = 50
GRID_LIMIT = 300


def setup_screen():
    screen = turtle.Screen()
    screen.title("Midpoint Circle Drawing Algorithm")
    screen.setup(800, 800)
    screen.setworldcoordinates(-350, -350, 350, 350)
    screen.tracer(False)
    return screen


def draw_grid(t, limit=GRID_LIMIT, step=GRID_STEP):
    t.color("#d9d9d9")
    t.pensize(1)

    for x in range(-limit, limit + 1, step):
        t.penup()
        t.goto(x, -limit)
        t.pendown()
        t.goto(x, limit)

    for y in range(-limit, limit + 1, step):
        t.penup()
        t.goto(-limit, y)
        t.pendown()
        t.goto(limit, y)


def draw_axes(t, limit=GRID_LIMIT):
    t.color("black")
    t.pensize(2)

    t.penup()
    t.goto(-limit, 0)
    t.pendown()
    t.goto(limit, 0)

    t.penup()
    t.goto(0, -limit)
    t.pendown()
    t.goto(0, limit)

    t.penup()
    t.goto(limit - 20, -20)
    t.write("X", font=("Arial", 12, "normal"))
    t.goto(-limit + 10, -20)
    t.write("-X", font=("Arial", 12, "normal"))
    t.goto(10, limit - 20)
    t.write("Y", font=("Arial", 12, "normal"))
    t.goto(10, -limit + 10)
    t.write("-Y", font=("Arial", 12, "normal"))


def draw_octants(t, offset=70):
    t.color("#1a1a1a")
    labels = [
        ((offset, offset), "1"),
        ((-offset, offset), "2"),
        ((-offset, -offset), "3"),
        ((offset, -offset), "4"),
        ((offset * 2, offset // 2), "5"),
        ((-offset * 2, offset // 2), "6"),
        ((-offset * 2, -offset // 2), "7"),
        ((offset * 2, -offset // 2), "8"),
    ]

    for (x, y), label in labels:
        t.penup()
        t.goto(x, y)
        t.write(label, align="center", font=("Arial", 11, "bold"))


screen = setup_screen()

pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()

draw_grid(pen)
draw_axes(pen)
draw_octants(pen)

def put_pixel(x, y):
    pen.goto(x, y)
    pen.dot(4)  # draw a small dot

def draw_circle(h, k, r):
    x = 0
    y = r
    p = 1 - r  # Initial decision parameter

    while x <= y:
        # Plot all 8 symmetric points
        put_pixel(x + h, y + k)
        put_pixel(-x + h, y + k)
        put_pixel(x + h, -y + k)
        put_pixel(-x + h, -y + k)

        put_pixel(y + h, x + k)
        put_pixel(-y + h, x + k)
        put_pixel(y + h, -x + k)
        put_pixel(-y + h, -x + k)

        time.sleep(0.05)  # delay like delay(100)

        x += 1

        if p < 0:
            p = p + 2 * x + 1
        else:
            y -= 1
            p = p + 2 * (x - y) + 1


# Input from user
h = int(input("Enter center h: "))
k = int(input("Enter center k: "))
r = int(input("Enter radius: "))

draw_circle(h, k, r)

screen.tracer(True)
screen.update()

turtle.done()