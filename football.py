import helligame as game, random

def ball_collision(item):
	if item==bgoal:
		bscore.text += 1
		randSpeed()
	elif item==rgoal:
		rscore.text += 1
		randSpeed()
		
def randSpeed():
	v=random.randint(5, 8)
	ball.speed=(v, 12-v)
	ball.position=(384, 264)

game.Image("images/stadium800.jpg")
ball=game.Image("images/football.png", (384, 264))
ball.moveBy("WASD", 10)
ball.collision=ball_collision
randSpeed()

rscore=game.Label(0, (10,0), color=game.RED)
bscore=game.Label(0, (770,0), color=game.BLUE)
bgoal=game.Box((0,180), (10, 200), color=game.RED, alpha=.2)
rgoal=game.Box((790,180), (10, 200), color=game.BLUE, alpha=.2)

game.mainloop("football", -1, 800, 560)
