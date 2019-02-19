import helligame as game, random

def start(x):
	if score1.text == 11:
		end("Green", game.GREEN)
	elif score2.text == 11:
		end("  Red", game.RED)
	else:
		ball.position = (385, 285)
		if x== 0: x = game.randomItem([-1, 1])
		ball.speed = (x * 3, 0)

def end(name, color):
	game.sound("audio/launch.ogg")
	game.pause = True
	game.Label(name + " is winner!", (140, 180), color, size=72, tag="temp")
	re = game.Label(" Restart ", (240, 300), game.WHITE, back=color, size=72, radius=.3, tag="temp")
	re.click = restart

def restart(label):
	game.remove("temp")
	score1.text = 0
	score2.text = 0
	rocket1.position = (20, 250)
	rocket2.position = (750, 250)
	start(0)
	game.pause = False

def ball_return(r):
	x = random.random() * 5 + 10  # 10 ~ 15
	y = random.random() * 10 - 5  # -5 ~ 5
	ball.speed = (r * x, y)

def ball_collision(item):
	if item == rocket1:
		game.sound("audio/fallbig.ogg")
		ball_return(1)
	elif item == rocket2:
		game.sound("audio/fallsmall.ogg")
		ball_return(-1)
	elif item == wall1:
		game.sound("audio/blast.ogg")
		score2.text += 1
		start(1)
	elif item == wall2:
		game.sound("audio/blast.ogg")
		score1.text += 1
		start(-1)

ball = game.Ellipse((400, 300), (30, 30), game.BLUE)
ball.collision = ball_collision

rocket1 = game.Box((20, 250), (30, 100), game.GREEN)
rocket1.moveBy("W_S", 15)
wall1 = game.Box((1, 0), (0, 600), game.GREEN)
score1 = game.Label(0, (80, 0), game.GREEN)

rocket2 = game.Box((750, 250), (30, 100), game.RED)
rocket2.moveBy(("Up", None, "Down"), 15)
wall2 = game.Box((799, 0), (0, 600), game.RED)
score2 = game.Label(0, (700, 0), game.RED)

start(0)
game.mainloop()
