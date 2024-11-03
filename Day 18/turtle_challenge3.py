import turtle as t

tim = t.Turtle()

i = 0
num_sides = [3,4,5,6,7,8,9,10]
colors = ["green yellow","cyan","magenta","yellow","deep sky blue","deep pink","red","blue violet"]
loop = True
while loop:
    for shape in range(num_sides[i]):
        angle = 360 / num_sides[i]
        tim.forward(100)
        tim.right(angle)
        tim.color(colors[i])
    if num_sides[i] == 10:
        loop = False
    i+=1

t.exitonclick()

