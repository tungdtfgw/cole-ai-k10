import turtle as t

n = int(input('Enter n: '))
size = int(input('Enter size: '))
angle = 360/n

for i in range(n):
    t.forward(size)
    t.left(angle)


t.exitonclick()
