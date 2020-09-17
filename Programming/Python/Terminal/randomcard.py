#Randomizer Card Game
import random

while True:
	
	print("Input (Play) to play the game\nInput (Quit) to exit this file")
	ui = input("Action:")
	if ui.upper() == "QUIT":
		print("Program Terminated. . .")
		break

	if ui.upper() == "PLAY":
		while True:
			play = ["0","0","0","0","0"]
			opp = ["0","0","0","0","0"]
			print("\nInstructions:")
			print("\nPlace your cards wherever u want, and guess where your opponent's card is")
			print("\n0 means that there is no card in such place, and 1 is otherwise")

			print("\nYour Cards")
			print("-----------------")
			print(f"{play[0]} | {play[1]} | {play[2]} | {play[3]} | {play[4]}  ")
			print("-----------------")

			while True:
				while True:
					a = input("\nWhere do u want your card to be? ( 1 - 5 )")
					try:
						choice = int(a)
						break
					except ValueError:
						pass
				if choice in range(5):
					break

			print(f"\nYour card will be on position {choice}")

			choice -= 1

			play[choice] = "1"

			print("\n-----------------")
			print(f"{play[0]} | {play[1]} | {play[2]} | {play[3]} | {play[4]}  ")
			print("-----------------")

			print("\nThe Bot will now also pick where to place its card")

			aichoice = random.randint(0,4)
			opp[aichoice] = "1"

			while True:
				while True:
					a = input("\nWhere do u think the bots card is? ( 1 - 5 )")
					try:
						guess = int(a)
						break
					except ValueError:
						pass
				if guess in range(5):
					break


			aiguess = random.randint(0,4)

			if opp[guess-1] == "1":
				print(f"\nYou guessed correctly, the bot placed its card on position {aichoice+1}")
			if opp[guess-1] == "0":
				print(f"\nAw you didnt get it, the bot placed its card on position {aichoice+1}")

			print("\n-----------------")
			print(f"{opp[0]} | {opp[1]} | {opp[2]} | {opp[3]} | {opp[4]}  ")
			print("-----------------")

			if play[aiguess] == "1":
				print(f"\nThe bot guessed correctly, the bot guessed your card to be on position {aiguess+1}")
			if play[aiguess] == "0":
				print(f"\nAw the bot didnt get it, the bot guessed your card to be on position {aiguess+1}")
			
			print("\n-----------------")
			print(f"{play[0]} | {play[1]} | {play[2]} | {play[3]} | {play[4]}  ")
			print("-----------------")

			print("\nWould you like to play again?")
			a = input("Yes or No:")

			if a.upper() == "NO" : break


