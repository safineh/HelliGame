'''
* for implement:
- timer
- mouse enter/exit
- mouse down/up
- collision: once
- fade in/out
- animation: like 1..2..3
- speed on angle (bullet fire)
- taget rather than speed
- ellipse: fix collision
- line: (size | get/set position2(x,y) | get/set angle,length), alpha, collision
- pivot
'''
import pygame, random, time, math

WHITE = (255, 255, 255)
SMOKE = (225, 224, 224)
DARK_SMOKE = (192, 192, 192)
SILVER = (157, 157, 157)
GREY = (128, 128, 128)
GRAY = GREY
BLUE_GREY = (94, 124, 139)
BLUE_GRAY = BLUE_GREY
BLACK = (0, 0, 0)

DARK_RED = (128, 0, 0)
PURE_RED = (255, 0, 0)
RED = (246, 64, 44)

PINK = (235, 19, 96)
PURE_PINK = (255, 0, 128)
ROSE = (246, 39, 157)

MAGENTA = (255, 0, 255)
VIOLET = (238, 130, 239)
PURPLE = (156, 26, 177)
PURE_PURPLE = (128, 0, 128)
DARK_PURPLE = (102, 51, 185)

INDEGO = (61, 76, 183)
DARK_BLUE = (0, 0, 128)
NAVY = DARK_BLUE
BLUE = (15, 147, 245)
PURE_BLUE = (0, 0, 255)
WATER = (0, 166, 246)
SKY = (140, 220, 250)

PURE_CYAN = (0, 255, 255)
AQUA = PURE_CYAN
CYAN = (0, 187, 213)
TEAL = (0, 149, 135)
DARK_CYAN = (0, 128, 128)

DARK_GREEN = (0, 128, 0)
GREEN = (70, 175, 74)
GRASS = (136, 196, 64)
PURE_GREEN = (0, 255, 0)

OLIVE = (128, 128, 0)
LIME = (204, 221, 30)
YELLOW = (255, 236, 22)
PURE_YELLOW = (255, 255, 0)

GOLD = (252, 214, 3)
PURE_ORANGE = (255, 192, 0)
AMBER = PURE_ORANGE
ORANGE = (255, 151, 0)
DARK_ORANGE = (255, 85, 3)

BROWN = (121, 84, 70)
LIGHT_CHOCOLATE = (133, 85, 56)
PURE_BROWN = (128, 64, 0)
CHOCOLATE = (105, 58, 42)
DARK_CHOCOLATE = (72, 51, 50)
WHITE_CHOCOLATE = (234, 225, 201)

inited = False
done = False
breaked = False
pause = False
frame = None
click = None
other = None
start = None
keyup = None
keydown = None
backColor = SKY
sleep_sec = 0
screensize = (800, 600)
fps = 60
fontName = "comicsansms"
fontSize = 32
room = []
keys = []
pygame.init()
font = pygame.font.SysFont(fontName, fontSize)

def version():
	return "0.4"

def sum2d(a, b):
	return (a[0] + b[0], a[1] + b[1])

def randomItem(items):
	i = random.randint(0, len(items) - 1)
	return items[i]

def randomSign(n):
	return randomItem((-1, 1)) * n

def random2d(radius1, radius2=None):
	a = random.random() * 2 * math.pi
	r = radius1 if radius2==None else radius1 + (radius2 - radius1) * random.random()
	return (r * math.sin(a), r * math.cos(a))

def inPoint(p, pos, size):
	end = sum2d(pos, size)
	return p[0] >= pos[0] and p[1] >= pos[1] and p[0] <= end[0] and p[1] <= end[1]

def inCollision(p1, s1, p2, s2): #####
	return p1[0] < p2[0] + s2[0] and p1[0] + s1[0] > p2[0] and p1[1] < p2[1] + s2[1] and s1[1] + p1[1] > p2[1]

