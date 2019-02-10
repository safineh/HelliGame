import helligame as game

def add_score(item):
	emtiaz.text += 1

emtiaz=game.Label(0, position=(35,20))
b=game.Box( position=(350,250) , size=(100,40) , color=game.BLUE, speed=(5, 0) )
b.click=add_score
game.mainloop()
