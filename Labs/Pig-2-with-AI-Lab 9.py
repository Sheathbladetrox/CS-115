# Andrew Chuah, Ronald Estevez
# I pledge my honor that I have abided by the Stevens Honor System
# Lab 9
# 11-08-18

'''
Pig Game
Adapted from Java to Python by Justin Barish,  11/2018

Pig is a game where players take turns rolling 2 dice.

A person's turn lasts until they want to stop rolling.

If at any point during the player's turn they roll a 1,
they lose all points for the round, and their turn is over.

If at any point during the round the player rolls a snake-eye (2 ones),
they lose all of their points in the game, and their turn is over.

Whenever they decide to stop their turn, their round points are
added to their game points.

When a player's game points reach 100, they win.
'''
import random
debug = False

POINTS_TO_WIN = 100
AI_ROUND_TARGET = 20

'''this lab has 2 parts:

Part 1: complete the pig game for two human players.
That is, fill in all of the methods, except for AIWantsRollAgain().
This part is worth 90 points, and due by the end of lab.

Part 2: Add in an AI as the second player, using AIWantsRollAgain().
The AI takes the place of player 2, and will continue rolling until
it reaches its AI_ROUND_TARGET. NOTE: You may need to change some of the
function paramaters (I.E. pass in additional values).
This is worth 10 points, and is due roughly 5 hours after your lab ends
(see canvas for more details)
'''


def wantsContinue(response):
	'''checks if the response a user gives indicates they want to continue'''
	if response=='y':
		return True
	else:
		return False


def wantsPlayAgain():
	'''asks a player if they want to play the game again, uses wantsContinue()'''
	response = input('Would you like to continue? (y or n): ').strip()
	return wantsContinue(response)

def AIWantsRollAgain(scores):
	'''checks if the AI wants to roll again'''
	'''implement in part 2'''
	if scores[-1] >= AI_ROUND_TARGET:
		return 'n'
	else:
		return 'y'

def wantsRollAgain(player,scores):
    '''asks player if they want to roll again, uses wantsContinue().
    For part2, also handles case where player is AI'''
    if player == 1:
        response = input('Would you like to roll again? (y or n): ').strip()
    else:
        response = AIWantsRollAgain(scores)
    return wantsContinue(response)


def main():
	'''This is the main function for the pig game'''
	welcome()
	while True:
		if debug: print('About to enter playGame()')
		playGame()
		if not wantsPlayAgain():
			print('Bye!')
			return

def welcome():
	'''Prints the welcome message for the game.
	We might also print the rules for the game and any other
	information that the user might need to know.'''
	print('Welcome to Pig!')
	print()
	print("""Pig is a game where players take turns rolling 2 dice.

			 A person's turn lasts until they want to stop rolling.

			 If at any point during the player's turn they roll a 1,
			 they lose all points for the round, and their turn is over.

			 If at any point during the round the player rolls a snake-eye (2 ones),
			 they lose all of their points in the game, and their turn is over.

			 Whenever they decide to stop their turn, their round points are
			 added to their game points.

			 When a player's game points reach 100, they win.""")

def printScore(scores):
	'''prints the current game score for each player'''
	print("Player 1's current gamescore is " + str(scores[0]))
	print("Player 2's current gamescore is " + str(scores[1]))


def printWinMessage(winningPlayer, scores):
	print()
	print('***********************Player ' + str(winningPlayer) + ' Won!************************')
	print('***********************Final Score:*************************')
	printScore(scores)

def gameOver(scores):
	'''checks if the game is over
		game is over when either player reaches >= POINTS_TO_WIN.
		Prints the win message for the player who won
		If no one won, just returns false'''
	if scores[0] >= POINTS_TO_WIN:
		printWinMessage(1, scores)
		return True
	elif scores[1] >= POINTS_TO_WIN:
		printWinMessage(2, scores)
		return True
	else:
		return False

def initScores():
	'''initialize the scores to 0'''
	scores = [0,0]
	return scores

def playGame():
	'''Play one game of pig
	Alternates between players, and at the end of a player's turn,
	prints the overall game score for both players'''

	if debug: print('Entering the playGame() function')
	player = 1
	scores = initScores()
	while not gameOver(scores):
		getMove(scores, player)

		if player == 1: player = 2
		else: player = 1
		print()
		print('Current Scores:')
		printScore(scores)


def rollDie():
	'''rolls a single die'''
	return random.randint(1,6)

def rollDice():
	'''grabs the roll for two dice'''
	return [rollDie()] + [rollDie()]

def isSnakeEye(roll):
	'''checks if the roll is a snake-eye'''
	if roll[0]==1 and roll[1]==1:
		return True
	else:
		return False

def hasOne(roll):
	'''checks if the roll has a one in it'''
	if roll[0]==1 and roll[1]!=1:
		return True
	elif roll[1]==1 and roll[0]!=1:
		return True
	else:
		return False


def showRoll(roll):
	''' prints out the roll'''
	print("First roll is: " + str(roll[0]))
	print("First roll is: " + str(roll[1]))

def printPlayerMessage(player):
	print()
	print('--------------------------------------------------------------')
	print('-------------------Player ' + str(player) + '\'s turn----------------------------')
	print('--------------------------------------------------------------')
	print()

def printSnakeEyeMessage(player):
	'''prints the message for when the player rolls a snake eye '''
	print('Player ' + str(player) + ' has rolled a snake eye! All points for this game are lost!' )

def printOnesMessage(player):
	'''prints the message for when the player rolls a one '''
	print('Player ' + str(player) + ' has rolled a one! All points for this round are lost!' )

def printCurrentPlayerScore(scores,player):
	'''print the score for a specific player. Prints their round score
	and their overall game score not including their current round score'''
	print("Player " + str(player) + " round score: " + str(scores[-1]))
	print("Player " + str(player) + " game score: " + str(scores[player - 1]))

def getMove(scores, player):
	'''gets a player's move.
	Before every move, prints the current round score and the game score for the player
	Checks if the player wants to continue, and if they do, rolls dice and appropriately changes scores
	'''
	printPlayerMessage(player)
	roundScore = 0
	while True:
		scores.append(roundScore)
		printCurrentPlayerScore(scores,player)

		if(not wantsRollAgain(player,scores)):
			scores[player-1] += roundScore
			break

		roll = rollDice()
		showRoll(roll)
		if hasOne(roll):
			printOnesMessage(player)
			roundScore = 0
			break;
		elif isSnakeEye(roll):
			printSnakeEyeMessage(player)
			roll = 0
			scores[player-1] = 0
			break;
		else:
			roundScore += roll[0] + roll[1]


if __name__ == '__main__':
    main()
