from pico2d import *
speed = 2


def handle_events():
    global running
    global tx, ty
    events1 = get_events()
    for event in events1:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_MOUSEMOTION:
            tx = event.x
            ty = 600 - event.y


open_canvas(800, 600)
frame = 0
running = True
x = 30
y = 90
tx = x
ty = y
grass = load_image('grass.png')
character = load_image('run_animation.png')
while running:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        handle_events()
        if x < tx:
            x = x+speed
        if x > tx:
            x = x-speed
        if y < ty:
            y = y + speed
        if y > ty:
            y = y - speed
        frame = (frame + 1) % 8
        delay(0.01)
close_canvas()
