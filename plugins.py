import pygame, os, sys, random

class Cow:
	def __init__(self, x, y, img, linha):
		self.x     = x
		self.y     = y
		self.img   = img
		self.linha = linha

class Dino:
	def __init__(self, x, y, img, linha):
		self.x     = x
		self.y     = y
		self.img   = img
		self.linha = linha

class Player:
	def __init__(self, x, y, img, linha):
		self.x     = x
		self.y     = y
		self.img   = img
		self.linha = linha

class Ufo:
	def __init__(self, x, y, img, linha):
		self.x     = x
		self.y     = y
		self.img   = img
		self.linha = linha

def get_music_file():
	lista = os.listdir('assets/music')
	for i in lista:
		if "gameover" not in i:
			return f"assets/music/{random.choice(lista)}"