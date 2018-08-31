"""This is a game where the user challenges the computer. 
The computer will roll dice, find the sum, then ask the 
user to guess the sum. If the user chooses the 
correct sum, they will score a point. Otherwise,
the computer scores."""

from random import randint
from time import sleep

def get_user_guess():
  guess = int(raw_input("The dice have been rolled. Guess the sum. \n... "))
  return guess

def roll_dice(number_of_dice, number_of_sides):
  """Takes as input the number of sides on the dice, as integers."""
  score = [0,0]
  rolls = []
  for x in range(0, number_of_dice):
    roll = randint(1, number_of_sides)
    rolls.append(roll)
  return rolls

def play_game():
  print "The game has begun! \n"
  while True:
    try:
      number_of_dice = int(raw_input("How many dice do you want to roll? "))
    except ValueError:
      print "That was not an integer. Try again."
      continue
    else:
      break

  while True:
    try:
      number_of_sides = int(raw_input("How many sides does each die have? "))
    except ValueError:
      print "That was not an integer. Try again."
      continue
    else:
      break

  max_value = number_of_sides * number_of_dice
  print "\nThe maximum possible value is: %d" % max_value
  
  score = [0, 0]
  play = True
  
  while play:
    guess = get_user_guess()
    
    if guess > max_value:
      print "Your guess is too high."
    if guess < 2:
      print "Your guess must be more than the number of dice being rolled."
    else:
      rolls = roll_dice(number_of_dice, number_of_sides)
      print "Rolling..."
      sleep(number_of_dice)
      print "Here are the rolls: %r" % rolls
      total_roll = sum(rolls)
      print "The sum is %d.\n" % total_roll
      
      sleep(2)
      if guess == total_roll:
        print "You win!\n"
        score[0] += 1
      else:
        print "The computer won."
        score[1] += 1
      
    print "The score is now: \n YOU: %d \n COMPUTER: %d \n" %(score[0], score[1])
  
    play_again = raw_input("Do you want to play again? Y or N? \n ... ").upper()
    if play_again == "N":
      print "Good game!"
      play = False
                    
  
play_game()