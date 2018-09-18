from pico2d import *
import math as m

open_canvas()

grass = load_image('grass.png')
character = load_image('run_animation.png')

go = 0
frame = 0
x = 0
y = 90
angle = -90
r = 0
phase = 'right1'
while True:
    while phase == 'right1':
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        frame = (frame + 1) % 8
        update_canvas()
        x = x + 4
        if x > 400:
            phase = 'circle'
            x = 400
            y = 290
        delay(0.01)
        get_events()
    while phase == 'circle':
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        frame = (frame + 1) % 8
        update_canvas()
        r = m.radians(angle)
        x = 400 + (200*m.cos(r))
        y = 290 + (200*m.sin(r))
        angle = angle + 2
        if angle > 270:
            phase = 'right2'
            x = 400
            y = 90
            angle = -90
        delay(0.01)
        get_events()
    while phase == 'right2':
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        frame = (frame + 1) % 8
        update_canvas()
        x = x + 4
        if x > 780:
            phase = 'up'
            x = 780
        delay(0.01)
        get_events()
    while phase == 'up':
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        frame = (frame + 1) % 8
        update_canvas()
        y = y + 4
        if y > 550:
            phase = 'left'
            y = 550
        delay(0.01)
        get_events()
    while phase == 'left':
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        frame = (frame + 1) % 8
        update_canvas()
        x = x - 2
        if x < 0:
            phase = 'down'
            x = 0
    while phase == 'down':
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        frame = (frame + 1) % 8
        update_canvas()
        y = y - 4
        if y < 90:
            phase = 'right1'
            y = 90
        delay(0.01)
        get_events()
close_canvas()
