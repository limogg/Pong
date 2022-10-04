import turtle

wn = turtle.Screen()
wn.title("Pong by Piotr Janicki")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Wynik
score_a = 0
score_b = 0


#Paletka a
paletka_a = turtle.Turtle()
paletka_a.speed(0)
paletka_a.shape("square")
paletka_a.color("white")
paletka_a.shapesize(stretch_wid=5, stretch_len=1)
paletka_a.penup()
paletka_a.goto(-350, 0)

#Paletka b
paletka_b = turtle.Turtle()
paletka_b.speed(0)
paletka_b.shape("square")
paletka_b.color("white")
paletka_b.shapesize(stretch_wid=5, stretch_len=1)
paletka_b.penup()
paletka_b.goto(350, 0)
#Piłka
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Gracz A:0   Gracz B: 0", align="center", font=("Courier", 26, "bold"))

#funkcje
def paletka_a_up():
    y = paletka_a.ycor()
    y += 10
    paletka_a.sety(y)

def paletka_a_down():
    y = paletka_a.ycor()
    y -= 10
    paletka_a.sety(y)

def paletka_b_up():
    y = paletka_b.ycor()
    y += 10
    paletka_b.sety(y)

def paletka_b_down():
    y= paletka_b.ycor()
    y -= 10
    paletka_b.sety(y)
#input
wn.listen()
wn.onkeypress(paletka_a_up, "w")
wn.onkeypress(paletka_a_down, "s")
wn.onkeypress(paletka_b_up, "Up")
wn.onkeypress(paletka_b_down, "Down")

#główna pentla gry

while True:
    wn.update()

    #ruch
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #granice
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.dx *= -1
        score_a += 1
        ball.goto(0, 0)
        pen.clear()
        pen.write("Gracz A:{}   Gracz B: {}".format(score_a, score_b), align="center", font=("Courier", 26, "bold"))

    if ball.xcor() < -390:
        ball.dx *= -1
        score_b += 1
        ball.goto(0, 0)
        pen.clear()
        pen.write("Gracz A:{}   Gracz B: {}".format(score_a, score_b), align="center", font=("Courier", 26, "bold"))


    #odbicie a
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paletka_b.ycor() + 50 and ball.ycor() > paletka_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.ycor() > -350) and (ball.ycor() < paletka_a.ycor() + 50 and ball.ycor() > paletka_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1


