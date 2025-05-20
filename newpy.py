import turtle
import time
import random

delay = 0.2

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("yellow")
wn.setup(width=600, height=600)
wn.tracer(0)


#snake head
head = turtle.Turtle()  
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)  #(x(left-right),y(up-down)) 
head.direction = "stop"

#snake food

food = turtle.Turtle() # object (snake food)
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

# score board
sc = turtle.Turtle()  
sc.speed(0)
sc.shape("square")
sc.color("black")
sc.penup()
sc.hideturtle()
sc.goto(0,260)
sc.write("score: 0  High score: 0", align = "center", font=("ds-digital", 24, "normal"))

# buttons
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"
def move():
    if head.direction == "up":
        y = head.ycor() #(0,0)
        head.sety(y+20) # (0,20) upwards
    if head.direction == "down":
        y = head.ycor() # (0,0)
        head.sety(y-20) # (0,-20)
    if head.direction == "left":
        x = head.xcor() # (0,0)
        head.setx(x-20) # (-20,0)
    if head.direction == "right":
        x = head.xcor() # (0,0)
        head.setx(x+20) # (20,0)

wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

score = 0
high_score = 0

while True:
    wn.update()
    if head.xcor()>270 or head.xcor()<-280 or head.ycor()>270 or head.ycor()<-270:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        
        for segment in segments:
            segment.goto(1000,1000) #out of range
        #clear the segments
        segments.clear()
        
        
        #reset score
        score = 0

        #reset delay
        delay = 0.1
        

        sc.clear()
        sc.write("score: {}  High score: {}".format(score, high_score), align="center", font=("ds-digital", 24, "normal"))
 
    move()
    if head.distance(food) <20:
        # move the food to random place
        x = random.randint(-270,270)
        y = random.randint(-270,270)
        food.goto(x,y)
        
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("black")
        new_segment.penup()
        segments.append(new_segment)
        
        
        delay -= 0.001
        #increase the score
        score += 10

        if score > high_score:
            high_score = score
        sc.clear()
        sc.write("score: {}  High score: {}".format(score,high_score), align="center", font=("ds-digital", 24, "normal")) 
        
        
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    #move segment 0 to head
    if len(segments)>0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
    time.sleep(delay)

