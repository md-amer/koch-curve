import tk.turtle as tk

s = turtle.getscreen()
t = turtle.Turtle()
t.speed(10)

def koch(x):
    if x<3:
        t.fd(x)
    else:
        koch(x/3)
        t.lt(60)
        koch(x/3)
        t.rt(120)
        koch(x/3)
        t.lt(60)
        koch(x/3)

for i in range(3):
    koch(500)
    t.rt(120)

turtle.done()
