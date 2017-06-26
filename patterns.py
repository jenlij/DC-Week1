from turtle import *

COLORS = ['orange', 'brown', '#7eacf7']
CIRCLE_SIZE = 120
SQUARE_SIZE = 256
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

def draw_a_square(size):
  forward(size)
  right(90)
  forward(size)
  right(90)
  forward(size)
  right(90)
  forward(size)
  

def fly_turtle_fly():
  up()
  right(90)
  forward(150)
  down()
  
def draw_circle(size):
  # begin_fill()
  # fillcolor(COLORS[0])
  # pencolor(COLORS[1])
  # width(10)
  width(1)
  circle(size)
  # end_fill()

def main():
  pencolor(COLORS[2])
  center_turtle()
  # should_continue = True
  speed(10)
  for i in range(1000):
    print i
    rotate_by(ROTATION)
    # draw_a_square(SQUARE_SIZE)
    draw_circle(CIRCLE_SIZE)
    if i > 0 and i % 60 == 0:
      up()
      rotate_by(ROTATION)
      forward(42)
      down()






  # return 0

  # while should_continue:
  #   choice = raw_input("\n1. circle\n2. square\nchoose one: ")
  #   rotate_by(ROTATION)
  #   if choice in "012":
  #     choice = int(choice)
  #     if choice == 1:
  #       draw_circle()
  #     elif choice == 2:
  #       draw_a_square()
  #     elif choice == 0:
  #       should_continue = False
  #     else:
  #       pass
  #   else:
  #     print "\n\nno soup for you"
    
main()