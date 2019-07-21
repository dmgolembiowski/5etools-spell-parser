import re
from slugify import slugify
from helper import *

class Book:
	'''
	A book contains many spells in an orderly fashion.
	'''
	def __init__(self):
		self.spells = {}
		self.name = None
		self.acronym = None
		self.slug = None

	def add(self, Spell):
		self.spells[Spell.slug] = Spell
	
	def add_name(self, acronym):
		# simply add an acronym
		self.acronym = acronym
		# also look up the name
		self.name = book_acronyms[acronym]
		# might as well fix up a slug too
		slug = re.sub(r'([^\s\w/]|_)+', '', self.name)
		slug = slug.lower()
		slug = slugify(slug)
		self.slug = slug
