import random

def play_Lucky7():
    deck = list(range(1, 14)) * 16
    random.shuffle(deck)
    winning_number = random.choice(deck)
    
    if winning_number == 7:
        print("The winner is Lucky 7! Congrats!")
    elif winning_number < 7:
        print("The winner is 7 down! Congrats!")
    elif winning_number > 7:
        print("The winner is 7 up! Congrats!")
    
if __name__ == "__main__":
    play_Lucky7()