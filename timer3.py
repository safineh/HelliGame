import helligame as game

def keydown(key):
	if game.keyMap(" "):
		lbl.color = game.SILVER
		tmr.Pause()

def keyup(key):
	if key == game.keyMap(" "):
		lbl.color = game.WHITE
		tmr.Pause(False)

def frame():
	if tmr.done():
		lbl.text += 1
		tmr.restart()

lbl = game.Label(0, (10, 0))
game.Label("Hold SPACE to PAUSE timer", (350, 0))
tmr = game.Timer(2)
game.keydown = keydown
game.keyup = keyup
game.frame = frame

game.mainloop("timer test", game.SKY, 800, 560)
game.quit()
