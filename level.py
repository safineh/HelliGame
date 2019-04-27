import helligame as game

def collision(item):
	if item == bomb:
		game.back()

def level1_click():
	player.position = (100,275)
	player.speed = (10,0)
	game.mainloop(room=[btnX, player, bomb])

def level2_click():
	player.position = (375,25)
	player.speed = (10,10)
	game.mainloop(room=[btnX, player])

# level select
btn1 = game.Label("  LEVEL 1 ", (170,50),  back=game.BLUE, size= 100, radius=.5)
btn2 = game.Label("  LEVEL 2 ", (160,225), back=game.BLUE, size= 100, radius=.5)
btnQ = game.Label("   QUIT   ", (170,400), back=game.BLUE, size= 100, radius=.5)
btn1.click = level1_click
btn2.click = level2_click
btnQ.click = game.quit

# all levels
player = game.Ellipse(size=(50,50), color=game.GREEN)
player.collision = collision
btnX = game.Label(" X ", (750,10), back=game.RED, radius=1)
btnX.click = game.back

# level 1
bomb = game.Ellipse((25,275), (50,50), color=game.BLACK, tag="bomb")

# mainloop
game.mainloop("level game", game.SKY, 800, 600, room=[btn1, btn2, btnQ])
