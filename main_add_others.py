#    _____ __  ______   _____ __  __   __  ______  __ 
#   / ___//  |/  /   | / ___// / / /  / / / / __ \/ /
#   \__ \/ /|_/ / /| | \__ \/ /_/ /  / / / / /_/ / /
#  ___/ / /  / / ___ |___/ / __  /  / /_/ / ____/_/
# /____/_/  /_/_/  |_/____/_/ /_/   \____/_/   (_)
#
#  _    __   ____       ___     _____
# | |  / /  / __ \     <  /    |__  /
# | | / /  / / / /     / /      /_ < 
# | |/ /  / /_/ /     / /     ___/ / 
# |___/   \____(_)   /_(_)   /____/  

import random
import os
from itertools import *

play = []
base_play = []
play_factions = []
current_player = None

#Input
#Program
#Module
	
def move_card(index, place_from, place_to, deck = "bottom" ):
	#Moves a card from one place to another
	if deck == "top":
		current_player.deck = [place_from.pop(index)] + current_player.deck
	else:
		place_to.append(place_from.pop(index))

def play_card(place_from, index):
	temp_loop = True
	while temp_loop == True:
		try:
			flip()
			follow_up = input(":: Which base will you play " + place_from[index].name + " on? (c to cancel): ")
			if follow_up == "c":
				flip()
				temp_loop = False
			elif int(follow_up) - 1 <= len(play):
				place_from[index].owner = current_player
				move_card(index, place_from, play[int(follow_up) - 1][place_from[index].owner.number - 1])
				flip()
				temp_loop = False
			else:
				flip()
				print(":: " + follow_up)
				print("")
				input("\nInvalid base")
		except:
			flip()
			print(":: " + follow_up)
			print("")
			input5("\nInvalid base")

def draw_card(player, numCards, discard_cards = False):
	player.draw(numCards)
	if len(player.hand) > 10 and discard_cards == True:
		input(player.name + "'s hand is too full. " + player.name + " needs to discard a card. (press enter for list of cards) ")
		while(1 == 1):
			player.show_hand(basic = True)
			print("")
			follow_up = input(":: ")
			try:
				if follow_up[:7] == 'discard' and int(follow_up[-2:]) <= len(player.hand):
					if len(follow_up) == 9:
							flip()
							#input(player.hand[int(follow_up) - 1].name + " was discarded")
							move_card(int(follow_up[-1:]) - 1, player.hand, player.discard)
							if len(player.hand) > 10:
								continue
							else:
								flip()
								break
					elif len(follow_up) == 10:
							flip()
							#input(player.hand[int(follow_up) - 1].name + " was discarded")
							move_card(int(follow_up[-2:]) - 1, player.hand, player.discard)
							if len(player.hand) > 10:
								continue
							else:
								flip()
								break
					else:
						input("\nInvalid Value")
				elif follow_up[:4] == 'read':
					if len(follow_up) == 6:
						print_card(player.hand[int(follow_up[-1:]) - 1])
						input("")
						continue

					if len(follow_up) == 7:
						print_card(player.hand[int(follow_up[-2:]) - 1])
						input("")
						continue

					else:
						card_to_print = ""
						for card in player.hand:
							if card.name == follow_up[5:]:
								card_to_print = card
						if(card_to_print != ""):
							print_card(card_to_print)
							input("")
						else:
							print("")
							input("Invalid Name")
							
						
				else:
					input("\nInvalid Value")
			except:
				input("\nInvalid Value Error: 101") ###
	

###MOSTLY USELESS, CONSIDER DELETING/PATCHING
def discard_card(player, index):
	player.discard_card(index)
	
def discard_random(player):
	randomInteger = random.randint(0, len(player.hand) - 1)
	name = player.hand[randomInteger].name
	move_card(randomInteger, current_player.hand, current_player.discard)
	return name
###

#Main
#Program
#Module

class player():
	'''
	Representation of a smashup player including a deck, hand, and discard pile
	'''
	def __init__(self, deck_one, deck_two, name, victory = 0, number = 0):
		self.deck_one = Master[deck_one]
		self.deck_two = Master[deck_two]
		self.name = name
		self.victory = victory
		self.number = number
		
		self.deck = []
		self.hand = []
		self.discard = []

	def create_deck(self):
		#Creates a deck of two smash up factions
		for card in self.deck_one:
			self.deck.append(card)
			
		for card in self.deck_two:
			self.deck.append(card)
		
	def shuffle_deck(self):
		#Shuffles the current deck
		random.shuffle(self.deck)
		
	def draw_hand(self):
		#Draws five cards and puts them in the player's hand
		for i in range(5):
			self.hand.append(self.deck.pop(0))
	
	def draw(self, numCards):
		for card in range(numCards):
			self.hand.append(self.deck.pop(0))

	def discard_card(self, index):
		move_card(index, self.hand, self.discard)

	def show_hand(self, last = False, basic = False):
		#Shows the player's hand
		if basic == True:
			flip()
			if len(self.hand) <= 8:
				for i in range(len(self.hand)):
					print(str(i + 1) + ". " + self.hand[i].name)
			elif len(self.hand) <= 16:
				if len(self.hand) == 16:
					for i in range(0, 8):
						line = ((str(i + 1) + ". " + self.hand[i].name)).ljust(35) + str(i + 9) + ". " + self.hand[i + 8].name
						print(line)
				else:
					for i in range((len(self.hand)%8)):
						line = ((str(i + 1) + ". " + self.hand[i].name)).ljust(35) + str(i + 9) + ". " + self.hand[i + 8].name
						print(line)
					for i in range (len(self.hand)%8, 8):
						line = str(i + 1) + ". " + self.hand[i].name
						print(line)
			elif len(self.hand) < 24:
				for i in range((len(self.hand)%8)):
					line = (str(i + 1) + ". " + self.hand[i].name).ljust(35) + (str(i + 9) + ". " + self.hand[i + 8].name).ljust(35) + str(i + 17) + ". " + self.hand[i + 16].name
					print(line)
				for i in range (len(self.hand)%8, 8):
					line = (str(i + 1) + ". " + self.hand[i].name).ljust(35) + (str(i + 9) + ". " + self.hand[i + 8].name).ljust(35)
					print(line)
			else:
				print("Output has not been coded for that many cards. HOW THE HECK DID YOU GET THAT MANY!!!")
		else:
			player_hand_lines = ["", "", "", "", "", "", "", "", "", "", ""]
			flip()
			print(":: show hand")
			if last == "OVERFLOW":
				if len(self.hand) > 12: 
					for i in range(len(player_hand_lines)):
						for j in range(12, len(self.hand)):
							executable = "player_hand_lines[" + str(i) + "] = player_hand_lines[" + str(i) + "] + self.hand[" + str(j) + "].graphic.line_" + str(i + 1)
							exec(executable)	
				elif len(self.hand) <= 6:
					for i in range(len(player_hand_lines)):
						for j in range(len(self.hand)):
							executable = "player_hand_lines[" + str(i) + "] = player_hand_lines[" + str(i) + "] + self.hand[" + str(j) + "].graphic.line_" + str(i + 1)
							exec(executable)
				else:
					for i in range(len(player_hand_lines)):
						for j in range(6, len(self.hand)):
							executable = "player_hand_lines[" + str(i) + "] = player_hand_lines[" + str(i) + "] + self.hand[" + str(j) + "].graphic.line_" + str(i + 1)
							exec(executable)
			elif last == False:
				if len(self.hand) <= 6:
					for i in range(len(player_hand_lines)):
						for j in range(len(self.hand)):
							executable = "player_hand_lines[" + str(i) + "] = player_hand_lines[" + str(i) + "] + self.hand[" + str(j) + "].graphic.line_" + str(i + 1)
							exec(executable)
				else:
					for i in range(len(player_hand_lines)):
						for j in range(0, 6):
							executable = "player_hand_lines[" + str(i) + "] = player_hand_lines[" + str(i) + "] + self.hand[" + str(j) + "].graphic.line_" + str(i + 1)
							exec(executable)
			else:
				if len(self.hand) <= 6:
					for i in range(len(player_hand_lines)):
						for j in range(len(self.hand)):
							executable = "player_hand_lines[" + str(i) + "] = player_hand_lines[" + str(i) + "] + self.hand[" + str(j) + "].graphic.line_" + str(i + 1)
							exec(executable)
				elif len(self.hand) <= 12:
					for i in range(len(player_hand_lines)):
						for j in range(6, len(self.hand)):
							executable = "player_hand_lines[" + str(i) + "] = player_hand_lines[" + str(i) + "] + self.hand[" + str(j) + "].graphic.line_" + str(i + 1)
							exec(executable)
				else:
					for i in range(len(player_hand_lines)):
						for j in range(6, 12):
							executable = "player_hand_lines[" + str(i) + "] = player_hand_lines[" + str(i) + "] + self.hand[" + str(j) + "].graphic.line_" + str(i + 1)
							exec(executable)
			for line in player_hand_lines:
				print(line)
	
	def show_discard(self):
		flip()
		print(":: show discard")
		print("")
		#Shows the player's discard pile
		print(self.name + "'s discard pile: ")
		if len(self.discard) <= 8:
			for i in range(len(self.discard)):
				print(str(i + 1) + ". " + self.discard[i].name)
		elif len(self.discard) <= 16:
			if len(self.discard) == 16:
				for i in range(0, 8):
					line = ((str(i + 1) + ". " + self.discard[i].name)).ljust(35) + str(i + 9) + ". " + self.discard[i + 8].name
					print(line)
			else:
				for i in range((len(self.discard)%8)):
					line = ((str(i + 1) + ". " + self.discard[i].name)).ljust(35) + str(i + 9) + ". " + self.discard[i + 8].name
					print(line)
				for i in range (len(self.discard)%8, 8):
					line = str(i + 1) + ". " + self.discard[i].name
					print(line)
		elif len(self.discard) <= 24:
			if len(self.discard) == 24:
				for i in range(0, 8):
					line = ((str(i + 1) + ". " + self.discard[i].name)).ljust(35) + (str(i + 9) + ". " + (self.discard[i + 8]).name).ljust(35) + (str(i + 17) + ". " + self.discard[i + 16].name).ljust(35)
					print(line)
			else:
				for i in range((len(self.discard)%8)):
					line = (str(i + 1) + ". " + self.discard[i].name).ljust(35) + (str(i + 9) + ". " + self.discard[i + 8].name).ljust(35) + (str(i + 17) + ". " + self.discard[i + 16].name).ljust(35)
					print(line)
				for i in range (len(self.discard)%8, 8):
					line = (str(i + 1) + ". " + self.discard[i].name).ljust(35) + str(i + 9) + ". " + self.discard[i + 8].name
					print(line)
		elif len(self.discard) <= 32:
			if len(self.discard) == 32:
				for i in range(0, 8):
					line = ((str(i + 1) + ". " + self.discard[i].name)).ljust(35) + (str(i + 9) + ". " + self.discard[i + 8].name).ljust(35) + (str(i + 17) + ". " + self.discard[i + 16].name).ljust(35) + (str(i + 25) + ". " + self.discard[i + 24].name).ljust(35)
					print(line)
			else:
				for i in range((len(self.discard)%8)):
					line = (str(i + 1) + ". " + self.discard[i].name).ljust(35) + (str(i + 9) + ". " + self.discard[i + 8].name).ljust(35) + (str(i + 17) + ". " + self.discard[i + 16].name).ljust(35) + (str(i + 25) + ". " + self.discard[i + 24].name).ljust(35)
					print(line)
				for i in range((len(self.discard)%8), 8):
					line = (str(i + 1) + ". " + self.discard[i].name).ljust(35) + (str(i + 9) + ". " + self.discard[i + 8].name).ljust(35) + (str(i + 17) + ". " + self.discard[i + 16].name).ljust(35)
					print(line)
		elif len(self.discard) <= 40:
			if len(self.discard) == 40:
				for i in range(0, 8):
					line = ((str(i + 1) + ". " + self.discard[i].name)).ljust(35) + (str(i + 9) + ". " + self.discard[i + 8].name).ljust(35) + (str(i + 17) + ". " + self.discard[i + 16].name).ljust(35) + (str(i + 25) + ". " + self.discard[i + 24].name).ljust(35) + (str(i + 33) + ". " + self.discard[i + 32].name)
					print(line)
			else:
				for i in range((len(self.discard)%8)):
					line = (str(i + 1) + ". " + self.discard[i].name).ljust(35) + (str(i + 9) + ". " + self.discard[i + 8].name).ljust(35) + (str(i + 17) + ". " + self.discard[i + 16].name).ljust(35) + (str(i + 25) + ". " + self.discard[i + 24].name).ljust(35) + (str(i + 33) + ". " + self.discard[i + 32].name)
					print(line)
				for i in range((len(self.discard)%8), 8):
					line = (str(i + 1) + ". " + self.discard[i].name).ljust(35) + (str(i + 9) + ". " + self.discard[i + 8].name).ljust(35) + (str(i + 17) + ". " + self.discard[i + 16].name).ljust(35) + (str(i + 25) + ". " + self.discard[i + 24].name).ljust(35)
					print(line)
		print("")
			
	def show_deck(self, cards = 'ALL'):
		#Shows the player's deck
		if (cards == "ALL"):
			flip()
			print(":: show deck")
			print("")
			print(self.name + "'s deck: ")
			if len(self.deck) <= 8:
				for i in range(len(self.deck)):
					print(str(i + 1) + ". " + self.deck[i].name)
			elif len(self.deck) <= 16:
				if len(self.deck) == 16:
					for i in range(0, 8):
						line = ((str(i + 1) + ". " + self.deck[i].name)).ljust(35) + (str(i + 9) + ". " + self.deck[i + 8].name).ljust(35)
						print(line)
				else:
					for i in range((len(self.deck)%8)):
						line = ((str(i + 1) + ". " + self.deck[i].name)).ljust(35) + str(i + 9) + ". " + self.deck[i + 8].name
						print(line)
					for i in range (len(self.deck)%8, 8):
						line = str(i + 1) + ". " + self.deck[i].name
						print(line)
			elif len(self.deck) <= 24:
				if len(self.deck) == 24:
					for i in range(0, 8):
						line = ((str(i + 1) + ". " + self.deck[i].name)).ljust(35) + (str(i + 9) + ". " + self.deck[i + 8].name).ljust(35) + (str(i + 17) + ". " + self.deck[i + 16].name).ljust(35)
						print(line)
				else:
					for i in range((len(self.deck)%8)):
						line = (str(i + 1) + ". " + self.deck[i].name).ljust(35) + (str(i + 9) + ". " + self.deck[i + 8].name).ljust(35) + (str(i + 17) + ". " + self.deck[i + 16].name).ljust(35)
						print(line)
					for i in range (len(self.deck)%8, 8):
						line = (str(i + 1) + ". " + self.deck[i].name).ljust(35) + str(i + 9) + ". " + self.deck[i + 8].name
						print(line)
			elif len(self.deck) <= 32:
				if len(self.deck) == 32:
					for i in range(0, 8):
						line = ((str(i + 1) + ". " + self.deck[i].name)).ljust(35) + (str(i + 9) + ". " + self.deck[i + 8].name).ljust(35) + (str(i + 17) + ". " + self.deck[i + 16].name).ljust(35) + (str(i + 25) + ". " + self.deck[i + 24].name).ljust(35)
						print(line)
				else:
					for i in range((len(self.deck)%8)):
						line = (str(i + 1) + ". " + self.deck[i].name).ljust(35) + (str(i + 9) + ". " + self.deck[i + 8].name).ljust(35) + (str(i + 17) + ". " + self.deck[i + 16].name).ljust(35) + (str(i + 25) + ". " + self.deck[i + 24].name).ljust(35)
						print(line)
					for i in range((len(self.deck)%8), 8):
						line = (str(i + 1) + ". " + self.deck[i].name).ljust(35) + (str(i + 9) + ". " + self.deck[i + 8].name).ljust(35) + (str(i + 17) + ". " + self.deck[i + 16].name).ljust(35)
						print(line)
			elif len(self.deck) <= 40:
				if len(self.deck) == 40:
					for i in range(0, 8):
						line = ((str(i + 1) + ". " + self.deck[i].name)).ljust(35) + (str(i + 9) + ". " + self.deck[i + 8].name).ljust(35) + (str(i + 17) + ". " + self.deck[i + 16].name).ljust(35) + (str(i + 25) + ". " + self.deck[i + 24].name).ljust(35) + (str(i + 33) + ". " + self.deck[i + 32].name)
						print(line)
				else:
					for i in range((len(self.deck)%8)):
						line = (str(i + 1) + ". " + self.deck[i].name).ljust(35) + (str(i + 9) + ". " + self.deck[i + 8].name).ljust(35) + (str(i + 17) + ". " + self.deck[i + 16].name).ljust(35) + (str(i + 25) + ". " + self.deck[i + 24].name).ljust(35) + (str(i + 33) + ". " + self.deck[i + 32].name)
						print(line)
					for i in range((len(self.deck)%8), 8):
						line = (str(i + 1) + ". " + self.deck[i].name).ljust(35) + (str(i + 9) + ". " + self.deck[i + 8].name).ljust(35) + (str(i + 17) + ". " + self.deck[i + 16].name).ljust(35) + (str(i + 25) + ". " + self.deck[i + 24].name).ljust(35)
						print(line)
			print("")
		else:
			if cards <= len(self.deck) and cards > 0:
				flip()
				print(":: show deck " + str(cards))
				print("")
				print(self.name + "'s deck: ")
				if cards <= 8:
					for i in range(cards):
						print(str(i + 1) + ". " + self.deck[i].name)
				elif cards <= 16:
					if cards == 16:
						for i in range(0, 8):
							line = ((str(i + 1) + ". " + self.deck[i].name)).ljust(35) + (str(i + 9) + ". " + self.deck[i + 8].name).ljust(35)
							print(line)
					else:
						for i in range((cards%8)):
							line = ((str(i + 1) + ". " + self.deck[i].name)).ljust(35) + str(i + 9) + ". " + self.deck[i + 8].name
							print(line)
						for i in range (cards%8, 8):
							line = str(i + 1) + ". " + self.deck[i].name
							print(line)
				elif cards <= 24:
					if cards == 24:
						for i in range(0, 8):
							line = ((str(i + 1) + ". " + self.deck[i].name)).ljust(35) + (str(i + 9) + ". " + self.deck[i + 8].name).ljust(35) + (str(i + 17) + ". " + self.deck[i + 16].name).ljust(35)
							print(line)
					else:
						for i in range(cards%8):
							line = (str(i + 1) + ". " + self.deck[i].name).ljust(35) + (str(i + 9) + ". " + self.deck[i + 8].name).ljust(35) + (str(i + 17) + ". " + self.deck[i + 16].name).ljust(35)
							print(line)
						for i in range (cards%8, 8):
							line = (str(i + 1) + ". " + self.deck[i].name).ljust(35) + str(i + 9) + ". " + self.deck[i + 8].name
							print(line)
				elif cards <= 32:
					if cards == 32:
						for i in range(0, 8):
							line = ((str(i + 1) + ". " + self.deck[i].name)).ljust(35) + (str(i + 9) + ". " + self.deck[i + 8].name).ljust(35) + (str(i + 17) + ". " + self.deck[i + 16].name).ljust(35) + (str(i + 25) + ". " + self.deck[i + 24].name).ljust(35)
							print(line)
					else:
						for i in range(cards%8):
							line = (str(i + 1) + ". " + self.deck[i].name).ljust(35) + (str(i + 9) + ". " + self.deck[i + 8].name).ljust(35) + (str(i + 17) + ". " + self.deck[i + 16].name).ljust(35) + (str(i + 25) + ". " + self.deck[i + 24].name).ljust(35)
							print(line)
						for i in range(cards%8, 8):
							line = (str(i + 1) + ". " + self.deck[i].name).ljust(35) + (str(i + 9) + ". " + self.deck[i + 8].name).ljust(35) + (str(i + 17) + ". " + self.deck[i + 16].name).ljust(35)
							print(line)
				elif cards <= 40:
					if cards == 40:
						for i in range(0, 8):
							line = ((str(i + 1) + ". " + self.deck[i].name)).ljust(35) + (str(i + 9) + ". " + self.deck[i + 8].name).ljust(35) + (str(i + 17) + ". " + self.deck[i + 16].name).ljust(35) + (str(i + 25) + ". " + self.deck[i + 24].name).ljust(35) + (str(i + 33) + ". " + self.deck[i + 32].name)
							print(line)
					else:
						for i in range((cards%8)):
							line = (str(i + 1) + ". " + self.deck[i].name).ljust(35) + (str(i + 9) + ". " + self.deck[i + 8].name).ljust(35) + (str(i + 17) + ". " + self.deck[i + 16].name).ljust(35) + (str(i + 25) + ". " + self.deck[i + 24].name).ljust(35) + (str(i + 33) + ". " + self.deck[i + 32].name)
							print(line)
						for i in range((cards%8), 8):
							line = (str(i + 1) + ". " + self.deck[i].name).ljust(35) + (str(i + 9) + ". " + self.deck[i + 8].name).ljust(35) + (str(i + 17) + ". " + self.deck[i + 16].name).ljust(35) + (str(i + 25) + ". " + self.deck[i + 24].name).ljust(35)
							print(line)
			else:
				flip()
				print("Invalid Command")
			print("")
		
