import random
low=1
high=100
number=random.randint(low,high)
guesses=0
while True:
	guess=int(input("guess a number between 1-100 : "))
	guesses+=1
	if guess<number:
		print("its too small")
	elif guess>number:
		print("its too big")
	else:
		print("guess is correct")
		break
	
print(f"no of guesses={guesses} ")
