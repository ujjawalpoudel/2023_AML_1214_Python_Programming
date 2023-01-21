"""
This assigment generate tree shape graphic using turtle builtin package of python.
"""

# * Import Python Package
import turtle

# * First design top part of tree structure
turtle.fillcolor("green")
turtle.begin_fill()
turtle.goto(100, 0)
turtle.goto(0, 100)
turtle.goto(-100, 0)
turtle.goto(0, 0)
turtle.end_fill()

# * Second design middle part of tree structure
turtle.fillcolor("green")
turtle.begin_fill()
turtle.goto(100, -100)
turtle.goto(-100, -100)
turtle.goto(0, 0)
turtle.goto(100, -100)
turtle.end_fill()

# # * Third design bottom part of tree structure
turtle.fillcolor("green")
turtle.begin_fill()
turtle.goto(0, -100)
turtle.goto(100, -200)
turtle.goto(-100, -200)
turtle.goto(0, -100)
turtle.end_fill()

# * Drawing steam part of tree structure
turtle.begin_fill()
turtle.goto(100, -200)
# turtle.goto(-20, -200)
turtle.end_fill()

# # * Drawing steam part of tree structure
turtle.fillcolor("brown")
turtle.begin_fill()
turtle.goto(-20, -200)
turtle.goto(-20, -300)
turtle.goto(20, -300)
turtle.goto(20, -200)
turtle.end_fill()

# * End graphic process generation
turtle.done()
