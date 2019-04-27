import helligame as game

def timer_done(owner, timer):
	owner.text += 1
	timer.restart()

lbl = game.Label(0, (10, 0))
lbl.addTimer(2, timer_done, True)

game.mainloop("timer test", game.SKY, 800, 560)
game.quit()
