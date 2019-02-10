import helligame as game

def add_score(item):
	if item.tag == "gift":
		emtiaz.text += 1
	elif item.tag == "bomb":
		emtiaz.text += -1

emtiaz=game.Label(0, position=(35,20))
b=game.Box( position=(350,250) , size=(100,40) , color=game.RED, speed=(0, 5) , tag="bomb" )
c=game.Box( position=(350,200) , size=(100,40) , color=game.BLUE, speed=(5, 0) , tag="gift" )
d=game.Box( position=(350,350) , size=(100,40) , color=game.BLUE, speed=(5, 0) , tag="gift" )

b.click=add_score
c.click=add_score
d.click=add_score

game.mainloop()
