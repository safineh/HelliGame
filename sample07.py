import helligame as game, pygame

def onFrame():
	if pygame.K_d in game.keys or pygame.K_RIGHT in game.keys:
		player.move(10, 0)
	elif pygame.K_a in game.keys or pygame.K_LEFT in game.keys:
		player.move(-10, 0)

player=game.Box( position=(260,400) , size=(100,40) , color=game.INDEGO )
game.Box( position=(350,280) , size=(100,40) , color=game.RED, speed=(0, -5) , tag="bomb" )

game.frame = onFrame
game.mainloop()
