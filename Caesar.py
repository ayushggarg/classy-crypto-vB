def Caesar(message, mode, key):
	key = int(key)
	LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	translated = ''
	message = message.upper()

	for symbol in message:
		if symbol in LETTERS:
			num = LETTERS.find(symbol)
			if mode == 'encrypt':
				num = (num+key)%26
			elif mode == 'decrypt':
				num = (num-key)%26
			translated = translated + LETTERS[num]
		else:
			translated = translated + symbol
	translated = translated.lower()
	return (translated)
