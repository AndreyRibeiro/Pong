import turtle

wn = turtle.Screen()
wn.title("Pong por AndreyRibeiro")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Barra A
barra_a = turtle.Turtle()
barra_a.speed(0)
barra_a.shape("square")
barra_a.color("white")
barra_a.shapesize(stretch_wid=5, stretch_len=1)
barra_a.penup()
barra_a.goto(-350, 0)

# Barra B
barra_b = turtle.Turtle()
barra_b.speed(0)
barra_b.shape("square")
barra_b.color("white")
barra_b.shapesize(stretch_wid=5, stretch_len=1)
barra_b.penup()
barra_b.goto(350, 0)

# Bola
bola = turtle.Turtle()
bola.speed(0)
bola.shape("square")
bola.color("white")
bola.penup()
bola.goto(0, 0)
bola.dx = 0.2
bola.dy = 0.2

# Texto
pon = turtle.Turtle()
pon.speed(0)
pon.color("white")
pon.penup()
pon.hideturtle()
pon.goto(0, 260)
pon.write("Jogador A: 0   Jogador B: 0", align="center", font=("Courier", 20, "normal"))

# Pontuação
pontos_a = 0
pontos_b = 0

# Funções
def barra_a_cima():
    y = barra_a.ycor()
    y += 20
    barra_a.sety(y)

def barra_a_baixo():
    y = barra_a.ycor()
    y += -20
    barra_a.sety(y)

def barra_b_cima():
    y = barra_b.ycor()
    y += 20
    barra_b.sety(y)

def barra_b_baixo():
    y = barra_b.ycor()
    y += -20
    barra_b.sety(y)

# Binds
wn.listen()
wn.onkeypress(barra_a_cima, "w")
wn.onkeypress(barra_a_baixo, "s")
wn.onkeypress(barra_b_cima, "Up")
wn.onkeypress(barra_b_baixo, "Down")

# Loops
while True:
    wn.update()

    # Movimento da bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    # Bordas
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1

    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1

    if bola.xcor() > 390:
        bola.goto(0, 0)
        bola.dx *= -1
        pontos_a += 1
        pon.clear()
        pon.write("Jogador A: {}   Jogador B: {}".format(pontos_a, pontos_b), align="center", font=("Courier", 20, "normal"))

    if bola.xcor() < -390:
        bola.goto(0, 0)
        bola.dx *= -1
        pontos_b += 1
        pon.clear()
        pon.write("Jogador A: {}   Jogador B: {}".format(pontos_a, pontos_b), align="center", font=("Courier", 20, "normal"))

    # Colisão das barras e da bola
    if (bola.xcor() > 340 and bola.xcor() < 350) and (bola.ycor() < barra_b.ycor() + 40 and bola.ycor() > barra_b.ycor() -40):
        bola.setx(340)
        bola.dx *= -1

    if (bola.xcor() < -340 and bola.xcor() > -350) and (bola.ycor() < barra_a.ycor() + 40 and bola.ycor() > barra_a.ycor() -40):
        bola.setx(-340)
        bola.dx *= -1
