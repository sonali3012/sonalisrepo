"""This file contains code to create a table with legs, and a cake on top of it with a candle and cherries using turtle."""

import turtle

s = turtle.Screen()
s.bgcolor("pink")    #background color

t = turtle.Turtle()

def table(width, height, color):  #making the table
    """Drawing a rectangular table.  The parameters are width, height and color."""

    t.pencolor(color)
    t.fillcolor(color)     
    t.begin_fill()
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.end_fill()


def draw_leg(legHeight, legWidth, color):
    """Drawing the table legs.  The parameters are the height, width and color"""

    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    t.left(90)
    t.forward(legHeight)
    t.left(90)
    t.forward(legWidth)
    t.left(90)
    t.forward(legHeight)
    t.end_fill()

def cake(cake_length, cake_height):
    """This function draws the cake.  It will take the length and height as parameters."""

    t.forward(cake_length)
    t.right(90)
    
    t.forward(cake_height)
    t.right(90)
    t.forward(cake_length*2)
    t.right(90)
    t.forward(cake_height)
    t.right(90)
    t.forward(cake_length)

def candle(candle_width, candle_height, candle_color):
    """This function creates a candle with parameters that take its width, height and color."""

    t.pencolor(candle_color)
    t.fillcolor(candle_color)
    t.begin_fill()
    t.right(90)
    t.forward(candle_height)
    t.right(90)
    t.forward(candle_width)
    t.right(90)
    t.forward(candle_height)
    t.end_fill()


def main():
    """The main function prompts users to give their input such as the length, width, hight and color of the table, legs, candle and cake."""

    width = int(input("Enter the width of the table from 10-250: "))
    height = int(input("Enter the height of the table from 10-30: "))  # Fixed height range
    color = input("Enter the color of the table: ")
    legHeight = int(input("Enter leg height from 10-50: "))
    legWidth = int(input("Enter the width of the leg from 10-20: "))
    cake_length = int(input("Enter the length of the cake.  It should be less than the width of the table: "))
    cake_height = int(input("Enter the height of the cake from 10-30: "))
    cake_color1 = input("Enter first color of the cake: ")
    cake_color2 = input("Enter second color of the cake: ")
    cake_color3 = input("Enter third color of the cake: ")
    candle_width = int(input("Enter the width of the candle from 10-15: "))
    candle_height = int(input("Enter the height of the candle from 10-20: "))
    candle_color = input("Enter the color of the candle: ")
    decoration_radius = int(input("Enter the radius of the cherry decoration from 5-10: "))
    decoration_color = input("Enter the color of the decoration: ")
    print("Your cake is loading...Happy Birthday!")
    print("Press and key to exit...")
    
    t.speed(10)
    
    
    table(width, height, color)  # Call the table function

    t.left(180)  #reposition the turtle
    t.forward(width)  # Move back to the starting position for the legs

    draw_leg(legHeight, legWidth, color) #call the leg function
    distance = (width/2) - legWidth #positioning the legs

    t.right(90)  # Positioning for the leg 2 
    t.forward(distance)  # Move to position for leg 2 
    t.left(180)  # Turn to face the correct direction
    draw_leg(legHeight, legWidth, color) #draw leg 2 

    t.right(90)   # Positioning for the leg 3 
    t.forward(width-legWidth)   # Move to position for leg 3
    t.left(180)  # Turn to face the correct direction
    draw_leg(legHeight, legWidth, color) # draw leg 3 
 
    t.right(90)    # Positioning for the leg 4 
    t.forward(distance-legWidth)   # Move to position for leg 4
    t.left(180)  # Turn to face the correct direction
    draw_leg(legHeight, legWidth, color) # draw leg 4 

    t.left(90)  # Move the turtle to the top of the table to draw the cake
    t.forward(width)    # Move to the center of the table
    t.right(90)    # Turn right to start drawing the cake layers

   # now we draw the layers of the cake
    t.penup()
    t.forward(height)   # Move to the top of the table
    t.pendown()

    t.left(90)
    t.pencolor(cake_color1)
    t.fillcolor(cake_color1)
    t.begin_fill()
    cake(cake_length, cake_height)
    t.end_fill()

    t.right(90)    # Turn right to position for the second layer
    t.penup()
    t.forward(cake_height)   # Move up to position for the second layer
    t.pendown()
    t.left(90)    # Turn left to face the correct direction
    t.pencolor(cake_color2)
    t.fillcolor(cake_color2)
    t.begin_fill()
    cake(cake_length, cake_height)
    t.end_fill()

    t.right(90)  # Turn right to position for the third layer
    t.penup()
    t.forward(cake_height)    # Move up to position for the third layer
    t.pendown()
    t.left(90)   # Turn left to face the correct direction
    t.pencolor(cake_color3)
    t.fillcolor(cake_color3)
    t.begin_fill()
    cake(cake_length, cake_height)
    t.end_fill()

    # draw the candle for the cake
    t.penup()
    t.right(90)  # Turn right to position above the cake
    t.forward(cake_height)    # Move above the cake
    t.left(90)    # Turn left to center the candle
    t.forward(candle_width/2)   # Center the candle
    candle(candle_width, candle_height, candle_color)

    # draw the cherry 1
    t.right(90)   # Turn right to position for decoration
    t.forward(cake_length/2 + candle_width/2)     # Position for decoration
    t.penup()
    t.right(90)    # Turn right to face the correct direction
    t.pencolor(decoration_color)
    t.forward(decoration_radius)   # Move to starting position for decoration
    t.fillcolor(decoration_color)
    t.begin_fill()
    t.circle(decoration_radius)
    t.end_fill()

    #draw cherry 2 
    t.penup()
    t.right(90)     # Turn right to position for the second decoration
    t.forward(cake_length)    # Move to position for the second decoration
    t.right(90)
    t.forward(decoration_radius/8)    # Adjust position for smaller circle
    t.begin_fill() 
    t.circle(decoration_radius)
    t.end_fill()
    t.hideturtle() # hide the turtle cursor 
    
main() #calling the main function

turtle.done()  #finished