import turtle
import random

pencere = turtle.Screen()
pencere.screensize(600, 600)
pencere.title("Kaplumbağa Yakalama")
pencere.bgcolor("blue")
pencere.tracer(2)
pencere.bgpic("cool1.gif")
# Create an instance of the turtle
oyuncu = turtle.Turtle()
oyuncu.color("white")
oyuncu.shape("triangle")
oyuncu.shapesize(3)

# oyuncu herhangi bir çizim yapmayacağı için kalemi kaldırdık
oyuncu.penup()
skor=0
skorPuan=turtle.Turtle()
skorPuan.speed(0)
skorPuan.shape("square")
skorPuan.color("white")
skorPuan.penup()
skorPuan.hideturtle()
skorPuan.goto(-200,200)
skorPuan.write('Puan: {}'.format(skor),align="center",font=("courier",24,"normal"))

speed = 1
hizPuan=turtle.Turtle()
hizPuan.speed(0)
hizPuan.shape("square")
hizPuan.color("white")
hizPuan.penup()
hizPuan.hideturtle()
hizPuan.goto(200,200)
hizPuan.write('Hız: {}'.format(speed),align="center",font=("courier",24,"normal"))

# Klavye kontrollerinin eklenmesi
def Soladon():
    oyuncu.left(30)

def Sagadon():
    oyuncu.right(30)

def HizArttir():
    global speed
    speed = speed + 1
    hizPuan.clear()
    hizPuan.write('Hız: {}'.format(speed), align="center", font=("courier", 24, "normal"))

def HizAzalt():
    global speed
    speed = max(speed - 1, 1)
    hizPuan.clear()
    hizPuan.write('Hız: {}'.format(speed), align="center", font=("courier", 24, "normal"))

pencere.listen()
pencere.onkey(fun=Soladon, key="Left")
pencere.onkey(fun=Sagadon, key="Right")
pencere.onkey(fun=HizArttir, key="Up")
pencere.onkey(fun=HizAzalt, key="Down")

MaxHedef = 5
hedefler = []
for i in range(MaxHedef):
    hedefler.append(turtle.Turtle())
    hedefler[i].penup()
    hedefler[i].color("red")
    hedefler[i].shape("turtle")
    hedefler[i].speed(0)
    hedefler[i].setposition(random.randint(-300, 300), random.randint(-300, 300))

while True:
    oyuncu.forward(speed)

    # oyuncu pencere dışına çıkarsa geri dönsün
    if oyuncu.xcor() > 300 or oyuncu.xcor() < -300:
        oyuncu.right(180)
    if oyuncu.ycor() > 300 or oyuncu.ycor() < -300:
        oyuncu.right(180)

    for i in range(MaxHedef):
        hedefler[i].forward(1)
        if hedefler[i].xcor()>500 or hedefler[i].xcor()<-500:
            hedefler[i].right(random.randint(150,250))
        if hedefler[i].ycor()>500 or hedefler[i].ycor()<-500:
            hedefler[i].right(random.randint(150,250))

        if oyuncu.distance(hedefler[i]) < 40:
            hedefler[i].setposition(random.randint(-300, 300), random.randint(-300, 300))
            hedefler[i].right(random.randint(0,360))
            skor +=1
            skorPuan.clear()
            skorPuan.write('Puan: {}'.format(skor), align="center", font=("courier", 24, "normal"))


turtle.done()
