import pyxel 

pyxel.init(30, 30)

fruit = [
    pyxel.rndi(0, 29),
    pyxel.rndi(0, 29)
]

snake_geometry = [
    [10, 15],
    [11, 15],
    [12, 15],
]

snake_direction = [1,0]

arrow_keys = [
    pyxel.KEY_UP,
    pyxel.KEY_DOWN,
    pyxel.KEY_LEFT,
    pyxel.KEY_RIGHT
]
def update():
    global snake_geometry, snake_direction
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
    arrow_keys_pressed = []
    for key in arrow_keys:
        if pyxel.btnp(key):
            arrow_keys_pressed.append(key)
    for key in arrow_keys_pressed:
        if key == pyxel.KEY_UP:
            snake_direction = [0,1]
        elif key == pyxel.KEY_DOWN:
            snake_direction = [-1,0]
        elif key == pyxel.KEY_LEFT:
            snake_direction = [-1,0]
        elif key == pyxel.KEY_RIGHT:
            snake_direction = [1,0]
    snake_head = snake_geometry[-1]+snake_direction
    snake_geometry= snake_geometry[1:]+snake_head

def draw():
    pyxel.cls(13)
    for i in range(30):
        for j in range(30):
            if (i+j) % 2 == 0:
             pyxel.pset(i, j, 7)
    pyxel.pset(fruit[0], fruit[1], 8)
    pyxel.pset(snake_geometry[-1][0],snake_geometry[-1][1],11)
    for i in range (len(snake_geometry)-1) : 
        pyxel.pset(snake_geometry[i][0],snake_geometry[i][1],3)


pyxel.run(update, draw)
