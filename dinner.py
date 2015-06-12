from sys import exit
import random

def last_game(money):
	print "This is the last game."
	print "You now have %r dollars." % money 
	print "How much do you want to bet?"
	
	choice = raw_input("> ")

	bet = int(choice)
	if bet > money:
		dead("You cannot bet more than you have!")
	elif bet < 0:
		dead("You cannot bet a negative amount!")
	else:
		chance = random.random()
		if chance < 0.5:
			money = money - bet
		else:
			money = money + bet
	
	if money < 0:
		dead("You ran out of money!")
	elif money > 10:
		print "Congratulation! You win, now pay your dinner!"
		exit(0)
	else:
		dead("You have %r dollars, but it is still not enough." % money)

def second_game(money):
	print "This is the second game."
	print "You now have %r dollars." % money 
	print "How much do you want to bet?"
	
	choice = raw_input("> ")

	bet = int(choice)
	if bet > money:
		dead("You cannot bet more than you have!")
	elif bet < 0:
		dead("You cannot bet a negative amount!")
	else:
		chance = random.random()
		if chance < 0.5:
			money = money - bet
		else:
			money = money + bet
	
	if money < 0:
		dead("You ran out of money!")
	else:
		last_game(money)

def first_game():
	print "This is the first game."
	print "You now have 4 dollars."
	print "How much do you want to bet?"
	print "(Enter a number between 0 and 4)"
	
	choice = raw_input("> ")

	bet = int(choice)
	if bet > 4:
		dead("You cannot bet more than you have!")
	elif bet < 0:
		dead("You cannot bet a negative amount!")
	else:
		chance = random.random()
		if chance < 0.5:
			money = 4 - bet
		else:
			money = 4 + bet
	
	if money < 0:
		dead("You ran out of money!")
	else:
		second_game(money)

def dead(why):
	print why, "Loser!"
	exit(0)

def start():
	print "You need 10 dollars to pay your meal."
	print "You only have 4 dollars in your pocket."
	print "You are invited to play three games."
	print "For every win you will double your bet."
	print "If you lose, you will lose your bet."
	print "You have equal chance of winning and losing each game."
	
	print "Do you want to start the game? [Y/N]"

	choice = raw_input("> ")

	if choice == "Y":
		first_game()
	elif choice == "N":
		dead("You will have to wash the dishes for the restaurant until the rest of your life.")
	else:
		dead("As you are not capable of making simple choice, you are not worthy of this game.")


start()

