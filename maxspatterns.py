from turtle import *
import colorsys

def center_turtle():
    up()
    left(90)
    forward(50)
    down()

def center_star():
    up()
    left(45)
    forward(20)
    right(50)
    down()

def draw_circle(w, size, innerColor, outerColor):
    begin_fill()
    fillcolor(innerColor)
    pencolor(outerColor)
    width(w)
    circle(size)
    end_fill()

def star(size, outerColor):
    pencolor(outerColor)
    for i in range(5):
        forward(size)
        right(144)

def rainbowMadness():
    for i in range(1000):
        color = colorsys.hsv_to_rgb(i/1000, 1.0, 1.0)
        color[color]
        forward(i)
        right(98)

def sun():
    # color('red', 'yellow')
    colormode(255)
    begin_fill()
    width(1)
    count = 0
    while True and count <= 200:
        if (count < 100):
            c = 126, 172, 247
        else:
            c = 247, 125, 234
        pencolor(c)
        forward(500)
        left(170)
        forward(250)
        left(172)
        forward(250)
        left(172)
        print count
        count = count + 1
        if abs(pos()) < 1:
            break
    end_fill()

def main():
    #draws a circle with a star in it
    def circle_star():
        draw_circle(10, 100, "blue", "green")
        center_turtle()
        center_star()
        star(75, "orange")
    
    # circle_star()
    # right(270)
    # forward(200)
    # circle_star()
    # rainbowMadness()
    up()
    left(270)
    forward(250)
    left(180)
    down()
    speed(10)
    sun()
    mainloop()

main()