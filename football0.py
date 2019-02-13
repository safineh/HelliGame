import helligame as game

game.Image("images/stadium800.jpg")
game.Image("images/football.png", (384, 264))
game.Label(0, (10,0), color=game.RED)
game.Label(0, (770,0), color=game.BLUE)
game.Box((0,180), (10, 200), color=game.RED, alpha=.2)
game.Box((790,180), (10, 200), color=game.BLUE, alpha=.2)

game.mainloop("football", -1, 800, 560)
