import helligame as game, random

def ball_collision(item):
	if item==bgoal:
		game.sound("audio/fallsmall.ogg")
		bscore.text += 1
		randSpeed()
	elif item==rgoal:
		game.sound("audio/fallbig.ogg")
		rscore.text += 1
		randSpeed()

def randSpeed():
	v=random.random() * 3
	ball.speed=(game.randomSign(v + 5), game.randomSign(7 - v))
	ball.position=(384, 264)

def ball_bounce():
	game.sound("audio/hit1.ogg")

back=game.Image("images/stadium800.jpg")
ball=game.Image("images/football.png", (384, 264))
ball.moveBy("WASD", 10)
ball.collision=ball_collision
ball.bounce=ball_bounce
randSpeed()

rscore=game.Label(0, (10,0), color=game.RED)
bscore=game.Label(0, (770,0), color=game.BLUE)
bgoal=game.Box((0,180), (10, 200), color=game.RED, alpha=.2)
rgoal=game.Box((790,180), (10, 200), color=game.BLUE, alpha=.2)

room = [back, ball, rscore, bscore, bgoal, rgoal]
game.init("football", game.SKY, 800, 560)
while not game.done:
	game.events(room)
	game.update(room)
	game.draw(room)
game.quit()
