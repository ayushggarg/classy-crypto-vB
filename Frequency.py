ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F':
0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N':
0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V':
0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

def getLetterCount(message):
	for symbol in message.upper():
		if symbol in LETTERS:
			letterCount[symbol] += 1
	return (letterCount)

def getItemAtIndexZero(x):
	return (x[0])

def getFrequencyOrder(message, letterToFreq):
	freqToLetter = {}
	for letter in LETTERS:
		if letterToFreq[letter] not in freqToLetter:
			freqToLetter[letterToFreq[letter]] = [letter]
		else:
			freqToLetter[letterToFreq[letter]].append(letter)

	for freq in freqToLetter:
		freqToLetter[freq].sort(key=ETAOIN.find, reverse=True)
		freqToLetter[freq] = ''.join(freqToLetter[freq])
	#print (freqToLetter)

	freqPairs = list(freqToLetter.items())
	freqPairs.sort(key=getItemAtIndexZero, reverse=True)
	freqOrder = []
	for freqPair in freqPairs:
		freqOrder.append(freqPair[1])
	return ''.join(freqOrder)

def Frequency(message):
	translated = str()
	letterToFreq = getLetterCount(message)
	freqOrder = getFrequencyOrder(message, letterToFreq)
	for symbol in freqOrder:
		translated += symbol + ':' + str(letterToFreq[symbol]) + '<br/>'
	return (translated)