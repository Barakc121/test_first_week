
from game_logic.game import init_game, play_round

def play_game():
  
    game_state = init_game()
    player1 = game_state.get('player1')
    player2 = game_state.get('player2')
    
    if not player1 or not player2:
        print("error")
        return
        
    print("The game begins")
    print(f"users: {player1["name"]} ו {player2["name"]}")
    print(f"every player play game with{len(player1["hand"])} cards.")
    
    
    round_count = 0
    while player1["hand"] and player2["hand"]:
        round_count += 1
        
        play_round(player1, player2)
    

    p1_score = len(player1["pile_won"])
    p2_score = len(player2["pile_won"])
    
    print("\n==============================")
    print("game over man")
    print(f"total rounds: {round_count}")
    print(f"{player1["name"]} have is{p1_score} cards.")
    print(f"{player2["name"]} have is{p2_score} cards.")
    
    if p1_score > p2_score:
        print(f"the winner is {player1["name"]}! ")
    elif p2_score > p1_score:
        print(f"the winner is{player2["name"]}! ")
    else:
        print("draw!")
    print("==============================")


if __name__ == "__main__":
    play_game()