import random
from turtle import Turtle, Screen


# import colorgram

def hirst_painting(cl):
    for upward_move in range(10):
        toddle.right(90)
        toddle.forward(50)
        toddle.right(90)
        toddle.forward(450)
        toddle.right(180)
        for forward_move in range(10):
            toddle.dot(20, random.choice(cl))
            if forward_move != 9:
                toddle.forward(50)


def shape_draw(n):
    angle = float(360 / n)
    toddle.pencolor(random_color())
    for side in range(n):
        toddle.right(angle)
        toddle.forward(100)


def spirograph(gap):
    for gaps in range(int(360 / gap)):
        toddle.pencolor(random_color())
        toddle.circle(100)
        toddle.setheading(toddle.heading() + gap)


def random_walk():
    for movement in range(200):
        toddle.pencolor(random_color())
        toddle.right(random.randint(1, 360))
        toddle.forward(random.randint(10, 100))


def random_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    color_tuple = (r, g, b)
    return color_tuple


toddle = Turtle()
toddle.shape("turtle")
screen = Screen()
screen.colormode(255)
toddle.pensize(3)
toddle.speed("fastest")
toddle.pu()
toddle.setheading(45)
toddle.forward(300)
toddle.setheading(0)

# for i in range(3, 11):
#     shape_draw(i)

# random_walk()
# colors = colorgram.extract('hirst-1.webp', 30)
# rgb_colors =[]
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     tup = (r, g, b)
#     rgb_colors.append(tup)
#
# print(rgb_colors)

color_list = [(198, 159, 116), (70, 92, 129), (147, 85, 53), (218, 210, 116), (138, 160, 191), (178, 160, 38),
              (184, 146, 164), (28, 32, 46), (58, 34, 23), (120, 70, 93), (139, 175, 154), (77, 115, 79), (143, 25, 16),
              (186, 97, 82), (61, 31, 42), (121, 27, 41), (45, 58, 94), (177, 96, 114), (102, 119, 170), (34, 52, 45),
              (100, 160, 85), (214, 175, 192), (216, 181, 173), (160, 209, 191), (67, 86, 23), (219, 206, 8)]

hirst_painting(color_list)

# spirograph(5)
screen.exitonclick()
