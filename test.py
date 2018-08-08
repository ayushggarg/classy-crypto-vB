#!/usr/bin/env python

import flask
import webbrowser
from Atbash import Atbash
from Affine import Affine
from Base64 import encryptBase, decryptBase
from Caesar import Caesar
from Frequency import Frequency
from Letter import Letter
from Morse import Morse
from OTP import OTP
from Reverse import Reverse
from Transposition import TranspositionEn, TranspositionDy
from Vigenere import encryptVigenere, decryptVigenere

url = "http://127.0.0.1:5000/"
webbrowser.open_new_tab(url) 

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('home.html')

@app.route('/Mystery')
def Mystery():
    return flask.render_template('home.html')

@app.route("/eNdE" , methods=['GET', 'POST'])
def eNdE():
	return flask.render_template('ende.html')

@app.route("/CaesarCipher")
def CaesarCipher():
    return flask.render_template("caesarcipher.html")

@app.route("/caesar" , methods=['GET', 'POST'])
def caesar():
	if flask.request.method == 'POST':
		status = flask.request.form.get('submit')
		key = flask.request.form.get('key')
		if status == "encrypt":
			plaintext = flask.request.form.get('plain')
			ciphertext = Caesar(plaintext, status, key)
			#return jsonify(ciphertext=ciphertext)
			return("You Entererd Plaintext" + '<br/>' + plaintext + '<br/>' + "The Resultant Ciphertext" + '<br/>' + ciphertext)
		elif status == "decrypt":
			ciphertext = flask.request.form.get('plain')
			plaintext = Caesar(ciphertext, status, key)
			return("You Entererd Ciphertext" + '<br/>' + ciphertext + '<br/>' + "The Resultant Plaintext" + '<br/>' + plaintext)

@app.route("/ReverseCipher")
def ReverseCipher():
    return flask.render_template("reversecipher.html")

@app.route("/reverse" , methods=['GET', 'POST'])
def reverse():
	if flask.request.method == 'POST':
		status = flask.request.form.get('submit')
		if status == "encrypt":
			plaintext = flask.request.form.get('plain')
			ciphertext = Reverse(plaintext)
			return("You Entererd Text" + '<br/>' + plaintext + '<br/>' + "The Resultant Reverse text" + '<br/>' + ciphertext)


@app.route("/TranspositionCipher")
def TranspositionCipher():
    return flask.render_template("transpositioncipher.html")

@app.route("/transposition" , methods=['GET', 'POST'])
def transposition():
	if flask.request.method == 'POST':
		status = flask.request.form.get('submit')
		key = flask.request.form.get('key')
		if status == "encrypt":
			plaintext = flask.request.form.get('plain')
			ciphertext = TranspositionEn(plaintext, key)
			return("You Entererd Plaintext" + '<br/>' + plaintext + '<br/>' + "The Resultant Ciphertext" + '<br/>' + ciphertext)
		elif status == "decrypt":
			ciphertext = flask.request.form.get('plain')
			plaintext = TranspositionDy(ciphertext, key)
			return("You Entererd Ciphertext" + '<br/>' + ciphertext + '<br/>' + "The Resultant Plaintext" + '<br/>' + plaintext)

@app.route("/VigenereCipher")
def VigenereCipher():
	return flask.render_template("vigenerecipher.html")

@app.route("/vigenere", methods=['GET', 'POST'])
def vigenere():
	if flask.request.method == 'POST':
		status = flask.request.form.get('submit')
		key = flask.request.form.get('key')
		if status == "encrypt":
			plaintext = flask.request.form.get('plain')
			ciphertext = encryptVigenere(key, plaintext)
			return("You Entererd Plaintext" + '<br/>' + plaintext + '<br/>' + "The Resultant Ciphertext" + '<br/>' + ciphertext)
		elif status == "decrypt":
			ciphertext = flask.request.form.get('plain')
			plaintext = decryptVigenere(key, ciphertext)
			return("You Entererd Ciphertext" + '<br/>' + ciphertext + '<br/>' + "The Resultant Plaintext" + '<br/>' + plaintext)

@app.route("/AffineCipher")
def AffineCipher():
	return flask.render_template("affinecipher.html")

@app.route("/affine", methods=['GET', 'POST'])
def affine():
	if flask.request.method == 'POST':
		status = flask.request.form.get('submit')
		key1 = flask.request.form.get('key1')
		key2 = flask.request.form.get('key2')
		if status == "encrypt":
			plaintext = flask.request.form.get('plain')
			ciphertext = Affine(plaintext, key1, key2, status)
			return("You Entererd Plaintext" + '<br/>' + plaintext + '<br/>' + "The Resultant Ciphertext" + '<br/>' + ciphertext)
		elif status == "decrypt":
			ciphertext = flask.request.form.get('plain')
			plaintext = Affine(ciphertext, key1, key2, status)
			return("You Entererd Ciphertext" + '<br/>' + ciphertext + '<br/>' + "The Resultant Plaintext" + '<br/>' + plaintext)

