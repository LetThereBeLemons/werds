def genDict():
	import requests
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