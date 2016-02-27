import math

def TranspositionDy(message, key):
	#myMessage = 'Cenoonommstmme oo snnio. s s c'
	#myKey = 8
	key = int(key)
	plaintext = decryptMessage(key, message)
	return(plaintext + '|')

def decryptMessage(key, message):
	numOfColumns = math.ceil(len(message) / key)
	numOfRows = key
	numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
	plaintext = [''] * numOfColumns
	col = 0
	row = 0
	for symbol in message:
		plaintext[col] += symbol
		col += 1
		if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
			col = 0
			row += 1
	return ''.join(plaintext)


def TranspositionEn(message, key):
	#myMessage = 'Common sense is not so common.'
	#myKey = 8
	key = int(key)
	ciphertext = encryptMessage(key, message)
	return(ciphertext)

def encryptMessage(key, message):
	ciphertext = [''] * key
	for col in range(key):
		pointer = col
		while pointer < len(message):
			ciphertext[col] += message[pointer]
			pointer += key
	return ''.join(ciphertext)
