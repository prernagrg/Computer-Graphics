from tkinter import *

# Create window
root = Tk()
root.title("2D Scaling Transformation")

canvas = Canvas(root, width=800, height=600, bg="white")
canvas.pack()

# Input original triangle coordinates
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))

x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

x3 = int(input("Enter x3: "))
y3 = int(input("Enter y3: "))

# Input scaling factors
sx = float(input("Enter scaling factor sx: "))
sy = float(input("Enter scaling factor sy: "))

# Draw original triangle
canvas.create_line(x1, y1, x2, y2, fill="black")
canvas.create_line(x2, y2, x3, y3, fill="black")
canvas.create_line(x3, y3, x1, y1, fill="black")

# Apply scaling transformation
sx1 = x1 * sx
sy1 = y1 * sy

sx2 = x2 * sx
sy2 = y2 * sy

sx3 = x3 * sx
sy3 = y3 * sy

# Draw scaled triangle
canvas.create_line(sx1, sy1, sx2, sy2, fill="red")
canvas.create_line(sx2, sy2, sx3, sy3, fill="red")
canvas.create_line(sx3, sy3, sx1, sy1, fill="red")

print("Scaling Transformation Completed")

root.mainloop()