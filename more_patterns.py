from turtle import *

COLORS = ['orange', 'brown', '#7eacf7']
SQUARE_SIZE = 200
HEX_SIZE = 100
ROTATION = 12

def rotate_by(amount):
  setheading(heading() + amount)

def center_turtle():
  up()
  forward(50)
  left(90)
  forward(50)
  left(270)
  down()

def draw_equilateral():
    pencolor('#B233FF')
    forward(150)
    left(120)
    forward(150)
    left(120)
    forward(150)

def draw_a_square(size):
    pencolor(COLORS[2])
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)

def draw_hexagon(size):
    pencolor('green')
    forward(size)
    left(60)
    forward(size)
    left(60)
    forward(size)
    left(60)
    forward(size)
    left(60)
    forward(size)
    left(60)
    forward(size)
  

def main():
  
  center_turtle()
  speed(10)
  for i in range(100):
    print i
    rotate_by(ROTATION)
    draw_equilateral()
    draw_a_square(SQUARE_SIZE)
    draw_hexagon(HEX_SIZE)
    if i > 0 and i % 60 == 0:
      up()
      rotate_by(ROTATION)
      forward(42)
      down()

    
main()