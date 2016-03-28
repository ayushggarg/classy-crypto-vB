LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def Letter(message, mode):
	message = message.upper()
	translated = str()

	if mode == 'encrypt':
		for symbol in message:
			if symbol in LETTERS:
				num = str(LETTERS.find(symbol)+1).zfill(2)
				translated += num
			elif (translated[len(translated)-1] != ' '):
				translated += ' '
		return (translated)

	if mode == 'decrypt':
		i = 0
		while (i < (len(message))):
			if(message[i] != ' '):
				text = message[i:i+2]
				#print (text)
				translated +=  LETTERS[int(text)-1]
				i += 2
			else:
				translated += message[i]
				i += 1
		return (translated.lower())