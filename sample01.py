import helligame as game
game.Ellipse ( (50,50), (700,500), game.WHITE )           # Ellipse: دایره یا بیضی
game.Box( (200,150) , (400,100) , game.GREEN )
game.Box( (200,250) , (400,100) , game.GRAY, thick = 1 )  # thick: ضخامت، جعبه توخالی می‌شود
game.Box( (200,350) , (400,100) , game.RED, radius = .2 ) # radius: درصد گردی لبه. بین 0 تا 1

game.mainloop("Salam", game.YELLOW) # عنوان صفحه و رنگ زمینه
