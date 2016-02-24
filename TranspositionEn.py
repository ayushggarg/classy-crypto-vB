def TranspositionEn(message, key):
	#myMessage = 'Common sense is not so common.'
	#myKey = 8
	key = int(key)
	ciphertext = encryptMessage(key, message)
	return(ciphertext + '|')

def encryptMessage(key, message):
	ciphertext = [''] * key
	for col in range(key):
		pointer = col
		while pointer < len(message):
			ciphertext[col] += message[pointer]
			pointer += key
	return ''.join(ciphertext)
