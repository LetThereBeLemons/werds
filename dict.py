def genDict(dict_var): # A function which generates the dictionary into whatever variable is passed to it.
	import requests # Imports the requests library, which is used to get the dictionary from the website.
	word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
	response = requests.get(word_site) # Gets the response from the website.
	dict_var = response.content.splitlines() # Splits the response into a list of words.
	doIt = True # This is set to False when the dictionary has been generated with no error. Janky, right?

	#! Warning: This is a really janky method of doing this. I can do better. FML.
	# Hint: Never do this. I am a fool. I am a fool. I am a fool.
	#* The code below is not commented properly because it is sh*t, I am stupid, and I hate myself.

	while doIt == True:
		try: #! AAAARRRRRRRGGGGGHHHHHHH GOD HELP ME
			for i in range(0, len(dict_var)):
				if len(dict_var[i]) != 4:
					dict_var.remove(dict_var[i])
			doIt = False
		except IndexError: #! WHAT HAVE I CREATED
			doIt = True #! WHAT HAVE I DONE
			continue
# Whew, ok. It's over. The work is done. I'm done. I'm done. I'm done. Help me.
#? Why am i like this.

	for i in range(0, len(dict_var)):
		dict_var[i] = dict_var[i].decode("UTF-8") # Decodes the bytes into a string.