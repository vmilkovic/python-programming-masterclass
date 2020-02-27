import tkinter

# print(tkinter.TkVersion)
# print(tkinter.TclVersion)

mainWindow = tkinter.Tk()
mainWindow.title("Hello World")
mainWindow.geometry('640x480')
# mainWindow.geometry('640x480+8+400')

label = tkinter.Label(mainWindow, text="Hello World")
label.pack(side='top')

leftFrame = tkinter.Frame(mainWindow)
leftFrame.pack(side="left", anchor="n", fill=tkinter.Y, expand=False)

canvas = tkinter.Canvas(leftFrame, relief="raised", borderwidth=1)
# canvas.pack(side='left', fill=tkinter.BOTH, expand=True)
canvas.pack(side="left", anchor="n")

rightFrame = tkinter.Frame(mainWindow)
rightFrame.pack(side="right", anchor="n", expand=True)

button1 = tkinter.Button(rightFrame, text="button1")
button2 = tkinter.Button(rightFrame, text="button2")
button3 = tkinter.Button(rightFrame, text="button3")

button1.pack(side="top")
button2.pack(side="top")
button3.pack(side="top")

mainWindow.mainloop()


