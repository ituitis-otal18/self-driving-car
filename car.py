from draw import *
import math
import time

drawPage()


def positionInfo(event):
    print(event.x, event.y)


class Sensors:

    distance = 100

    def __init__(self):
        self.startX = 0
        self.startY = 0
        self.foundX = 0
        self.foundY = 0
        self.targetX = 0
        self.targetY = 0
        self.line = 0

    def drawTarget(self, car, amount):
        self.startX = car.positionX - (amount * 15 * math.sin(car.angleRad))
        self.startY = car.positionY - (amount * 15 * math.cos(car.angleRad))
        self.targetX = self.startX + (self.distance * math.cos(car.angleRad))
        self.targetY = self.startY - (self.distance * math.sin(car.angleRad))

        self.line = canvas.create_line(self.startX,
                                       self.startY,
                                       self.targetX,
                                       self.targetY,
                                       fill="red")


class Car:
    isRunning = False
    angle = 0
    angleRad = 0

    width = 60
    height = 45

    positionX = 100
    positionY = 100

    def drawCar(self):
        self.angleRad = math.radians(self.angle)

        carImage = canvas.create_image(0, 0, image=carPNG)
        canvas.move(carImage, self.positionX, self.positionY)


def control(sensorA, sensorB):
    cond1 = False
    cond2 = False

    for i in range(Sensors.distance):
        A.foundX = sensorA.startX + (i * math.cos(araba.angleRad))
        A.foundY = sensorA.startY - (i * math.sin(araba.angleRad))
        B.foundX = sensorB.startX + (i * math.cos(araba.angleRad))
        B.foundY = sensorB.startY - (i * math.sin(araba.angleRad))

        if pix_val[A.foundX, A.foundY] == (0, 0, 0):
            # print("A :", sensorA.targetX, sensorA.targetY)
            canvas.create_oval(A.foundX - 5,
                               A.foundY - 5,
                               A.foundX + 5,
                               A.foundY + 5,
                               fill="blue")
            cond1 = True
            break

        if pix_val[B.foundX, B.foundY] == (0, 0, 0):
            # print("B :", sensorB.targetX, sensorB.targetY)
            canvas.create_oval(B.foundX - 5,
                               B.foundY - 5,
                               B.foundX + 5,
                               B.foundY + 5,
                               fill="blue")
            cond2 = True
            break

    if cond1 and not cond2:
        araba.angle -= 3

    if not cond1 and cond2:
        araba.angle += 3

    if not cond1 and not cond2:
        araba.positionX += 1 * math.cos(araba.angleRad)
        araba.positionY -= 1 * math.sin(araba.angleRad)

    if cond1 and cond2:
        x = 0
        while x < 30:
            araba.angle += 60
            araba.positionX -= 1 * math.cos(araba.angleRad)
            araba.positionY += 1 * math.sin(araba.angleRad)
            x += 1


def closeApp():
    Car.isRunning = False
    root.destroy()


def turnLeft(event):
    araba.angle += 5


def turnRight(event):
    araba.angle -= 5


def speedUp(event):
    araba.positionX += 5 * math.cos(araba.angleRad)
    araba.positionY -= 5 * math.sin(araba.angleRad)


# INITIALIZE
araba = Car()
A = Sensors()
B = Sensors()

root = Tk()
root.title('Artificially Intelligent Car')
root.geometry(screenResolution)
canvas = Canvas(root, width=900, height=600)
canvas.create_rectangle(2, 2, canvasWidth, canvasHeight, outline="red")
canvas.pack(side=LEFT, fill=BOTH)
button = tk.Button(root, text='Close', width=10, command=closeApp)
button.pack(side=RIGHT)

mapFile = Image.open("map.png")
pix_val = mapFile.load()
mapPNG = ImageTk.PhotoImage(mapFile)

carFile = Image.open("car.png")

root.bind("<Left>", turnLeft)
root.bind("<Right>", turnRight)
root.bind("<Up>", speedUp)
canvas.bind("<Button-3>", positionInfo)

Car.isRunning = True
# UPDATE
while Car.isRunning:
    canvas.delete("all")
    canvas.create_image(450, 300, image=mapPNG)

    A.drawTarget(araba, 1)
    B.drawTarget(araba, -1)
    control(A, B)

    carPNG = ImageTk.PhotoImage(carFile.rotate(araba.angle))
    araba.drawCar()

    time.sleep(0.01)
    root.update()
