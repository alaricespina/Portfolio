import random 
results = []
ai = []
def aiidentify(a):
	global ai
	return ai.count(a)

while True:
	print("type PLS GUESS to start the game")
	x = input("Action:")
	a = x.upper()
	if a == "PLS QUIT": break
	if a == "PLS GUESS":
		n = 3
		print("\nThe bot will now choose number between 1 to 10")
		print("\nYou must now enter a number that you think it is")
		botnumber = random.randint(1,10)
		guessed = False
		while not n == 0:
			print(f"Remaining tries: {n}")
			while True:
				g = input("Number:")
				try:
					guess = int(g)
					break
				except ValueError:
					print("Input a number only please")
			if guess == n:
				guessed = True
				break
			n -= 1
		if guessed == True:
			print("\nDeym addict")
			results.append("Won")
		if guessed == False:
			print("\nU suck ass")
			results.append("Lost")

	if a == "PLS STATS":
		print(results)

	if a == "PLS AI":
		print("Train or Stats?:")
		o = input("")
		if o.upper() == "STATS":
			print("Current Stats of AI:")
			print(ai)

		if o.upper() == "TRAIN":
			while True:
				print("Enter Depth (1 to 100)")
				depth = input("")
				try:
					aidepth = int(depth)
					break
				except ValueError:
					print("Numbers only")
			aix = 1
			while aix <= aidepth:
				ai.append(random.randint(1,10))
				aix += 1

			print(f"training results: {ai}")
			maxofnumbers = []
			ain = 1
			while ain <= 10:
				m = ai.count(ain)
				maxofnumbers.append(m)
				ain += 1
			print(f"Maximum count of each numbers from 1 to 10: {maxofnumbers}")

		if o.upper() == "PLAY":
			maxes = []
			for x in maxofnumbers:
				maxes.append(x)
			maxes.sort(reverse=1)


			print(f"Max list:{maxes}")
			first = maxofnumbers.index(maxes[0])+1
			print(first)
			
			second = maxofnumbers.index(maxes[1])+1
			print(second)
			
			third = maxofnumbers.index(maxes[2])+1
			print(third)




			

			