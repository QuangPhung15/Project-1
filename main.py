#This project05 is done by Quang and Hoa

#import library, module

#define rolling 3 dice function
	#loop 3 times
		#random number from 1 to (input dice's side)

#define a re-roll dice function
	#ask players if they want to re-roll (and also which dice they want to re-roll) or not
	#while loop to make sure player only type '1', '2', '3', or hit 'Enter/Return' button
	#if players choose dice 1
		#random a number from 1 to (the number of dice's side)
	#if players choose dice 2
		#random a number from 1 to (the number of dice's side)
	#if players choose dice 3
		#random a number from 1 to (the number of dice's side)
	
#define a calculated point after 3 rolls and also re-roll function for each turn

#define player turn function
	#call rolling dice function
	#print out the point after 3 rolls
	#call re-roll dice function
	#print 3 random numbers after re-roll
	#calculate total point (calling calculating point function)
	#print total
	#end the turn

#define a calculating score function after each round
	#compare 2 total points and decide the winner per round

#define round function
	#call player turn function 2 times
	#compare 2 total points and decide the winner per round

#define tie-break round if, after the last round, 2 players still have the same score
	#while the final scores of 2 players are equal
		#call round function

#define the winner deciding function
	#if the player1's final score > player2's
		#print "player 1 is the winner"
	#else
		#print "player 2 is the winner"
	
#define game function
	#loop round function call according to the player's round input
	#call tie-break round function
	#call winner deciding function

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

#print game's rule
print(intro)

#input players' names

#input round number

#input dice's side

#call game function