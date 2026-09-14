#Win Lose or Tie
def game_outcome(your_score,opponent_score):
    if your_score>opponent_score:
        return "You win!"
    elif opponent_score>your_score:
        return "You lose!"
    else:
        return "Tie game!"
    
def main():
    result = game_outcome(90,20)
    print(result)
    
    result = game_outcome(80,100)
    print(result)
    
    result = game_outcome(100,100)
    print(result)
main()