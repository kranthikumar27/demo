from collections import counter

def game_winner(matrix):
	counter = counter()
	flag = 0
	for row in game:
		for value in game:
			if value in ('x', 'o', '.'):
				counter[value] += 1
			elif value not in ('x', 'o', '.'):
				flag = 1
	if flag == 1:
		return "invalid input"

	if abs(counter['x'] - counter['o'] == 1):
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
			return final

	if abs((counter['x'] - counter['o'] == 0) or (counter['x'] - counter['o'] > 1)):
		return "invalid input"

def main():
	game =[]
	for _ in range(3):
		row = list(map(int, input().split(' ')))
		game.append(row)
	print(game_winner(game))

if __name__ == '__main__':
	main()