def handle_input_shell():
	#Prompts the user for a main game loop command and processes it
	quit = False
	
	while not quit:
		
		command = input(":: ")
		print("")
		
		if command == 'c':
			flip()
			print(":: c")
			print("")
			print("List of Card Commands: \n")
			print("show hand - shows your current hand")
			print("show discard - shows your current discard pile")
			print("show deck - shows your current deck")
			print("show deck 'int' - shows the top 'int' card(s) in your deck\n")
			print("shuffle deck - shuffles your deck")
			print("draw 'int' - draws the top 'int' card(s) from your deck\n")
			print("discard 'index'- discards the specified card from your hand")
			print("discard random - discards a random card from your hand")
			print("discard base 'index' card 'index' - discards the specified card from the specified base")
			print("discard base 'index' - discards all cards from the specified base\n")
			print("play 'index' - plays a card from your hand")
			print("play discard 'index' - plays the specified card from the discard pile - ADD DOUBLE")
			print("return base 'index' card 'index' - places the specified card into your hand from the specified base\n")
			print("move base 'index' card 'index' - moves the speficied card at the specified base to a new one of your choosing")
			print("recard 'index' - places the specified card into your hand from your discard pile")
			print("recard deck 'index' - places the specified card into your deck from your discard pile\n")
			print("retrieve 'index' - places the specified card into your hand from your deck")
			print("distrieve 'index' - places the specified card into your deck from your hand\n")
			print("read 'card name' - shows you the card text from 'card name'\n")
			print("victory 'int' - gives you 'int' victory points")
			print("show victory - shows you your current victory point total\n")
			print("q - quit")
			print("")
		
		elif command[:4] == "show":
			if command == "show hand":
				current_player.show_hand()
			elif command == "show discard":
				current_player.show_discard()
			elif command[:9] == "show deck" and len(command) == 9:
				current_player.show_deck()
			elif command[:9] == "show deck" and (len(command) == 11 or len(command) == 12):
				current_player.show_deck(cards = int(command[10:]))
			elif command[:12] == "show victory":
				flip()
				print(":: show victory")
				print("")
				print(current_player.name + " has " + str(current_player.victory) + " victory points")
				print("")
			else:
				flip()
				print(":: " + command)
				print("")
				print("Invalid Command")
				print("")
		
		elif command == "<":
			current_player.show_hand()
					
		elif command == ">":
			current_player.show_hand(last = True)

		elif command == ">>":
			current_player.show_hand(last = "OVERFLOW")

		elif command == "shuffle deck":
			current_player.shuffle_deck()
			flip()
		
		elif command[:4] == "draw":
			try:
				if len(command) == 6:
					flip()
					print(":: draw " + command[5:])
					print("")
					print("You have drawn " + command[5:] + " card(s).")
					print("")
					draw_card(current_player, int(command[5:]))
				else:
					flip()
					print(":: draw " + command[5:])
					print("")
					print("Invalid Command - Keep In Mind That You Can't Draw More Than Nine Cards At Once")
					print("")
			except:
				flip()
				print(":: " + command)
				print("")
				print("Not Enough Cards in Deck")
				print("")
		elif command[:5] == "ddraw":
			try:
				if len(command) == 7:
					flip()
					print(":: draw " + command[6:])
					print("")
					print("You have drawn " + command[6:] + " card(s).")
					print("")
					draw_card(current_player, int(command[6:]), discard_cards = True)
				else:
					flip()
					print(":: draw " + command[6:])
					print("")
					print("Invalid Command - Keep In Mind That You Can't Draw More Than Nine Cards At Once")
					print("")
			except:
				flip()
				print(":: " + command)
				print("")
				print("Not Enough Cards in Deck")
				print("")
		
		elif command[:7] == "discard":
			try:
				if len(command) == 9:
					if int(command[8:]) <= len(current_player.hand):
						flip()
						print(":: " + command)
						print("")
						print(current_player.hand[int(command[8:]) - 1].name + " was discarded")
						current_player.discard_card(int(command[8:]) - 1)
						print("")
					else:
						flip()
						print(":: " + command)
						print("")
						print("Invalid Command")
						print("")

				elif len(command) == 10:
					if int(command[-2:]) <= len(current_player.hand):
						flip()
						print(":: " + command)
						print("")
						print(current_player.hand[int(command[-2:]) - 1].name + " was discarded")
						current_player.discard_card(int(command[-2:]) - 1)
						print("")
					else:
						flip()
						print(":: " + command)
						print("")
						print("Invalid Command")
						print("")

				elif command == "discard random":
					flip()
					print(":: " + command)
					print("")
					name = discard_random(current_player)
					print(name + " was randomly discarded!")
					print("")

				elif command[:12] == "discard base":
					if len(command) == 14:
						words = ""
						for card in range(len(play[int(command[13]) - 1][current_player.number - 1])):
							words = words + "\n" + play[int(command[13]) - 1][current_player.number - 1][0].name + " was discarded from base " + command[13]
							move_card(0, play[int(command[13]) - 1][current_player.number - 1], current_player.discard)
						flip()
						print(":: " + command)
						print(words)
						print("")
					if len(command) == 21:
						words = play[int(command[13]) - 1][current_player.number - 1][int(command[20]) - 1].name + " was discarded from base " + command[13]
						move_card(int(command[20]) - 1, play[int(command[13]) - 1][current_player.number - 1], current_player.discard)
						flip()
						print(":: " + command)
						print("")
						print(words)
						print("")
					elif len(command) == 22:
						words = play[int(command[13]) - 1][current_player.number - 1][int(command[-2:]) - 1].name + " was discarded from base " + command[13]
						move_card(int(command[-2:]) - 1, play[int(command[13]) - 1][current_player.number - 1], current_player.discard)
						flip()
						print(":: " + command)
						print("")
						print(words)
						print("")
				else:
					flip()
					print(":: " + command)
					print("Invalid Command")
					print("")
			except:
				flip()
				print(":: " + command)
				print("")
				print("Invalid Command Error 102")
				print("")
			
		elif command[:4] == "play":
			try:
				if len(command) == 6 and int(command[5:]) > 0:
					play_card(current_player.hand, int(command[5:]) - 1)
		
				elif len(command) == 7 and int(command[5:]) > 0:
					play_card(current_player.hand, int(command[-2:]) - 1)
		
				elif command[:12] == "play discard":
					if len(command) == 14:
						play_card(current_player.discard, int(command[13:]) - 1)
					elif len(command) == 15:
						play_card(current_player.discard, int(command[13:]) - 1)
					else:
						card_to_play = ""
						for card in range(len(current_player.discard)):
							if current_player.discard[card].name == command[13:]:
								card_to_play = card
						if card_to_play != "":
							play_card(current_player.discard, card_to_play)
						else:
							flip()
							print(":: " + command)
							print("")
							print("Invalid Name")
							print("")
				else:
					card_to_play = ""
					for card in range(len(current_player.hand)):
						if current_player.hand[card].name == command[5:]:
							card_to_play = card
					if card_to_play != "":
						play_card(current_player.hand, card_to_play)
					else:
						flip()
						print(":: " + command)
						print("")
						print("Invalid Name")
						print("")
			except:
				flip()
				print(":: " + command)
				print("")
				print("Invalid Command Error 103")
				print("")
		
		elif command[:6] == "return":
			try:
				move_card(int(command[19]) - 1, play[int(command[12]) - 1][current_player.number - 1], current_player.hand)
				flip()
			except:
				flip()
				print(":: " + command)
				print("")
				print("Invalid Command Error 103")
				print("")
			
		elif command[:4] == "move":
			try:
				if len(command) == 18:
					flip()
					follow_up = input(":: Which base would would you like to move " + play[int(command[10]) - 1][current_player.number - 1][int(command[17]) - 1].name + " to? (c to cancel): ")
					if follow_up == "c":
						flip()
					else:
						move_card(int(command[17]) - 1, play[int(command[10]) - 1][current_player.number - 1], play[int(follow_up) - 1][current_player.number - 1])
						flip()
				elif len(command) == 19:
					flip()
					follow_up = input(":: Which base would would you like to move " + play[int(command[10]) - 1][current_player.number - 1][int(command[-2:]) - 1] + " to? (c to cancel): ")
					if follow_up == "c":
						flip()
					else:
						move_card(int(command[-2:]) - 1, play[int(command[10]) - 1][current_player.number - 1], play[int(follow_up) - 1][current_player.number - 1])
						flip()
				else:
					flip()
					print(":: " + command)
					print("")
					print("Invalid Command")
					print("")
					
			except:
				flip()
				print(":: " + command)
				print("")
				print("Invalid Command Error 104")
				print("")

		elif command[:6] == "recard":
			try:
				if command[:11] == "recard deck":
					if len(command) == 13:
						flip()
						print(":: " + command)
						print("")
						print(current_player.discard[int(command[12]) - 1].name + " was recarded to your deck")
						move_card(int(command[12]) - 1, current_player.discard, current_player.deck)
						print("")
					elif len(command) == 14:
						flip()
						print(":: " + command)
						print("")
						print(current_player.discard[int(command[-2:]) - 1].name + " was recarded to your deck")
						move_card(int(command[-2:]) - 1, current_player.discard, current_player.deck)
						print("")
					else:
						flip()
						print(":: " + command)
						print("")
						print("Invalid Command")
						print("")
						
				else: # command == 'recard #'
					if len(command) == 8:
						flip()
						print(":: " + command)
						print("")
						print(current_player.discard[int(command[7]) - 1].name + " was recarded to your hand")
						move_card(int(command[7]) - 1, current_player.discard, current_player.hand)
						print("")
					elif len(command) == 9:
						flip()
						print(":: " + command)
						print("")
						print(current_player.discard[int(command[-2:]) - 1].name + " was recarded to your hand")
						move_card(int(command[-2:]) - 1, current_player.discard, current_player.hand)
						print("")
					else:
						flip()
						print(":: " + command)
						print("")
						print("Invalid Command")
						print("")
			except:
				flip()
				print(":: " + command)
				print("")
				print("Invalid Command Error 105")
				print("")
		
		elif command[:8] == "retrieve":
			try:
				if len(command) == 10:
					flip()
					print(":: " + command)
					print("")
					print(current_player.deck[int(command[9]) - 1].name + " was retrieved to your hand")
					move_card(int(command[9]) - 1, current_player.deck, current_player.hand)
					print("")
				elif len(command) == 11:
					flip()
					print(":: " + command)
					print("")
					print(current_player.deck[int(command[-2:]) - 1].name + " was retrieved to your hand")
					move_card(int(command[-2:]) - 1, current_player.deck, current_player.hand)
					print("")
				else:
					flip()
					print(":: " + command)
					print("")
					print("Invalid Command")
					print("")
			except:
				flip()
				print(":: " + command)
				print("")
				print("Invalid Command Error 106")
				print("")
		
		elif command[:9] == "distrieve":
			try:
				flip()
				print(":: " + command)
				print("")
				follow_up = input("top or bottom?: ")
				if follow_up == "bottom":
					flip()
					print(":: " + follow_up)
					print("")
					print(current_player.hand[int(command[10]) - 1].name + " was distrieved to the bottom of your deck")
					move_card(int(command[10]) - 1, current_player.hand, current_player.deck)
					print("")
				elif follow_up == "top":
					flip()
					print(":: " + follow_up)
					print("")
					print(current_player.hand[int(command[10]) - 1].name + " was distrieved to the top of your deck")
					move_card(int(command[10]) - 1, current_player.hand, current_player.deck, deck = 'top')
					print("")
				elif follow_up == "":
					flip()
					print(":: " + follow_up)
					print("")
					print(current_player.hand[int(command[10]) - 1].name + " was distrieved to your deck")
					move_card(int(command[10]) - 1, current_player.hand, current_player.deck)
					print("")
				else:
					flip()
					print(":: " + follow_up)
					print("")
					print("Invalid Commmand")
			except:
				flip()
				print(":: " + command)
				print("")
				print("Invalid Command Error 106")
				print("")
				
		elif command[:7] == "victory" and len(command) == 9:
			try:
				flip()
				print(":: " + command)
				print("")
				current_player.victory = current_player.victory + int(command[-1])
				print(command[-1] + " victory point(s) were added")
				print("Your new total victory points is: " + str(current_player.victory))
				print("")
			except:
				flip()
				print(":: " + command)
				print("")
				print("Invalid Command Error 107")
				print("")
		
		elif command[:4] == "read":
			flip()
			print(":: " + command)
			card_to_print = ""
			for faction in play_factions:
				for card in faction:
					if command[5:] == card.name:
						card_to_print = card
		
			if card_to_print != "":
				print_card(card_to_print)
			else:
				print("")
				print("Invalid Name")
		
			print("")				
		
		elif command == 'q':
			break 
		
		else:
			flip()
			print(":: " + command)
			print("")	
			print("Invalid Command")
			print("")

def init_game():
	#Welcomes player and initializes the game with the inputted settings
	num_players = 0
	flip()
	print("WELCOME TO SMASH-UP!!!\n")
	
	name = input("What is your name?: ")
	while 1 == 1:
		num_players = input("How many players will be joining us?: ")
		try:
			if int(num_players) > 1 and int(num_players) < 5:
				for i in range(int(num_players) + 1):
					play.append([])
				for base in range(len(play)):
					for i in range(int(num_players)):
						play[base].append([])
				break
			else:
				flip()
				print("How many players will be joining us?: " + num_players)
				print("")
				print("Invalid Number")
				print("")
				continue
		except:
			flip()
			print("How many players will be joining us?: " + num_players)
			print("")
			print("Invalid Number")
			print("")
			continue

	temp_loop = True
	while temp_loop == True:
		flip()
		deck_one = input('\nWhat will be your first deck?(type "decks" for list): ')
		
		if deck_one == "decks":
			i = 1
			print("")
			for deck, deck_obj in Master.items():
				print(str(i) + ". " + deck)
				i = i + 1
			input("")
			continue
		
		deck_two = input('What will be your second deck?: ')

		if deck_one not in Master or deck_two not in Master:
			input("\nI'm sorry, one or both of the decks you selected are not available.")
		else:
			temp_loop = False
			
	name_mix = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']
		
	try:
		if Master[deck_one][0].graphic:
			safe = True
	except:
		i = 0
		for card_1 in Master[deck_one]:
			card_name = card_1
			card_name = card_name.replace(" ", "")
			card_name = card_name.replace(".", "")
			card_name = card_name.replace("?", "")
			excecutable = card_name + name_mix[i] + " = card(name = '" + card_1 + "', graphic = card_graphics(' _________________________ ', '|" + card_1.center(25) + "|', '|                         |', '|            O            |', '|           -|-           |', '|           / \           |', '|                         |', '|                         |', '|                         |', '|                         |', '|_________________________|'))"
			exec(excecutable)
			excecutable = "Master[deck_one][i] = " + card_name + name_mix[i]
			exec(excecutable)
			i = i + 1
	try:
		if Master[deck_two][0].graphic:
			safe = True
	except:
		i = 0
		for card_2 in Master[deck_two]:
			card_name = card_2
			card_name = card_name.replace(" ", "")
			card_name = card_name.replace(".", "")
			card_name = card_name.replace("?", "")
			excecutable = name_mix[i] + card_name + name_mix[i] + " = card(name = '" + card_2 + "', graphic = card_graphics(' _________________________ ', '|" + card_2.center(25) + "|', '|                         |', '|            O            |', '|           -|-           |', '|           / \           |', '|                         |', '|                         |', '|                         |', '|                         |', '|_________________________|'))"
			exec(excecutable)
			excecutable = "Master[deck_two][i] = " + name_mix[i] + card_name + name_mix[i]
			exec(excecutable)
			i = i + 1
	
	play_factions.append(Master[deck_one])
	play_factions.append(Master[deck_two])	
	player_one = player(deck_one, deck_two, name, number = 1)
	player_two = player(deck_one, deck_two, "Player Two", number = 2)
	if int(num_players) >= 3:
		player_three = player(deck_one, deck_two,"Player Three", number = 3)
	else:
		player_three = None
	if int(num_players) == 4:
		player_four = player(deck_one, deck_two, "Player Four", number = 4)
	else:
		player_four = None

	player_one.create_deck()
	player_one.shuffle_deck()
	player_one.draw_hand()
	
	player_two.create_deck()
	player_two.shuffle_deck()
	player_two.draw_hand()
	if player_three:
		player_three.create_deck()
		player_three.shuffle_deck()
		player_three.draw_hand()
	if player_four:
		player_four.create_deck()
		player_four.shuffle_deck()
		player_four.draw_hand()
	
	print("\nYour starting hand is:")
	for i in range(len(player_one.hand)):
					print(str(i + 1) + ". " + player_one.hand[i].name)

	input("\nPress 'c' at any time to see your list of actions!\nPress Enter to Begin!")
	
	#construct starting bases
	for base in range(len(play)):
		base_play.append(core_bases[random.randint(0, len(core_bases)-1)])
	
	return player_one, player_two, player_three, player_four