def roundedRect(surface, color, rect, radius):
    """
    AAfilledRoundedRect(surface,rect,color,radius)

    surface : destination
    rect    : rectangle
    color   : rgb or rgba
    radius  : 0 <= radius <= 1
    """

    rect         = pygame.Rect(rect)
    color        = pygame.Color(*color)
    alpha        = color.a
    color.a      = 0
    pos          = rect.topleft
    rect.topleft = 0,0
    rectangle    = pygame.Surface(rect.size, pygame.SRCALPHA)

    circle       = pygame.Surface([min(rect.size)*3]*2, pygame.SRCALPHA)
    pygame.draw.ellipse(circle,(0,0,0),circle.get_rect(),0)
    circle       = pygame.transform.smoothscale(circle,[int(min(rect.size)*radius)]*2)

    radius              = rectangle.blit(circle, (0,0))
    radius.bottomright  = rect.bottomright
    rectangle.blit(circle, radius)
    radius.topright     = rect.topright
    rectangle.blit(circle, radius)
    radius.bottomleft   = rect.bottomleft
    rectangle.blit(circle, radius)

    rectangle.fill((0,0,0),rect.inflate(-radius.w, 0))
    rectangle.fill((0,0,0),rect.inflate(0, -radius.h))

    rectangle.fill(color, special_flags=pygame.BLEND_RGBA_MAX)
    rectangle.fill((255, 255, 255, alpha), special_flags=pygame.BLEND_RGBA_MIN)

    return surface.blit(rectangle, pos)

def restart():
	global room, pause
	room = []
	pause = False
	if start != None: start()

def screenshot(filename):
	global screen
	pygame.image.save(screen, filename)
	
def sleep(seconds):
	global sleep_sec
	sleep_sec += seconds

def sound(filename):
	pygame.mixer.Sound(filename).play()

def remove(tag):
	i = 0
	while i<len(room):
		if room[i].tag == tag:
			del room[i]
		else:
			i += 1

def keyMap(name):
	if type(name) != str:
		return name
	name = name.lower()

	if len(name) == 1: 
		source = "_ abcdefghijklmnopqrstuvwxyz01234567890+-*\\/.,`\t\n"
		target = (None, pygame.K_SPACE, pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d, pygame.K_e, pygame.K_f, pygame.K_g, pygame.K_h, pygame.K_i, pygame.K_j, pygame.K_k, pygame.K_l, pygame.K_m, pygame.K_n, pygame.K_o, pygame.K_p, pygame.K_q, pygame.K_r, pygame.K_s, pygame.K_t, pygame.K_u, pygame.K_v, pygame.K_w, pygame.K_x, pygame.K_y, pygame.K_z, pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9, pygame.K_0, pygame.K_PLUS, pygame.K_MINUS, pygame.K_ASTERISK, pygame.K_SLASH, pygame.K_BACKSLASH, pygame.K_PERIOD, pygame.K_COMMA, pygame.K_BACKQUOTE, pygame.K_TAB, pygame.K_RETURN)
		i = source.find(name.lower())
		if i >= 0:
			return target[i]
	else:
		d = {"left": pygame.K_LEFT, "right": pygame.K_RIGHT, "up": pygame.K_UP, "down": pygame.K_DOWN, "esc": pygame.K_ESCAPE, "escape": pygame.K_ESCAPE, "tab": pygame.K_TAB, "backspace": pygame.K_BACKSPACE, "enter": pygame.K_RETURN, "ins": pygame.K_INSERT, "insert": pygame.K_INSERT, "del": pygame.K_DELETE, "delete": pygame.K_DELETE, "home": pygame.K_HOME, "end": pygame.K_END, "pageup": pygame.K_PAGEUP, "pagedown": pygame.K_PAGEDOWN}
		if name in d:
			return d[name]

	return None 
	
def init(caption="game", color=SKY, width=800, height=600):
	global screensize, screen, done, clock, backColor, inited
	done=False
	pygame.display.set_caption(caption)
	screensize = (width, height)
	screen = pygame.display.set_mode(screensize)
	clock = pygame.time.Clock()
	backColor = color
	inited = True

def events(room):
	global done, keys
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.KEYDOWN:
			keys.append(event.key)
			if keydown != None: keydown(event.key)
		elif event.type == pygame.KEYUP:
			keys.remove(event.key)
			if keyup != None: keyup(event.key)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			for item in room:
				if item.underPoint(event.pos):
					if item.mouseDown != None:
						item.mouseDown(item)
					if event.button == 1 and item.enabled and item.click != None:
						if item.detailed:
							item.click(item)
						else:
							item.click()
			if click != None:
				click(event.pos)
		elif event.type == pygame.MOUSEBUTTONUP:
			for item in room:
				if item.underPoint(event.pos):
					if item.mouseUp != None:
						item.mouseUp(item)
		else:
			if other != None: other(event) #####

