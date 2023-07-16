import random
cards = ["DIAMONDS", "SPADES", "HEARTS", "CLUBs"]
ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "JACK", "QUEEN", "KING", "ACE"]

def pick_a_card():
    card = random.choices(cards)
    rank = random.choices(ranks)
    return(f"THE{rank} of {card}")

print(pick_a_card())
