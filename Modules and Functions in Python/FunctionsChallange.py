import math

try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

# Modify the circle function so that it allows the colour of the circle to be specified
# and defaults to red if a colour is not given. You may want to review the previous lecture
# about named parameters and default values.

def circle(page, radius, g, h, color="red"):
    page.create_oval(g + radius, h + radius, g - radius, h - radius, outline=color, width=2)


def draw_axes(page):
    page.update()
    x_origin = page.winfo_width() / 2
    y_origin = page.winfo_height() / 2
    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    page.create_line(-x_origin, 0, x_origin, 0, fill="black")
    page.create_line(0, y_origin, 0, -y_origin, fill="black")


mainWindow = tkinter.Tk()
mainWindow.title('Parabola')
mainWindow.geometry('640x480')

canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)

draw_axes(canvas)

circle(canvas, 100, 100, 100, "green")
circle(canvas, 100, 100, -100, "yellow")
circle(canvas, 100, -100, 100, "black")
circle(canvas, 100, -100, -100, "blue")
circle(canvas, 10, 30, 30)
circle(canvas, 10, 30, -30)
circle(canvas, 10, -30, 30)
circle(canvas, 10, -30, -30)
circle(canvas, 30, 0, 0)

mainWindow.mainloop()
