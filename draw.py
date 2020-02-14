from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image, ImageDraw
import PIL

screenWidth = 1120
screenHeight = 630
screenResolution = "1120x630"
canvasWidth = 900
canvasHeight = 600


def drawPage():
    class Line:
        Color = "black"
        Size = 10

    def changeColor(colour):
        Line.Color = colour

    def changeSize(amount):
        Line.Size = Line.Size + amount

    def save():
        filename = "map.png"
        image.save(filename)

    def paint(event):
        x1, y1 = (event.x - Line.Size*2), (event.y - Line.Size*2)
        x2, y2 = (event.x + Line.Size*2), (event.y + Line.Size*2)
        canvas.create_oval(x1, y1, x2, y2, outline=Line.Color, fill=Line.Color)
        draw.ellipse([x1, y1, x2, y2], fill=Line.Color)

    window = tk.Tk()
    window.title('Drawing App')
    window.geometry(screenResolution)

    button0 = tk.Button(window, text='Car ->', width=10, command=window.destroy)
    button1 = tk.Button(window, text='Save', width=10, command=save)
    button2 = tk.Button(window, text='Red', width=10, command=lambda: changeColor("red"))
    button3 = tk.Button(window, text='Green', width=10, command=lambda: changeColor("green"))
    button4 = tk.Button(window, text='Blue', width=10, command=lambda: changeColor("blue"))
    button5 = tk.Button(window, text='Black', width=10, command=lambda: changeColor("black"))
    button6 = tk.Button(window, text='Size +', width=10, command=lambda: changeSize(2))
    button7 = tk.Button(window, text='Size -', width=10, command=lambda: changeSize(-2))
    canvas = tk.Canvas(window, width=canvasWidth, height=canvasHeight)
    canvas.pack(side=LEFT)
    button0.pack(side=BOTTOM, fill=BOTH)
    button1.pack(side=BOTTOM, fill=BOTH)
    button2.pack(side=TOP, fill=BOTH)
    button3.pack(side=TOP, fill=BOTH)
    button4.pack(side=TOP, fill=BOTH)
    button5.pack(side=TOP, fill=BOTH)
    button6.pack(side=TOP, fill=BOTH)
    button7.pack(side=TOP, fill=BOTH)

    canvas.create_rectangle(2, 2, canvasWidth, canvasHeight, outline="red")
    image = PIL.Image.new("RGB", (canvasWidth, canvasHeight), "white")
    draw = ImageDraw.Draw(image)

    canvas.bind("<B1-Motion>", paint)
    window.mainloop()
