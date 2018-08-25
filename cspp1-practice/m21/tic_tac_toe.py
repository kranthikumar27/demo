''' it is a program for desideing the winner of the game tic tac toe'''

from collections import Counter

def game_winner(game):
    ''' this method returns the winner'''
    counter = Counter()
    flag = 0
    for row in game:
        for value in row:
            if value in ('x', 'o', '.'):
                counter[value] += 1
            elif value not in ('x', 'o', '.'):
                flag = 1
    if flag == 1:
        return "invalid input"

    if abs(counter['x'] - counter['o']) == 1:
        if ((game[0][0] == 'x' and game[0][1] == 'x' and game[0][2] == 'x') or
                (game[1][0] == 'x' and game[1][1] == 'x' and game[1][2] == 'x') or
                (game[2][0] == 'x' and game[2][1] == 'x' and game[2][2] == 'x') or
                (game[0][0] == 'x' and game[1][0] == 'x' and game[2][0] == 'x') or
                (game[0][1] == 'x' and game[1][1] == 'x' and game[2][1] == 'x') or
                (game[0][2] == 'x' and game[1][2] == 'x' and game[2][2] == 'x') or
                (game[0][0] == 'x' and game[1][1] == 'x' and game[2][2] == 'x') or
                (game[2][0] == 'x' and game[1][1] == 'x' and game[0][2] == 'x')):
            return 'x'
        if ((game[0][0] == 'o' and game[0][1] == 'o' and game[0][2] == 'o') or
                (game[1][0] == 'o' and game[1][1] == 'o' and game[1][2] == 'o') or
                (game[2][0] == 'o' and game[2][1] == 'o' and game[2][2] == 'o') or
                (game[0][0] == 'o' and game[1][0] == 'o' and game[2][0] == 'o') or
                (game[0][1] == 'o' and game[1][1] == 'o' and game[2][1] == 'o') or
                (game[0][2] == 'o' and game[1][2] == 'o' and game[2][2] == 'o') or
                (game[0][0] == 'o' and game[1][1] == 'o' and game[2][2] == 'o') or
                (game[2][0] == 'o' and game[1][1] == 'o' and game[0][2] == 'o')):
            return 'o'
        return 'draw'

    if abs((counter['x'] - counter['o'] == 0) or (counter['x'] - counter['o'] > 1)):
        return "invalid game"

def main():
    '''this is the main method'''
    game = []
    for _ in range(3):
        row = list(map(str, input().split(' ')))
        game.append(row)
    print(game_winner(game))

if __name__ == '__main__':
    main()
