import random
low=1
high=100
number=random.randint(low,high)
guesses=0
while True:
	guess=input(f"guess a number between ({low}-{high}) : ")
	if guess.isdigit():
			guess=int(guess)
			guesses+=1
			if guess<low or guess>high:
				print("your number is out of range")
			elif guess<number:
				print("its too small")
			elif guess>number:
				print("its too big")
			else:
				print(" your guess is correct")
				break
	else:
		print("you have entered invalid number")
		guess=int(input(f"guess a number between ({low}-{high}) : "))
	
print(f"no of guesses={guesses} ")