#Card
#Storage
#Module

class card():
	def __init__(self, name, graphic = None, power = None, ongoing_power = None, entrance_effect = [], ongoing_effect = [], minion_effect = [], protect_effect = [], discard_effect = [], end_of_turn_effect = [], special_effect = [], talent_effect = [], attach = None, tags = [], owner = None):
		'''
		Defines a card with neccessary abilities and card graphics
		'''
		self.name = name
		self.graphic = graphic
		self.power = power
		self.ongoing_power = ongoing_power
		self.entrance_effect = entrance_effect
		self.ongoing_effect = ongoing_effect
		self.minion_effect = minion_effect
		self.protect_effect = protect_effect
		self.discard_effect = discard_effect
		self.end_of_turn_effect = end_of_turn_effect
		self.special_effect = special_effect
		self.talent_effect = talent_effect
		self.attach = attach
		self.tags = tags
		self.owner = owner

class card_graphics():
	
	def __init__(self, line_1, line_2, line_3, line_4, line_5, line_6, line_7, line_8, line_9, line_10, line_11 = None):
		'''
		Graphics to diplay when reading card
		'''
		self.line_1 = line_1
		self.line_2 = line_2
		self.line_3 = line_3
		self.line_4 = line_4
		self.line_5 = line_5
		self.line_6 = line_6
		self.line_7 = line_7
		self.line_8 = line_8
		self.line_9 = line_9
		self.line_10 = line_10
		self.line_11 = line_11

class base():
	def __init__(self, name, graphic, break_point, ongoing_effect = [], minion_effect = [], destroy_effect = [], base_effect = []):
		'''
		Defines a card with neccessary abilities and card graphics
		'''
		self.name = name
		self.graphic = graphic
		self.break_point = break_point
		self.ongoing_effect = ongoing_effect
		self.minion_effect = minion_effect
		self.destroy_effect = destroy_effect
		self.base_effect = base_effect

def print_card(card):
	'''
	?Temporary? function that prints a card
	'''
	print(card.graphic.line_1)
	print(card.graphic.line_2)
	print(card.graphic.line_3)
	print(card.graphic.line_4)
	print(card.graphic.line_5)
	print(card.graphic.line_6)
	print(card.graphic.line_7)
	print(card.graphic.line_8)
	print(card.graphic.line_9)
	print(card.graphic.line_10)
	print(card.graphic.line_11)

#ALIENS
collector1 = card(name = "Collector", 
	graphic = card_graphics(
	" _________________________ ", 
	"|2       Collector       2|", 
	"|         (o)             |", 
	"|         -|-r======      |", 
	"|         / \             |", 
	"|       -------           |",
	"| You may return a minion |", 
	"|  of power 3 or less on  |", 
	"| this base to its owner's|", 
	"|         hand.           |", 
	"|_________________________|"),
	power = 2,
	entrance_effect = ["return_minion(3)"],
	tags = ['minion'])
collector2 = card(name = "Collector", 
	graphic = card_graphics(
	" _________________________ ", 
	"|2       Collector       2|", 
	"|         (o)             |", 
	"|         -|-r======      |", 
	"|         / \             |", 
	"|       -------           |",
	"| You may return a minion |", 
	"|  of power 3 or less on  |", 
	"| this base to its owner's|", 
	"|         hand.           |", 
	"|_________________________|"),
	power = 2,
	entrance_effect = ["return_minion(3)"],
	tags = ['minion'])
collector3 = card(name = "Collector", 
	graphic = card_graphics(
	" _________________________ ", 
	"|2       Collector       2|", 
	"|         (o)             |", 
	"|         -|-r======      |", 
	"|         / \             |", 
	"|       -------           |",
	"| You may return a minion |", 
	"|  of power 3 or less on  |", 
	"| this base to its owner's|", 
	"|         hand.           |", 
	"|_________________________|"),
	power = 2,
	entrance_effect = ["return_minion(3)"],
	tags = ['minion'])
collector4 = card(name = "Collector", 
	graphic = card_graphics(
	" _________________________ ", 
	"|2       Collector       2|", 
	"|         (o)             |", 
	"|         -|-r======      |", 
	"|         / \             |", 
	"|       -------           |",
	"| You may return a minion |", 
	"|  of power 3 or less on  |", 
	"| this base to its owner's|", 
	"|         hand.           |", 
	"|_________________________|"),
	power = 2,
	entrance_effect = ["return_minion(3)"],
	tags = ['minion'])

invader1 = card( name = "Invader",
	graphic = card_graphics(
	" _________________________ ", 
	"|3        Invader        3|", 
	"|              ___        |", 
	"|         (o) [___]       |", 
	"|         -|--|           |", 
	"|         / \ |           |",
	"|                         |", 
	"|                         |", 
	"|       Gain 1 VP         |", 
	"|                         |", 
	"|_________________________|"),
	entrance_effect = ["victory(1)"],
	power = 3,
	tags = ['minion'])
invader2 = card( name = "Invader",
	graphic = card_graphics(
	" _________________________ ", 
	"|3        Invader        3|", 
	"|              ___        |", 
	"|         (o) [___]       |", 
	"|         -|--|           |", 
	"|         / \ |           |",
	"|                         |", 
	"|                         |", 
	"|       Gain 1 VP         |", 
	"|                         |", 
	"|_________________________|"),
	power = 3,
	entrance_effect = ["victory(1)"],
	tags = ['minion'])

scout1 = card( name = "Scout",
	graphic = card_graphics(
	" _________________________ ", 
	"|3         Scout         3|", 
	"|         (o)             |", 
	"|         0|-r            |", 
	"|         / >             |", 
	"|Special: After this base |", 
	"|is scored, you may place |", 
	"|  this minion into your  |", 
	"|   hand instead of the   |", 
	"|      discard pile       |",
	"|_________________________|"),
	power = 3,
	special_effect = ["return_to_hand"],
	tags = ['minion'])
scout2 = card( name = "Scout",
	graphic = card_graphics(
	" _________________________ ", 
	"|3         Scout         3|", 
	"|         (o)             |", 
	"|         0|-r            |", 
	"|         / >             |", 
	"|Special: After this base |", 
	"|is scored, you may place |", 
	"|  this minion into your  |", 
	"|   hand instead of the   |", 
	"|      discard pile       |",
	"|_________________________|"),
	power = 3,
	special_effect = ["return_to_hand"],
	tags = ['minion'])
scout3 = card( name = "Scout",
	graphic = card_graphics(
	" _________________________ ", 
	"|3         Scout         3|", 
	"|         (o)             |", 
	"|         0|-r            |", 
	"|         / >             |", 
	"|Special: After this base |", 
	"|is scored, you may place |", 
	"|  this minion into your  |", 
	"|   hand instead of the   |", 
	"|      discard pile       |",
	"|_________________________|"),
	power = 3,
	special_effect = ["return_to_hand"],
	tags = ['minion'])

supreme_overlord = card( name = "Supreme Overlord",
	graphic = card_graphics(
	" _________________________ ", 
	"|5   Supreme Overlord    5|", 
	"|          _ w _          |", 
	"|         / (o) \         |", 
	"|        |_/-|-\_|        |", 
	"|       ()___|___()       |",
	"|       ||__/_\__||       |", 
	"|                         |", 
	"| You may return a minion |", 
	"|   to its owner's hand.  |", 
	"|_________________________|"),
	power = 5,
	entrance_effect = ["return_minion()"],
	tags = ['minion'])

beam_up1 = card( name = "Beam Up",
	graphic = card_graphics(
	" _________________________ ", 
	"|A        Beam Up        A|", 
	"|      \___________/      |", 
	"|         |     |         |", 
	"|         | \ / |         |", 
	"|         |  |  |         |",
	"|         | /o\ |         |", 
	"|                         |", 
	"| Return a minion to its  |", 
	"|      owner's hand.      |", 
	"|_________________________|"),
	entrance_effect = ["return_minion()"],
	tags = ['action'])
beam_up2 = card( name = "Beam Up",
	graphic = card_graphics(
	" _________________________ ", 
	"|A        Beam Up        A|", 
	"|      \___________/      |", 
	"|         |     |         |", 
	"|         | \ / |         |", 
	"|         |  |  |         |",
	"|         | /o\ |         |", 
	"|                         |", 
	"| Return a minion to its  |", 
	"|      owner's hand.      |", 
	"|_________________________|"),
	entrance_effect = ["return_minion()"],
	tags = ['action'])

disintegrator1 = card( name = "Disintegrator",
	graphic = card_graphics(
	" _________________________ ", 
	"|A     Disintegrator     A|", 
	"| \___________/           |", 
	"|   |                     |", 
	"|   |               \o/   |", 
	"|   [}--------|      |    |",
	"|            / \    / \   |", 
	"|Place a minion of power 3|", 
	"|or less on the bottom of |", 
	"|     its owner's deck.   |", 
	"|_________________________|"),
	entrance_effect = ["distrieve()"],
	tags = ['action'])
disintegrator2 = card( name = "Disintegrator",
	graphic = card_graphics(
	" _________________________ ", 
	"|A     Disintegrator     A|", 
	"| \___________/           |", 
	"|   |                     |", 
	"|   |               \o/   |", 
	"|   [}--------|      |    |",
	"|            / \    / \   |", 
	"|Place a minion of power 3|", 
	"|or less on the bottom of |", 
	"|     its owner's deck.   |", 
	"|_________________________|"),
	entrance_effect = ["distrieve()"],
	tags = ['action'])

abduction = card( name = "Abduction",
	graphic = card_graphics(
	" _________________________ ", 
	"|A       Abduction       A|", 
	"|         O=====<         |", 
	"|          \(o)/          |", 
	"|            |            |", 
	"|           / \           |",
	"|         -------         |",
	"| Return a minion to its  |", 
	"|  owner's hand. Play an  |", 
	"|      extra minion       |",  
	"|_________________________|"),
	entrance_effect = ["return(3)"],
	tags = ['action'])

crop_circles = card( name = "Crop Circles",
	graphic = card_graphics(
	" _________________________ ", 
	"|A     Crop Circles      A|", 
	"|       O  ____  O        |", 
	"|        \/    \/         |", 
	"|    O---|      |---O     |", 
	"|        /\____/\         |",
	"|       O        O        |", 
	"|  Choose a base. Return  |", 
	"|each minion on that base |", 
	"|  to its owner's hand.   |", 
	"|_________________________|"),
	entrance_effect = ["return('base')"],
	tags = ['action'])

probe = card( name = "Probe",
	graphic = card_graphics(
	" _________________________ ", 
	"|A         Probe         A|",
	"|                         |", 
	"|     (o)         (o)     |", 
	"|     -|- _>-->O_ -|-     |", 
	"|     / \ |-----| / \     |", 
	"|Look at another player's |", 
	"|hand and choose a minion |",
	"|   in it. That player    |", 
	"|  discards that minion.  |", 
	"|_________________________|"),
	entrance_effect = ["another_hand('discard minion')"],
	tags = ['action'])

jammed_signal = card( name = "Jammed Signal",
	graphic = card_graphics(
	" _________________________ ", 
	"|A     Jammed Signal     A|", 
	"|         ___\/__         |", 
	"|        | ~~~~~ |        |", 
	"|        | ~~~~~ |        |", 
	"|        |_~~~~~_|        |",
	"|         V     V         |", 
	"|Play on a base. Ongoing: |", 
	"| All players ignore this |", 
	"|     base's ability      |", 
	"|_________________________|"),
	entrance_effect = ["on_base('ignore')"],
	tags = ['action'])

terraforming = card( name = "Terraforming",
	graphic = card_graphics(
	" _________________________ ", 
	"|A     Terraforming      A|", 
	"|    ____           / n   |", 
	"|  _/____\_        |  nn  |", 
	"| |________|       |   nn |", 
	"|    \[}            \ nn  |",
	"| Search base deck for a  |", 
	"|base. Swap it with a base|", 
	"|in play. You may play an |", 
	"|  extra minion on it.    |", 
	"|_________________________|"),
	entrance_effect = ["replace_base()", "extra_minion()"],
	tags = ['action'])

invasion = card( name = "Invasion",
	graphic = card_graphics(
	" _________________________ ", 
	"|A       Invasion        A|", 
	"|    ____         ____    |", 
	"|  _/____\_     _/____\_  |", 
	"| |________|   |________| |", 
	"|          ____           |",
	"|        _/____\_         |", 
	"|       |________|        |", 
	"|Move a minion to another |", 
	"|          base.          |", 
	"|_________________________|"),
	entrance_effect = ["move('minion')"],
	tags = ['action'])

#DINOSAURS
war_raptor1 = card(name = "War Raptor", 
	graphic = card_graphics(
	" _________________________ ",
	"|2      War Raptor       2|",
	"|     _oVo--.__           |",
	"|    '^^`)._  `\\'_'_'     |",
	"|     \"\"' //(( ,_.-'      |",
	"|           / /           |",
	"|         `~`~            |",
	"| Ongoing: Gains +1 power |",
	"| for each War Raptor on  |",
	"|this base, including this|",
	"|_________________________|"),
	power = 2,
	minion_effect = ["gain_power(1, 'War Raptor')"],
	tags = ['minion', 'War Raptor', 'Dinosaurs'])
war_raptor2 = card(name = "War Raptor", 
	graphic = card_graphics(
	" _________________________ ",
	"|2      War Raptor       2|",
	"|     _oVo--.__           |",
	"|    '^^`)._  `\\'_'_'     |",
	"|     \"\"' //(( ,_.-'      |",
	"|           / /           |",
	"|         `~`~            |",
	"| Ongoing: Gains +1 power |",
	"| for each War Raptor on  |",
	"|this base, including this|",
	"|_________________________|"),
	power = 2,
	minion_effect = ["gain_power(1, 'War Raptor')"],
	tags = ['minion', 'War Raptor', 'Dinosaurs'])
war_raptor3 = card(name = "War Raptor", 
	graphic = card_graphics(
	" _________________________ ",
	"|2      War Raptor       2|",
	"|     _oVo--.__           |",
	"|    '^^`)._  `\\'_'_'     |",
	"|     \"\"' //(( ,_.-'      |",
	"|           / /           |",
	"|         `~`~            |",
	"| Ongoing: Gains +1 power |",
	"| for each War Raptor on  |",
	"|this base, including this|",
	"|_________________________|"),
	power = 2,
	minion_effect = ["gain_power(1, 'War Raptor')"],
	tags = ['minion', 'War Raptor', 'Dinosaurs'])
war_raptor4 = card(name = "War Raptor", 
	graphic = card_graphics(
	" _________________________ ",
	"|2      War Raptor       2|",
	"|     _oVo--.__           |",
	"|    '^^`)._  `\\'_'_'     |",
	"|     \"\"' //(( ,_.-'      |",
	"|           / /           |",
	"|         `~`~            |",
	"| Ongoing: Gains +1 power |",
	"| for each War Raptor on  |",
	"|this base, including this|",
	"|_________________________|"),
	power = 2,
	minion_effect = ["gain_power(1, 'War Raptor')"],
	tags = ['minion', 'War Raptor', 'Dinosaurs'])

armored_stego1 = card(name = "Armored Stego", 
	graphic = card_graphics(
	" _________________________ ",
	"|3     Armored Stego     3|",
	"|                  __     |",
	"|        _/\/\/\/\/ _)    |",
	"|      _|          /      |",
	"|    _|  (  | (   /       |",
	"|   /__.-'|_|--|_|        |",
	"|  Ongoing: Has +2 power  |",
	"|      during other       |",
	"|     players' turns.     |",
	"|_________________________|"),
	power = 3,
	ongoing_effect = ["gain_power(2, condition = 'current_player != self.owner'"],
	tags = ['minion', 'Dinosaurs'])
armored_stego2 = card(name = "Armored Stego", 
	graphic = card_graphics(
	" _________________________ ",
	"|3     Armored Stego     3|",
	"|                  __     |",
	"|        _/\/\/\/\/ _)    |",
	"|      _|          /      |",
	"|    _|  (  | (   /       |",
	"|   /__.-'|_|--|_|        |",
	"|  Ongoing: Has +2 power  |",
	"|      during other       |",
	"|     players' turns.     |",
	"|_________________________|"),
	power = 3,
	ongoing_effect = ["set_power(5, condition = 'current_player != self.owner)'"],
	tags = ['minion', 'Dinosaurs'])
armored_stego3 = card(name = "Armored Stego", 
	graphic = card_graphics(
	" _________________________ ",
	"|3     Armored Stego     3|",
	"|                  __     |",
	"|        _/\/\/\/\/ _)    |",
	"|      _|          /      |",
	"|    _|  (  | (   /       |",
	"|   /__.-'|_|--|_|        |",
	"|  Ongoing: Has +2 power  |",
	"|      during other       |",
	"|     players' turns.     |",
	"|_________________________|"),
	power = 3,
	ongoing_effect = ["gain_power(2, condition = 'current_player != self.owner'"],
	tags = ['minion', 'Dinosaurs'])

lazertops1 = card(name = "Lazertops", 
	graphic = card_graphics(
	" _________________________ ",
	"|4      Lazertops        4|",
	"|     ====<[]             |",
	"|     /| __||___          |",
	"|  \\\| |/       \         |",
	"|  (___   ) |  )  \_      |",
	"|      |_|--|_|'-.__\     |",
	"| ----------------------  |",
	"|Destroy a minion of power|",
	"| 2 or less on this base. |",
	"|_________________________|"),
	power = 4,
	entrance_effect = ["destroy_minion(base = 'SAME', power = 2)"],
	tags = ['minion', 'Dinosaurs'])
lazertops2 = card(name = "Lazertops", 
	graphic = card_graphics(
	" _________________________ ",
	"|4      Lazertops        4|",
	"|     ====<[]             |",
	"|     /| __||___          |",
	"|  \\\| |/       \         |",
	"|  (___   ) |  )  \_      |",
	"|      |_|--|_|'-.__\     |",
	"| ----------------------  |",
	"|Destroy a minion of power|",
	"| 2 or less on this base. |",
	"|_________________________|"),
	power = 4,
	entrance_effect = ["destroy_minion(base = 'SAME', power = 2)"],
	tags = ['minion', 'Dinosaurs'])

king_rex = card(name = "King Rex", 
	graphic = card_graphics(
	" _________________________ ",
	"|7       King Rex        7|",
	"|          ____           |",
	"|       .-~    '.         |",
	"|      / /  ~@\   )       |",
	"|     | /  \~\.  `\       |",
	"|    /  |  |< ~\(..)      |",
	"|       \  \<   .,,       |",
	"|       /~\ \< /          |",
	"|       /-~\ \_|          |",
	"|_________________________|"),
	power = 7,
	tags = ['minion', 'Dinosaurs'])
	
