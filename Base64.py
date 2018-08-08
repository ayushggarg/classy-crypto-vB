LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

def encryptBase(message):
	translated = str()
	for i in range (0,len(message),3):
		arr = str()
		text = message[i:i+3]
		for j in range(0,len(text)):
			arr +=  (str(bin(ord(text[j])))[2:].zfill(8))

		if (len(arr)==24):
			for j in range(0,len(arr),6):
				translated +=  LETTERS[int(arr[j:j+6],2)]
		elif (len(arr)==16):
			arr += '00'
			for j in range(0,len(arr),6):
				translated +=  LETTERS[int(arr[j:j+6],2)]
			translated += '='
		elif (len(arr)==8):
			arr += '0000'
			for j in range(0,len(arr),6):
				translated +=  LETTERS[int(arr[j:j+6],2)]
			translated += '=='
	return (translated)

def decryptBase(message):
	translated = str()
	for i in range (0,len(message),4):
		arr = str()
		if (message[len(message)-1] == '='):
			message = message[0:len(message)-1]

		text = message[i:i+4]
		for j in range(0,len(text)):
			arr +=  (str(bin(LETTERS.find(text[j])))[2:].zfill(6))

		if (len(arr)==24):
			for j in range(0,len(arr),8):
				translated +=  chr(int(arr[j:j+8],2))
		elif (len(arr)==18):
			arr = arr[0:16]
			for j in range(0,len(arr),8):
				translated +=  chr(int(arr[j:j+8],2))
		elif (len(arr)==12):
			arr = arr[0:8]
			for j in range(0,len(arr),8):
				translated +=  chr(int(arr[j:j+8],2))
	return (translated)