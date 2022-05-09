# I could write turtle.Turtle.circle(100) to simplify i could write it as body = turtle.Turtle() and body.circle(100) on the next line

import turtle # imports turtle library

wn = turtle.Screen() # defines wn the class "Screen"

wn.bgcolor("lightblue") # Set the window background color

wn.title("Hello, I'm Dr. Subhajit!") # Set the window title




# ground

ground = turtle.Turtle() # defines ground as the class "Turtle" and makes a new turtle named ground

ground.fillcolor("green") # defines the fill color as green, to use in the later fill commands

ground.hideturtle() # hides the ground turtle head to make it look nicer

ground.pensize(3) # makes the turtle pen have a thickness of 3 to look better

ground.penup() # moves the turtle pen up so it doesn't write when it moves to the ground location

ground.goto(-400,-205) # tells the ground turtle to go to coordinates (-400,-205) to get ready to draw the ground

ground.pendown() # moves the turtle pen down so it it ready to begin drawing the ground

ground.begin_fill() # tells the turtle head to remember the starting point to execute a end_fill() command later for the ground

ground.forward(800) # draws the upper ground

ground.right(90) # turns to draw the right side of the ground, bc the fill command doesnt work if shape is not complete

ground.forward(200) # draws the right side of the ground

ground.right(90) # turns to draw the bottom side of the ground

ground.forward(800) # draws the bottom side of the ground

ground.right(90) # turns to draw the left side of the ground

ground.forward(200) # draws the left side of the ground

ground.end_fill() # tells the turtle head to fill in everything drawn from the begin_fill() point to the end_fill() point for the ground




# body

body = turtle.Turtle() # defines body as the class "Turtle" and makes a second turtle named body

body.hideturtle() # hides the body turtle head to make it look nicer

body.pensize(3) # makes the turtle pen have a thickness of 3 to look better

body.circle(100) # makes a circle with "100" as the radius for the head

body.right(90) # turns turtle head downward

body.forward(50) # makes the neck of the person

body.left(125) # turns turtle head right upward diagional facing to draw right arm

body.forward(75) # draws right arm 

body.left(180) # turns turtle head left downward diagional facing to return to arm vertex to get ready to draw left arm

body.forward(75) # returns turtle head to arm vertex to get reay to draws left arm 

body.right(70) # turns turtle head left upward diagional facing do draw left arm

body.forward(75) # draws left arm

body.left(180) # turns turtle head right downward diagional facing to return to arm vertex to get ready to draw lower body

body.forward(75) # returns to arm vertex to get ready to draw lower body

body.right(55) # turns turtle head downward facing to position to draw lower body

body.forward(100) # draws lower body

body.right(45) # turns turtle head left downward diagonal facing to draw left leg

body.forward(75) # draws left leg

body.right(180) # turns turtle head around to position to draw right leg

body.forward(75) # returns turtle head to vertex of legs to draw right leg

body.right(90) # turns turtle head right downward facing to draw right leg

body.forward(75) # draws right leg




# mouth

mouth = turtle.Turtle() # defines mouth as the class "Turtle" and makes a third turtle named mouth

mouth.hideturtle() # hides the mouth turtle head to make it look nicer

mouth.penup() # moves the turtle pen up so it doesn't write when it moves to the mouth location

mouth.goto(-45,65) # tells the mouth turtle to go to coordinates (-45,65) to get ready to draw the mouth

mouth.pendown() # moves the turtle pen down so it it ready to begin drawing the mouth

mouth.pensize(3) # makes the turtle pen have a thickness of 3 to look better

mouth.right(90) # turns the turtle head downward facing so that it is ready to begin drawing the mouth

mouth.circle(45, extent = 180) # draws a circle with the radius of 80 with the property of only drawing 180 degrees of the circle for the mouth




# eyes

eyes = turtle.Turtle() # defines eyes as the class "Turtle" and makes a fourth turtle named eyes

eyes.hideturtle() # hides the eyes turtle head to make it look nicer

eyes.penup() # moves the turtle pen up so it doesn't write when it moves to the left eye location

eyes.goto(-30,110) # tells eyes turtle to go to coordinates (-30,110) to get ready to draw the left eye

eyes.pendown() # moves the turtle pen down so it it ready to begin drawing the left eye

eyes.begin_fill() # tells the turtle head to remember the starting point to execute a end_fill() command later for the left eye

eyes.circle(12) # makes a circle with "12" as the radius for left eye

eyes.end_fill() # tells the turtle head to fill in everything drawn from the begin_fill() point to the end_fill() point for the left eye

