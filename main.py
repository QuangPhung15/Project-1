#This project05 is done by Quang and Hoa

#import library, module
from random import *

#define rolling 3 dice function
def roll_3D(sides):
	"""Roll a die 3 times based on the number of sides of the dice, put them into a list, and return the list"""
	dice_list = []
	#loop 3 times
	for i in range(3):
		#random number from 1 to (input dice's side)
		dice = randint(1, sides)
		dice_list.append(dice)
	return dice_list

#define a re-roll dice function
def reRoll(orgList, sides):
	"""Re-roll one of the three die based on the choice of the player and return the new dice list"""
	#ask player if they want to re-roll (and also which dice they want to re-roll) or not
	dice_change = input("Type the dice number ('1', '2', '3') that you want to re-roll or just hit 'Enter/Return' to keep what you have \n>> ")
	#while loop to make sure player only type '1', '2', '3', or hit 'Enter/Return' button
	while dice_change != "1" and dice_change != "2" and dice_change != "3" and dice_change != "":
		print("Please type only '1', '2', '3', or hit 'Enter/Return' button")
		dice_change = input("Type the dice number ('1', '2', '3') that you want to re-roll or just hit 'Enter/Return' to keep what you have \n>> ")
	#if players choose dice 1
	if dice_change == "1":
		#random a number from 1 to (the number of dice's side)
		orgList[0] = randint(1, sides)
	#if players choose dice 2
	elif dice_change == "2":
		#random a number from 1 to (the number of dice's side)
		orgList[1] = randint(1, sides)
	#if players choose dice 3
	elif dice_change == "3":
		#random a number from 1 to (the number of dice's side)
		orgList[2] = randint(1, sides)
	return orgList
	
#define a calculated point after 3 rolls and also re-roll function for each turn
def calPoint(nList):
	"""Calculate the total point of 3 dice after 3 rolls and also re-roll for each turn""" 
	if nList[0] == nList[1] == nList[2]:
		total_point = nList[0] * nList[1] * nList[2]
	elif nList[0] == nList[1]:
		total_point = nList[0] * nList[1] + nList[2]
	elif nList[1] == nList[2]:
		total_point = nList[0] + nList[1] * nList[2]
	elif nList[0] == nList[2]:
		total_point = nList[0] * nList[2] + nList[1]
	else:
		total_point = nList[0] + nList[1] + nList[2]
	return total_point

def pTurn(sides, pName):
	"""Play a player's turn by rolling 3 dice, then ask the player if they want to re-roll, and calculate the point"""
	#call rolling dice function
	orignRoll = roll_3D(sides)
	#print out the point after 3 rolls
	print(pName + "'s dice points after 3 rolls are " + str(orignRoll[0]) + ", " + str(orignRoll[1]) + ", and " + str(orignRoll[2]) + "\n")
	#call re-roll dice function
	newRoll = reRoll(orignRoll, sides)
	#print 3 random numbers after re-roll
	print(pName + "'s dice points after re-roll are " + str(newRoll[0]) + ", " + str(newRoll[1]) + ", and " + str(newRoll[2]) + "\n")
	#calculate total point (calling calculating point function)
	pPoint = calPoint(newRoll)
	#print total
	print(pName + "'s total point is " + str(pPoint))
	#end the turn
	return pPoint

#define a calculating score function after each round
def calScore(sides, pName1, pName2, pPoint1, pPoint2, pScore1, pScore2):
	"""Calculating the scores of the player after each round by comparing the players' points"""
	#compare 2 total points per round
	if pPoint1 > pPoint2:
		pScore1 += 1
	elif pPoint1 < pPoint2:
		pScore2 += 1
	return pScore1, pScore2

#define round function
def pRound(sides, pName1, pName2, pScore1, pScore2):
	"""Play a whole round for each of the players and decide who is the winner of the round"""
	#call player turn function 2 times for 2 players
	pPoint1 = pTurn(sides, pName1)
	pPoint2 = pTurn(sides, pName2)
	#compare 2 total points and decide the winner per round
	if pPoint1 > pPoint2:
		print("Player 1 is the winner of this round \n")
	elif pPoint1 < pPoint2:
		print("Player 2 is the winner of this round \n")
	else:
		print("Player 1 and Player 2 are draw this round. No one gets a point! \n")
	#call calculating players' scores function
	pScore1, pScore2 = calScore(sides, pName1, pName2, pPoint1, pPoint2, pScore1, pScore2)
	return pScore1, pScore2
	
#define tie-break round if, after the last round, 2 players still have the same score
	#while the final scores of 2 players are equal
		#call round function

#define the winner deciding function
def decide_winner(pScore1, pScore2):
	"""Decide the winner by comparing 2 players' scores"""
	#if the player1's final score > player2's
	if pScore1 > pScore2:
		#print "player 1 is the winner"
		print("Player 1 is the final winner! Congratulation!")
	#else
	elif pScore1 < pScore2:
		#print "player 2 is the winner"
		print("Player 2 is the final winner! Congratulation!")
	else:
		print("We will need a tie-break round to decide who is the winner of the game.")
	
#define game function
def pGame(sides, pName1, pName2, pScore1, pScore2, rounds):
	"""Play the entire game"""
	#loop round function call according to the player's round input
	for i in range(rounds):
		pScore1, pScore2 = pRound(sides, pName1, pName2, pScore1, pScore2)
		print("Round " + str(i + 1) + " : P1 - P2 : " + str(pScore1) + " - " + str(pScore2) + "\n")
	#call winner deciding function
	decide_winner(pScore1, pScore2)
	#call tie-break round function
	
#define any variables that need to use
intro = """Now we're going to play TOTALITY:
Players will choose a number of rounds to play.

Player 1 will roll 3 dice.
They are trying to get the highest total possible on the three dice,
but dice with the same value MUST be multiplied together!
Example: 332 --> 3 * 3 + 2 --> score of 11

After rolling 3 dice, Player 1 has the option to end their turn
or re-roll 1 of the dice in an attempt to get a higher score.

Player 2 then gets a turn to do the same thing.
After player 2 has finished, the final scores are compared to determine the winner.
The player with a higher score receives 1 point for the round.

Points are totaled after the final round and the winner will be declared.
.............................................................................
Now let's start the game \n"""

player_score1 = 0
player_score2 = 0

#print game's rule
print(intro)

#input players' names
player_name1 = input("What is the Player 1 name ? \n>> ")
player_name2 = input("What is the Player 2 name ? \n>> ")

#input round number
game_round = int(input("What is the total number of rounds you want to play? \n>> "))

#input dice's side
dice_sides = int(input("What is the total number of sides do you want your dice will have? \n>> "))

#call game function
game = pGame(dice_sides, player_name1, player_name2, player_score1, player_score2, game_round)