#!/usr/bin/env python3

from textblob import TextBlob
from textblob import Word
from textblob.taggers import NLTKTagger
import argparse
import nltk
import sys

"""translator script & Polarity, Subjectivity 
after testing, auto-correct (correct method) didn't really work as expected"""


def sent(args):
	"""grabs input, applies TextBlob, and outputs sentiment"""
	word = sys.argv[1:]
	output = TextBlob(str(word))		# had to force str here to avoid TypeError
	# print(type(output))
	print(str(output.sentiment))


def translate(args):
	"""translator function
	TextBlob actually uses google translate under the hood"""
	word = sys.argv[2:]
	output = TextBlob(str(word))
	print(output.translate(to='es'))


def detect_lang(args):
	"""detects language for input"""
	word = sys.argv[1:]
	output = TextBlob(str(word))
	print("{} is in {}".format(word[1:], output.detect_language()))

# argparser
def main():
	"""main instantiates VTSafe class and executes functionality for all functions"""
	parser = argparse.ArgumentParser(description="""Translate words and does sentiment analysis on them.""")
	parser.add_argument('-s', '--sentiment', help='Performs a sentiment analysis in the words\n'
												  'where 0 is very objective, 1.0 is very subjective')
	parser.add_argument('-t', '--translate', help='Performs a translation of the words, to spanish')
	parser.add_argument('-d', '--detect_lang', help='Detects language of the words')
	args = parser.parse_args()

	if len(sys.argv) < 2:
		sys.exit("Usage: Run script as follows: translator_script.py [words]\n\n"
				 	"translator_script.py -h for full help details")

	if args.sentiment:
		sent(args.sentiment)

	if args.translate:
		translate(args.translate)

	if args.detect_lang:
		detect_lang(args.detect_lang)


if __name__ == '__main__':
	main()
