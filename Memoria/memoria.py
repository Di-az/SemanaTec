from random import *
from turtle import *
from freegames import path

car = path('car.gif')
nTiles = 32
tiles = list(range(nTiles)) * 2
state = {'mark': None}
hide = [True] * 64

#variable que lleva la cuenta del numero de taps
global nTaps, correctas
nTaps = 0
correctas = 0

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

#variable que se llama al dar un tap
def tap(x, y):
    global nTaps, correctas
    #se aumenta su valor por 1
    nTaps += 1
    print(nTaps)
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        correctas += 1
        if(correctas == nTiles):
            print(f"Felicidades, haz terminado usando {nTaps} taps")

def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(chr(tiles[mark] + 65), font=('Arial', 30, 'normal'), align="center")

    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()