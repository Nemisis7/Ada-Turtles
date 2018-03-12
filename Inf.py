import turtle
import Tkinter
i = 200
r = 95



turtle.setup(900, 900)

wn = turtle.Screen()
wn.bgcolor("grey")


nem = turtle.Turtle()

nem.shape("turtle")

nem.speed("fastest")

nem.color("red")

while True:

    nem.forward(i)
    nem.left(r)
    
  

    
    i -= 1
