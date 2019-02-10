import helligame as game, pygame

x = 0
y = 0
c = 0
cols = 3
max_rows = 48 // cols
size = 768 // max_rows
col_width = 1024 // cols
def draw(color, text):
	global size, x, y, c, max_rows, col_width
	game.Box((x, y), (size, size), color)
	game.Label(text, (x+size+8, y+5), color, size=22)
	y += size
	c += 1
	if c >= max_rows:
		c = 0
		y = 0
		x += col_width

game.Box((0,0), (col_width, size), game.DARK_SMOKE)
draw(game.WHITE, 'WHITE')
draw(game.SMOKE, 'SMOKE')
draw(game.DARK_SMOKE, 'DARK_SMOKE')
draw(game.SILVER, 'SILVER')
draw(game.GREY, 'GREY, GRAY')
draw(game.BLUE_GREY, 'BLUE_GREY, BLUE_GRAY')
draw(game.BLACK, 'BLACK')

draw(game.DARK_RED, 'DARK_RED')
draw(game.PURE_RED, 'PURE_RED')
draw(game.RED, 'RED')

draw(game.PINK, 'PINK')
draw(game.PURE_PINK, 'PURE_PINK')
draw(game.ROSE, 'ROSE')

draw(game.MAGENTA, 'MAGENTA')
draw(game.VIOLET, 'VIOLET')
draw(game.PURPLE, 'PURPLE')
draw(game.PURE_PURPLE, 'PURE_PURPLE')
draw(game.DARK_PURPLE, 'DARK_PURPLE')

draw(game.INDEGO, 'INDEGO')
draw(game.DARK_BLUE, 'NAVY, DARK_BLUE')
draw(game.PURE_BLUE, 'PURE_BLUE')
draw(game.BLUE, 'BLUE')
draw(game.WATER, 'WATER')
draw(game.SKY, 'SKY')

draw(game.PURE_CYAN, 'AQUA, PURE_CYAN')
draw(game.CYAN, 'CYAN')
draw(game.TEAL, 'TEAL')
draw(game.DARK_CYAN, 'DARK_CYAN')

draw(game.DARK_GREEN, 'DARK_GREEN')
draw(game.GREEN, 'GREEN')
draw(game.GRASS, 'GRASS')
draw(game.PURE_GREEN, 'PURE_GREEN')

draw(game.OLIVE, 'OLIVE')
draw(game.LIME, 'LIME')

draw(game.YELLOW, 'YELLOW')
draw(game.PURE_YELLOW, 'PURE_YELLOW')
draw(game.GOLD, 'GOLD')
draw(game.AMBER, 'AMBER, PURE_ORANGE')
draw(game.ORANGE, 'ORANGE')
draw(game.DARK_ORANGE, 'DARK_ORANGE')

draw(game.BROWN, 'BROWN')
draw(game.LIGHT_CHOCOLATE, 'LIGHT_CHOCOLATE')
draw(game.PURE_BROWN, 'PURE_BROWN')
draw(game.CHOCOLATE, 'CHOCOLATE')
draw(game.DARK_CHOCOLATE, 'DARK_CHOCOLATE')
draw(game.WHITE_CHOCOLATE, 'WHITE_CHOCOLATE')

save = True
def frame():
	global save
	if save:
		game.screenshot("colors.png")
		save = False

game.frame=frame

game.mainloop("colors", game.WHITE, 1024, 768)
