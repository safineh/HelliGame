import helligame as game

fade = False
ball = game.Ellipse( (400,10), (20,20), speed=(0,25), color=(255,0,0))
wall = game.Box( (0,550), (800,10), color=(0,0,255))
alphaBox = game.Box( (0,0), (800,600), color=(0,0,0), alpha=0)

def ball_collision(item):
	global fade
	if item == wall:
		ball.position = (400,530)
		game.pause = True
		fade = True

def game_frame():
	global fade
	if fade:
		if alphaBox.color[3] >= 255 - 10:
			fade = False
			game.Label("FINISH !", (270,250), color=(255,255,255), size=64)
		else:
			alphaBox.color = (0, 0, 0, alphaBox.color[3] + 10)

ball.collision = ball_collision
game.frame = game_frame
game.mainloop()
