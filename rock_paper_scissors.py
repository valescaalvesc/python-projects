import random

def start():
    you = input("What's your choice:'r' for rock, 'p' for paper, 's' for scissors\np")
    computer = random.choice(['r', 'p', 's'])
    print(computer)

    if you == computer:
        return 'its a tie'

    if winner(you, computer):
        return 'You won!'

    return 'You lost!'

def winner(player, opponent):
    if(player=='r' and opponent=='s') or (player=='s' and opponent=='p') or (player=='p' and opponent=='r'):
        return True

print(start())