augmentation1 = card(name = "Augmentation", 
	graphic = card_graphics(
	" _________________________ ",
	"|A      Augmention       A|",
	"|         ________/\      |",
	"|      _ / |_O_|   0|     |",
	"|     /_|       ____|     |",
	"|     /_|      _____|     |",
	"|     /_|     |           |",
	"|   One minion gains +4   |",
	"| power until the end of  |",
	"|       your turn.        |",
	"|_________________________|"),
	entrance_effect = ["give_power(4)"],
	end_of_turn_effect = ["remove_power(4, chosen_minion)"],
	tags = ['action'])
augmentation2 = card(name = "Augmentation", 
	graphic = card_graphics(
	" _________________________ ",
	"|A      Augmention       A|",
	"|         ________/\      |",
	"|      _ / |_O_|   0|     |",
	"|     /_|       ____|     |",
	"|     /_|      _____|     |",
	"|     /_|     |           |",
	"|   One minion gains +4   |",
	"| power until the end of  |",
	"|       your turn.        |",
	"|_________________________|"),
	entrance_effect = ["give_power(4)"],
	end_of_turn_effect = ["remove_power(4, chosen_minion)"],
	tags = ['action'])

howl1 = card(name = "Howl", 
	graphic = card_graphics(
	" _________________________ ",
	"|A         Howl          A|",
	"|      ____        \      |",
	"|     /    \     \  \     |",
	"|    |   ===O  )  |  |    |",
	"|     \____/     /  /     |",
	"|       ||         /      |",
	"|  Each of your minions   |",
	"|gains +1 power until the |",
	"|    end of your turn     |",
	"|_________________________|"),
	entrance_effect = ["give_power(1, area_of_effect = 'ALL OWNED')"],
	end_of_turn_effect = ["remove_power(1, area_of_effect = 'ALL OWNED')"],
	tags = ['action'])
howl2 = card(name = "Howl", 
	graphic = card_graphics(
	" _________________________ ",
	"|A         Howl          A|",
	"|      ____        \      |",
	"|     /    \     \  \     |",
	"|    |   ===O  )  |  |    |",
	"|     \____/     /  /     |",
	"|       ||         /      |",
	"|  Each of your minions   |",
	"|gains +1 power until the |",
	"|    end of your turn     |",
	"|_________________________|"),
	entrance_effect = ["give_power(1, area_of_effect = 'ALL OWNED')"],
	end_of_turn_effect = ["remove_power(1, area_of_effect = 'ALL OWNED')"],
	tags = ['action'])

natural_selection = card(name = "Natural Selection", 
	graphic = card_graphics(
	" _________________________ ",
	"|A   Natural Selection   A|",
	"|        O                |",
	"|      --|--    o         |",
	"|        |     /|\        |",
	"|       / \    / \        |",
	"|   Choose one of your    |",
	"|   minions on a base.    |",
	"| Destroy a minion there  |",
	"|with less power than it. |",
	"|_________________________|"),
	entrance_effect = ["destroy_minion(base = 'WITH OWN MINION', power = chosen_minion.play_power + 1)"],
	tags = ['action'])

upgrade = card(name = "Upgrade", 
	graphic = card_graphics(
	" _________________________ ",
	"|A        Upgrade   __   A|",
	"|                  / _)   |",
	"|        _________/ /_    |",
	"|      _(________()/_()   |",
	"|    _/  (  | (   /       |",
	"|   /__.-'|_|--|_|        |",
	"|    Play on a minion     |",
	"|Ongoing: This minion has |",
	"|        +2 power         |",
	"|_________________________|"),
	entrance_effect = ["give_power(2)"],
	discard_effect = ["remove_power(2, chosen_minion)"],
	tags = ['action', 'attachment'])

tooth_and_claw_and_guns = card(name = "Tooth And Claw... And Guns", 
	graphic = card_graphics(
	" _________________________ ",
	"|A   Tooth And Claw...   A|",
	"|        And Guns         |",
	"|    ----------------     |",
	"|    Play on a minion     |",
	"| Ongoing: if an ability  |",
	"|would affect this minion,|",
	"|destroy this card and the|",
	"| ability does not affect |",
	"|       this minion       |",
	"|_________________________|"),
	protect_effect = ["negate_destroy(self.attach), discard(self)"],
	tags = ['action', 'attachment'])

survival_of_the_fittest = card(name = "Survival Of The Fittest", 
	graphic = card_graphics(
	" _________________________ ",
	"|A    Survival Of The    A|",
	"|         Fittest         |",
	"|         |_____|         |",
	"|        |/     \|        |",
	"|         \_____/         |",
	"|           >->o          |",
	"|Destroy the lowest-power |",
	"|minion on each base with |",
	"| a higher-power minion.  |",
	"|_________________________|"),
	entrance_effect = ["destroy_minion(area_of_effect = 'All BASES', automatic = True, power = lowest_power_minion())"],
	tags = ['action'])

wildlife_preserve = card(name = "Wildlife Preserve", 
	graphic = card_graphics(
	" _________________________ ",
	"|A   Wildlife Preserve   A|",
	"|             /\/\/\      |",
	"|          O /\/\/\/\     |",
	"|      ___/     ||        |",
	"|     '/\/\     ||        |",
	"|     Play on a base      |",
	"|  Ongoing: Your minions  |",
	"|here are not affected by |",
	"| other players' actions  |",
	"|_________________________|"),
	protect_effect = ["negate_actions(self.attach)"],
	tags = ['action', 'base attachment'])

rampage = card(name = "Rampage", 
	graphic = card_graphics(
	" _________________________ ",
	"|A        Rampage  __    A|",
	"|    __      O    |  |    |",
	"|   | {__   /|\    } |    |",
	"|   |    |  / \   |  |    |",
	"|Reduce the breakpoint of |",
	"| a base by the power of  |",
	"| one of your minions on  |",
	"| that base until the end |",
	"|      of the turn.       |",
	"|_________________________|"),
	entrance_effect = ["lower_breakpoint(chosen_minion)"],
	end_of_turn_effect = ["heighten_breakpoint(chosen_minion)"],
	tags = ['action', 'attachment'])

#NINJAS

ninja_alcolyte1 = card(name = "Ninja Alcolyte", 
	graphic = card_graphics(
	" _________________________ ",
	"|2     Ninja Alcolyte    2|",
	"|            o            |",
	"|          X-|-X          |",
	"|           / >           |",
	"| Talent: If you have not |",
	"|played a minion, you may |",
	"|  return this minion to  |",
	"|  your hand and play an  |",
	"|extra minion on this base|",
	"|_________________________|"),
	power = 2,
	talent_effect = ["return(self), get_extra('minion')"],
	tags = ['minion', 'Ninjas'])
ninja_alcolyte2 = card(name = "Ninja Alcolyte", 
	graphic = card_graphics(
	" _________________________ ",
	"|2     Ninja Alcolyte    2|",
	"|            o            |",
	"|          X-|-X          |",
	"|           / >           |",
	"| Talent: If you have not |",
	"|played a minion, you may |",
	"|  return this minion to  |",
	"|  your hand and play an  |",
	"|extra minion on this base|",
	"|_________________________|"),
	power = 2,
	talent_effect = ["return(self), get_extra('minion')"],
	tags = ['minion', 'Ninjas'])
ninja_alcolyte3 = card(name = "Ninja Alcolyte", 
	graphic = card_graphics(
	" _________________________ ",
	"|2     Ninja Alcolyte    2|",
	"|            o            |",
	"|          X-|-X          |",
	"|           / >           |",
	"| Talent: If you have not |",
	"|played a minion, you may |",
	"|  return this minion to  |",
	"|  your hand and play an  |",
	"|extra minion on this base|",
	"|_________________________|"),
	talent_effect = ["return(self), get_extra('minion')"],
	tags = ['minion', 'Ninjas'])
ninja_alcolyte4 = card(name = "Ninja Alcolyte", 
	graphic = card_graphics(
	" _________________________ ",
	"|2     Ninja Alcolyte    2|",
	"|            o            |",
	"|          X-|-X          |",
	"|           / >           |",
	"| Talent: If you have not |",
	"|played a minion, you may |",
	"|  return this minion to  |",
	"|  your hand and play an  |",
	"|extra minion on this base|",
	"|_________________________|"),
	power = 2,
	talent_effect = ["return(self), get_extra('minion')"],
	tags = ['minion', 'Ninjas'])

shinobi1 = card(name = "Shinobi", 
	graphic = card_graphics(
	" _________________________ ",
	"|3        Shinobi        3|",
	"|          | o            |",
	"|          I-|-x          |",
	"|          |< \           |",
	"| Special: Before a base  |",
	"|scores, you can play this|",
	"|  minion there. You can  |",
	"| only use one Shinobi's  |",
	"|    ability per base.    |",
	"|_________________________|"),
	power = 3,
	special_effect = ["play(self, scoring_base)"],
	tags = ['minion', 'Ninjas'])
shinobi2 = card(name = "Shinobi", 
	graphic = card_graphics(
	" _________________________ ",
	"|3        Shinobi        3|",
	"|          | o            |",
	"|          I-|-x          |",
	"|          |< \           |",
	"| Special: Before a base  |",
	"|scores, you can play this|",
	"|  minion there. You can  |",
	"| only use one Shinobi's  |",
	"|    ability per base.    |",
	"|_________________________|"),
	power = 3,
	special_effect = ["play(self, scoring_base)"],
	tags = ['minion', 'Ninjas'])
shinobi3 = card(name = "Shinobi", 
	graphic = card_graphics(
	" _________________________ ",
	"|3        Shinobi        3|",
	"|          | o            |",
	"|          I-|-x          |",
	"|          |< \           |",
	"| Special: Before a base  |",
	"|scores, you can play this|",
	"|  minion there. You can  |",
	"| only use one Shinobi's  |",
	"|    ability per base.    |",
	"|_________________________|"),
	power = 3,
	special_effect = ["play(self, scoring_base)"],
	tags = ['minion', 'Ninjas'])

tiger_assassin1 = card(name = "Tiger Assassin", 
	graphic = card_graphics(
	" _________________________ ",
	"|4    Tiger Assassin     4|",
	"|                         |",
	"|            o            |",
	"|        ==|-|-|==        |",
	"|           < >           |",
	"|                         |",
	"|You may destroy a minion |",
	"|  of power 3 or less on  |",
	"|       this base.        |",
	"|_________________________|"),
	power = 3,
	entrance_effect = ["destroy_minion(base = 'SAME', optional = 'TRUE', power = 3)"],
	tags = ['minion', 'Ninjas'])
tiger_assassin2 = card(name = "Tiger Assassin", 
	graphic = card_graphics(
	" _________________________ ",
	"|4    Tiger Assassin     4|",
	"|                         |",
	"|            o            |",
	"|        ==|-|-|==        |",
	"|           < >           |",
	"|                         |",
	"|You may destroy a minion |",
	"|  of power 3 or less on  |",
	"|       this base.        |",
	"|_________________________|"),
	power = 3,
	entrance_effect = ["destroy_minion(base = 'SAME', optional = 'TRUE', power = 3)"],
	tags = ['minion', 'Ninjas'])

ninja_master = card(name = "Ninja Master", 
	graphic = card_graphics(
	" _________________________ ",
	"|5     Ninja Master      5|",
	"|       |       |         |",
	"|       |   O   |         |",
	"|       I---|---I         |",
	"|           |             |",
	"|          / \            |",
	"|         |   |           |",
	"|You may destroy a minion |",
	"|      on this base.      |",
	"|_________________________|"),
	power = 5,
	entrance_effect = ["destroy_minion(base = 'SAME', optional = 'TRUE', power = 3)"],
	tags = ['minion', 'Ninjas'])

seeing_stars1 = card(name = "Seeing Stars", 
	graphic = card_graphics(
	" _________________________ ",
	"|A     Seeing Stars      A|",
	"|     X                   |",
	"|      \O                 |",
	"|       |\                |",
	"|      / >   \   \        |",
	"|              _/\_       |",
	"|           \ \    /      |",
	"|  Destroy a  /_  _\minion|",
	"|of power 2 or  \/  less. |",
	"|_________________________|"),
	entrance_effect = ["destroy_minion(power = 2)"],
	tags = ['action'])
seeing_stars2 = card(name = "Seeing Stars", 
	graphic = card_graphics(
	" _________________________ ",
	"|A     Seeing Stars      A|",
	"|     X                   |",
	"|      \O                 |",
	"|       |\                |",
	"|      / >   \   \        |",
	"|              _/\_       |",
	"|           \ \    /      |",
	"|  Destroy a  /_  _\minion|",
	"|of power 2 or  \/  less. |",
	"|_________________________|"),
	entrance_effect = ["destroy_minion(power = 2)"],
	tags = ['action'])

infiltrate1 = card(name = "Infiltrate", 
	graphic = card_graphics(
	" _________________________ ",
	"|A       Infiltrate !    A|",
	"|     _____         O]    |",
	"|    |     |       \u250c|\u2518    |",
	"|  __|_____|__     / \    |",
	"| Play on a base. Destroy |",
	"|an action here. Ongoing: |",
	"|   you may ignore this   |",
	"|base's  ability until the|",
	"|start of your next turn. |",
	"|_________________________|"),
	entrance_effect = ["destroy_action(attach = 'BASE')"],
	ongoing_effect = ["ignore_base(area_of_effect = self.owner), on_owners_turn(destroy_action(self))"],
	tags = ['action'])
infiltrate2 = card(name = "Infiltrate", 
	graphic = card_graphics(
	" _________________________ ",
	"|A       Infiltrate !    A|",
	"|     _____         O]    |",
	"|    |     |       \u250c|\u2518    |",
	"|  __|_____|__     / \    |",
	"| Play on a base. Destroy |",
	"|an action here. Ongoing: |",
	"|   you may ignore this   |",
	"|base's  ability until the|",
	"|start of your next turn. |",
	"|_________________________|"),
	entrance_effect = ["destroy_action(attach = 'BASE')"],
	ongoing_effect = ["ignore_base(area_of_effect = self.owner), on_owners_turn(destroy_action(self))"],
	tags = ['action'])

poison = card(name = "Poison", 
	graphic = card_graphics(
	" _________________________ ",
	"|A         Poison        A|",
	"|          _| |_          |",
	"|         /     \         |",
	"|        | X X X |        |",
	"|         \_____/         |",
	"|Play on a minion. Destroy|",
	"|any number of actions on |",
	"|it. Ongoing: This minion |",
	"| has -4 power. (Min. 0)  |",
	"|_________________________|"),
	entrance_effect = ["destroy_action(attatch = 'action', times = 'ALL')"],
	ongoing_effect = ["attach_lower_power(self.attach, 4)"],
	tags = ['action', 'attachment'])

disguise = card(name = "Disguise", 
	graphic = card_graphics(
	" _________________________ ",
	"|A        Disguise       A|",
	"|    \  O        (o)      |",
	"|     \-|-X  ->  -|-      |",
	"|      < >       / \      |",
	"|Choose one or two of your|",
	"|minions on one base. Play|",
	"|an equal number of extra |",
	"|minions there, and return|",
	"| chosen minions to hand. |",
	"|_________________________|"),
	entrance_effect = ["return(choose = 'OWN_MINIONS', area_of_effect = 'BASE')"],
	tags = ['action'])

assassinaion = card(name = "Assassination", 
	graphic = card_graphics(
	" _________________________ ",
	"|A     Assassination     A|",
	"|                         |",
	"|        O     \o/        |",
	"|       -|-|==  |         |",
	"|       / >    / \        |",
	"|    Play on a minion.    |",
	"|  Ongoing: Destroy this  |",
	"|    minion at the end    |",
	"|       of the turn.      |",
	"|_________________________|"),
	end_of_turn_effect = ["destroy_minion(self.attach)"],
	tags = ['action', 'attachment'])
	
hidden_ninja = card(name = "Hidden Ninja", 
	graphic = card_graphics(
	" _________________________ ",
	"|A     Hidden Ninja      A|",
	"|                         |",
	"|     o      o      o     |",
	"|    /|\    /|\    /|\    |",
	"|    / \    / \    / \    |",
	"|                         |",
	"| Special: Before a base  |",
	"|     scores, play a      |",
	"|      minion there.      |",
	"|_________________________|"),
	special_effect = ["extra(power = 2)"],
	tags = ['action'])
	
way_of_deception = card(name = "Way Of Deception", 
	graphic = card_graphics(
	" _________________________ ",
	"|A    Way Of Deception   A|",
	"|            o            |",
	"|           /|\           |",
	"|          X< >X          |",
	"|            I            |",
	"|            I            |",
	"|            I            |",
	"|    Move one of your     |",
	"|minions to another base. |",
	"|_________________________|"),
	entrance_effect = ["move_minion(area_of_effect = 'OWN_SINGLE')"],
	tags = ['action'])
	
smoke_bomb = card(name = "Smoke Bomb", 
	graphic = card_graphics(
	" _________________________ ",
	"|A      Smoke Bomb       A|",
	"|~~~~~~~~~~~~~~~~~~~~~~~~~|",
	"|~~~~~~~~~~~~~~~~~~~~~~~~~|",
	"|~Play on one of your own~|",
	"|~minions. Ongoing: This~~|",
	"|minion is not affected by|",
	"|~other players' actions.~|",
	"|Destroy this card at the~|",
	"|~~~start of your turn.~~~|",
	"|_________________________|"),
	protect_effect = ["negate_actions(self.attach)"],
	ongoing_effect = ["on_owners_turn(destroy_action(self))"],
	tags = ['action', 'attachment'])

#PIRATES

first_mate1 = card(name = "First Mate", 
	graphic = card_graphics(
	" _________________________ ",
	"|2      First Mate       2|",
	"|           n_            |",
	"|          (\")            |",
	"|          -|-            |",
	"|          / \            |",
	"|Special: After this base |",
	"| is scored, you may move |",
	"| this minion to another  |",
	"|base instead of discard. |",
	"|_________________________|"),
	power = 2,
	special_effect = ["move_minion(self)"],
	tags = ['minion', 'Pirates'])
first_mate2 = card(name = "First Mate", 
	graphic = card_graphics(
	" _________________________ ",
	"|2      First Mate       2|",
	"|           n_            |",
	"|          (\")            |",
	"|          -|-            |",
	"|          / \            |",
	"|Special: After this base |",
	"| is scored, you may move |",
	"| this minion to another  |",
	"|base instead of discard. |",
	"|_________________________|"),
	power = 2,
	special_effect = ["move_minion(self)"],
	tags = ['minion', 'Pirates'])
first_mate3 = card(name = "First Mate", 
	graphic = card_graphics(
	" _________________________ ",
	"|2      First Mate       2|",
	"|           n_            |",
	"|          (\")            |",
	"|          -|-            |",
	"|          / \            |",
	"|Special: After this base |",
	"| is scored, you may move |",
	"| this minion to another  |",
	"|base instead of discard. |",
	"|_________________________|"),
	power = 2,
	special_effect = ["move_minion(self)"],
	tags = ['minion', 'Pirates'])
