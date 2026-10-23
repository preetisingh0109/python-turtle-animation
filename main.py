import turtle
import colorsys

#create  the screen
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor("Black")
screen.title("Pyhton Animation spiral Art!")
screen.tracer(0)

#Create the turtle
artist = turtle.Turtle()
artist.speed(0)
artist.width(2)
artist.hideturtle()

#generate turle using HSV
total_step= 360

for i in range(total_step):
    hue = i/total_step
    red, green, blue =colorsys.hsv_to_rgb(hue,1,1)

    artist.pencolor(red,green,blue)
    artist.forward(i* 0.8)
    artist.right(91)

    #update the animation
    screen.update()

screen.exitonclick()

