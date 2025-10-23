from utils.deck import create_deck, shuffle, compare_cards


def create_player(name: str="AI") -> dict:
   
    return {
        "name": name,
        "hand": [],     
        "card_won": []  
    }


def init_game() -> dict:
    
    player1 = create_player("barak")
    player2 = create_player("mark")
    
    deck = create_deck()
    shuffled_deck = shuffle(deck)
    
    player1["hand"] = shuffled_deck[::2]  
    player2["hand"] = shuffled_deck[1::2] 
    
    return {
        "player1": player1,
        "player2": player2
    }

def play_round(p1: dict, p2: dict):
   
    
    if not p1["hand"] or not p2["hand"]:
        return 
    
    
    p1_card = p1["hand"].pop(0)
    p2_card = p2["hand"].pop(0)
    
    winner = compare_cards(p1_card, p2_card)
    
    if winner == "P1":
        p1["card_won"].append(p1_card)
        p1["card_won"].append(p2_card)
    elif winner == "P2":
        p2["card_won"].append(p1_card)
        p2["card_won"].append(p2_card)
    elif winner == "TIE":
        pass


print(play_round(dict,dict))