first_mate4 = card(name = "First Mate", 
	graphic = card_graphics(
	" _________________________ ",
	"|2      First Mate       2|",
	"|           n_            |",
	"|          (\")            |",
	"|          -|-            |",
	"|          / \            |",
	"|Special: After this base |",
	"| is scored, you may move |",
	"| this minion to another  |",
	"|base instead of discard. |",
	"|_________________________|"),
	power = 2,
	special_effect = ["move_minion(self)"],
	tags = ['minion', 'Pirates'])

saucy_wench1 = card(name = "Saucy Wench", 
	graphic = card_graphics(
	" _________________________ ",
	"|3      Saucy Wench      3|",
	"|            _            |",
	'|          /(")\          |',
	"|           <|-r          |",
	"|           / \           |",
	"|                         |",
	"|You may destroy a minion |",
	"|   of power 2 or less    |",
	"|      on this base.      |",
	"|_________________________|"),
	power = 3,
	entrance_effect = ["destroy_minion(area_of_effect = 'SAME BASE', power = 2)"],
	tags = ['minion', 'Pirates'])
saucy_wench2 = card(name = "Saucy Wench", 
	graphic = card_graphics(
	" _________________________ ",
	"|3      Saucy Wench      3|",
	"|            _            |",
	'|          /(")\          |',
	"|           <|-r          |",
	"|           / \           |",
	"|                         |",
	"|You may destroy a minion |",
	"|   of power 2 or less    |",
	"|      on this base.      |",
	"|_________________________|"),
	power = 3,
	entrance_effect = ["destroy_minion(area_of_effect = 'SAME BASE', power = 2)"],
	tags = ['minion', 'Pirates'])
saucy_wench3 = card(name = "Saucy Wench", 
	graphic = card_graphics(
	" _________________________ ",
	"|3      Saucy Wench      3|",
	"|            _            |",
	'|          /(")\          |',
	"|           <|-r          |",
	"|           / \           |",
	"|                         |",
	"|You may destroy a minion |",
	"|   of power 2 or less    |",
	"|      on this base.      |",
	"|_________________________|"),
	power = 3,
	entrance_effect = ["destroy_minion(area_of_effect = 'SAME BASE', power = 2)"],
	tags = ['minion', 'Pirates'])

buccaneer1 = card(name = "Buccaneer", 
	graphic = card_graphics(
	" _________________________ ",
	"|4       Buccaneer       4|",
	"|          /v\            |",
	"|          (\")            |",
	"|          -|-|===>       |",
	"|          / \            |",
	"|                         |",
	"| Special: If this minion |",
	"|would be destroyed, move |",
	"|   it to another base.   |",
	"|_________________________|"),
	power = 4,
	entrance_effect = ["destroy_minion(power = 2)"],
	tags = ['action', 'Pirates'])
buccaneer2 = card(name = "Buccaneer", 
	graphic = card_graphics(
	" _________________________ ",
	"|4       Buccaneer       4|",
	"|          /v\            |",
	"|          (\")            |",
	"|          -|-|===>       |",
	"|          / \            |",
	"|                         |",
	"| Special: If this minion |",
	"|would be destroyed, move |",
	"|   it to another base.   |",
	"|_________________________|"),
	power = 4,
	entrance_effect = ["destroy_minion(power = 2)"],
	tags = ['action', 'Pirates'])

pirate_king = card(name = "Pirate King", 
	graphic = card_graphics(
	" _________________________ ",
	"|5  Pirate  _ _   King   5|",
	"|          /_V_\          |",
	"|          (' ') ?        |",
	"|    <===|--WWW--\u2518        |",
	"|            |            |",
	"|           / \           |",
	"|          |   |          |",
	"| Before a base scores you|",
	"|  may move this there.   |",
	"|_________________________|"),
	power = 5,
	special_effect = ["move_minion(self, breaking_base)"],
	tags = ['minion', 'Pirates'])

dinghy1 = card(name = "Dinghy", 
	graphic = card_graphics(
	" _________________________ ",
	"|A         Dinghy        A|",
	"|                         |",
	"|      ____/_\______      |",
	"|     |       \     |     |",
	"|~~~~~~\_______\ __/~~~~~~|",  
	"|              \_\        |",
	"|                         |",
	"| Move up to two of your  |",
	"| minions to other bases. |",
	"|_________________________|"),
	entrance_effect = ["move_minion(area_of_effect = 'OWN 2')"],
	tags = ['action'])
dinghy2 = card(name = "Dinghy", 
	graphic = card_graphics(
	" _________________________ ",
	"|A         Dinghy        A|",
	"|                         |",
	"|      ____/_\______      |",
	"|     |       \     |     |",
	"|~~~~~~\_______\ __/~~~~~~|",  
	"|              \_\        |",
	"|                         |",
	"| Move up to two of your  |",
	"| minions to other bases. |",
	"|_________________________|"),
	entrance_effect = ["move_minion(area_of_effect = 'OWN 2')"],
	tags = ['action'])

broadside1 = card(name = "Broadside", 
	graphic = card_graphics(
	" _________________________ ",
	"|A       Broadside       A|",
	"|   ________| |________   |",
	"|  |  _   _    _   _   |  |",
	"|  | (O) (O)  (O) (O)  |  |",
	"|   \_________________/   |",
	"|   Destroy all of one    |",
	"|player's minions of power|",
	"|2 or less at a base where|",
	"|   you have a minion.    |",
	"|_________________________|"),
	entrance_effect = ["destroy_minion(area_of_effect = 'SINGLE PLAYER ON OCCUPIED BASE', power = 2)"],
	tags = ['action'])
broadside2 = card(name = "Broadside", 
	graphic = card_graphics(
	" _________________________ ",
	"|A       Broadside       A|",
	"|   ________| |________   |",
	"|  |  _   _    _   _   |  |",
	"|  | (O) (O)  (O) (O)  |  |",
	"|   \_________________/   |",
	"|   Destroy all of one    |",
	"|player's minions of power|",
	"|2 or less at a base where|",
	"|   you have a minion.    |",
	"|_________________________|"),
	entrance_effect = ["destroy_minion(area_of_effect = 'SINGLE PLAYER ON OCCUPIED BASE', power = 2)"],
	tags = ['action'])

shangai = card(name = "Shanghi", 
	graphic = card_graphics(
	" _________________________ ",
	"|A        Shanghi        A|",
	"|        _                |",
	'|      /(")\     \O/      |',
	"|       <|-r      |       |",
	"|       / \      / \      |",
	"|    -----------------    |",
	"|                         |",
	"|  Move another player's  |",
	"| minion to another base. |",
	"|_________________________|"),
	entrance_effect = ["move_minion(area_of_effect(!owner))"],
	tags = ['action'])

powderkeg = card(name = "Powderkeg", 
	graphic = card_graphics(
	" _________________________ ",
	"|A       Powderkeg       A|",
	"|          ______         |",
	"|         |      |        |",
	"|         |Powder|        |",
	"|         |______|        |",
	"|   Destroy one of your   |",
	"| minions and all minions |",
	"|with equal or less power |",
	"|    on the same base.    |",
	"|_________________________|"),
	entrance_effect = ["destroy_minion(area_of_effect(own)), destroy_minion(area_of_effect(chosen_minion.base))"],
	tags = ['action'])
	
swashbuckling = card(name = "Swashbuckling ", 
	graphic = card_graphics(
	" _________________________ ",
	"|A     Swashbuckling     A|",
	"|                         |",
	"|       /v\  \/           |",
	"|       ( )  /\  o        |",
	"|        |--/  \-|        |",
	"|       / \     < \       |",
	"|  Each of your minions   |",
	"|gains +1 power until the |",
	"|    end of the turn.     |",
	"|_________________________|"),
	entrance_effect = ["give_power(1, area_of_effect = 'ALL OWNED')"],
	tags = ['action'])
	
cannon = card(name = "Cannon", 
	graphic = card_graphics(
	" _________________________ ",
	"|A        Cannon_        A|",
	"|   ___________/ |     __ |",
	"|  /           | |   __  /|",
	"|O|____        | |   __ | |",
	"| /    \_______| |     __\|",
	"||      |      \_|        |",
	"| \____/                  |",
	"|Destroy up to two minions|",
	"|   of power 2 or less.   |",
	"|_________________________|"),
	entrance_effect = ["destroy_minion(number = 2, power = 2)"],
	tags = ['action'])
	
full_sail = card(name = "Full Sail", 
	graphic = card_graphics(
	" _________________________ ",
	"|A       Full Sail       A|",
	"|      |\        |\       |",
	"|      | \       | \      |",
	"|    __|--`_   __|--`_    |",
	"|    \_____/   \_____/    |",
	"| Move any number of your |",
	"| minions to other bases. |",
	"| Special: Before a base  |",
	"|scores, you may play this|",
	"|_________________________|"),
	entrance_effect = ["move_minion(area_of_effect = 'ALL OWNED')"],
	special_effect = ["move_minion(area_of_effect = 'ALL OWNED')"],
	tags = ['action'])
	
sea_dogs = card(name = "Sea Dogs", 
	graphic = card_graphics(
	" _________________________ ",
	"|A       Sea Dogs        A|",
	"|              /\_        |",
	"|       |\____/ o_)       |",
	"|       |  __   /         |",
	"|       |_|  |_|          |",
	"|Name a faction. Move all |",
	"|other players' minions of|",
	"|  that faction from one  |",
	"|     base to another.    |",
	"|_________________________|"),
	entrance_effect = ["move_minion(area_of_effect = 'BASE, SINGLE FACTION, !USER')"],
	tags = ['action'])

#ROBOTS

zapbot1 = card(name = "Zapbot", 
	graphic = card_graphics(
	" _________________________ ",
	"|2        Zapbot         2|",
	"|           ___           |",
	"|     |__| [__()          |",
	"|       \ __|__           |",
	"|        |     |--[}==    |",
	"|        |_____|          |",
	"|        O     O          |",
	"|  You may play an extra  |",
	"|minion of power 2 or less|",
	"|_________________________|"),
	power = 2,
	entrance_effect = ["extra_minion(power = 2)"],
	tags = ['minion', 'Robots'])
zapbot2 = card(name = "Zapbot", 
	graphic = card_graphics(
	" _________________________ ",
	"|2        Zapbot         2|",
	"|           ___           |",
	"|     |__| [__()          |",
	"|       \ __|__           |",
	"|        |     |--[}==    |",
	"|        |_____|          |",
	"|        O     O          |",
	"|  You may play an extra  |",
	"|minion of power 2 or less|",
	"|_________________________|"),
	power = 2,
	entrance_effect = ["extra_minion(power = 2)"],
	tags = ['minion', 'Robots'])
zapbot3 = card(name = "Zapbot", 
	graphic = card_graphics(
	" _________________________ ",
	"|2        Zapbot         2|",
	"|           ___           |",
	"|     |__| [__()          |",
	"|       \ __|__           |",
	"|        |     |--[}==    |",
	"|        |_____|          |",
	"|        O     O          |",
	"|  You may play an extra  |",
	"|minion of power 2 or less|",
	"|_________________________|"),
	power = 2,
	entrance_effect = ["extra_minion(power = 2)"],
	tags = ['minion', 'Robots'])
zapbot4 = card(name = "Zapbot", 
	graphic = card_graphics(
	" _________________________ ",
	"|2        Zapbot         2|",
	"|           ___           |",
	"|     |__| [__()          |",
	"|       \ __|__           |",
	"|        |     |--[}==    |",
	"|        |_____|          |",
	"|        O     O          |",
	"|  You may play an extra  |",
	"|minion of power 2 or less|",
	"|_________________________|"),
	power = 2,
	entrance_effect = ["extra_minion(power = 2)"],
	tags = ['minion', 'Robots'])

hoverbot1 = card(name = "Hoverbot", 
	graphic = card_graphics(
	" _________________________ ",
	"|3       Hoverbot        3|",
	"|        __|--|__         |",
	"|       /__    __\        |",
	"|        / \  / \         |",
	"|         / \/ \          |",
	"|Reveal the top card of   |",
	"|your deck. Play it if it |",
	"| is a minion. Otherwise, |",
	"| return it to your deck. |",
	"|_________________________|"),
	power = 3,
	entrance_effect = ["reveal_top('PLAY IF MINION')"],
	tags = ['minion', 'Robots'])
hoverbot2 = card(name = "Hoverbot", 
	graphic = card_graphics(
	" _________________________ ",
	"|3       Hoverbot        3|",
	"|        __|--|__         |",
	"|       /__    __\        |",
	"|        / \  / \         |",
	"|         / \/ \          |",
	"|Reveal the top card of   |",
	"|your deck. Play it if it |",
	"| is a minion. Otherwise, |",
	"| return it to your deck. |",
	"|_________________________|"),
	power = 3,
	entrance_effect = ["reveal_top('PLAY IF MINION')"],
	tags = ['minion', 'Robots'])
hoverbot3 = card(name = "Hoverbot", 
	graphic = card_graphics(
	" _________________________ ",
	"|3       Hoverbot        3|",
	"|        __|--|__         |",
	"|       /__    __\        |",
	"|        / \  / \         |",
	"|         / \/ \          |",
	"|Reveal the top card of   |",
	"|your deck. Play it if it |",
	"| is a minion. Otherwise, |",
	"| return it to your deck. |",
	"|_________________________|"),
	power = 3,
	entrance_effect = ["reveal_top('PLAY IF MINION')"],
	tags = ['minion', 'Robots'])

warbot1 = card(name = "Warbot", 
	graphic = card_graphics(
	" _________________________ ",
	"|4        Warbot         4|",
	"|       __________        |",
	"| |__| | ________ | |__|  |",
	"|   \  ||________||  /    |",
	"|    \_|          |_/     |",
	"|      |__________|       |",
	"|        |_|  |_|         |",
	"|  Ongoing: This minion   |",
	"|  cannot be destroyed.   |",
	"|_________________________|"),
	power = 4,
	protect_effect = ["negate_destroy(self)"],
	tags = ['minion', 'Robots'])
warbot2 = card(name = "Warbot", 
	graphic = card_graphics(
	" _________________________ ",
	"|4        Warbot         4|",
	"|       __________        |",
	"| |__| | ________ | |__|  |",
	"|   \  ||________||  /    |",
	"|    \_|          |_/     |",
	"|      |__________|       |",
	"|        |_|  |_|         |",
	"|  Ongoing: This minion   |",
	"|  cannot be destroyed.   |",
	"|_________________________|"),
	power = 4,
	protect_effect = ["negate_destroy(self)"],
	tags = ['minion', 'Robots'])

nukebot = card(name = "Nukebot", 
	graphic = card_graphics(
	" _________________________ ",
	"|5        Nukebot        5|",
	"|           ___           |",
	"|        <=|_=_|=>        |",
	"|            |            |",
	"|        /--[_]--\        |",
	"|       /    |    \       |",
	"| After this is destroyed,|",
	"|   destroy each other    |",
	"|  player's minions here. |",
	"|_________________________|"),
	power = 5,
	entrance_effect = ["destroy_minion(area_of_effect = 'ALL !owner')"],
	tags = ['minion', 'Robots'])

microbot_fixer1 = card(name = "Microbot Fixer",
	graphic = card_graphics(
	" _________________________ ", 
	"|1     Microbot Fixer    1|", 
	"|     o-\  __|_           |", 
	"|        \| o  |-[        |", 
	"|      }--|____|--X       |", 
	"|   If this is the first  |", 
	"|  minion you played this |", 
	"|  turn, you may play an  |", 
	"|  extra minion. Ongoing: |", 
	"| Microbots gain +1 power |", 
	"|_________________________|"),
	entrance_effect = ["robot_extra_minion"],
	ongoing_effect = ["gain_power(1, 'microbots')"],
	tags = ['minion', 'microbot', 'Robots'],)
microbot_fixer2 = card(name = "Microbot Fixer",
	graphic = card_graphics(
	" _________________________ ", 
	"|1     Microbot Fixer    1|", 
	"|     o-\  __|_           |", 
	"|        \| o  |-[        |", 
	"|      }--|____|--X       |", 
	"|   If this is the first  |", 
	"|  minion you played this |", 
	"|  turn, you may play an  |", 
	"|  extra minion. Ongoing: |", 
	"| Microbots gain +1 power |", 
	"|_________________________|"),
	power = 1,
	entrance_effect = ["robot_extra_minion"],
	ongoing_effect = ["gain_power(1, 'microbots')"],
	tags = ['minion', 'microbot', 'Robots'],)

microbot_guard1 = card(name = "Microbot Guard", 
	graphic = card_graphics(
	" _________________________ ",
	"|1     Microbot Guard    1|",
	"|           ___           |",
	"|         /\ _ /\         |",
	"|        |--|O|--|        |",
	"|         \ | | /         |",
	"|Destroy a minion on this |",
	"|base with power less than|",
	"|  the number of minions  |",
	"|      you have here.     |",
	"|_________________________|"),
	entrance_effect = ["destroy_minion(power = (play[base][player].length - 1))"],
	tags = ['minion', 'microbot', 'Robots'])
microbot_guard2 = card(name = "Microbot Guard", 
	graphic = card_graphics(
	" _________________________ ",
	"|1     Microbot Guard    1|",
	"|           ___           |",
	"|         /\ _ /\         |",
	"|        |--|O|--|        |",
	"|         \ | | /         |",
	"|Destroy a minion on this |",
	"|base with power less than|",
	"|  the number of minions  |",
	"|      you have here.     |",
	"|_________________________|"),
	entrance_effect = ["destroy_minion(power = (play[base][player].length - 1))"],
	tags = ['minion', 'microbot', 'Robots'])

microbot_reclaimer1 = card(name = "Microbot Reclaimer", 
	graphic = card_graphics(
	" _________________________ ",
	"|1  Microbot Reclaimer   1|",
	"|       |---[o]--\        |",
	"|      [ ] __|__  \       |",
	"|         /_____\  D      |",
	"|   If this is the first  |", 
	"|  minion you played this |", 
	"|  turn, you may play an  |", 
	"|extra minion. Put in deck|", 
	"|any # discarded Microbots|",
	"|_________________________|"),
	power = 1,
	entrance_effect = ["robot_extra_minion, reclaim('microbots')"],
	tags = ['minion', 'microbot', 'Robots'])
microbot_reclaimer2 = card(name = "Microbot Reclaimer", 
	graphic = card_graphics(
	" _________________________ ",
	"|1  Microbot Reclaimer   1|",
	"|       |---[o]--\        |",
	"|      [ ] __|__  \       |",
	"|         /_____\  D      |",
	"|   If this is the first  |", 
	"|  minion you played this |", 
	"|  turn, you may play an  |", 
	"|extra minion. Put in deck|", 
	"|any # discarded Microbots|",
	"|_________________________|"),
	power = 1,
	entrance_effect = ["robot_extra_minion, reclaim('microbots')"],
	tags = ['minion', 'microbot', 'Robots'])

microbot_archive = card(name = "Microbot Archive", 
	graphic = card_graphics(
	" _________________________ ",
	"|1   Microbot Archive    1|",
	"|            [=}          |",
	"|         ___|_           |",
	"|        /   _ \--\o      |",
	"|        |  |O||          |",
	"|        |_____|          |",
	"|  Ongoing: After one of  |",
	"|    your Microbots is    |",
	"| destroyed, draw a card. |",
	"|_________________________|"),
	power = 1,
	protect_effect = ["after_destroy('microbot', self.owner.draw_card(1))"],
	tags = ['minion', 'microbot', 'Robots'])