def update(room):
	for item in room:
		for tmr in item.timers:
			if tmr.done() and tmr.function != None:
				if tmr.detailed:
					tmr.function(item, tmr)
				else:
					tmr.function()

	if not(pause):
		for item in room:
			if not(item.pause):
				if item.movement != None: item.movement()

				for item2 in room: #####
					if item.collision!=None and not(item2.pause) and item!=item2 and inCollision(item.position, item.size, item2.position, item2.size):
						if item.detailed:
							item.collision(item, item2)
						else:
							item.collision(item2)

def draw(room):
	global backColor, sleep_sec, clock
	
	screen.fill(backColor)
	for item in room:
		if item.visible:
			item.draw(screen)
	pygame.display.flip()

	if sleep_sec > 0:
		time.sleep(sleep_sec)
		sleep_sec = 0
	else:
		clock.tick(fps)

def mousePosition():
	return pygame.mouse.get_pos()

def mouseButtons():
	return pygame.mouse.get_pressed()

def back():
	global breaked
	breaked = True

def quit():
	global done
	done = True
	pygame.quit()
		
def mainloop(caption="game", color=SKY, width=800, height=600, room=room):
	global done, frame, inited, breaked

	window = not(inited)
	if (window): init(caption, color, width, height)
	if start != None: start()

	while not done or breaked:
		breaked = False
		events(room)
		update(room)
		if done or breaked:
			breaked = False
			break
			
		draw(room)
		if frame != None: frame()

	if (window and done): quit()

class Timer:
	def __init__(self, sec, autorestart=False):
		self.__check = time.time()
		self.sec = sec
		self.remain = sec
		self.__pause = False
		self.autorestart = autorestart
		
	def __update(self):
		if not(self.__pause):
			self.remain -= time.time() - self.__check
			if self.remain < 0:
				self.remain = 0
				self.__pause = True
		self.__check = time.time()
		
	def Pause(self, value = True):
		self.__pause = value
		self.__update()

	def working(self):
		return not(self.__pause) and self.remain > 0

	def done(self):
		working = self.working()
		self.__update()
		ret = working and self.remain <= 0
		if self.autorestart and ret: self.restart()
		return ret

	def restart(self):
		self.remain = self.sec
		self.__pause = False

class Box:
	def __init__(self, position=(0, 0), size=(1, 1), color=BLACK, speed=(0, 0), thick=0, radius=0, alpha=1, tag="", detailed=False, visible=True, enabled=True, pause=False, bound=True):
		self.position = position
		self.size = size
		self.thick = thick
		self.radius = radius
		self.speed = speed
		self.color = (color[0], color[1], color[2], int(alpha * 255))
		self.tag = tag
		self.detailed = detailed
		self.visible = visible
		self.enabled = enabled
		self.pause = pause
		self.bound = bound
		self.controlKeys = None
		self.controlSpeed = 0
		self.timers = []

		#events
		self.click = None
		self.mouseDown = None
		self.mouseUp = None
		self.collision = None
		self.out = None
		self.bounce= None

		room.append(self)
	
	def draw(self, screen):
		area = (self.position[0], self.position[1], self.size[0], self.size[1])
		if self.thick > 0:
			pygame.draw.rect(screen, self.color, area, self.thick)
		else:
			roundedRect(screen, self.color, area, self.radius)

	def moveBy(self, keys, speed=1):
		self.controlSpeed = speed
		if type(keys) == str:
			if len(keys) <= 4:
				self.controlKeys = []
				for ch in keys:
					self.controlKeys.append(keyMap(ch))
		elif type(keys) == tuple:
			self.controlKeys = []
			for key in keys:
				self.controlKeys.append(keyMap(key))

	def underPoint(self, point):
		return self.visible and inPoint(point, self.position, self.size)

	def underMouse(self, point):
		return underPoint(MOUSE_POINT)

	def turnX(self):
		self.speed = (-self.speed[0], self.speed[1])

	def turnY(self):
		self.speed = (self.speed[0], -self.speed[1])

	def movement(self):
		ctrlX = 0
		ctrlY = 0
		if self.controlSpeed != 0 and self.controlKeys != None:
			for i in range(len(self.controlKeys)):
				if self.controlKeys[i] in keys:
					if i == 0:
						ctrlY -= self.controlSpeed
					elif i == 1:
						ctrlX -= self.controlSpeed
					elif i == 2:
						ctrlY += self.controlSpeed
					elif i == 3:
						ctrlX += self.controlSpeed
		self.move(self.speed[0] + ctrlX, self.speed[1] + ctrlY)

		if self.bound:
			bounced = False
			if self.position[0] + self.size[0] >= screensize[0] or self.position[0] <= 0:
				self.turnX()
				bounced = True
			if self.position[1] + self.size[1] >= screensize[1] or self.position[1] <= 0:
				self.turnY()
				bounced = True
			if bounced and self.bounce != None:
				self.bounce()
				
	def isOut(self):
		return self.position[0]+self.size[0]<0 or self.position[0]>screensize[0] or self.position[1]+self.size[1]<0 or self.position[1]>screensize[1]

	def move(self, x, y):
		x += self.position[0]
		y += self.position[1]
		if self.bound:
			if x < 0:
				x = 0
			elif x + self.size[0] > screensize[0]:
				x = screensize[0] - self.size[0]
			if y < 0:
				y = 0
			elif y + self.size[1] > screensize[1]:
				y = screensize[1] - self.size[1]
			self.position = (x, y)
		elif self.out != None :
			self.position = (x, y)
			if self.isOut():
				self.out(self)

	def show(self):
		self.visible = True

	def hide(self):
		self.visible = False

	def sizeX(self, r):
		self.size = (r * self.size[0], r * self.size[1])

	def sizeAdd(self, x, y):
		self.size = (x + self.size[0], y + self.size[1])

	def speedX(self, r):
		self.speed = (r * self.speed[0], r * self.speed[1])

	def speedAdd(self, x, y):
		self.speed = (x + self.speed[0], y + self.speed[1])

	def addTimer(self, time, function = None, detailed = False, autorestart=True, tag = ""):
		tmr = Timer(time, autorestart)
		tmr.function = function
		tmr.detailed = detailed
		tmr.tag = tag
		self.timers.append(tmr)
		return tmr

