from tkinter import *

# Create window
root = Tk()
root.title("2D Translation Transformation")

canvas = Canvas(root, width=800, height=600, bg="white")
canvas.pack()

# Input triangle coordinates
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))

x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

x3 = int(input("Enter x3: "))
y3 = int(input("Enter y3: "))

# Input translation factors
tx = int(input("Enter translation factor tx: "))
ty = int(input("Enter translation factor ty: "))

# Draw original triangle
canvas.create_line(x1, y1, x2, y2, fill="black")
canvas.create_line(x2, y2, x3, y3, fill="black")
canvas.create_line(x3, y3, x1, y1, fill="black")

# Apply translation
tx1 = x1 + tx
ty1 = y1 + ty

tx2 = x2 + tx
ty2 = y2 + ty

tx3 = x3 + tx
ty3 = y3 + ty

# Draw translated triangle
canvas.create_line(tx1, ty1, tx2, ty2, fill="red")
canvas.create_line(tx2, ty2, tx3, ty3, fill="red")
canvas.create_line(tx3, ty3, tx1, ty1, fill="red")

print("Translation Completed")

root.mainloop()