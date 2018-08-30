"""This game allows the user to play Rock, Paper, Scissors 
with the computer. It will keep score as the user plays."""

from random import randint

options = ["ROCK", "PAPER", "SCISSORS"]
message = {"tie": "Boring, it's a tie.", "won": "Yay, you win!", 
"lost": "Too bad, you lose."}

def decide_winner(user_choice, computer_choice):
  print "The computer chose: %s" %computer_choice
  
  result = "won"
  
  if user_choice == computer_choice:
    print message["tie"]
    result = "tie"
  elif user_choice == options[0] and computer_choice == options[2]:
    print message["won"]
  elif user_choice == options[1] and computer_choice == options[0]:
    print message["won"]
  elif user_choice == options[2]  and computer_choice == options[1]:
    print message["won"]
  else:
    print message["lost"]
    result = "lost"
  
  return result

def play_RPS():
  play = True
  score = [0, 0]
  
  while play:
    user_choice = raw_input("Enter rock, paper, or scissors... \n").upper()
    computer_choice = options[randint(0,2)]
    result = decide_winner(user_choice, computer_choice)
    
    if result == "won":
    	score[0] += 1
    elif result == "tie":
    	pass
    else:
    	score[1] += 1

    print "The score is: %r" %score

    play_again = raw_input("Do you want to play again? Y or N? \n ... ").upper()
    
    if play_again == "Y":
      play = True
    elif play_again == "N":
      play = False
      print "Good game!"
    else:
    	print "The computer did not understand your input. It chooses to play again."
      pass
  
play_RPS()