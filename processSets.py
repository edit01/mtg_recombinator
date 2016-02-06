#!/usr/bin/bash
#Parse through "All Sets-2013-11-21.txt", and create a CSV to import

import re
import argparse

#Scheme: Cardname/Type:Scheme/CardText/Set
#Creature: Cardname/CC/Type:Creature -- Human Knight/PowerToughness/CardText/Set
#Artifact: Cardname/CC/Type:Artifact/CardText/Set
#Enchantment: Cardname/CC/Type:Enchantment/CardText/Set
class Card():

	cardTypes ={ 
		'Creature' : ['Creature '], 
		'Scheme' : ['Scheme', 'Ongoing Scheme'], 
		'Land' : ['Land'],
		'Sorcery' : ['Sorcery', 'Tribal Sorcery'],
		'Artifact' : ['Artifact'],
		'Enchantment' : ['Enchantment'],
		'Instant' : ['Instant'],
		'Vanguard' : ['Vanguard'],
		'Plane' : ['Plane'],
		'Plainswalker' : ['Plainswalker'],
		'Phenomenon' : ['Phenomenon']
	}
	def __init__(self, data):
		self.data = data
		self.cardName = data[0]
		self.sets = data[-1]
		self.primaryType = self.inspectCardType()#Inspect card if importing from txt file		
		print self.cardName, self.primaryType
		
	def inspectCardType(self):#Inspect/Determine the card type
		type = None
		for x in self.data[1:3]:#Loop through card attr
			for k, v in self.cardTypes.iteritems():#Loop through regex
				mo = re.search(k, x)
				if(mo != None):
					type = (mo.group(0), self.data.index(x) ,str(x))  
		
#		print type
		return type

	def inspectCardSet(self):
		return None #Inspect/Determine all of the sets	

def parseSetFile(file):	
	try:
		fh = open(file, 'rU')
	except IOError:
		print file, "does not exist"
	else:	
		allCards = []
		card = []
		for line in fh:#Isolate every card
			if line == '\n' and card != []:#Prevent EOF 2x \n		
				allCards.append(card)#Append cur card to master list
				card = []#Reset for next card			
			else:
				line = line.rstrip()
				if(line != ''):
					card.append(line)#for everyline, append to card
		fh.close()
		return allCards
	return None

parser = argparse.ArgumentParser(description='Process some arguments')
parser.add_argument("file")
args = parser.parse_args()

results = parseSetFile(args.file)
cardlist = []
[cardlist.append(Card(x)) for x in results]#Create all the card objects

#for x in results:
#	cardlist.append(Card(x))
	#print x
#testcard = Card(results[9])
#print testcard.cardName, testcard.sets
#testcard.inspectCardType()

#Use psycopg2 module for postGreSQL interface
#Read in FULL card list, update card database as necessary
#Drop all existing records? and recreating all cards?
#Read in new card list
#Retrieve results
