#bound, out, screensize
import helligame as game, pygame, random

def bombOut(item):
	item.position = (random.randint(100, 600), game.screensize[1])

player = game.Box( position=(260,400) , size=(100,40) , color=game.INDEGO )
player.moveBy((None, "Left", None, "Right"), 10)
bomb = game.Box( position=(350,280) , size=(100,40) , color=game.RED, speed=(0, -5) , tag="bomb" )
bomb.bound = False
bomb.out = bombOut

game.mainloop()
