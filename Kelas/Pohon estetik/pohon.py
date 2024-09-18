import turtle

li = turtle.Turtle()
li.screen.bgcolor("black")
li.pensize(2)
li.color("green")
li.left(90)
li.backward(100)
li.speed(20000)
li.shape("turtle")

def tree(i):
    if i<10:
        return
    else:
        li.forward(i)
        li.color("orange")
        li.circle(2)
        li.color("red")
        li.left(30)
        
        tree(3*i/4)
        
        li.right(60)
        
        tree(3*i/4)
        
        li.left(30)
        li.backward(i)
        
tree(100)
turtle.done()