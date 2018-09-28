from pico2d import *
import random


class Grass:
	def __init__(self):
		self.image = load_image('grass.png')
		print(self.image)
	def draw(self):
		self.image.draw(400, 30)


class Boy:
    def __init__(self):
        print("Creating..")
        self.x = random.randint(0, 200)
        self.y = random.randint(90, 550)
        self.speed = random.uniform(1.0, 3.0)
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')
    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
    def update(self):
        self.frame = (self.frame + 1) % 8
        if self.x > tx:
            self.x = self.x - self.speed
        if self.x < tx:
            self.x = self.x + self.speed
        if self.y > ty:
            self.y = self.y - self.speed
        if self.y < ty:
            self.y = self.y + self.speed


def handle_events():
    global running
    global boys
    global tx, ty
    event = get_events()
    for e in event:
        if e.type == SDL_QUIT:
            running = False
        if e.type == SDL_KEYDOWN and e.key == SDLK_ESCAPE:
            running = False
        if e.type == SDL_MOUSEMOTION:
                tx, ty = e.x, 600 - e.y


open_canvas()

g = Grass()

boys = [ Boy() for i in range(20) ]

running = True

while running:
	handle_events()
	for b in boys:
		b.update()
	clear_canvas()
	g.draw()
	for b in boys:
		b.draw()
	update_canvas()

	delay(0.03)

close_canvas()