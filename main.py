import pyglet
from pyglet.window import key
import random as rd
window = pyglet.window.Window(780, 760)
# задний фон
bg_load = pyglet.image.load('img/background.png')
bg = pyglet.sprite.Sprite(bg_load, 0, 0)
# создние персонажа
birdload = pyglet.image.load('img/bird.png')
bird = pyglet.sprite.Sprite(birdload, 345, 380)
# создание Hitbox для персонажа
bird_hitbox = pyglet.shapes.Rectangle(x=bird.x, y=bird.y, width=bird.width, height=bird.height, color=(0,0,0,0))
# создание пола
floorload = pyglet.image.load('img/floor.png')
floor = pyglet.sprite.Sprite(floorload, 0, 0)
# hitbox пола
floor_hitbox = pyglet.shapes.Rectangle(x=floor.x, y=floor.y, width=floor.width, height=floor.height, color=(0,0,0,0))
# создание объекта 
pipe_load = pyglet.resource.image('img/pipe.png')
pipe = pyglet.sprite.Sprite(pipe_load, x=800, y=-450)
pipe2_load = pyglet.resource.image('img/pipe2.png')
pipe2 = pyglet.sprite.Sprite(pipe2_load, x=800, y=500)
# создание хитбоксов для обьектов
pipe_hitbox = pyglet.shapes.Rectangle(x=pipe.x, y=pipe.y, width=pipe.width, height=pipe.height)
pipe2_hitbox = pyglet.shapes.Rectangle(x=pipe2.x, y=pipe2.x, width=pipe2.width, height=pipe2.height)
# переменые bool
a = True
b = True
count = 0
# текст для счетчика
point = pyglet.text.Label(f'{count}', font_size=36,
                         x=window.width // 2, y=window.height - 50,
                         anchor_x='center', anchor_y='top')
# функция для движения обьектов
def pipe_move():
    global pipe, pipe2
    if pipe.x <= 0:
        pipe.x = 800
    else:
        pipe.x -= 6
    if pipe2.x <= 0:
        pipe2.x = 800
    else:
        pipe2.x -= 6
    if pipe.x == 800 and pipe2.x == 800:
        pipe.y = rd.randrange(1, 185) - 425
        if not pipe.y == pipe2.y:
            pipe2.y = pipe.y + 925
    pipe_hitbox.x = pipe.x
    pipe_hitbox.y = pipe.y
    pipe2_hitbox.x = pipe2.x
    pipe2_hitbox.y = pipe2.y
# создние переменной для действия
keys = key.KeyStateHandler()
window.push_handlers(keys)
# проверка соприкосновений
def check_collision(bird_hitbox, floor_hitbox):
    x1 = bird_hitbox.x
    y1 = bird_hitbox.y
    x2 = bird_hitbox.x + bird_hitbox.width
    y2 = bird_hitbox.y + bird_hitbox.height
 
    x3 = floor_hitbox.x
    y3 = floor_hitbox.y
    x4 = floor_hitbox.x + floor_hitbox.width
    y4 = floor_hitbox.y + floor_hitbox.height
    if x1 < x4 and x2 > x3 and y1 < y4 and y2 > y3:
        return True
    else:
        return False
# проверка соприкосновений 2
def check_collision2(bird_hitbox, pipe_hitbox):
    x1 = bird_hitbox.x
    y1 = bird_hitbox.y
    x2 = bird_hitbox.x + bird_hitbox.width
    y2 = bird_hitbox.y + bird_hitbox.height
 
    x3 = pipe_hitbox.x
    y3 = pipe_hitbox.y
    x4 = pipe_hitbox.x + pipe_hitbox.width
    y4 = pipe_hitbox.y + pipe_hitbox.height
    if x1 < x4 and x2 > x3 and y1 < y4 and y2 > y3:
        return True
    else:
        return False
# проверка соприкосновений 3
def check_collision3(bird_hitbox, pipe2_hitbox):
    x1 = bird_hitbox.x
    y1 = bird_hitbox.y
    x2 = bird_hitbox.x + bird_hitbox.width
    y2 = bird_hitbox.y + bird_hitbox.height
 
    x3 = pipe2_hitbox.x
    y3 = pipe2_hitbox.y
    x4 = pipe2_hitbox.x + pipe2_hitbox.width
    y4 = pipe2_hitbox.y + pipe2_hitbox.height
    if x1 < x4 and x2 > x3 and y1 < y4 and y2 > y3:
        return True
    else:
        return False
# управление персонажем
@window.event
def on_key_press(symbol, mmodifiers):
    global b, a, count
    if a == True and symbol == pyglet.window.key.SPACE:
        bird.y += (10 ** 2) / 2
        b = False
    if a == False and symbol == pyglet.window.key.R:
        bird.x = 345
        bird.y = 380
        pipe2.x = 800
        pipe.x = 800
        a = True
        count = 0
        pyglet.clock.schedule_interval(update, 1/60.0)
# обновление 
def update(dt):
    global bird, floor, bg, a, b, pipe, count
    # обновление координат 
    bird_hitbox.x = bird.x
    bird_hitbox.y = bird.y
    pipe_move()
    # столкновение хитбоксов
    if check_collision(bird_hitbox, floor_hitbox) or check_collision2(bird_hitbox, pipe_hitbox) or check_collision3(bird_hitbox, pipe2_hitbox):
        pyglet.clock.unschedule(update)
        a = False
    # это для того чтобы персонаж опускался
    if b == False:
        b = True
    if b:
        bird.y -= (3**2) / 4

    if pipe.x == 344:
        count += 1
    point.text = f'{count}'
# обновление происходит в 60 кадров
pyglet.clock.schedule_interval(update, 1/60.0)
# вывод изображения
@window.event
def on_draw():
    bg.draw()
    pipe.draw()
    pipe2.draw()
    floor.draw()
    bird.draw()
    floor_hitbox.draw()
    bird_hitbox.draw()
    point.draw()
pyglet.app.run()