import helligame as game

img = ["images/walk1.png", "images/walk2.png", "images/walk3.png", "images/walk4.png"]
player = game.Image(images=img, position=(364, 237))
player.addTimer(.2, player.next, autorestart=True)
game.mainloop("sprite", game.SKY, 800, 560)
game.quit()
