from random import randint

moves = {
    0: "Rock",
    1: "Paper",
    2: "Scissors"
}

""" 0 1 2
    R P S (p)
R   0 1 2
P   2 0 1
S   1 2 0
(c)
"""
wins = [[0, 2, 1], [1, 0, 2], [2, 1, 0]]


def get_attack():
    num = randint(0, 2)
    return num


def get_winner(player, comp):
    if wins[player][comp] == 1:
        return "Player"
    elif wins[player][comp] == 2:
        return "Comp"
    return "Tie"
