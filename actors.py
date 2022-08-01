from typing import List, Tuple, Dict, Union, Any, Literal
from random import randint, choice

class Creature:
	id = 0
	'''USE CLASSMETHOD FOR OBJECT GENERATION'''
	@classmethod
	def gen_creature(cls, dic: dict) -> list[object]:
		return [cls(key, value) for key, value in dic.items()]

	def __init__(self, name: str, lvl: int):
		self.name: str = name
		self.lvl: int = lvl
		Creature.id += 1
		self.id: int = Creature.id

	def __repr__(self):
		'''to return a machine readable representation of a type. instead of objects'''
		return "Creature:{} of lvl {}".format(self.name, self.lvl)

	def get_defensive_roll(self):
		return randint(1, 12) * self.lvl


class Wizard(Creature):

	def __init__(self, name: str, lvl: int):
		super().__init__(name, lvl)
		self.id = 0
		print(f"{self.name} has {self.id} id")

	def attack(self, creature: Creature):
		print(f"The wizard {self.name} attacks {creature.name}!")

		my_roll = self.get_defensive_roll()
		creature_roll = creature.get_defensive_roll()

		print("Your roll {}...".format(my_roll))
		print("{} rolls {}...".format(creature.name, creature_roll))
		'''MATCH_CASE METHOD INSTEAD OF if elif else'''
		match my_roll >= creature_roll:
			case True:
				print("The Wizard has handily triumphed over {}".format(creature.name))
				return True
			case _:
				print("The wizard has been defeated!")
				return False


class SmallAnimal(Creature):
	def get_defensive_roll(self):
		new_roll = super().get_defensive_roll()
		return new_roll * 2


class EpicCreature(Creature):
	@classmethod
	def gen_creature(cls, dic: dict) -> list[object]:
		return [cls(key, value, True, 20) for key, value in dic.items()]

	def __init__(self, name: str, lvl: int, breath_fire: bool, scaliness: int):
		super().__init__(name, lvl)
		self.breath_fire = breath_fire
		self.scaliness = scaliness

	def get_defensive_roll(self):
		new_roll = super().get_defensive_roll()
		fire_modifier = 5 if self.breath_fire else 2
		scale_modifier = self.scaliness // 10
		return  new_roll * fire_modifier * scale_modifier

