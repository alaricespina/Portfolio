from tkinter import *
from tkinter import messagebox

import random

win = Tk()
win.title("Dice Game")

rollopt = IntVar()

class Random:
	def __init__(self):
		Random.BalNum = 100
	def RollDice(self):
		chance = random.randint(1,6)
		odd = [1,3,5]
		even = [2,4,6]
		choices = [odd,even]
		print(chance)
		if chance in choices[rollopt.get()]:
			print('win')
			Random.BalNum += Random.stake
		else:
			print('lose')
			Random.BalNum -= Random.stake
		print(Random.BalNum)
		if Random.BalNum <= 0:
			messagebox.showinfo("Defeat","Your balance reached 0")
		elif Random.BalNum >= 1000:
			messagebox.showinfo("Victory, You have reached 1000 points")
		Balance.delete("1.0","end")
		Balance.insert(END,Random.BalNum)
	def betam(self):
		BAmmount = int(Bet.get())
		if BAmmount > Random.BalNum or BAmmount < 0:
			messagebox.showwarning("Warning","Cannot bet more than balance")
			BAmmount = 0
		else:
			Random.stake = BAmmount
			print(Random.stake)
		Bet.delete(first=0,last=5)

game = Random()
BalanceText=Label(win,text="Balance").grid()
Balance = Text(win,height=1,width=5)
Balance.insert(END,game.BalNum)
BetText = Label(win, text="Bet").grid(row=1)
Bet = Entry(win, width=5)
SetBet = Button(win, text="Set", command=game.betam).grid(row=1,column=2)
Odd = Radiobutton(win, text="ODD", variable=rollopt, value=0).grid(row=2)
Even = Radiobutton(win, text="EVEN", variable=rollopt, value=1).grid(row=2,column=1)
Roll = Button(win, text="ROLL",command=game.RollDice).grid(row=3,columnspan=2)
Bet.grid(row=1,column=1)
Balance.grid(row=0,column=1)
win.mainloop()