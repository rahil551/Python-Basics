import turtle


wn = turtle.Screen()    #Creates the screen 
wn.title("First game")  #Title of the screen
wn.bgcolor("black")     #bgcolor of the screen
wn.setup(width =800, height = 600) #size of the screen
wn.tracer(0)

# paddle A
paddle_a = turtle.Turtle() #creates a turtle object
paddle_a.speed(0)          #speed = 0 means that no animation takes place
paddle_a.shape("square")    #shapes the turtle
paddle_a.color("Blue")      
paddle_a.shapesize(stretch_wid = 5,stretch_len = 1) #size of the turtle
paddle_a.penup() #moves the turtle without drawing
paddle_a.goto(-350,0) #moves the turtle to an absolute position

# paddle B
paddle_b = turtle.Turtle()   #creates a turtle object
paddle_b.speed(0)        #speed = 0 means that no animation takes place
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid = 5,stretch_len = 1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350,0)


# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.3  #the amount by which it would move in the x cordinate
ball.dy = 0.3  #the amount by which it would move in the x cordinate
 

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()  #it will hide the turtle.
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align="center",font =("courier",24, "normal")) #writes the scorecard

score_a = 0   #intializing the score
score_b = 0

# Function

def paddle_a_up():
  y = paddle_a.ycor()    #function to move the paddle_a up
  y += 20
  paddle_a.sety(y)


def paddle_a_down():
  y = paddle_a.ycor()   #function to move the paddle_a up
  paddle_a.sety(y)
  y -= 20
  paddle_a.sety(y)
  
  
def paddle_b_up():
  y = paddle_b.ycor() #function to move the paddle_b up
  paddle_b.sety(y)
  y += 20
  paddle_b.sety(y)

def paddle_b_down():
  y = paddle_b.ycor() #function to move the paddle_b up
  paddle_b.sety(y)
  y -= 20
  paddle_b.sety(y)
#   keyboard binding 
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
# main game loop
while True:

     wn.update()
     ball.setx(ball.xcor()+ball.dx)
     ball.sety(ball.ycor()+ball.dy)
    
     if ball.ycor()>290:
      ball.sety(290)
      ball.dy*= -1
      
     if ball.ycor()<-290:
      ball.sety(-290)
      ball.dy*= -1
     

     if ball.xcor()>390:
      ball.goto(0,0)
      ball.dx*= -1
      score_a += 1
      pen.clear()
      pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center",font =("courier",24, "normal"))
      
     if ball.xcor()<-390:
      ball.goto(0,0)
      ball.dx*= -1
      score_b += 1
      pen.clear()
      pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center",font =("courier",24, "normal"))
      

      # paddle collision
     if (ball.xcor() >340 and ball.xcor()< 350) and (ball.ycor() < paddle_b.ycor()+ 40 and ball.ycor() > paddle_b.ycor() - 40):
       ball.setx(340)
       ball.dx *= -1 
        
     if (ball.xcor()< -340 and ball.xcor() > - 350) and (ball.ycor() < paddle_a.ycor()+ 40 and ball.ycor() > paddle_a.ycor() - 40):
           ball.setx(-340)
           ball.dx *= -1 
          