microbot_alpha = card(name = "Microbot Alpha", 
	graphic = card_graphics(
	" _________________________ ",
	"|1    Microbot Alpha     1|",
	"|          _[o]_          |",
	"|       ]-|_ | _|-[       |",
	"|          _|_|_          |",
	"|         /_____\         |",
	"| Ongoing: Gains +1 power |",
	"| for each of your other  |",
	"|   Microbots. All your   |",
	"|  minions are Microbots. |",
	"|_________________________|"),
	power = 1,
	entrance_effect = ["ggive_power(1, area_of_effect = 'ALL OWNED')"],
	tags = ['minion', 'microbot', 'Robots'])

tech_center1 = card(name = "Tech Center", 
	graphic = card_graphics(
	" _________________________ ",
	"|A      Tech Center      A|",
	"|          __|__          |",
	"|        _|     |_        |",
	"|    ]--/_       _\--[    |",
	"|       _|__ _ __|_       |",
	"|      / |__| |__| \      |",
	"|     Choose a base.      |",
	"|  Draw a card for each   |",
	"| of your minions there.  |",
	"|_________________________|"),
	entrance_effect = ["self.owner.draw_card(play[chosen_base][self.owner].length)"],
	tags = ['action'])
tech_center2 = card(name = "Tech Center", 
	graphic = card_graphics(
	" _________________________ ",
	"|A      Tech Center      A|",
	"|          __|__          |",
	"|        _|     |_        |",
	"|    ]--/_       _\--[    |",
	"|       _|__ _ __|_       |",
	"|      / |__| |__| \      |",
	"|     Choose a base.      |",
	"|  Draw a card for each   |",
	"| of your minions there.  |",
	"|_________________________|"),
	entrance_effect = ["self.owner.draw_card(play[chosen_base][self.owner].length)"],
	tags = ['action'])

#TRICKSTERS

gremlin1 = card(name = "Gremlin", 
	graphic = card_graphics(
	" _________________________ ",
	"|2        Gremlin        2|",
	"|         _  _  _         |",
	"|        /_(o o)_\        |",
	"|          /|_|\          |",
	"|           | |           |",
	"| Ongoing: After this is  |",
	"| destroyed, draw a card  |",
	"|  and each other player  |",
	"| discards a random card. |",
	"|_________________________|"),
	power = 2,
	protect_effect = ["negate_destroy(destroy_minion(self), self.owner.draw_card(1)) discard_card(area_of_effect = !owner, random = TRUE)"],
	tags = ['minion', 'Tricksters'])
gremlin2 = card(name = "Gremlin", 
	graphic = card_graphics(
	" _________________________ ",
	"|2        Gremlin        2|",
	"|         _  _  _         |",
	"|        /_(o o)_\        |",
	"|          /|_|\          |",
	"|           | |           |",
	"| Ongoing: After this is  |",
	"| destroyed, draw a card  |",
	"|  and each other player  |",
	"| discards a random card. |",
	"|_________________________|"),
	power = 2,
	protect_effect = ["negate_destroy(destroy_minion(self), self.owner.draw_card(1)) discard_card(area_of_effect = !owner, random = TRUE)"],
	tags = ['minion', 'Tricksters'])
gremlin3 = card(name = "Gremlin", 
	graphic = card_graphics(
	" _________________________ ",
	"|2        Gremlin        2|",
	"|         _  _  _         |",
	"|        /_(o o)_\        |",
	"|          /|_|\          |",
	"|           | |           |",
	"| Ongoing: After this is  |",
	"| destroyed, draw a card  |",
	"|  and each other player  |",
	"| discards a random card. |",
	"|_________________________|"),
	power = 2,
	protect_effect = ["negate_destroy(destroy_minion(self), self.owner.draw_card(1)) discard_card(area_of_effect = !owner, random = TRUE)"],
	tags = ['minion', 'Tricksters'])
gremlin4 = card(name = "Gremlin", 
	graphic = card_graphics(
	" _________________________ ",
	"|2        Gremlin        2|",
	"|         _  _  _         |",
	"|        /_(o o)_\        |",
	"|          /|_|\          |",
	"|           | |           |",
	"| Ongoing: After this is  |",
	"| destroyed, draw a card  |",
	"|  and each other player  |",
	"| discards a random card. |",
	"|_________________________|"),
	power = 2,
	protect_effect = ["negate_destroy(destroy_minion(self), self.owner.draw_card(1)) discard_card(area_of_effect = !owner, random = TRUE)"],
	tags = ['minion', 'Tricksters'])

gnome1 = card(name = "Gnome", 
	graphic = card_graphics(
	" _________________________ ",
	"|3         Gnome         3|",
	"|          /___\          |",
	"|        \ (o o)-U        |",
	"|         \/|_|\          |",
	"|           | |           |",
	"|You may destroy a minion |",
	"| on this base with power |",
	"| less than the number of |",
	"|  minions you have here. |",
	"|_________________________|"),
	power = 3,
	entrance_effect = ["destroy_minion(power = (play[base][player].length - 1), optional = True)"],
	tags = ['minion', 'Tricksters'])
gnome2 = card(name = "Gnome", 
	graphic = card_graphics(
	" _________________________ ",
	"|3         Gnome         3|",
	"|          /___\          |",
	"|        \ (o o)-U        |",
	"|         \/|_|\          |",
	"|           | |           |",
	"|You may destroy a minion |",
	"| on this base with power |",
	"| less than the number of |",
	"|  minions you have here. |",
	"|_________________________|"),
	power = 3,
	entrance_effect = ["destroy_minion(power = (play[base][player].length - 1), optional = True)"],
	tags = ['minion', 'Tricksters'])
gnome3 = card(name = "Gnome", 
	graphic = card_graphics(
	" _________________________ ",
	"|3         Gnome         3|",
	"|          /___\          |",
	"|        \ (o o)-U        |",
	"|         \/|_|\          |",
	"|           | |           |",
	"|You may destroy a minion |",
	"| on this base with power |",
	"| less than the number of |",
	"|  minions you have here. |",
	"|_________________________|"),
	power = 3,
	entrance_effect = ["destroy_minion(power = (play[base][player].length - 1), optional = True)"],
	tags = ['minion', 'Tricksters'])

brownie1 = card(name = "Brownie", 
	graphic = card_graphics(
	" _________________________ ",
	"|4        Brownie        4|",
	"|          www   c        |",
	"|         (o o) /         |",
	"|         /www-/          |",
	"|          | |            |",
	"| Ongoing: After another  |",
	"|player plays a card that |",
	"|affects this minion, they|",
	"|discard two random cards.|",
	"|_________________________|"),
	power = 4,
	entrance_effect = ["negate_all(negated_card.owner.discard_random(2))"], #Code Last
	tags = ['minion', 'Tricksters'])
brownie2 = card(name = "Brownie", 
	graphic = card_graphics(
	" _________________________ ",
	"|4        Brownie        4|",
	"|          www   c        |",
	"|         (o o) /         |",
	"|         /www-/          |",
	"|          | |            |",
	"| Ongoing: After another  |",
	"|player plays a card that |",
	"|affects this minion, they|",
	"|discard two random cards.|",
	"|_________________________|"),
	power = 4,
	entrance_effect = ["negate_all(negated_card.owner.discard_random(2))"], #Code Last
	tags = ['minion', 'Tricksters'])

leprechaun = card(name = "Leprechaun", 
	graphic = card_graphics(
	" _________________________ ",
	"|5      Leprechaun       5|",
	"|          _[_]_          |",
	"|        c (o o) O        |",
	"|        |__www__/        |",
	"|        |   |            |",
	"|        |  / \           |",
	"|  After another player   |",
	"|plays a minion here with |",
	"| less power, destroy it. |",
	"|_________________________|"),
	power = 5,
	minion_effect = ["destroy_minion(power = self.ongoing_power - 1)"],
	tags = ['action'])

block_the_path = card(name = "Block The Path", 
	graphic = card_graphics(
	" _________________________ ",
	"|A    Block the Path     A|",
	"|   WWW  c \      _[ ]    |",
	"|  ( |o) |  |  ]-|_ ||    |",
	"|   |_W--|  |     _|_|_   |",
	"|   | |  | /     /_____\  |",
	"| Play on a base and name |",
	"|   a faction. Ongoing:   |",
	"| minions of that faction |",
	"| cannot be played here.  |",
	"|_________________________|"),
	minion_effect = ["block_play(), if minion on base and card.card.tags.find('minion') and card.tags.find('chosen_faction')"],
	tags = ['action', 'attachment'])

disenchant1 = card(name = "Disenchant", 
	graphic = card_graphics(
	" _________________________ ",
	"|A      Disenchant       A|",
	"|       www   c**         |",
	"|      (o o) /  ***       |",
	"|      /www-/     ***     |",
	"|      _|_|_              |",
	"|     |     |             |",
	"|Destroy an an action that|",
	"|  has been played on a   |",
	"|     minion or base.     |",
	"|_________________________|"),
	entrance_effect = ["destroy_action(attach = ['BASE', 'MINION'])"],
	tags = ['action', 'attachment'])
disenchant2 = card(name = "Disenchant", 
	graphic = card_graphics(
	" _________________________ ",
	"|A      Disenchant       A|",
	"|       www   c**         |",
	"|      (o o) /  ***       |",
	"|      /www-/     ***     |",
	"|      _|_|_              |",
	"|     |     |             |",
	"|Destroy an an action that|",
	"|  has been played on a   |",
	"|     minion or base.     |",
	"|_________________________|"),
	entrance_effect = ["destroy_action(attach = ['BASE', 'MINION'])"],
	tags = ['action', 'attachment'])

enshrouding_mist1 = card(name = "Enshrouding Mist", 
	graphic = card_graphics(
	" _________________________ ",
	"|A   Enshrouding Mist    A|",
	"|~~~~~~~~~~~~~~~~~~~~~~~~~|",
	"|~~~~~~~~_~~_~~_~~*~~~~~~~|",
	"|~~~~~~~/_(o o)_\*O*~~~~~~|",
	"|~~~~~~~~~/|_|---/~~~~~~~~|",
	"|~~~~~~~~~~| |~~~~~~~~~~~~|",
	"|Play on a base. Ongoing: |",
	"|  On your turn, you may  |",
	"|play an extra minion here|",
	"|_________________________|"),
	ongoing_effect = ["extra_minion('played_on(attach)')"],
	tags = ['action', 'attachment'])
enshrouding_mist2 = card(name = "Enshrouding Mist", 
	graphic = card_graphics(
	" _________________________ ",
	"|A   Enshrouding Mist    A|",
	"|~~~~~~~~~~~~~~~~~~~~~~~~~|",
	"|~~~~~~~~_~~_~~_~~*~~~~~~~|",
	"|~~~~~~~/_(o o)_\*O*~~~~~~|",
	"|~~~~~~~~~/|_|---/~~~~~~~~|",
	"|~~~~~~~~~~| |~~~~~~~~~~~~|",
	"|Play on a base. Ongoing: |",
	"|  On your turn, you may  |",
	"|play an extra minion here|",
	"|_________________________|"),
	ongoing_effect = ["extra_minion('played_on(attach)')"],
	tags = ['action', 'attachment'])

flame_trap = card(name = "Flame Trap", 
	graphic = card_graphics(
	" _________________________ ",
	"|A      Flame Trap       A|",
	"|          )(             |",
	"|        )\O/\            |",
	"|       / )| (|  __       |",
	"|       \(/ \)/ |__ _     |",
	"|Play on a base. Ongoing: |",
	"|  After another player   |",
	"|  plays a minion here,   |",
	"|destroy it and this card.|",
	"|_________________________|"),
	protect_effect = ["minion_play(attach), destroy_minion(player_minion), destroy_action(self)"],
	tags = ['action', 'attachment'])

hideout = card(name = "Hideout", 
	graphic = card_graphics(
	" _________________________ ",
	"|A        Hideout        A|",
	"|         _______         |",
	"|        /_______\        |",
	"|         | | | |         |",
	"|Play on a base. Ongoing: |",
	"|If another players action|",
	"|would affect your minions|",
	"| here, destroy this card |",
	"|and protect your minions.|",
	"|_________________________|"),
	protect_effect = ["play_action(if(effects_self_on_base)), negate_action(played_action), destroy_action(self)"],
	tags = ['action', 'attachment'])

mark_of_sleep = card(name = "Mark Of Sleep",
	graphic = card_graphics(
	" _________________________ ",
	"|A     Mark Of Sleep     A|",
	"|           Z             |",
	"|    ____ z               |",
	"|   /|  o\ _____________  |",
	"|  |      |_____________  |",
	"|   \____/                |",
	"|  Choose a player. That  |",
	"|player can't play actions|",
	"|   on thier next turn.   |",
	"|_________________________|"),
	ongoing_effect = ["negate_action_play(chosen_player)"],
	end_of_turn_effect = ["destroy_action_effect(self, turn(chosen_player))"],
	tags = ['action'])

pay_the_piper = card(name = "Pay The Piper", 
	graphic = card_graphics(
	" _________________________ ",
	"|A     Pay The Piper     A|",
	"|   ___    \u266b  \_____/     |",
	"|  ( |o)==    /     \     |",
	"|   |_|/     |  $$$  |    |",
	"|   | |       \_____/     |",
	"|Play on a base. Ongoing: |",
	"|  After another player   |",
	"|plays a minion here, that|",
	"| player discards a card. |",
	"|_________________________|"),
	minion_effect = ["player.discard(choose = 'True', base = attach)"],
	tags = ['action', 'attachment'])

take_the_shinies = card(name = "Take The Shinies", 
	graphic = card_graphics(
	" _________________________ ",
	"|A   Take The Shinies    A|",
	"|       |   $$$   |       |",
	"|       |         |       |",
	"|        \_______/        |",
	"|       _ \(o o)/         |",
	"|        _  |_|           |",
	"|       _   | |           |",
	"|    Each other player    |",
	"|discards two random cards|",
	"|_________________________|"),
	entrance_effect = ["discard_card(area_of_effect = '!owner', random = True)"],
	tags = ['action', 'attachment'])

#WIZARDS

neophyte1 = card(name = "Neophyte", 
	graphic = card_graphics(
	" _________________________ ",
	"|2       Neophyte        2|",
	"|          o              |",
	"|          |- [_]         |",
	"|         / \ | |         |",
	"| Reveal the top card of  |",
	"|your deck. You may place |",
	"| it in your hand or play |",
	"|     it as an action.    |",
	"|  Otherwise, return it.  |",
	"|_________________________|"),
	power = 2,
	entrance_effect = ["deck_top(play(action), retrive(action), 'Return It To The Top')"],
	tags = ['minion', 'Wizards'])
neophyte2 = card(name = "Neophyte", 
	graphic = card_graphics(
	" _________________________ ",
	"|2       Neophyte        2|",
	"|          o              |",
	"|          |- [_]         |",
	"|         / \ | |         |",
	"| Reveal the top card of  |",
	"|your deck. You may place |",
	"| it in your hand or play |",
	"|     it as an action.    |",
	"|  Otherwise, return it.  |",
	"|_________________________|"),
	power = 2,
	entrance_effect = ["deck_top(play(action), retrive(action), 'Return It To The Top')"],
	tags = ['minion', 'Wizards'])
neophyte3 = card(name = "Neophyte", 
	graphic = card_graphics(
	" _________________________ ",
	"|2       Neophyte        2|",
	"|          o              |",
	"|          |- [_]         |",
	"|         / \ | |         |",
	"| Reveal the top card of  |",
	"|your deck. You may place |",
	"| it in your hand or play |",
	"|     it as an action.    |",
	"|  Otherwise, return it.  |",
	"|_________________________|"),
	power = 2,
	entrance_effect = ["deck_top(play(action), retrive(action), 'Return It To The Top')"],
	tags = ['minion', 'Wizards'])
neophyte4 = card(name = "Neophyte", 
	graphic = card_graphics(
	" _________________________ ",
	"|2       Neophyte        2|",
	"|          o              |",
	"|          |- [_]         |",
	"|         / \ | |         |",
	"| Reveal the top card of  |",
	"|your deck. You may place |",
	"| it in your hand or play |",
	"|     it as an action.    |",
	"|  Otherwise, return it.  |",
	"|_________________________|"),
	power = 2,
	entrance_effect = ["deck_top(play(action), retrive(action), 'Return It To The Top')"],
	tags = ['minion', 'Wizards'])


enchantress1 = card(name = "Enchantress", 
	graphic = card_graphics(
	" _________________________ ",
	"|2      Enchantress      2|",
	"|         _*_*_*_         |",
	"|       */* * * *\*       |",
	"|      *|*   O | *|*      |",
	"|      *|*  -|-| *|*      |",
	"|      *|*  / \  *|*      |",
	"|                         |",
	"|       Draw a card.      |",
	"|                         |",
	"|_________________________|"),
	power = 2,
	entrance_effect = ["self.owner.draw_card(1)"],
	tags = ['minion', 'Wizards'])
enchantress2 = card(name = "Enchantress", 
	graphic = card_graphics(
	" _________________________ ",
	"|2      Enchantress      2|",
	"|         _*_*_*_         |",
	"|       */* * * *\*       |",
	"|      *|*   O | *|*      |",
	"|      *|*  -|-| *|*      |",
	"|      *|*  / \  *|*      |",
	"|                         |",
	"|       Draw a card.      |",
	"|                         |",
	"|_________________________|"),
	power = 2,
	entrance_effect = ["self.owner.draw_card(1)"],
	tags = ['minion', 'Wizards'])
enchantress3 = card(name = "Enchantress", 
	graphic = card_graphics(
	" _________________________ ",
	"|2      Enchantress      2|",
	"|         _*_*_*_         |",
	"|       */* * * *\*       |",
	"|      *|*   O | *|*      |",
	"|      *|*  -|-| *|*      |",
	"|      *|*  / \  *|*      |",
	"|                         |",
	"|       Draw a card.      |",
	"|                         |",
	"|_________________________|"),
	power = 2,
	entrance_effect = ["self.owner.draw_card(1)"],
	tags = ['minion', 'Wizards'])
	
chronomage1 = card(name = "Chronomage", 
	graphic = card_graphics(
	" _________________________ ",
	"|3      Chronomage       3|",
	"|              _______    |",
	"|             |*******|   |",
	"|              \_***_/    |",
	"|    O__ __     _|*|_     |",
	"|   /|         /  *  \    |",
	"|   / \       |_______|   |",
	"|  You may play an extra  |",
	"|    action this turn.    |",
	"|_________________________|"),
	power = 3,
	entrance_effect = ["extra_action(self.owner)"],
	tags = ['minion', 'Wizards'])