@app.route("/OTPCipher")
def OTPCipher():
	return flask.render_template("otpcipher.html")

@app.route("/otp", methods=['GET', 'POST'])
def otp():
	if flask.request.method == 'POST':
		status = flask.request.form.get('submit')
		key = flask.request.form.get('key')
		if status == "encrypt":
			plaintext = flask.request.form.get('plain')
			ciphertext = OTP(plaintext, key, status)
			return("You Entererd Plaintext" + '<br/>' + plaintext + '<br/>' + "The Resultant Ciphertext" + '<br/>' + ciphertext)
		elif status == "decrypt":
			ciphertext = flask.request.form.get('plain')
			plaintext = OTP(ciphertext, key, status)
			return("You Entererd Ciphertext" + '<br/>' + ciphertext + '<br/>' + "The Resultant Plaintext" + '<br/>' + plaintext)

@app.route("/BaseCipher")
def BaseCipher():
	return flask.render_template("base64cipher.html")

@app.route("/basecipher", methods=['GET', 'POST'])
def basecipher():
	if flask.request.method == 'POST':
		status = flask.request.form.get('submit')
		if status == "encrypt":
			plaintext = flask.request.form.get('plain')
			ciphertext = encryptBase(plaintext)
			return("You Entererd Plaintext" + '<br/>' + plaintext + '<br/>' + "The Resultant Ciphertext" + '<br/>' + ciphertext)
		elif status == "decrypt":
			ciphertext = flask.request.form.get('plain')
			plaintext = decryptBase(ciphertext)
			return("You Entererd Ciphertext" + '<br/>' + ciphertext + '<br/>' + "The Resultant Plaintext" + '<br/>' + plaintext)

@app.route("/AtbashCipher")
def AtbashCipher():
	return flask.render_template("atbashcipher.html")

@app.route("/atbashcipher", methods=['GET', 'POST'])
def atbashcipher():
	if flask.request.method == 'POST':
		plaintext = flask.request.form.get('plain')
		ciphertext = Atbash(plaintext)
		return("You Entererd Plaintext" + '<br/>' + plaintext + '<br/>' + "The Resultant Ciphertext" + '<br/>' + ciphertext)

@app.route("/MorseCipher")
def MorseCipher():
	return flask.render_template("morsecipher.html")

@app.route("/morsecipher", methods=['GET', 'POST'])
def morsecipher():
	if flask.request.method == 'POST':
		status = flask.request.form.get('submit')
		if status == "encrypt":
			plaintext = flask.request.form.get('plain')
			ciphertext = Morse(plaintext, status)
			return("You Entererd Plaintext" + '<br/>' + plaintext + '<br/>' + "The Resultant Ciphertext" + '<br/>' + ciphertext)
		elif status == "decrypt":
			ciphertext = flask.request.form.get('plain')
			plaintext = Morse(ciphertext, status)
			return("You Entererd Ciphertext" + '<br/>' + ciphertext + '<br/>' + "The Resultant Plaintext" + '<br/>' + plaintext)

@app.route("/LetterCipher")
def LetterCipher():
	return flask.render_template("lettercipher.html")

@app.route("/lettercipher", methods=['GET', 'POST'])
def lettercipher():
	if flask.request.method == 'POST':
		status = flask.request.form.get('submit')
		if status == "encrypt":
			plaintext = flask.request.form.get('plain')
			ciphertext = Letter(plaintext, status)
			return("You Entererd Plaintext" + '<br/>' + plaintext + '<br/>' + "The Resultant Ciphertext" + '<br/>' + ciphertext)
		elif status == "decrypt":
			ciphertext = flask.request.form.get('plain')
			plaintext = Letter(ciphertext, status)
			return("You Entererd Ciphertext" + '<br/>' + ciphertext + '<br/>' + "The Resultant Plaintext" + '<br/>' + plaintext)

@app.route("/FrequencyAnalysis")
def FrequencyAnalysis():
	return flask.render_template("frequencyanalysis.html")

@app.route("/frequencyanalysis", methods=['GET', 'POST'])
def frequencyanalysis():
	if flask.request.method == 'POST':
		plaintext = flask.request.form.get('plain')
		ciphertext = Frequency(plaintext)
		return("You Entererd Plaintext" + '<br/>' + plaintext + '<br/>' + "The Frequency Analysis is " + '<br/>' + ciphertext)



if __name__ == '__main__':
	app.debug=True
	app.run()