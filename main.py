import random
import time

from actors import *

def main():
	prin_header()
	game_loop()


def prin_header():
	print("--------------------------")
	print("-------WIZARD GAME--------")
	print("--------------------------")
	print("--------------------------")
 


def game_loop():

	mob_dic = {
		"dragon": 100,
		"Evil": 50,
		"Bully": 150,
	}
	smalls = {
		"turtle": 6,
		"bunny": 10,
	}
	epic_mobs = {
		"FuckerCrab": 200,
		"AssRaper": 300,
	}

	creatures: list = Creature.gen_creature(mob_dic) + SmallAnimal.gen_creature(smalls) + EpicCreature.gen_creature(epic_mobs)
	hero = Wizard("Gendolf", 85)
	# print(creatures)
	# check_monster: EpicCreature = creatures[5]
	# print(check_monster.name)
	# print(check_monster.id)
	while True:

		active_creature: Creature = random.choice(creatures)
		print("A {} of lvl {} has appeared from dark and foggy forest".format(active_creature.name, active_creature.lvl))

		cmd = input("Do you [a]ttack , [r]un away or [l]ook around?\n> ")
		match cmd:
			case "a":
				if hero.attack(active_creature):
					creatures.remove(active_creature)
				else:
					print("The wizard runs and hides , takes time to recover...")
					time.sleep(5)
					print(f"The wizard {hero.name} returns revitalized!")
			case "r":
				print("The wizard runs")
			case "l":
				print("The Wizard takes in the surrounding and sees:")
				[print(f"A {c.name} of lvl {c.lvl}") for c in creatures]
			case _:
				print("Exiting the game...Bye")
				break

		if not creatures:
			answer = input("All creatures have been defeated! congrats, wanna play again ? y or n")
			if answer not in "y":
				print("bye bye")
				break


if __name__ == '__main__':
    main()