chronomage2 = card(name = "Chronomage", 
	graphic = card_graphics(
	" _________________________ ",
	"|3      Chronomage       3|",
	"|              _______    |",
	"|             |*******|   |",
	"|              \_***_/    |",
	"|    O__ __     _|*|_     |",
	"|   /|         /  *  \    |",
	"|   / \       |_______|   |",
	"|  You may play an extra  |",
	"|    action this turn.    |",
	"|_________________________|"),
	power = 3,
	entrance_effect = ["extra_action(self.owner)"],
	tags = ['minion', 'Wizards'])

archmage = card(name = "Archmage", 
	graphic = card_graphics(
	" _________________________ ",
	"|4       Archmage        4|",
	"|         /*_*_* \        |",
	"|        ||/ O |*|        |",
	"|         |__|_/*/        |",
	"|         |  |            |",
	"|         | / \           |",
	"|Ongoing: You may play an |",
	"| extra action on each of |",
	"|       your turns.       |",
	"|_________________________|"),
	power = 4,
	ongoing_effect = ["extra_action(turn = 'self.owner')"],
	tags = ['minion', 'Wizards'])

mass_enchantment = card(name = "Mass Enchantment", 
	graphic = card_graphics(
	" _________________________ ",
	"|A    Mass Enchantment   A|",
	"|              |          |",
	"|      O  *****| __o      |",
	"|     -|-/*****|    \     |",
	"|     / \      |    /\    |",
	"|  Reveal the top card of |",
	"|each other player's deck.|",
	"|Play one revealed action |",
	"|   as an extra action.   |",
	"|_________________________|"),
	entrance_effect = ["deck_top(area_of_effect(!self.owner, actions))"],
	tags = ['action', 'Wizards'])
	
mystic_studies1 = card(name = "Mystic Studies", 
	graphic = card_graphics(
	" _________________________ ",
	"|A    Mystic Studies     A|",
	"|                         |",
	"|    _,-----. .-----,_    |",
	"|   //~~~~~~ | ~~~~~~\\\   |",
	"|  //~~~~~~  |  ~~~~~~\\\  |",
	"| //________ | ________\\\ |",
	"| '--------.___.--------' |",
	"|                         |",
	"|     Draw two cards.     |",
	"|_________________________|"),
	entrance_effect = ["self.owner.draw_card(2)"],
	tags = ['action', 'Wizards'])
mystic_studies2 = card(name = "Mystic Studies", 
	graphic = card_graphics(
	" _________________________ ",
	"|A    Mystic Studies     A|",
	"|                         |",
	"|    _,-----. .-----,_    |",
	"|   //~~~~~~ | ~~~~~~\\\   |",
	"|  //~~~~~~  |  ~~~~~~\\\  |",
	"| //________ | ________\\\ |",
	"| '--------.___.--------' |",
	"|                         |",
	"|     Draw two cards.     |",
	"|_________________________|"),
	entrance_effect = ["self.owner.draw_card(2)"],
	tags = ['action', 'Wizards'])
	
portal = card(name = "Portal", 
	graphic = card_graphics(
	" _________________________ ",
	"|A        Portal         A|",
	"|         /****\          |",
	"|        |******|         |",
	"|         \****/          |",
	"|Reveal the top 5 cards of|",
	"|your deck. Place any # of|",
	"|  minions revealed into  |",
	"| your hand. Return the   |",
	"|other cards to your deck.|",	
	"|_________________________|"),
	entrance_effect = ["deck_top(5, retrieve(minions), return in chosen order)"],
	tags = ['action', 'Wizards'])
	
sacrifice = card(name = "Sacrifice", 
	graphic = card_graphics(
	" _________________________ ",
	"|A       Sacrifice       A|",
	"|                         |",
	"|                         |",
	"|        | |  | |         |",
	"|       (__|  |__)        |",
	"|   Choose one of your    |",
	"|minions. Draw cards equal|",
	"|  to its power. Destroy  |",
	"|      that minion.       |",	
	"|_________________________|"),
	entrance_effect = ["destroy_minion(any(self.owner)), self.owner.draw_card(chosen_minion.ongoing_power)"],
	tags = ['action', 'Wizards'])

scry = card(name = "Scry", 
	graphic = card_graphics(
	" _________________________ ",
	"|A         Scry          A|",
	"|        /      \         |",
	"|       |        |        |",
	"|        \______/         |",
	"|       /________\        |",
	"| Search your deck for an |",
	"| action and reveal it to |",
	"|  all players. Place it  |",
	"|     into your deck.     |",
	"|_________________________|"),
	entrance_effect = ["retrieve(action, show_deck = True)"],
	tags = ['action', 'Wizards'])

summon1 = card(name = "Summon", 
	graphic = card_graphics(
	" _________________________ ",
	"|A   ___  Summon         A|",
	"|.-~     '.               |",
	"| / /  ~@\   )            |",
	"| |  |< ~\(..)            |",
	"| \  \<   .,,    _____    |",
	"|/~\ \< /         \O/     |",
	"|/-~\ \_|          |      |",
	"|                 / \     |",
	"|  Play an extra minion.  |",
	"|_________________________|"),

	entrance_effect = ["extra_minion(self.owner)"],
	tags = ['action', 'Wizards'])
summon2 = card(name = "Summon", 
	graphic = card_graphics(
	" _________________________ ",
	"|A   ___  Summon         A|",
	"|.-~     '.               |",
	"| / /  ~@\   )            |",
	"| |  |< ~\(..)            |",
	"| \  \<   .,,    _____    |",
	"|/~\ \< /         \O/     |",
	"|/-~\ \_|          |      |",
	"|                 / \     |",
	"|  Play an extra minion.  |",
	"|_________________________|"),

	entrance_effect = ["extra_minion(self.owner)"],
	tags = ['action', 'Wizards'])

time_loop = card(name = "Time Loop", 
	graphic = card_graphics(
	" _________________________ ",
	"|A       Time Loop       A|",
	"|       _________         |",
	"|      /   1|2   \        |",
	"|     |     |     |       |",
	"|     |9    O    3|       |",
	"|     |      \    |       |",
	"|      \____6_\__/        |",
	"|                         |",
	"| Play two extra actions. |",
	"|_________________________|"),
	entrance_effect = ["extra_action(self.owner), extra_action(self.owner)"],
	tags = ['action', 'Wizards'])

winds_of_change = card(name = "Winds of Change", 
	graphic = card_graphics(
	" _________________________ ",
	"|A    Winds of Change    A|",
	"|~  ~  ~  ~  ~  ~  ~  ~  ~|",
	"|  ~  ~  ~  ~  ~  ~  ~  ~ |",
	"|~  ~  ~  ~  ~  ~  ~  ~  ~|",
	"|  ~  ~  ~  ~  ~  ~  ~  ~ |",
	"| Shuffle your hand into  |",
	"| your deck and draw five |",
	"| cards. You may play an  |",
	"|      extra action.      |",
	"|_________________________|"),
	entrance_effect = ["discard_hand(self.owner), draw_hand(self.owner), extra_action(self.owner)"],
	tags = ['action', 'Wizards'])

#ZOMBIES

walker1 = card(name = "Walker", 
	graphic = card_graphics(
	" _________________________ ",
	"|2        Walker         2|",
	"|           O__           |",
	"|          /              |",
	"|         / \             |",
	"|      ---------          |",
	"| Look at the top card of |",
	"|your deck. Discard it or |",
	"|  return it to the top   |",
	"|      of your deck.      |",
	"|_________________________|"),
	power = 2,
	entrance_effect = ["deck_top(discard(card), 'Return It To The Top')"],
	tags = ['minion', 'Zombies'])
walker2 = card(name = "Walker", 
	graphic = card_graphics(
	" _________________________ ",
	"|2        Walker         2|",
	"|           O__           |",
	"|          /              |",
	"|         / \             |",
	"|      ---------          |",
	"| Look at the top card of |",
	"|your deck. Discard it or |",
	"|  return it to the top   |",
	"|      of your deck.      |",
	"|_________________________|"),
	power = 2,
	entrance_effect = ["deck_top(discard(card), 'Return It To The Top')"],
	tags = ['minion', 'Zombies'])
walker3 = card(name = "Walker", 
	graphic = card_graphics(
	" _________________________ ",
	"|2        Walker         2|",
	"|           O__           |",
	"|          /              |",
	"|         / \             |",
	"|      ---------          |",
	"| Look at the top card of |",
	"|your deck. Discard it or |",
	"|  return it to the top   |",
	"|      of your deck.      |",
	"|_________________________|"),
	power = 2,
	entrance_effect = ["deck_top(discard(card), 'Return It To The Top')"],
	tags = ['minion', 'Zombies'])
walker4 = card(name = "Walker", 
	graphic = card_graphics(
	" _________________________ ",
	"|2        Walker         2|",
	"|           O__           |",
	"|          /              |",
	"|         / \             |",
	"|      ---------          |",
	"| Look at the top card of |",
	"|your deck. Discard it or |",
	"|  return it to the top   |",
	"|      of your deck.      |",
	"|_________________________|"),
	power = 2,
	entrance_effect = ["deck_top(discard(card), 'Return It To The Top')"],
	tags = ['minion', 'Zombies'])

tenacious_z1 = card(name = "Tenacious Z", 
	graphic = card_graphics(
	" _________________________ ",
	"|2      Tenacious Z      2|",
	"|        ___              |",
	"|       |RIP|   O/        |",
	"|~~~~~~~~~~~~~//~~~~~~~~~~|",
	"|~~~~~~~~~~~~~/\~~~~~~~~~~|",
	"|Special: During your turn|",
	"| you may play this card  |",
	"| from your discard as an |",
	"|extra minion(Once a turn)|",
	"|_________________________|"),
	power = 2,
	discard_effect = ["extra_minion(self, constant = True)"],
	entrance_effect = ["remove_extra_minion()"],
	tags = ['minion', 'Zombies'])
tenacious_z2 = card(name = "Tenacious Z", 
	graphic = card_graphics(
	" _________________________ ",
	"|2      Tenacious Z      2|",
	"|        ___              |",
	"|       |RIP|   O/        |",
	"|~~~~~~~~~~~~~//~~~~~~~~~~|",
	"|~~~~~~~~~~~~~/\~~~~~~~~~~|",
	"|Special: During your turn|",
	"| you may play this card  |",
	"| from your discard as an |",
	"|extra minion(Once a turn)|",
	"|_________________________|"),
	power = 2,
	discard_effect = ["extra_minion(self, constant = True)"],
	entrance_effect = ["remove_extra_minion()"],
	tags = ['minion', 'Zombies'])
tenacious_z3 = card(name = "Tenacious Z", 
	graphic = card_graphics(
	" _________________________ ",
	"|2      Tenacious Z      2|",
	"|        ___              |",
	"|       |RIP|   O/        |",
	"|~~~~~~~~~~~~~//~~~~~~~~~~|",
	"|~~~~~~~~~~~~~/\~~~~~~~~~~|",
	"|Special: During your turn|",
	"| you may play this card  |",
	"| from your discard as an |",
	"|extra minion(Once a turn)|",
	"|_________________________|"),
	power = 2,
	discard_effect = ["extra_minion(self, constant = True)"],
	entrance_effect = ["remove_extra_minion()"],
	tags = ['minion', 'Zombies'])

grave_digger1 = card(name = "Grave Digger", 
	graphic = card_graphics(
	" _________________________ ",
	"|3     Grave Digger      3|",
	"|                         |",
	"|          _O             |",
	"|          |-\\\           |",
	"|__________|/_\___________|",
	"|~~~~~~~~~~U~~~~~~~~~~~~~~|",
	"| You may place a minion  |",
	"| from your discard pile  |",
	"|     into your hand.     |",
	"|_________________________|"),
	power = 3,
	entrance_effect = ["recard(1, 'MINION', optional = True)"],
	tags = ['minion', 'Zombies'])
grave_digger2 = card(name = "Grave Digger", 
	graphic = card_graphics(
	" _________________________ ",
	"|3     Grave Digger      3|",
	"|                         |",
	"|          _O             |",
	"|          |-\\\           |",
	"|__________|/_\___________|",
	"|~~~~~~~~~~U~~~~~~~~~~~~~~|",
	"| You may place a minion  |",
	"| from your discard pile  |",
	"|     into your hand.     |",
	"|_________________________|"),
	power = 3,
	entrance_effect = ["recard(1, 'MINION', optional = True)"],
	tags = ['minion', 'Zombies'])

zombie_lord = card(name = "Zombie Lord", 
	graphic = card_graphics(
	" _________________________ ",
	"|5  Zombie   _   Lord    5|",
	"|          _/_\_ |        |",
	"|           |_| /|        |",
	"|         [_]| / |        |",
	"|           / \           |",
	"|You may play a minion of |",
	"|power 2 or less from your|",
	"|  discard on each base   |",
	"|where you have no minions|",
	"|_________________________|"),
	power = 2,
	entrance_effect = ["extra_minion(unlimited = True, discard = True, power = 2)"],
	tags = ['minion', 'Zombies'])

they_keep_coming1 = card(name = "They Keep Coming", 
	graphic = card_graphics(
	" _________________________ ",
	"|A   They Keep Coming    A|",
	"|                         |",
	"|                         |",
	"|   O__    O__    \(o)/   |",
	"|  /      /         |     |",
	"|_/_\____/_\____O/_/_\____|",
	"|~~~~~~~~~~~~~~~|~~~~~~~~~|",
	"|Play an extra minion from|",
	"|   your discard pile.    |",
	"|_________________________|"),
	entrance_effect = ["extra_minion(discard = True)"],
	tags = ['action', 'Zombies'])
they_keep_coming2 = card(name = "They Keep Coming", 
	graphic = card_graphics(
	" _________________________ ",
	"|A   They Keep Coming    A|",
	"|                         |",
	"|                         |",
	"|   O__    O__    \(o)/   |",
	"|  /      /         |     |",
	"|_/_\____/_\____O/_/_\____|",
	"|~~~~~~~~~~~~~~~|~~~~~~~~~|",
	"|Play an extra minion from|",
	"|   your discard pile.    |",
	"|_________________________|"),
	entrance_effect = ["extra_minion(discard = True)"],
	tags = ['action', 'Zombies'])

grave_robbing1 = card(name = "Grave Robbing", 
	graphic = card_graphics(
	" _________________________ ",
	"|A     Grave Robbing     A|",
	"|          O              |",
	"|         /\       ___    |",
	"| _I--D__/\ \O _  |RIP|___|",
	"| ~~~~~~~~~|  \  |~~~~~~~~|",
    "| ~~~~~~~~~|___|\|~~~~~~~~|",
	"| Place a card from your  |",
	"| discard pile into your  |",
	"|          hand.          |",
	"|_________________________|"),
	entrance_effect = ["recard(1)"],
	tags = ['action', 'Zombies'])
grave_robbing2 = card(name = "Grave Robbing", 
	graphic = card_graphics(
	" _________________________ ",
	"|A     Grave Robbing     A|",
	"|          O              |",
	"|         /\       ___    |",
	"| _I--D__/\ \O _  |RIP|___|",
	"| ~~~~~~~~~|  \  |~~~~~~~~|",
    "| ~~~~~~~~~|___|\|~~~~~~~~|",
	"| Place a card from your  |",
	"| discard pile into your  |",
	"|          hand.          |",
	"|_________________________|"),
	entrance_effect = ["recard(1)"],
	tags = ['action', 'Zombies'])

overrun = card(name = "Overrun", 
	graphic = card_graphics(
	" _________________________ ",
	"|A        Overrun        A|",
	"|          \O             |",
	"|           |\            |",
	"|          /_\  X         |",
	"|  O/  O/ |   | \O  \O  \O|",
	"|Play on a base. Ongoing: |",
	"|Other players cannot play|",
	"|  minions on this base.  |",
	"|Destroy this on your turn|",
	"|_________________________|"),
	minion_effect = ["negate_minion(!self.owner)"],
	ongoing_effect = ["destroy_action(self, turn(self.owner))"],
	tags = ['action', 'attachment', 'Zombies'])

lend_a_hand = card(name = "Lend A Hand", 
	graphic = card_graphics(
	" _________________________ ",
	"|A      Lend A Hand      A|",
	"|                         |",
	"|        O   o   O        |",
	"|       /-/  |  \-\       |",
	"|      / \  / \   /\      |",
	"|                         |",
	"|  Shuffle any number of  |",
	"|cards from your discard  |",
	"|   pile into your deck.  |",
	"|_________________________|"),
	entrance_effect = ["recard(untimited = True)"],
	tags = ['action', 'Zombies'])

outbreak = card(name = "Outbreak", 
	graphic = card_graphics(
	" _________________________ ",
	"|A       Outbreak        A|",
	"|           __            |",
	"|          |  |           |",
	"|   O   O  |  |__O    (o) |",
	"|  /-  /-  |  |  |\   -|-r|",
	"| /\  /\   |  | / \X  / \ |",
	"|Play an extra minion on a|",
	"| base where you have no  |",
	"|         minions.        |",
	"|_________________________|"),
	entrance_effect = ["extra_minion(base = !self.owner))"],
	tags = ['action', 'Zombies'])
	
mall_crawl = card(name = "Mall Crawl", 
	graphic = card_graphics(
	" _________________________ ",
	"|A      Mall Crawl       A|",
	"|        ______           |",
	"|    ___/RHODES\___  o    |",
	"|   |   |PLAZA!|   | -\   |",
	"|   |   |      |   |  /\  |",
	"|Search your deck for any |",
	"|number of cards with the |",
	"|same name and place them |",
	"| into your discard pile. |",
	"|_________________________|"),
	entrance_effect = ["discard_deck(unlimited = True, name = 'SAME')"],
	tags = ['action', 'Zombies'])

they_comin_to_get_u = card(name = "They Comin' To Get ", 
	graphic = card_graphics(
	" _________________________ ",
	"|A They Comin' To Get U  A|",
	"|   ___        ___        |",
	"|  |RIP|      |RIP|   O   |",
	"|  |   |  O/  |   | // \  |",
	"|Play on a base. Ongoing: |",
	"|  On your turn, you may  |",
	"| a minion here from your |",
	"| discard pile instead of |",
	"|     from your hand.     |",
	"|_________________________|"),
	ongoing_effect = ["extra_minion(base = 'self.attach', discard = True)"],
	tags = ['action', 'Zombies'])

not_enough_bullets = card(name = "Not Enough Bullets", 
	graphic = card_graphics(
	" _________________________ ",
	"|A  Not Enough Bullets   A|",
	"|     _                   |",
	'|   /(")\      _O   _O    |',
	"|    <|-r   -    \    \   |",
	"|    / \  O==--< /\   /\  |",
	"|   Place any number of   |",
	"|  minions with the same  |",
	"| name from your discard  |",
	"|   pile into your hand.  |",
	"|_________________________|"),
	entrance_effect = ["recard(unlimited = True, name = 'Same')"],
	tags = ['action', 'Zombies'])

#BASES
the_homeworld = base( name = "The Homeworld",
	graphic = card_graphics(
	" ____________________________ ", 
	"|23     The Homeworld      23|", 
	"|      4      2      1       |", 
	"|                            |", 
	"|After each time a minion is |", 
	"| played here, ites owner may|", 
	"|  play an extra minion of   |", 
	"|      power 3 or less.      |", 
	"|____________________________|",
	"                              "),
	break_point = 23,
	minion_effect = ["extra_minion(played_minion.owner, power = 3)"])
