
# Do not modify!
import requests, random
word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(word_site)
WORDS = response.content.splitlines()
doIt = True
while doIt == True:
  try:
    for i in range(0, len(WORDS)):
      if len(WORDS[i]) != 4:
        WORDS.remove(WORDS[i])
    doIt = False
  except IndexError:
    doIt = True
    continue
  except AttributeError:
    print("weird error happened again")
    exit()

for i in range(0, len(WORDS)):
  WORDS[i] = WORDS[i].decode("UTF-8")
# ^^^

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