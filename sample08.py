import helligame as game, pygame, random

def bombOut(item):
	item.position = (random.randint(100, 600), game.screensize[1])

def onFrame():
	if pygame.K_d in game.keys or pygame.K_RIGHT in game.keys:
		player.move(10, 0)
	elif pygame.K_a in game.keys or pygame.K_LEFT in game.keys:
		player.move(-10, 0)

player=game.Box( position=(260,400) , size=(100,40) , color=game.INDEGO )
b=game.Box( position=(350,280) , size=(100,40) , color=game.RED, speed=(0, -5) , tag="bomb" )
b.bound=False
b.out = bombOut

game.frame = onFrame
game.mainloop()