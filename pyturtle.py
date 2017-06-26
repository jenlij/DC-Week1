from turtle import *
# def center_turtle():
#     up()
#     forward(50)
#     left(90)
#     forward(50)
#     left(270)

#     down()

# def draw_square():
#     forward(100)
#     right(90)
#     forward(100)
#     right(90)
#     forward(100)
#     right(90)
#     forward(100)

# def fly_turtle():
#     up()
#     right(90)
#     forward(150)
#     down()

# def draw_orange_circle():
#     fillcolor('yellow')
#     pencolor('orange')
#     width(10)
#     circle(180)

# def draw_star():
#     for i in range(5):
#         forward(100)
#         right(144)

# def main():
#     center_turtle()
#     draw_star()
#     #draw_orange_circle()
#     # draw_square()
#     # fly_turtle()

#     # draw_square()
#     # fly_turtle()

#     # draw_square()
    
#     mainloop()

# main()    


#EXERCISES
def draw_equilateral():
    forward(100)
    left(120)
    forward(100)
    left(120)
    forward(100)

def draw_square():
    forward(110)
    left(90) 
    forward(110)
    left(90) 
    forward(110)
    left(90) 
    forward(110)
    left(90)    


def draw_pentagon():
    forward(120)
    left(72)
    forward(120)
    left(72)
    forward(120)
    left(72)
    forward(120)
    left(72)
    forward(120)

def draw_hexagon():
    forward(130)
    left(60)
    forward(130)
    left(60)
    forward(130)
    left(60)
    forward(130)
    left(60)
    forward(130)
    left(60)
    forward(130)

def draw_heptagon():
    for i in range(7):
        forward(140)
        left(360/7)

def draw_octagon():
    forward(150)
    left(45)
    forward(150)
    left(45)
    forward(150)
    left(45)
    forward(150)
    left(45)
    forward(150)
    left(45)
    forward(150)
    left(45)
    forward(150)
    left(45)
    forward(150)
    left(45)

def draw_circle():
    circle(160)
def main():
    draw_equilateral()
    draw_square()
    draw_pentagon()
    draw_hexagon()
    draw_heptagon()
    draw_octagon()
    draw_circle()
    mainloop()

main()    