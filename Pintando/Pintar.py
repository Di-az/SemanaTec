from turtle import *

from freegames import vector


def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circulo(start, end):
    circle(end.x - start.x)
    
    
def rectangle(start, end):
    "Draw rectangle from start to end."

# drawing first side
    l = start.x - end.x
    w = end.x - start.y
    forward(l) # Forward turtle by l units
    left(90) # Turn turtle by 90 degree
    
    # drawing second side
    forward(w) # Forward turtle by w units
    left(90) # Turn turtle by 90 degree
    
    # drawing third side
    forward(l) # Forward turtle by l units
    left(90) # Turn turtle by 90 degree
    
    # drawing fourth side
    forward(w) # Forward turtle by w units
    left(90) # Turn turtle by 90 degree   
    

def triangle(start, end):
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, start.y)
    goto((start.x+end.x)/2,end.y)
    goto(start.x, start.y)

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    "Store value in state at key."
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('orange'), 'O') #Agregando nuevo color y relacionarlo con una key del teclado
onkey(lambda: color('cyan'), 'C') #Agregando nuevo color y relacionarlo con una key del teclado
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circulo), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()