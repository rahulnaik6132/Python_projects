# Player rolls a dice
# LUDO GAME
import random
random.seed()
def ludo():
    return random.randint(1, 6)

players = ['Player 1', 'Player 2', 'Player 3', 'Player 4']
random.shuffle(players)

for player in players:
    dice = ludo()
    print(f'{player} rolls a {dice}')