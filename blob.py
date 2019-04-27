import helligame as game

def blob_click(item):
	item.move(-1, -1)
	item.sizeAdd(2, 2)

def blob_collision(self, item):
	print(self.tag, item.tag)
	if self.size[0] > item.size[1]:
		game.room.remove(self)
	else:
		game.room.remove(item)
	game.sound("audio/blast.ogg")

tag = 0
def game_click(point):
	global tag
	tag += 1
	point = game.sum2d(point, (-5, -5))
	c = game.Ellipse(point, (10,10), game.WHITE, thick=2, detailed=True, tag=tag)
	c.click = blob_click
	c.collision = blob_collision

game.click = game_click
#game.other = print
game.mainloop()
