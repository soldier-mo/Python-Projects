import turtle

#screen config
wind = turtle.Screen() 
wind.title("Ping Pong Game")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0) #stops window from updating automatically
wind.
#init racket1
racket1 = turtle.Turtle()
racket1.speed(0) #set the speed of the animation
racket1.shape("square")
racket1.color("blue")
racket1.shapesize(stretch_wid=5, stretch_len=1)
racket1.penup() #no drawing when moving
racket1.goto(-350,0)

#init racket2
racket2 = turtle.Turtle()
racket2.speed(0) #set the speed of the animation
racket2.shape("square")
racket2.color("red")
racket2.shapesize(stretch_wid=5, stretch_len=1)
racket2.penup() #no drawing when moving
racket2.goto(350,0)

#ball
ball = turtle.Turtle()
ball.speed(0) #set the speed of the animation
ball.shape("square")
ball.color("white")
ball.penup() #no drawing when moving
ball.goto(0, 0)
ball.dx = 0.05
ball.dy = 0.05

#score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write(f"{score1} | {score2}", align="center", font=("Courier",24,"normal"))

#functions
def racket1_up():
    y = racket1.ycor()
    y += 20
    racket1.sety(y)

def racket1_down():
    y = racket1.ycor()
    y -= 20
    racket1.sety(y)

def racket2_up():
    y = racket2.ycor()
    y += 20
    racket2.sety(y)

def racket2_down():
    y = racket2.ycor()
    y -= 20
    racket2.sety(y)

#key bindings
wind.listen()
wind.onkeypress(racket1_up,"w")
wind.onkeypress(racket1_down,"s")
wind.onkeypress(racket2_up,"Up")
wind.onkeypress(racket2_down,"Down")

# main game loop
while True:
    wind.update()

    # #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write(f"{score1} | {score2}", align="center", font=("Courier",24,"normal"))


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write(f"{score1} | {score2}", align="center", font=("Courier",24,"normal"))


    #check ball hit racket
    if (ball.xcor() > 340 and
         ball.xcor() <350 and
         (ball.ycor() < racket2.ycor() + 45 and
          ball.ycor() > racket2.ycor() -45)):
        ball.setx(335)
        ball.dx *= -1

    if (ball.xcor() < -340 and
        ball.xcor() > -350 and
        (ball.ycor() < racket1.ycor() + 45 and
        ball.ycor() > racket1.ycor() -45)):
            ball.setx(-335)
            ball.dx *= -1
