import helligame as game, random

def start(x):
	if score1.text == 11:
		game.pause = True
		game.Label("Green is winner!", (130, 250), game.GREEN, size=72)
	elif score2.text == 11:
		game.pause = True
		game.Label("Red is winner!", (170, 250), game.RED, size=72)
	else:
		ball.position = (385, 285)
		ball.speed = (x * 3, 0)

def ball_return(r):
	x = random.random() * 5 + 10  # 10 ~ 15
	y = random.random() * 10 - 5  # -5 ~ 5
	ball.speed = (r * x, y)

def ball_collision(item):
	if item == rocket1:
		ball_return(1)
	elif item == rocket2:
		ball_return(-1)
	elif item == wall1:
		score2.text += 1
		start(1)
	elif item == wall2:
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

if random.randint(1, 2) == 1:
	start(1)
else:
	start(-1)
game.mainloop()
