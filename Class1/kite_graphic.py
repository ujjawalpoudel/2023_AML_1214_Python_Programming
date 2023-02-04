"""
This assigment generate kite shape graphic using turtle builtin package of python.
"""

# * Import Python Package
import turtle

# * First design kite shape in second quadrant of graph and colour by orange colour
turtle.fillcolor("orange")
turtle.begin_fill()
turtle.goto(0, 100)
turtle.goto(-100, 0)
turtle.goto(0, 0)
turtle.end_fill()


# * Second design kite shape in third quadrant of graph and colour by blue colour
turtle.fillcolor("blue")
turtle.begin_fill()
turtle.goto(-100, 0)
turtle.goto(0, -100)
turtle.goto(0, 0)
turtle.end_fill()

# * Third design kite shape in first quadrant of graph and colour by pink colour
turtle.fillcolor("pink")
turtle.begin_fill()
turtle.goto(100, 0)
turtle.goto(0, 100)
turtle.goto(0, -100)
turtle.end_fill()

# * Fourth design kite shape in fourth quadrant of graph and colour by red colour
turtle.fillcolor("red")
turtle.begin_fill()
turtle.goto(0, -100)
turtle.goto(100, 0)
turtle.goto(0, 0)
turtle.end_fill()

# * Design tail shape of kite
turtle.fillcolor("green")
turtle.begin_fill()
turtle.goto(0, -100)
turtle.goto(0, -150)
turtle.goto(0, -100)
turtle.end_fill()

turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.goto(50, -150)
turtle.goto(-50, -150)
turtle.goto(0, -100)
turtle.end_fill()

# * End graphic process generation
turtle.done()

# * end graphic process generation
