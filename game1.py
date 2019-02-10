import pygame
import random
import helligame as game

def onFrame():
	global score, score_add
	if not(game.pause): score.text += score_add

def onKeyDown(key):
	global player
	if key == pygame.K_ESCAPE:
		game.quit()
	elif key == pygame.K_RSHIFT or key == pygame.K_LSHIFT:
		player.speedX(2)
	elif key == pygame.K_RCTRL or key == pygame.K_LCTRL:
		player.speedX(.5)
	elif key == pygame.K_r and game.pause:
		game.restart();

def onKeyUp(key):
	if key == pygame.K_RSHIFT or key == pygame.K_LSHIFT:
		player.speedX(.5)
	elif key == pygame.K_RCTRL or key == pygame.K_LCTRL:
		player.speedX(2)
		
def onClick(position):
	player.speedX(-1)

def onClickBomb(item):
	if not(game.pause):
		if (item.size[0]>32):
			score.text += 20
			item.size = (4, 4)
			game.sound("sfx/hoop.wav")
		else:
			item.sizeAdd(8, 8)
			game.sound("sfx/boom.wav")

def onCollisionPlayer(collider):
	global score, score_add
	if collider.tag == "bomb":
		game.sound("sfx/haaa.wav")
		game.pause = True
		game.Label("GAME OVER", position=(220, 200), color=game.ROSE, size=64)
		r = game.Label(" Restart ", position=(280, 300), color=game.LIME, back=game.ROSE, size=64, radius=.5)
		r.click = onClickRestart
	'''elif collider.tag == "inc":
		player.sizeX(3/2)
	elif collider.tag == "dec":
		player.sizeX(2/3)'''

def addRandom(tag, color, click):
	x = 0
	y = 0
	s = random.randint(8, 12)
	while x + y < 300:
		x = random.randint(4, 1020-s)
		y = random.randint(4, 764-s)
	vx = random.random() * 6 - 3
	vy = random.random() * 6 - 3
	go = game.Box((x, y), (s, s), color, (vx, vy), tag=tag, radius=.4)
	go.click = click

def onStart():
	global score_add, score, player, counter

	player = game.Box(color=game.ORANGE, size=(40,40), speed=(4,4), radius=.4, tag="player")
	player.collision = onCollisionPlayer

	game.Image("images/coins.png", position=(10,10))
	score = game.Label(0, position=(45, 0), color=game.LIGHT_CHOCOLATE)
	score.format = int

	for i in range(random.randint(2, 4)): addRandom("inc",  game.INDEGO, None)
	for i in range(random.randint(2, 4)): addRandom("dec",  game.GREEN,  None)
	for i in range(random.randint(6, 8)): addRandom("bomb", game.RED,    onClickBomb)

	game.sleep(3)
	game.sound("sfx/123start.wav")
	
def onClickRestart(item):
	game.restart()

score_add = 1/60
#game.backColor = game.SKY
game.start = onStart
game.frame = onFrame
game.keydown = onKeyDown
game.keyup = onKeyUp
game.click = onClick
#game.other = print
game.mainloop()
