"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.

"""
#Librerias
from random import randrange
from random import randint
from turtle import *
from freegames import square, vector


#Generar un color al azar
def random_color():
    a = randint(1,5)
    if a == 1:
        return "green"
    if a == 2:
        return "blue"
    if a == 3:
        return "orange"
    if a == 4:
        return "violet"
    if a == 5:
        return "black"


#Vector de direccion de cada objeto
food = vector(0, 0)
snake = [vector(10, 0)] #La serpiente se mueve cada 10 px
aim = vector(0, -10)    #Empieza con direccion -y

#Random color
def color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color

#Cambio de direccion
def change(x, y):
    "Change snake direction."
    aim.x = x                               #Cambiar direccion horizontal
    aim.y = y                               #Cambiar direccion vertical

#Verificar si la serpiente esta dentro del playground
def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190  #Si head esta dentro de los limites -200<x<190, -200<y<190

#Mover a la serpiente
def move():
    "Move snake forward one segment."
    head = snake[-1].copy()                 #La cabeza esta un paso adelante de donde estaba antes
    head.move(aim)                          #La cabeza se mueve en la direccion aim

    #Si choca
    if not inside(head) or head in snake:   #Si out of boundaries o choca con si misma
        square(head.x, head.y, 9, 'red')    #Pintar de rojo el cuadro de la cabeza
        update()
        return

    snake.append(head)                      #Añadir cabeza al final del vector serpiente

    #Si comio
    if head == food:
        print('Snake:', len(snake))         #Print longitud de la serpiente
        food.x = randrange(-15, 15) * 10    #Generar comida dentro y en coordenadas aleatorias
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)                        #Elimina la ultima posicion de la serpiente

    clear()

    for body in snake:                      #Para el tamaño de la serpiente
        square(body.x, body.y, 9, snakeColor)  #Cuadro del cuerpo en cords x, y, tamaño, color

    square(food.x, food.y, 9, foodColor)      #Cuadro de la comida en cords x, y, tamaño, color
    update()
    ontimer(move, 50)                       #Delay/Velocidad del juego - Default:100




snakeColor = random_color()
foodColor = random_color()
while foodColor == snakeColor:
    foodColor = random_color()

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
