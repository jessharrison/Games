"""This program is a game where the user challenges the computer. The computer will roll dice and find the sum, then ask the user to guess the number. If the user chooses the correct number, they will score a point."""

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
  number_of_dice = int(raw_input("How many dice do you want to roll? "))
  number_of_sides = int(raw_input("How many sides does each die have? "))
  max_value = number_of_sides * number_of_dice
  print "The maximum possible value is: %d" % max_value
  
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
      print "The rolls were %r" % rolls
      total_roll = sum(rolls)
      print "The sum was %d" % total_roll
      
      if guess == total_roll:
        print "You win!"
        score[0] += 1
      else:
        print "The computer won. Try again!"
        score[1] += 1
      
    print score
  
    play_again = raw_input("Do you want to play again? Y or N? \n ... ")
    if play_again == "N":
      print "Good game!"
      play = False
                    
  
play_game()