import turtle
import winsound


# Opsett
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Martin's Ping Pong")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.dx = 0.15
ball.dy = 0.15

# Scoreboard
player_1 = 0
player_2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.hideturtle()
score.penup()
score.goto(0, 250)
score.write(""+ str(player_1) +"     -     " + str(player_2), align="center", font=("Arial",25,"normal"))

# Move Paddle
def move_a_up():
    y = paddle_a.ycor()
    if y < 250:
        y += 20
        paddle_a.sety(y)

def move_a_down():
    y = paddle_a.ycor()
    if y > -250:
        y -= 20
        paddle_a.sety(y)

def move_b_up():
    y = paddle_b.ycor()
    if y < 250:
        y += 20
        paddle_b.sety(y)

def move_b_down():
    y = paddle_b.ycor()
    if y > -250:
        y -= 20
        paddle_b.sety(y)

# Controls
wn.listen()
wn.onkeypress(move_a_up, "w")
wn.onkeypress(move_a_down, "s")
wn.onkeypress(move_b_up, "Up")
wn.onkeypress(move_b_down, "Down")

# Main game loop
while True:
    wn.update()

    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border check med ball
    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy *= -1
        winsound.PlaySound("hit.wav", winsound.SND_ASYNC)

    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1
        winsound.PlaySound("hit.wav", winsound.SND_ASYNC)

    if ball.xcor() > 380:
        ball.goto(0, 0)
        ball.dx *= -1
        player_1 += 1
        score.clear()
        score.write(""+ str(player_1) +"     -     " + str(player_2), align="center", font=("Arial",25,"normal"))
        winsound.PlaySound("wine.wav", winsound.SND_ASYNC)

    if ball.xcor() < -380:
        ball.goto(0, 0)
        ball.dx *= -1
        player_2 += 1
        score.clear()
        score.write(""+ str(player_1) +"     -     " + str(player_2), align="center", font=("Arial",25,"normal"))
        winsound.PlaySound("wine.wav", winsound.SND_ASYNC)

    # Paddle check med ball
    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() <= (paddle_a.ycor() + 50) and  ball.ycor() >= (paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("hit.wav", winsound.SND_ASYNC)

    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() <= (paddle_b.ycor() + 50) and  ball.ycor() >= (paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("hit.wav", winsound.SND_ASYNC)

    if ball.xcor() > 345 and ball.xcor() < 360 and ball.ycor() >= (paddle_b.ycor() + 51) and  ball.ycor() <= (paddle_b.ycor() + 60):
        ball.sety(paddle_b.ycor() + 61)
        ball.dy *= -1
        ball.dx *= -1
        winsound.PlaySound("hit.wav", winsound.SND_ASYNC)

    if ball.xcor() < -345 and ball.xcor() > -360 and ball.ycor() >= (paddle_a.ycor() + 51) and  ball.ycor() <= (paddle_a.ycor() + 60):
        ball.sety(paddle_a.ycor() - 61)
        ball.dy *= -1
        ball.dx *= -1
        winsound.PlaySound("hit.wav", winsound.SND_ASYNC)

    if ball.xcor() > 345 and ball.xcor() < 360 and ball.ycor() <= (paddle_b.ycor() - 51) and  ball.ycor() >= (paddle_b.ycor() - 60):
        ball.sety(paddle_b.ycor() + 61)
        ball.dy *= -1
        ball.dx *= -1
        winsound.PlaySound("hit.wav", winsound.SND_ASYNC)

    if ball.xcor() < -345 and ball.xcor() > -360 and ball.ycor() <= (paddle_a.ycor() - 51) and  ball.ycor() >= (paddle_a.ycor() - 60):
        ball.sety(paddle_a.ycor() - 61)
        ball.dy *= -1
        ball.dx *= -1
        winsound.PlaySound("hit.wav", winsound.SND_ASYNC)


