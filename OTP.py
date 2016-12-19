def OTP(message, key, mode):

	LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	translated = ''
	message = message.upper()
	key = key.upper()

	key_pos = 0
	for symbol in message:
		if symbol in LETTERS:
			num1 = LETTERS.find(symbol)
			if (key_pos < len(key)):
				num2 = LETTERS.find(key[key_pos])
				key_pos += 1
			else:
				num2 = 0

			if mode == 'encrypt':
				num = (num1 + num2)%26
			elif mode == 'decrypt':
				num = (num1 - num2)%26
			translated = translated + LETTERS[num]
		else:
			translated = translated + symbol
	translated = translated.lower()
	return (translated)
