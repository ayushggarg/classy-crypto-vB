LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def Atbash(message):
	translated = str()
	message = message.upper()

	for symbol in message:
	    if symbol in LETTERS:
	    	num = LETTERS.find(symbol)
	    	num = 25-num
	    	translated = translated + LETTERS[num]
	    else:
	    	translated = translated + symbol
	    translated = translated.lower()
	return (translated)