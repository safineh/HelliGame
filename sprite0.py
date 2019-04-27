import helligame as game

i = 0
def click():
	global i
	i = (i+1)%2
	if i==0:
		coin.load("images/coin1.png")
	else:
		coin.load("images/coins.png")

coin = game.Image("images/coin1.png", (385, 265))
game.Label("click on image", (290, 300))
coin.click = click
game.mainloop("sprite", game.SKY, 800, 560)
