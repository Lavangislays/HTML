import turtle

turtle.Screen().bgcolor("Green")

board = turtle.Turtle()

# Traingle
board.forward(100)

for i in range(2):
    board.left(120)
    board.forward(100)

for i in range(4):
    board.forward(100)
    board.left(90)