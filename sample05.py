#click argument
import helligame as game

def add_score(item):
	if item == bomb:
		emtiaz.text -= 1
	else:
		emtiaz.text += 1

emtiaz = game.Label(0, position=(35,20))
bomb   = game.Box( position=(350,250) , size=(100,40) , color=game.RED,  speed=(0, 5) , tag="bomb" )
gift1  = game.Box( position=(350,200) , size=(100,40) , color=game.BLUE, speed=(5, 0) , tag="gift" )
gift2  = game.Box( position=(350,350) , size=(100,40) , color=game.BLUE, speed=(5, 0) , tag="gift" )

bomb.click  = add_score
gift1.click = add_score
gift2.click = add_score

game.mainloop()
