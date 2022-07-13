# Werds - A LetThereBeLemons and @JamesBlake5 [repl.it] creation.
# Liscensed under DONT STEAL ME CODE YOU  (DSMCY )
version = "b1-3"

# Hint: "Better Comments" VSCode extension is recommended, it adds some nice colours based on the type of comment.
# Hint: Use the "Live Share" extension to collaborate, if you haven't already.



import requests # Imports the requests library, which is used to get the dictionary from the website.
word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(word_site) # Gets the response from the website.
WORDS = response.content.splitlines() # Splits the response into a list of words.
doIt = True # This is set to False when the dictionary has been generated with no error. Janky, right?

#! Warning: This is a really janky method of doing this. I can do better.
# Hint: Never do this. I am a fool. I am a fool. I am a fool.

while doIt == True:
  try: #! AAAARRRRRRRGGGGGHHHHHHH GOD HELP ME
    for i in range(0, len(WORDS)):
      if len(WORDS[i]) != 4:
        WORDS.remove(WORDS[i])
    doIt = False
  except IndexError: #! WHAT HAVE I CREATED
    doIt = True #! WHAT HAVE I DONE
    continue

  for i in range(0, len(WORDS)):
    WORDS[i] = WORDS[i].decode("UTF-8") # Decodes the bytes into a string.


import random


def stringFromList(input): # Converts a list into a string, by taking each character and adding them to the string.
  output = ""
  for i in range(0, len(input)):
    output = output + str(input[i])

  return output

game = True # This will be set to False when the game is over.
pwd = list(random.choice(WORDS).upper()) # "previous word", the string is converted into a list to save later pain.
pwdlist = []

while game == True:
  print("Current word is: " + pwd[0] + pwd[1] + pwd[2] + pwd[3]) # Prints the current word, one letter at a time.
  selection = int(input("Which letter would you like to change? [1-4]: ")) - 1
  newletter = str(input("What would you like to change it to? [a-z]: "))
  pwd_new = pwd # Sets the pwd_new variable to the pwd variable, so that it can be changed later.
  pwd_new[selection] = newletter.upper() # Sets the desired position to the desired letter.

  if stringFromList(pwd_new).lower() in pwdlist:
    print("fail, word already used " + stringFromList(pwdlist))
  elif stringFromList(pwd_new).lower() in WORDS:
    print("success")
    pwdlist.append(stringFromList(pwd_new).lower())
    game = False
  else:
    print("fail " + stringFromList(pwd_new).lower())
    game = False