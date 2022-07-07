# Werds - A LetThereBeLemons and @JamesBlake5 [repl.it] creation.
# Liscensed under DONT STEAL ME CODE YOU ASSHOLE (DSMCYA)
version = "b1-3"

# Hint: "Better Comments" VSCode extension is recommended, it adds some nice colours based on the type of comment.
# Hint: Use the "Live Share" extension to collaborate, if you haven't already.


WORDS = [] # Creates the WORDS variable before content is added by dict.py.
import dict # I put the dictionary-generating code in a separate file, dict.py.
# This makes managing each individual file easier.
import random

dict.genDict() # Generates the dictionary into the WORDS variable.

def stringFromList(input): # Converts a list into a string, by taking each character and adding them to the string.
	output = ""
	for i in range(0, len(input)):
		output = output + str(input[i])

	return output


game = True # This will be set to False when the game is over.
pwd = list(random.choice(WORDS).upper()) # "previous word", the string is converted into a list to save later pain.

while game == True:
	print("Current word is: " + pwd[0] + pwd[1] + pwd[2] + pwd[3]) # Prints the current word, one letter at a time.
	selection = int(input("Which letter would you like to change? [1-4]: "))
	newletter = str(input("What would you like to change it to? [a-z]: "))
	pwd_new = pwd # Sets the pwd_new variable to the pwd variable, so that it can be changed later.
	pwd_new[selection] = newletter.upper() # Sets the desired position to the desired letter.

	#! BUGGY CODE STARTS HERE
	#TODO: Fix this.

	if stringFromList(pwd_new).lower() in WORDS:
		print("success")
	else:
		print("fail " + stringFromList(pwd_new).lower())

	input() # Just so it doesn't keep looping.