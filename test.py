#!/usr/bin/env python

import flask
from Caesar import Caesar
from Reverse import Reverse
from TranspositionEn import TranspositionEn
from TranspositionDy import TranspositionDy

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
		key = flask.request.form.get('Key')
		if status == "encrypt":
			plaintext = flask.request.form.get('Plain')
			ciphertext = Caesar(plaintext, status, key)
			return("You Entererd Plainttext" + '<br/>' + plaintext + '<br/>' + "The Resultant Ciphertext" + '<br/>' + ciphertext)
		elif status == "decrypt":
			ciphertext = flask.request.form.get('Cipher')
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
			plaintext = flask.request.form.get('Plain')
			ciphertext = Reverse(plaintext)
			return("You Entererd Plainttext" + '<br/>' + plaintext + '<br/>' + "The Resultant Ciphertext" + '<br/>' + ciphertext)
		elif status == "decrypt":
			ciphertext = flask.request.form.get('Cipher')
			plaintext = Reverse(ciphertext)
			return("You Entererd Ciphertext" + '<br/>' + ciphertext + '<br/>' + "The Resultant Plaintext" + '<br/>' + plaintext)


@app.route("/TranspositionCipher")
def TranspositionCipher():
    return flask.render_template("transpositioncipher.html")

@app.route("/transposition" , methods=['GET', 'POST'])
def transposition():
	if flask.request.method == 'POST':
		status = flask.request.form.get('submit')
		key = flask.request.form.get('Key')
		if status == "encrypt":
			plaintext = flask.request.form.get('Plain')
			ciphertext = TranspositionEn(plaintext, key)
			return("You Entererd Plainttext" + '<br/>' + plaintext + '<br/>' + "The Resultant Ciphertext" + '<br/>' + ciphertext)
		elif status == "decrypt":
			ciphertext = flask.request.form.get('Cipher')
			plaintext = TranspositionDy(ciphertext, key)
			return("You Entererd Ciphertext" + '<br/>' + ciphertext + '<br/>' + "The Resultant Plaintext" + '<br/>' + plaintext)

if __name__ == '__main__':
	app.debug=True
	app.run()