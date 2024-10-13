"""
Group Members:
Sonali Bugwandin  repo: https://github.com/sonali3012/sonalisrepo.git
Aydin Huseynov repo: https://github.com/NupNupp/lunch.git
Abi Alakunta
"""

import turtle

""" Initialize turtle screen and turtle object"""
s = turtle.Screen()
turta = turtle.Turtle()

# Part 1 - 1: Get color based on character input
def get_color(character):
    if character == '0':
        return 'black'
    elif character == '1':
        return 'white'
    elif character == '2':
        return 'red'
    elif character == '3':
        return 'yellow'
    elif character == '4':
        return 'orange'
    elif character == '5':
        return 'green'
    elif character == '6':
        return 'yellowgreen'
    elif character == '7':
        return 'sienna'
    elif character == '8':
        return 'tan'
    elif character == '9':
        return 'gray'
    elif character == 'A':
        return 'darkgray'
    else:
        return None

# Part 1 - 2: Draw a colored pixel based on the color string
def draw_color_pixel(color_string, turta):
    turta.fillcolor(color_string)
    turta.begin_fill()
    for _ in range(2):  # Draw a 20x20 pixel
        turta.forward(20)
        turta.right(90)
        turta.forward(20)
        turta.right(90)
    turta.forward(20)
    turta.end_fill()

# Part 1 - 3: Draw pixel by character
def draw_pixel(character, turta):
    color_string = get_color(character)
    if color_string is not None:
        draw_color_pixel(color_string, turta)
    else:
        print(f"Invalid character {character}, cannot draw pixel.")

# Part 1 - 4: Draw a line based on a string of characters
def draw_line_from_string(color_string, turta):
    for i in range(len(color_string)):
        draw_pixel(color_string[i], turta)

# Part 1 - 5: Draw shape from a string
def draw_shape_from_string(color_string, turta):
    if not color_string:
        print("Empty string detected, stopping the drawing.")
        return
    draw_line_from_string(color_string, turta)
    count = len(color_string) * 20
    turta.right(90)
    turta.forward(20)
    turta.right(90)
    turta.forward(count)
    turta.right(180)

# Part 2: Draw a grid pattern
def draw_grid(turta):
    # Center the grid by moving to the starting position
    grid_size = 20 * 20  # Total size of the grid (20x20 squares, each 20px)
    turta.penup()
    turta.setpos(-grid_size / 2, grid_size / 2)  # Start from the top-left corner
    turta.pendown()

    for i in range(20):  # Drawing 20 rows
        if i % 2 == 0:
            color_string = '02020202020202020202'
        else:
            color_string = '20202020202020202020'
        draw_line_from_string(color_string, turta)

        # Move to the next line
        turta.penup()
        turta.setx(-grid_size / 2)  # Go back to the left side
        turta.sety(turta.ycor() - 20)  # Move down by 20 pixels for the next row
        turta.pendown()

# Part 3: Draw shape from file, centered
def draw_shape_from_file(turta):
    file_path = input("Enter the path of the file that you want to read its content: ")

    try:
        with open(file_path, 'r') as file:
            shape_data = file.readlines()

        # Calculate the starting y position to center the shape vertically
        num_rows = len(shape_data)
        start_y = (num_rows * 20) / 2  # Each row is 20 pixels high

        turta.penup()
        turta.setpos(-200, start_y)  # Center horizontally at x = -200
        turta.pendown()

        for row in shape_data:
            row = row.strip()  # Clean up spaces
            draw_line_from_string(row, turta)

            turta.penup()
            turta.setx(-200)  # Move to the start of the next row
            turta.sety(turta.ycor() - 20)  # Move down one row
            turta.pendown()

    except FileNotFoundError:
        print("The file was not found. Please check the file path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function to start the turtle drawing
def main():
    turta.speed(0)
    
    # Ask the user whether to draw the grid or the shape from file
    choice = input("Enter 'grid' to draw the red/black grid or 'file' to draw a shape from the txt files: ").lower()
    
    if choice == 'grid':
        draw_grid(turta)  # Call the grid drawing function
    elif choice == 'file':
        draw_shape_from_file(turta)  # Call the function to draw from a file
    else:
        print("Invalid choice. Please enter 'grid' or 'file'.")
    
    turtle.done()

main()
