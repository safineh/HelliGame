#tag
import helligame as game, pygame, random

def bombOut(item):
	item.position = (random.randint(100, 600), game.screensize[1])
	item.speed = (random.random() - .5, random.random() * -5)

def playerCollision(item):
	if item.tag == "bomb":
		game.pause = True
		game.Label("GAME OVER", (220, 200), color=game.WATER, size=64)

player = game.Box( position=(260,400) , size=(100,40) , color=game.INDEGO )
player.moveBy(("Up", "Left", "Down", "Right"), 10)
player.collision = playerCollision

for i in range(10):
	z = random.randint(5, 10)
	x = random.randint(100, 600)
	y = random.randint(0, 380)
	sx = random.random() - .5
	sy = random.random() * -5
	bomb = game.Ellipse( position=(x,y) , size=(z,z) , color=game.RED, speed=(sx, sy) , tag="bomb" )
	bomb.bound = False
	bomb.out = bombOut

game.mainloop()
