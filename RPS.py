"""This game allows the user to play Rock, Paper, Scissors 
with the computer. It will keep score as the user plays."""

from random import randint

options = ["rock", "paper", "scissors", "lizard", "spock"]
message = {"tie": "Boring, it's a tie.\n", "won": "You win!\n", "lost": "You lose.\n"}

win_dictionary = {"rock": ["lizard", "scissors"], "paper": ["rock", "spock"], 
              "scissors": ["paper", "lizard"], "spock": ["scissors", "rock"],
              "lizard": ["spock", "paper"]}

def decide_winner(user_choice, computer_choice):
  print "\nThe computer chose: %s" %computer_choice.upper()
  print "You chose: %s\n" %user_choice.upper()
  
  result = ""
  
  if user_choice == computer_choice:
    print message["tie"]
    result = "tie"
  elif computer_choice in win_dictionary[user_choice]:
    print message["won"]
    result = "won"
  else:
    print message["lost"]
    result = "lost"
  
  return result

def play_RPS():
  print "Let the games begin!\n"

  play = True
  score = [0, 0]
  
  while play:
    user_choice = raw_input("Enter your choice:\nROCK, PAPER, SCISSORS, LIZARD, SPOCK... \n... ").lower()
    computer_choice = options[randint(0,4)]
    result = decide_winner(user_choice, computer_choice)
    
    if result == "won":
      score[0] += 1
    elif result == "tie":
      pass
    else:
      score[1] += 1
    
    print "The score is: \nYOU: %d \nCOMPUTER: %d\n" %(score[0],score[1])
    
    play_again = raw_input("Do you want to play again? Y or N? \n ... ")
    if play_again == "Y":
      play = True
    elif play_again == "N" or "n":
      play = False
      print "Good game!"
    else:
      print "The computer did not understand your input."
      pass
  
play_RPS()