the_mothership = base( name = "The Great Library",
	graphic = card_graphics(
	" ____________________________ ", 
	"|20     The Mothership     20|", 
	"|      4      2      1       |", 
	"|                            |", 
	"|After this base scores, the |", 
	"|winner may return one of his|", 
	"|or her minions of power 3 or|", 
	"|less from here to thier hand|", 
	"|____________________________|",
	"                              "),
	break_point = 20,
	base_effect = ["return(minion, winner)"])

jungle_oasis = base( name = "Jungle Oasis",
	graphic = card_graphics(
	" ____________________________ ", 
	"|12      Jungle Oasis      12|", 
	"|      2      0      0       |", 
	"|                            |", 
	"|                            |", 
	"|                            |", 
	"|                            |", 
	"|                            |", 
	"|____________________________|",
	"                              "),
	break_point = 12)
tar_pits = base( name = "Tar Pits",
	graphic = card_graphics(
	" ____________________________ ", 
	"|16        Tar Pits        16|", 
	"|      4      3      1       |", 
	"|                            |", 
	"|After each time a minion is |", 
	"|destroyed here, place it at |", 
	"|     the bottom of its      |", 
	"|        owners deck.        |", 
	"|____________________________|",
	"                              "),
	break_point = 16,
	destroy_effect = ["distrieve(destroyed_minion, destroyed_minion.owner, bottom = True)"])

ninja_dojo = base( name = "Ninja Dojo",
	graphic = card_graphics(
	" ____________________________ ", 
	"|18       Ninja Dojo       18|", 
	"|      2      3      2       |", 
	"|                            |", 
	"|                            |", 
	"|After this base scores, the |", 
	"|   winner may destroy any   |", 
	"|        one minion.         |", 
	"|____________________________|",
	"                              "),
	break_point = 18,
	base_effect = ["destroy_minion(choose = winner)"])
temple_of_goju = base( name = "Temple of Goju",
	graphic = card_graphics(
	" ____________________________ ", 
	"|18     Temple of Goju     18|", 
	"|       4      2      1      |", 
	"|                            |",  
	"|  After this base scores,   |", 
	"|place each player's highest |", 
	"|  power minion here on the  |", 
	"|bottom of its owner's deck. |",
	"|____________________________|",
	"                              "),
	break_point = 18,
	base_effect = ["for_each(distrieve_minion(highest))"])

the_grey_opal = base( name = "The Grey Opal",
	graphic = card_graphics(
	" ____________________________ ", 
	"|17     The Grey Opal      17|", 
	"|      3      1      1       |", 
	"|After this base scores, all |", 
	"|   players other than the   |", 
	"|  winner may move a minion  |", 
	"|  from here to another base |", 
	"|instead of the discard pile.|", 
	"|____________________________|",
	"                              "),
	break_point = 17,
	base_effect = ["move_minion(!winner)"])
tortuga = base( name = "Tortuga",
	graphic = card_graphics(
	" ____________________________ ", 
	"|21        Tortuga         21|", 
	"|      4      3      2       |", 
	"|                            |", 
	"|                            |", 
	"| The runner up may move one |", 
	"|of his or her minions to the|", 
	"|base that replaces this base|", 
	"|____________________________|",
	"                              "),
	break_point = 21,
	base_effect = ["move_minion(runner_up, choose = True, replace_base)"])

factory_436_1337 = base( name = "Factory 436-1337",
	graphic = card_graphics(
	" ____________________________ ", 
	"|22    Factory 436-1337    22|", 
	"|       2      2      1      |", 
	"|                            |", 
	"|                            |", 
	"| When this base scores, the |", 
	"|winner gains 1 VP for every |", 
	"|5 power that player has here|", 
	"|____________________________|",
	"                              "),
	break_point = 22,
	base_effect = ["victory(winner, power/5)"])
the_central_brain = base( name = "The Central Brain",
	graphic = card_graphics(
	" ____________________________ ", 
	"|19   The Central Brain    19|", 
	"|      4      2      1       |", 
	"|                            |", 
	"|                            |", 
	"|                            |", 
	"|    Each minion here has    |", 
	"|         +1 power.          |", 
	"|____________________________|",
	"                              "),
	break_point = 19,
	minion_effect = ["minion.ongoing_power = ongoing_power + 1"])

cave_of_shinies = base( name = "Cave of Shinies",
	graphic = card_graphics(
	" ____________________________ ", 
	"|23    Cave of Shinies     23|", 
	"|      4      2      1       |", 
	"|                            |", 
	"|                            |", 
	"|After each time a minion is |", 
	"|  detroyed here, its owner  |", 
	"|        gains 1 VP.         |", 
	"|____________________________|",
	"                              "),
	break_point = 23,
	destroy_effect = ["victory(1, destroyed_minion.owner)"])
mushroom_kingdom = base( name = "Mushroom Kingdom",
	graphic = card_graphics(
	" ____________________________ ", 
	"|20    Mushroom Kingdom    20|", 
	"|       4      2      1      |", 
	"|                            |",  
	"|    At the start of each    |", 
	"| player's turn, that player |", 
	"|may move one other player's |", 
	"|minion from any base to here|",
	"|____________________________|",
	"                              "),
	break_point = 20,
	ongoing_effect = ["move_minion(current_player, any = True, choose = True)"])

school_of_wizardry = base( name = "School of Wizardry",
	graphic = card_graphics(
	" ____________________________ ", 
	"|20   School of Wizardry   20|", 
	"|      4      2      1       |", 
	"|After this base scores, the |", 
	"|  winner looks at the top   |", 
	"|  cards of the base deck,   |", 
	"|chooses one to replace this |", 
	"|base, and returns the others|", 
	"|____________________________|",
	"                              "),
	break_point = 20,
	base_effect = ["replace_base(look = 3, winner)"])
the_great_library = base( name = "The Great Library",
	graphic = card_graphics(
	" ____________________________ ", 
	"|22   The Great Library    22|", 
	"|      4      2      1       |", 
	"|                            |", 
	"|                            |", 
	"|After this base scores, all |", 
	"| players with minions here  |", 
	"|     may draw one card.     |", 
	"|____________________________|",
	"                              "),
	break_point = 22,
	base_effect = ["players_draw_card('optional')"])

evans_city_cemetery = base( name = "Evans City Cemetery",
	graphic = card_graphics(
	" ____________________________ ", 
	"|20  Evans City Cemetery   20|", 
	"|      5      3      1       |", 
	"|                            |", 
	"|                            |", 
	"|After this base scores, the |", 
	"| winner discards his or her |", 
	"| hand and draws five cards. |", 
	"|____________________________|",
	"                              "),
	break_point = 20,
	base_effect = ["winner.discard_hand()", "winner.draw_hand()"])
rhodes_plaza_mall = base( name = "Rhodes Plaza Mall",
	graphic = card_graphics(
	" ____________________________ ", 
	"|24   Rhodes Plaza Mall    24|", 
	"|                            |", 
	"|      0      0      0       |", 
	"|                            |", 
	"|When this base scores, each |", 
	"| player gains 1 VP for each |", 
	"|minion that player has here.|", 
	"|____________________________|",
	"                              "),
	break_point = 24,
	base_effect = ["for_each(victory(player, num_minions))"])


#SmashUp
#Decks
#Module

#Deck lists to be used in play
#CORE SET
aliens = [collector1, collector2, collector3, collector4, scout1, scout2, scout3, invader1, invader2, supreme_overlord, beam_up1, beam_up2, disintegrator1, disintegrator2, abduction, crop_circles, probe, jammed_signal, terraforming, invasion]
dinosaurs = [war_raptor1, war_raptor2, war_raptor3, war_raptor4, armored_stego1, armored_stego2, armored_stego3, lazertops1, lazertops2, king_rex, augmentation1, augmentation2, howl1, howl2, natural_selection, rampage, survival_of_the_fittest, tooth_and_claw_and_guns, upgrade, wildlife_preserve]
ninjas = [ninja_alcolyte1, ninja_alcolyte2, ninja_alcolyte3, ninja_alcolyte4, shinobi1, shinobi2, shinobi3, tiger_assassin1, tiger_assassin2, ninja_master, assassinaion, disguise, hidden_ninja, infiltrate1, infiltrate2, poison, seeing_stars1, seeing_stars2, smoke_bomb, way_of_deception]
pirates = [first_mate1, first_mate2, first_mate3, first_mate4, saucy_wench1, saucy_wench2, saucy_wench3, buccaneer1, buccaneer2, pirate_king, broadside1, broadside2, cannon, dinghy1, dinghy2, full_sail, powderkeg, sea_dogs, shangai, swashbuckling]
robots = [zapbot1, zapbot2, zapbot3, zapbot4, hoverbot1, hoverbot2, hoverbot3, microbot_reclaimer1, microbot_reclaimer2, microbot_guard1, microbot_guard2, microbot_fixer1, microbot_fixer2, microbot_archive, microbot_alpha, warbot1, warbot2, nukebot, tech_center1, tech_center2]
tricksters = [gremlin1, gremlin2, gremlin3, gremlin4, gnome1, gnome2, gnome3, brownie1, brownie2, leprechaun, block_the_path, disenchant1, disenchant2, enshrouding_mist1, enshrouding_mist2, flame_trap, hideout, mark_of_sleep, pay_the_piper, take_the_shinies]
wizards = [neophyte1, neophyte2, neophyte3, neophyte4, enchantress1, enchantress2, enchantress3, chronomage1, chronomage2, archmage, mass_enchantment, mystic_studies1, mystic_studies2, portal, sacrifice, scry, summon1, summon2, time_loop, winds_of_change]
zombies = [walker1, walker2, walker3, walker4, tenacious_z1, tenacious_z2, tenacious_z3, grave_digger1, grave_digger2, zombie_lord, they_keep_coming1, they_keep_coming2, grave_robbing1, grave_robbing2, overrun, lend_a_hand, outbreak, mall_crawl, they_comin_to_get_u, not_enough_bullets]
core_factions = [aliens, dinosaurs, ninjas, pirates, robots, tricksters, wizards, zombies]
core_bases = [the_homeworld, the_mothership, jungle_oasis, tar_pits, ninja_dojo, temple_of_goju, the_grey_opal, tortuga, factory_436_1337, the_central_brain, cave_of_shinies, mushroom_kingdom, school_of_wizardry, the_great_library, evans_city_cemetery, rhodes_plaza_mall]
#SCIENCE FICTION DOUBLE FEATURE
cyborg_apes = ["Furious George", "Furious George", "Furious George", "Furious George", "Baboom", "Baboom", "Baboom", "Clyde 2.0", "Clyde 2.0", "Cyberback", "Cyberevolution", "Cyberevolution", "Flying Monkey", "Going Bananas", "Juiced Up", "Missing Uplink", "Monkey on Your Back", "Monkey See, Monkey Do", "Shielding", "Shielding"]
shapeshifters = ["Copycat", "Copycat", "Copycat", "Copycat", "Mimic", "Mimic", "Mimic", "G.E.L.F.", "G.E.L.F.", "Doppelganger", "... Really?", "Bacta the Future", "Cellular Bonding", "Genetic Shift", "Genetic Shift", "Mitosis", "Shell Game", "Splice as Nice", "Transmogrify", "Transmogrify"]
super_spies = ["Spy", "Spy", "Spy", "Spy", "Operative", "Operative", "Operative", "Mole", "Mole", "Secret Agent", "Discards Are Forever", "For My Eyes Only", "For My Eyes Only", "From Q With Love", "Live and Let Chum", "Mindraker", "Permit to Kill", "The Base Is Not Enough", "The Spy Who Ditched Me", "The Spy Who Ditched Me"]
time_travelers = ["Jumper", "Jumper", "Jumper", "Jumper", "Time Raider", "Time Raider", "Time Raider", "Repeater Perfect", "Repeater Perfect", "Doctor When", "1.21 Gigawatts", "Do Over", "Do Over", "Into the Time Slip", "Into the Time Slip", "It is Astounding", "Statis Field", "Time is Fleeting", "Time Walk", "Wormhole"]
#IT'S YOUR FAULT
dragons = ["Hatchling", "Hatchling", "Hatchling", "Hatchling", "Imperial Dragon", "Imperial Dragon", "Imperial Dragon", "Wyvern", "Wyvern", "Great Wyrm", "Bring Down the Walls", "Bring Down the Walls", "Burn It Down", "Dangerous Ground", "Dragon Lands", "Flank Attack", "Intimidating Presence", "Raze", "Ruins", "Ruins"]
mythic_greeks = ["Argonaut", "Argonaut", "Argonaut", "Argonaut", "Spartan", "Spartan", "Spartan", "Jason", "Heracles", "Odysseus", "Favor of Aphrodite", "Favor of Apollo", "Favor of Ares", "Favor of Athena", "Favor of Dionysus", "Favor of Hades", "Favor of Hera", "Favor of Hermes", "Favor of Poseiden", "Favor of Zeus"]
sharks = ["Mako", "Mako", "Mako", "Mako", "Hammerhead", "Hammerhead", "Hammerhead", "Great White", "Great White", "Megalodon", "Air Jaws", "Blood in the Water", "Blood in the Water", "Chum", "Dangerous Waters", "Feeding Frenzy", "Freakin' Laser Beam", "Torn Apart", "Week of Sharks", "Week of Sharks"]
superheroes = ["Mild Mannered Citizen", "Mild Mannered Citizen", "Mild Mannered Citizen", "Mild Mannered Citizen", "Mild Mannered Citizen", "The Burst", "Mind Lady", "Captain Amazing", "Awesome Guy", "Expanded Power", "Golden Age", "Golden Age", "Justice Friends", "Justice Friends", "My Only Weakness", "Not Really Dead", "Not Really Dead", "Radioactive Exposure", "Secret Base", "Sidekick"]
tornados = ["Dust Devil", "Dust Devil", "Dust Devil", "Dust Devil", "Twister", "Twister", "Twister", "Cyclone", "Cyclone", "Monster Tornado", "Carried Away", "Carried Away", "Gone with the Wind", "Not in Kansas", "Over the Rainbow", "Picked Up", "Ripped Off", "Trade Winds", "Trade Winds", "Whirlwinds"]

all_factions = [aliens, dinosaurs, ninjas, pirates, robots, tricksters, wizards, zombies, cyborg_apes, shapeshifters, super_spies, time_travelers, dragons, mythic_greeks, sharks, superheroes, tornados]

#Master dictionaries for acessing lists
Master = {'aliens' : aliens, 'dinosaurs' : dinosaurs, 'ninjas': ninjas, 'pirates': pirates, 'robots': robots, 'tricksters': tricksters, 'wizards': wizards, 'zombies': zombies}


#Graphics
#Processing
#Module

base_graphics = 10

def construct_playfield():
	ordered_base_list  = [[], [], [], [], []]
	constructed_play_field = ["", "", "", "", "", "", "", "", "", "", "", "", "", ""]

	for base in range(len(play)):
		for player in range(len(play[base])):
			for card in range(len(play[base][player])):
				if card  == 0:
					ordered_base_list[base].append(play[base][player][card].owner.name + ":")
				if play[base][player][card].power:
					ordered_base_list[base].append(str(card + 1) + ". " + play[base][player][card].name + " (" + str(play[base][player][card].power) + ")")
				else:
					ordered_base_list[base].append(str(card + 1) + ". " + play[base][player][card].name + " (A)")
				if card == (len(play[base][player]) - 1):
					ordered_base_list[base].append(" ")
	
	line = 0
	for base_1, base_2, base_3, base_4, base_5 in zip_longest(ordered_base_list[0], ordered_base_list[1], ordered_base_list[2], ordered_base_list[3], ordered_base_list[4], fillvalue = ''):
		constructed_play_field[line] = constructed_play_field[line] + base_1.ljust(35)
		constructed_play_field[line] = constructed_play_field[line] + base_2.ljust(35)
		constructed_play_field[line] = constructed_play_field[line] + base_3.ljust(35)
		constructed_play_field[line] = constructed_play_field[line] + base_4.ljust(35)
		constructed_play_field[line] = constructed_play_field[line] + base_5.ljust(31)
		line = line + 1

	return constructed_play_field

def draw_logo():
	#Draws the Smash Up Logo
	print("   _____ __  ______   _____ __  __   __  ______  __  _    __   ____       ___     _____")
	print("  / ___//  |/  /   | / ___// / / /  / / / / __ \/ / | |  / /  / __ \     <  /    |__  /")
	print("  \__ \/ /|_/ / /| | \__ \/ /_/ /  / / / / /_/ / /  | | / /  / / / /     / /      /_ < ")
	print(" ___/ / /  / / ___ |___/ / __  /  / /_/ / ____/_/   | |/ /  / /_/ /     / /     ___/ / ")
	print("/____/_/  /_/_/  |_/____/_/ /_/   \____/_/   (_)    |___/   \____(_)   /_(_)   /____/  ")

#  _    __   ____       ___     _____
# | |  / /  / __ \     <  /    |__  /
# | | / /  / / / /     / /      /_ < 
# | |/ /  / /_/ /     / /     ___/ / 
# |___/   \____(_)   /_(_)   /____/  

def flip():
	os.system('cls')
	draw_screen()

def draw_screen():
	#Creates the playfield
	play_field = construct_playfield()
	#Draws the logo
	draw_logo()
	
	#Draws the bases
	for j in range(base_graphics):
		print(" ", end = "")
		i = 0
		for base in base_play:
			i = i + 1
			executable = "print(base.graphic.line_" + str(j + 1) + ", end = '')"
			exec(executable)
			if i != len(base_play):
				print("     ", end = "")
		print("")
	
	#Draws the play field
	for i in range(len(play_field)):
		print(" " + play_field[i])
	print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
	print("")

#Actual
#Processing
#Module

if __name__ == '__main__':
	player_one, player_two, player_three, player_four = init_game()
	current_player = player_one
	
	###FOR TESTING
	#play = [[[], [], [], []], [[], [], [], []], [[], [], [], []], [[], [], [], []], [[], [], [], []]]
	#for base in range(len(play)):
	#	base_play.append(core_bases[random.randint(0, len(core_bases)-1)])
	#player_one = player('aliens', 'aliens', "Player One", number = 1)
	#player_two = player('aliens', 'aliens', "Player Two", number = 2)
	#player_three = player('aliens', 'aliens',"Player Three", number = 3)
	#player_four = player('aliens', 'aliens', "Player Four", number = 4)
	#
	#player_one.create_deck()
	#player_one.shuffle_deck()
	#player_one.draw_hand()
	#
	#player_two.create_deck()
	#player_two.shuffle_deck()
	#player_two.draw_hand()
	#
	#player_three.create_deck()
	#player_three.shuffle_deck()
	#player_three.draw_hand()
	#
	#player_four.create_deck()
	#player_four.shuffle_deck()
	#player_four.draw_hand()
	#current_player = player_one
	#flip()
	###
	flip()
	handle_input_shell()
	print("Thanks for playing Smash-Up!!!")