class Ellipse(Box):
	def draw(self, screen):
		area = (self.position[0], self.position[1], self.size[0], self.size[1])
		pygame.draw.ellipse(screen, self.color, area, self.thick)

class Image(Box):
	def __init__(self, images="", position=(0, 0), speed=(0, 0), tag="", detailed=False, visible=True, enabled=True, pause=False, bound=True, index=0):
		Box.__init__(self, position=position, speed=speed, tag=tag, detailed=detailed, visible=visible, enabled=enabled, pause=pause, bound=bound)
		self.images=images
		self.index=index
		self.repeat=None
		self.load()

	def load(self, images=None, index=None):
		images = self.images if images==None else images
		index = self.index if index==None else index
		filename = images if type(images) == str else images[index]
		self.image = pygame.image.load(filename)
		self.size = self.image.get_size()
	
	def next(self, step=1):
		if type(self.images) == str: return
		self.index += step
		if self.index >= len(self.images):
			self.index = self.index % len(self.images)
			if self.repeat != None:
				if detailed:
					self.repeat(self)
				else:
					self.repeat()
		self.load()
		
	def draw(self, screen):
		screen.blit(self.image, self.position)

class Label(Box):
	def __init__(self, text="", position=(0, 0), color=WHITE, back=None, sysFont=None, size=None, thick=0, radius=0, alpha=1, tag="", format="", speed=(0,0), detailed=False, visible=True, enabled=True, pause=False, bound=True):
		global font, fontName, fontSize
		Box.__init__(self, position=position, speed=speed, color=color, thick=thick, tag=tag, detailed=detailed, visible=visible, enabled=enabled, pause=pause, bound=bound)
		self.text = text
		self.back = None if back==None else (back[0], back[1], back[2], int(alpha*255))
		self.radius = radius
		if sysFont == None and size == None:
			self.font = font
		else:
			if sysFont == None: sysFont = fontName
			if size == None: size = fontSize
			self.font = pygame.font.SysFont(sysFont, size)
		self.format = format
	
	def draw(self, screen):
		v = self.text
		if self.format == int:
			v = int(v)
		render = self.font.render(str(v), True, self.color)
		self.size = render.get_size()
		if self.back != None:
			area = (self.position[0], self.position[1], self.size[0], self.size[1])
			if self.thick > 0:
				pygame.draw.rect(screen, self.back, area, self.thick)
			else:
				roundedRect(screen, self.back, area, self.radius)
		screen.blit(render, self.position)
