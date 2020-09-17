from tkinter import *

#Snake Game
#Canvas, WASD and Arrow Keys
 
class move:
	def __init__(self):
		move.dim = 10 #square dimensions
		move.cw = 500 # canvas width
		move.ch = 500 # canvas height
		move.x = move.cw/2 
		move.y = move.ch/2
	def mup(self,event):	
		move.y -=move.dim
		print(move.y)
	def mdown(self,event):
		move.y += move.dim
	def mleft(self,event):
		move.x -= move.dim
	def mright(self,event):
		move.x += move.dim

game = move()



sqcoords = [game.x,game.y,game.x+game.dim,game.y,game.x+game.dim,game.y+game.dim,game.x,game.y+game.dim] #coords for square
main = Tk()
Everything = Canvas(main, width=game.cw, height=game.ch, bg="White")
square = Everything.create_polygon(sqcoords, outline="black",fill="red")
Everything.pack()


main.bind("<Up>", game.mup )

main.mainloop()