eyes.penup() # moves the turtle pen up so it doesn't write when it moves to the the right eye location

eyes.goto(30,110) # tells eyes turtle to go to coordinates (30,110) to get ready to draw the right eye

eyes.pendown() # moves the turtle pen down so it it ready to begin drawing the right eye

eyes.begin_fill() # tells the turtle head to remember the starting point to execute a end_fill() command later for the right eye

eyes.circle(12) # makes a circle with "12" as the radius for the right eye

eyes.end_fill() # tells the turtle head to fill in everything drawn from the begin_fill() point to the end_fill() point for the right eye




# hat

hat = turtle.Turtle() # defines hat as the class "Turtle" and makes a sixth turtle named hat

hat.fillcolor("red") # defines the fill color as red, to use in the later fill commands

hat.hideturtle() # hides the ground turtle head to make it look nicer

hat.pensize(3) # makes the turtle pen have a thickness of 3 to look better

hat.penup() # moves the turtle pen up so it doesn't write when it moves to the hat location

hat.goto(-100, 150) # moves the turtle head to the hat starting location

hat.pendown() # moves the turtle pen down so it it ready to begin drawing the hat

hat.begin_fill() # tells the turtle head to remember the starting point to execute a end_fill() command later for the hat

hat.forward(250) # draws the bottom of the hat

hat.left(90) # turns to draw the right side of the hat, bc the fill command doesnt work if shape is not complete

hat.forward(10) # draws the right side of the hat

hat.left(90) # turns to draw the upper bill of the hat

hat.forward(40) # draws the upper bill of the hat

hat.right(90) # turns to draw the front portion of the hat

hat.forward(60) # draws the front portion of the hat

hat.left(90) # turns to draw the top of the hat

hat.forward(210) # draws the top of the hat

hat.left(90) # turns to draw the backside of the hat

hat.forward(70) # draws the backside of the hat

hat.end_fill() # tells the turtle head to fill in everything drawn from the begin_fill() point to the end_fill() point for the ground




# text

text = turtle.Turtle() # defines text as the class "Turtle" and makes a fifth turtle named text

text.hideturtle() # hides the text turtle head to make it look nicer

text.penup() # moves the turtle pen up so it doesn't write when it moves to the location to draw at

text.goto(-240,235) # tells text turtle to go to coordinates (-240,235) to get ready to write text

text.write("Hello! I'm Dr. Subhajit! Here is my Sierpinski Triangle!", font =("Comic Sans", 15, "bold")) # Writes "Hello! I'm Dr. Subhajit!" with size 15 point in Bold Comic Sans




# Triangle

triangle = turtle.Turtle() # defines triangle as the class "Turtle" and makes a sixth turtle named triangle

triangle.hideturtle() # hides the triangle turtle head to make it look nicer

triangle.penup() # moves the turtle pen up so it doesn't write when it moves to the triangle location

triangle.goto(45,-40) # tells the mouth turtle to go to coordinates (-45,65) to get ready to draw the triangle

triangle.pendown() # moves the turtle pen up so it doesn't write when it moves to the triangle location

triangle.pensize(3) # makes the turtle pen have a thickness of 3 to look better

def draw_sierpinski(length,depth): # defines the function draw_sierpinski with the values length and depth tp be called later on

    if depth==0: # base case (Single Triangle) used to make the 3 smaller triangle

        for i in range(0,3): # for function defined as i in the range to make 3 triangles based on this code, 0 to 3 or 1 2 and 3

            triangle.forward(length) # defines the forward command according to the length within the for function

            triangle.left(120) # defines the left command as 120 degrees within the for function
    else:
        draw_sierpinski(length/2,depth-1) # first triangle in the whole triangle

        triangle.forward(length/2) # defines the forward command according to the length/2

        draw_sierpinski(length/2,depth-1) # second triangle in the whole triangle

        triangle.backward(length/2) # defines the backward command according to the length/2

        triangle.left(60) # defines the left command as 60 degrees 

        triangle.forward(length/2) # defines the forward command according to the length/2

        triangle.right(60)# defines the right command as 60 degrees 

        draw_sierpinski(length/2,depth-1) # third trianle in the whole triangle

        triangle.left(60) # defines the left command as 60 degrees 

        triangle.backward(length/2) # defines the backward command according to the length/2

        triangle.right(60)# defines the right command as 60 degrees 

draw_sierpinski(100,2) # calls and defines the values of draw_sierpiski function to draw the whole triangle




turtle.done() # keeps window open 

# EXPLAIN WHAT THIS DOES