
from typing import List, Dict
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

def create_deck() -> List[Dict]:
    
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




def shuffle(deck: List[Dict]) -> List[Dict]:
    
    random.shuffle(deck)
    return deck































# deck.py

from typing import List, Dict
import random

def create_card(rank: str, suite: str) -> dict:
    """
    יוצר קלף במבנה מילון.
    חתימה: create_card(rank:str, suite:str) -> dict
    """
    # ערכים מספריים לדרגות הקלפים: 2-10=דרגה, J=11, Q=12, K=13, A=14
    
    # מימוש הפונקציה (להשלמה בהמשך):
    return {} # מחזיר מילון ריק כערך התחלתי

def compare_cards(p1_card: dict, p2_card: dict) -> str:
    """
    משווה בין שני קלפים ומחזיר את שם המנצח (P1 או P2) או "TIE" למלחמה.
    חתימה: compare_cards(p1_card:dict, p2_card:dict) -> str
    """
    # מימוש הפונקציה (להשלמה בהמשך):
    return "" # מחזיר מחרוזת ריקה כערך התחלתי

def create_deck() -> List[Dict]:
    """
    יוצר חפיסת קלפים שלמה (52 קלפים).
    חתימה: create_deck() -> list[dict]
    """
    # מימוש הפונקציה (להשלמה בהמשך):
    return [] # מחזיר רשימה ריקה כערך התחלתי

def shuffle(deck: List[Dict]) -> List[Dict]:
    """
    מערבב את חפיסת הקלפים ומחזיר אותה מעורבבת.
    חתימה: shuffle(deck:list[dict]) -> list[dict]
    """
    # מימוש הפונקציה (להשלמה בהמשך):
    # נשתמש ב-random.shuffle עבור המימוש האמיתי
    return deck # מחזיר את הרשימה כפי שהיא כערך התחלתי