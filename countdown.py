import helligame as game

def collision(item):
	if item == bomb:
		lbl.text = 5
		lbl.visible = True
		game.pause = True
		timer.restart()

def countdown(owner, timer):
	if owner.text > 0:
		owner.text -= 1
		timer.restart()
	else:	
		owner.visible = False
		player.position = (375, 25)
		player.speed = (25, 0)
		player.visible = True
		bomb.position = (25, 25)
		bomb.visible = True
		game.pause = False

player = game.Ellipse(size=(50, 50), color=game.GREEN, visible = False)
bomb = game.Ellipse(size=(50, 50), color=game.RED, visible = False)
lbl = game.Label(5, (300, 70), alpha=.5, size=400)
timer = lbl.addTimer(.5, countdown, True)
player.collision = collision
game.pause = True

game.mainloop("countdown", game.SKY, 800, 560)
game.quit()
