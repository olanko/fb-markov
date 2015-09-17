#!/usr/bin/python3
# -*- coding: utf8 -*-

import random

class Markov(object):
	
	def __init__(self, open_file):
		self.cache = {}
		self.open_file = open_file
		self.words = self.file_to_words()
		self.word_size = len(self.words)
		self.database()
		
	
	def file_to_words(self):
		self.open_file.seek(0)
		data = self.open_file.read()
		words = data.split()
		return words
		
	
	def doubles(self):
		if len(self.words) < 2:
			return
		
		for i in range(len(self.words) - 1):
			yield (self.words[i], self.words[i+1])
			
	def database(self):
		for w1, w2 in self.doubles():
			key = (w1)
			if key in self.cache:
				self.cache[key].append(w2)
			else:
				self.cache[key] = [w2]
				
	def generate_markov_text(self, size=25):
		seed = random.randint(0, self.word_size-2)
		seed_word = self.words[seed]
		w1 = seed_word
		gen_words = []
		for i in range(size):
			gen_words.append(w1)
			w1 = random.choice(self.cache[(w1)])
		gen_words.append(w1)
		return ' '.join(gen_words)
