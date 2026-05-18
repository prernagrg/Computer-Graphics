from tkinter import *
import math

# Create window
root = Tk()
root.title("2D Rotation Transformation")

canvas = Canvas(root, width=800, height=600, bg="white")
canvas.pack()

# Input original triangle coordinates
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))

x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

x3 = int(input("Enter x3: "))
y3 = int(input("Enter y3: "))

# Input rotation angle
angle = float(input("Enter rotation angle in degrees: "))

# Convert angle into radians
radian = math.radians(angle)

# Draw original triangle
canvas.create_line(x1, y1, x2, y2, fill="black")
canvas.create_line(x2, y2, x3, y3, fill="black")
canvas.create_line(x3, y3, x1, y1, fill="black")

# Apply rotation transformation
xr1 = x1 * math.cos(radian) - y1 * math.sin(radian)
yr1 = x1 * math.sin(radian) + y1 * math.cos(radian)

xr2 = x2 * math.cos(radian) - y2 * math.sin(radian)
yr2 = x2 * math.sin(radian) + y2 * math.cos(radian)

xr3 = x3 * math.cos(radian) - y3 * math.sin(radian)
yr3 = x3 * math.sin(radian) + y3 * math.cos(radian)

# Draw rotated triangle
canvas.create_line(xr1, yr1, xr2, yr2, fill="red")
canvas.create_line(xr2, yr2, xr3, yr3, fill="red")
canvas.create_line(xr3, yr3, xr1, yr1, fill="red")

print("Rotation Transformation Completed")

root.mainloop()