"""
Charlotte Johnston
Course: CS 3725 Computational Creativity
Assignment: Mission 2: A Markov Distinction
September 17, 2019
"Composition 8008"

Composition 8008 uses Markov chains to create a drawing in the style of 
Vasily Kandinsky's Composition 8. This program incorporates three shapes from 
Kandinsky's work: concentric yellow and blue circles, yellow triangles, and 
concentric pink and purple circles. When a shape is drawn, the next shape is
picked based on a transitional matrix of probabilities. 

After running the system, enter how many shapes you want in your drawing, and 
the turtles will make it for you!
"""
import random 
import turtle

def draw_yellow_triangle():
    """Draws a yellow triangle like the one in the lower right corner of 
    Composition 8"""
    # Chooses coordinates in a range just inside the screen parameters to 
    # prevent the shapes being too cut off
    xcor = random.randrange(-300, 300) 
    ycor = random.randrange(-280, 280)
    turtle.penup()
    turtle.goto(xcor, ycor)  
    turtle.setheading(45)
    turtle.pencolor("gold")
    turtle.fillcolor("gold")
    turtle.begin_fill()
    turtle.down()
    for turt in range(3):
        turtle.forward(100)
        turtle.right(120)
    turtle.end_fill()
    
def draw_yellow_blue_circle():
    """Draws three concentric circles in yellow, blue and purple like the one
    in the lower left corner of Composition 8"""
    xcor = random.randrange(-300, 300)
    ycor = random.randrange(-280, 280)
    turtle.penup()
    turtle.goto(xcor, ycor)
    # Draws outer purple circle
    turtle.right(90)    
    turtle.forward(60)   
    turtle.right(270)   
    turtle.pencolor("Medium Purple")
    turtle.fillcolor("Medium Purple")
    turtle.begin_fill()    
    turtle.pendown()    
    turtle.circle(60)    
    turtle.penup()
    turtle.end_fill()
    turtle.goto(xcor, ycor)
    # Draws middle blue circle
    turtle.goto(xcor, ycor)
    turtle.right(90) 
    turtle.forward(50)
    turtle.right(270)
    turtle.pencolor("Light Blue")
    turtle.fillcolor("Light Blue")
    turtle.begin_fill()        
    turtle.pendown() 
    turtle.circle(50)    
    turtle.penup() 
    turtle.end_fill()
    turtle.goto(xcor, ycor)
    # Draws inner yellow circle
    turtle.goto(xcor, ycor)
    turtle.right(90)    
    turtle.forward(40)  
    turtle.right(270)  
    turtle.pencolor("Light Goldenrod")
    turtle.fillcolor("Light Goldenrod") 
    turtle.begin_fill()
    turtle.pendown()    
    turtle.circle(40)    
    turtle.penup() 
    turtle.end_fill()
    turtle.goto(xcor, ycor)


def draw_black_purple_circle():
    """Draws three concentric circles in pink, black and purple like the one
    in the upper left corner of Composition 8"""
    xcor = random.randrange(-300, 300)
    ycor = random.randrange(-280, 280)
    turtle.penup()
    turtle.goto(xcor, ycor)
    # Draws outer pink circle
    turtle.right(90)    
    turtle.forward(120)  
    turtle.right(270)
    turtle.pencolor("Light Pink")
    turtle.fillcolor("Light Pink")
    turtle.begin_fill()    
    turtle.pendown()    
    turtle.circle(120)    
    turtle.penup()
    turtle.end_fill()
    turtle.goto(xcor, ycor)
    # Draws middle black circle
    turtle.goto(xcor, ycor)
    turtle.right(90)    
    turtle.forward(80) 
    turtle.right(270)
    turtle.pencolor("black")
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(80)
    turtle.penup()
    turtle.end_fill()
    turtle.goto(xcor, ycor)
    #Draws inner dark purple circle
    turtle.goto(xcor, ycor)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(270)
    turtle.pencolor("Dark Orchid")
    turtle.fillcolor("Dark Orchid") 
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(40)
    turtle.penup()
    turtle.end_fill()
    turtle.goto(xcor, ycor)
    
def main():
    """Main method that draws a painting in the style of Kandinsky using 
    transitional probabilities between the different shapes. Takes in user
    input for the number of shapes that appear in the drawing."""
    # "BC" refers to the black_purple_circle
    # "YT" refers to the yellow_triangle
    # "YC" refers to the yellow_blue_circle
    num_shapes = int(input("How many shapes do you want in your drawing? "))
    turtle.speed(20)
    
    # Transition states for each current shape
    BC_transitions = ["BC|BC", "YT|BC", "YC|BC"]
    YT_transitions = ["BC|YT", "YT|YT", "YC|YT"]
    YC_transitions =  ["BC|YC", "YT|YC", "YC|YC"]
    
    # Probabilities for the transition states
    # I kept the transition states as lists rather than a matrix for readibility
    BC_probs = [0.2, 0.4, 0.4]
    YT_probs = [0.3, 0.1, 0.6]
    YC_probs = [0.4, 0.5, 0.1]
    
    # Starts at this shape (can change if desired)
    current_shape = "black_purple_circle"
    cur_shapes = 0 
    #num_shapes = 12
    while cur_shapes < num_shapes:
        # Transitions if the current state is the black_purple_circle
        if current_shape == "black_purple_circle":
            next_choice = random.choices(BC_transitions, BC_probs, k = 1)
            next_choice = next_choice[0]
            if next_choice == "BC|BC":
                # No change in state, just draw it again 
                draw_black_purple_circle()
                cur_shapes = cur_shapes + 1 
            elif next_choice == "YT|BC":
                current_shape = "yellow_triangle"
                draw_yellow_triangle()
                cur_shapes = cur_shapes + 1
            else: 
                # i.e. next_choice == "YC|BC"
                current_shape = "yellow_blue_circle"
                draw_yellow_blue_circle()
                cur_shapes = cur_shapes + 1
                
        # Transitions if the current state is the yellow_triangle     
        elif current_shape == "yellow_triangle":
            next_choice = random.choices(YT_transitions, YT_probs, k = 1)
            next_choice = next_choice[0]
            if next_choice == "BC|YT":
                current_shape = "black_purple_circle"
                draw_black_purple_circle()
                cur_shapes = cur_shapes + 1 
            elif next_choice == "YT|TY":
                #state doesnt change
                draw_yellow_triangle()
                cur_shapes = cur_shapes + 1      
            else:
                current_shape = "yellow_blue_circle"
                draw_yellow_blue_circle()
                cur_shapes = cur_shapes + 1
        # Transitions if the current state is the yellow_blue_circle          
        else:
            next_choice = random.choices(YC_transitions, YC_probs, k = 1)
            next_choice = next_choice[0] 
            if next_choice == "BC|YC":
                current_shape = "black_purple_circle"
                draw_black_purple_circle()
                cur_shapes = cur_shapes + 1 
            elif next_choice == "YT|YC":
                current_shape = "yellow_triangle"
                draw_yellow_triangle()
                cur_shapes = cur_shapes + 1 
            else:
                draw_yellow_blue_circle()
                cur_shapes = cur_shapes + 1
                             
     
main()
turtle.done()