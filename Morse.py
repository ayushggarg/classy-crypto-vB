CODE = {
'A': '.-', 'B': '-...', 'C': '-.-.',
'D': '-..', 'E': '.', 'F': '..-.',
'G': '--.', 'H': '....', 'I': '..',
'J': '.---', 'K': '-.-', 'L': '.-..',
'M': '--', 'N': '-.', 'O': '---',
'P': '.--.', 'Q': '--.-', 'R': '.-.',
'S': '...', 'T': '-', 'U': '..-',
'V': '...-', 'W': '.--', 'X': '-..-',
'Y': '-.--', 'Z': '--..',
'0': '-----', '1': '.----', '2': '..---',
'3': '...--', '4': '....-', '5': '.....',
'6': '-....', '7': '--...', '8': '---..',
'9': '----.',
' ': '/',
'.': '.-.-.-', 
',': '--..--',
'?': '..--..',
'-': '-....-',
'=': '-...-',
':': '---...',
';': '-.-.-.',
'(': '-.--.',
')': '-.--.-',
'/': '-..-.',
'"': '.-..-.',
}

def Morse(message, mode):
	inverse = dict((v,k) for (k,v) in CODE.items())
	message = message.upper()
	translated = ''

	if mode == 'encrypt':
		for symbol in message:
			if symbol in CODE:
				translated += CODE[symbol] + ' '
		return (translated)

	elif mode == 'decrypt':
		for symbol in message.split():
			translated += inverse[symbol]
		return (translated.lower())

