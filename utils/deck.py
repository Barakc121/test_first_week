# from typing import List, Dict
import random





RANKS = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
SUITES = ['h', 'c', 'd', 's']
CARD_VALUES = {
    "2":2,"3":3,"4":4,"5":5,"6":6
    ,"7":7,"8":8,"9":9,"10":10,
    "j":11,"q":12,"k":13,"as":14
}


def create_card(rank: str, suite: str) -> dict:
  
    value = CARD_VALUES.get(rank)
    return {
        "rank": rank,
        "suite": suite,
        "value": value
    }


def create_deck() -> list[dict]:
    
    deck = []
    for suite in SUITES:
        for rank in RANKS:
            card = create_card(rank, suite)
            deck.append(card)
    return deck


def compare_cards(p1_card: dict, p2_card: dict) -> str:
    p1_value = p1_card.get("value")
    p2_value = p2_card.get("value")

    if p1_value > p2_value:
        return "P1"
    elif p2_value > p1_value:
        return "P2"
    else:
        return "TIE"




def shuffle(deck: list[dict]) -> list[dict]:
    for i in range(1000):
        result_card=deck
    
        a=random.randint(0,51)
        b=random.randint(0,51)

        result_card[a],result_card[b]==result_card[b],result_card[a]


deck= create_deck()
print(deck)
print(shuffle(deck))

