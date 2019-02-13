import helligame as game, random

game.Image("images/stadium800.jpg")
ball=game.Image("images/football.png", (384, 264))
ball.moveBy("WASD", 10)

rscore=game.Label(0, (10,0), color=game.RED)
bscore=game.Label(0, (770,0), color=game.BLUE)
bgoal=game.Box((0,180), (10, 200), color=game.RED, alpha=.2)
rgoal=game.Box((790,180), (10, 200), color=game.BLUE, alpha=.2)

game.mainloop("football", -1, 800, 560)
