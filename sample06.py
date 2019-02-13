#moveBy (keyboard control)
import helligame as game, pygame

player=game.Box( position=(260,400) , size=(100,40) , color=game.INDEGO )
player.moveBy((None, "Left", None, "Right"), 10)
game.Box( position=(350,280) , size=(100,40) , color=game.RED, speed=(0, -5) , tag="bomb" )

game.mainloop()
