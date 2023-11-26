from drawbot_skia.drawbot import *

# задание 1 #

y = 150
# определим величину шага
step = 150
# напишем цикл для рисования:
for i in range(5):
    fill (0.4, 0.7, 0.1)
    rect(400, y, 100, 100)
    # внутри каждой итерации
    # будем увеличивать y на step
    y = y + step

# сохраним под новым именем
    saveImage("drawbot1.pdf")

# задание 2 #

newDrawing()   
x = 50
y = 50

radius = 50
step = 100

for col in range(6):
    for row in range(6):
        x = step + col * (radius + step)
        y = step + row * (radius + step)

        fill(0.1, 0.3, 1)
        oval (x, y, radius*2, radius*2)

saveImage("drawbot2.pdf")

# задание 3 #
newDrawing()   
size(500, 500)

step = 50
y = 300
 
    # Небо
fill(0.2, 0.6, 1)
rect(0, 0, 500, 500)
    
    # Трава
fill(0.5, 0.8, 0.2)
rect(0, 0, 500, 150)

    #Дом
fill(0.5, 0.4, 0.3)
polygon((150, y), (350, y), (250, y + step), close=True)
fill(0.6, 0.5, 0.4)
rect(150, 150, 200, 150)

    #Дверь
fill(0.5, 0.4, 0.3)
rect(180, 150, 50, 70)

    #Окно

fill(0.2, 0.6, 1)
rect(270, 220, 50, 50)

fill(1, 1, 1)
rect(270, 220, 50, 5)
rect(270, 270, 50, 5)
rect(270, 245, 50, 5)
rect(270, 220, 5, 50)
rect(320, 220, 5, 55)
rect(295, 220, 5, 55)

saveImage("drawbot3.pdf")
