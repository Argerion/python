from graphics import *

"""
# Chapter 4 Exercises

# Exercise 4.1

# Alter the program from the last discussion question in the following ways:
# (a) Make it draw squares instead of circles.
# (b) Have each successive click draw an additional square on the screen
# (rather than moving the existing one).
# (c) Print a message on the window "Click again to quit" after the loop,
# and wait for a final click before closing the window.

def draw_squares():
    win = GraphWin("Exercise 4.1")
    shape = Rectangle(Point(30,30), Point(70, 70))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    for i in range(10):
        p = win.getMouse()
        newPoint1 = Point(p.getX() - 20, p.getY() - 20)
        newPoint2 = Point(p.getX() + 20, p.getY() + 20)
        newshape = Rectangle(newPoint1, newPoint2)
        newshape.setOutline("red")
        newshape.setFill("red")
        newshape.draw(win)
    message = Text(Point(100, 100), "Click anywhere to Quit")
    message.draw(win)
    q = win.getMouse()
    win.close()

draw_squares()



# Exercise 4.2

# An archery target consists of a central circle of yellow surrounded by concentric
# rings of red, blue, black and white. Each ring has the same width,
# which is the same as the radius of the yellow circle. Write a program
# that draws such a target. Hint : Objects drawn later will appear on top of
# objects drawn earlier.

def archery_target():
    win = GraphWin("Archery Target")
    white_ring = Circle(Point(100, 100), 50)
    white_ring.setFill("white")
    white_ring.draw(win)
    black_ring = Circle(Point(100, 100), 40)
    black_ring.setFill("black")
    black_ring.draw(win)
    blue_ring = Circle(Point(100, 100), 30)
    blue_ring.setFill("blue")
    blue_ring.draw(win)
    red_ring = Circle(Point(100, 100), 20)
    red_ring.setFill("red")
    red_ring.draw(win)
    yellow_ring = Circle(Point(100, 100), 10)
    yellow_ring.setFill("yellow")
    yellow_ring.draw(win)

    q = win.getMouse()
    win.close()

archery_target()

"""
