# Werds - A LetThereBeLemons and @JamesBlake5 [repl.it] creation.
# Liscensed under DONT STEAL ME CODE YOU ASSHOLE (DSMCYA)
version = "b1-2"

#TODO: Currently in the process of adding comments to this sh*tty code.
# Hint: "Better Comments" VSCode extension is recommended, it adds some nice colours based on the type of comment.


WORDS = []
import dict
import random

def stringFromList(input):
	output = ""
	for i in range(0, len(input)):
		output = output + str(input[i])

	return output


game = True
pwd = list(random.choice(WORDS).upper())

while game == True:
	print("Current word is: " + pwd[0] + pwd[1] + pwd[2] + pwd[3])
	selection = int(input("Which letter would you like to change? [1-4]: "))
	newletter = str(input("What would you like to change it to? [a-z]: "))
	pwd_new = pwd; pwd_new[selection] = newletter.upper()
	if stringFromList(pwd_new).lower() in WORDS:
		print("success")
	else:
		print("fail " + stringFromList(pwd_new).lower())

	input()