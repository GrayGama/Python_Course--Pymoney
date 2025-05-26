import turtle

t1 = turtle.Turtle()
t1.up()
t1.goto(-100, 0); t1.down()
t1.fillcolor('orange')
t1.begin_fill()
t2 = turtle.Turtle()
t2.up()
t2.goto(100, 0); t2.down()
t2.fillcolor('red')
t2.begin_fill()
for i in range(3):
    t1.forward(50)
    t1.left(120)
    t2.backward(70)
    t2.right(120)

t2.end_fill()
t1.end_fill()

# More references:
# https://medium.com/analytics-vidhya/python-turtle-graphics-5ed7d97b13a9
