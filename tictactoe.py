# Filename: tictactoe.py
# By: Andrew Holbrook
# Date: 9/21/2016

class Game:
	def __init__(self, dim=3):
		self.board = [[' ' for i in range(dim)] for j in range(dim)]
		self.active_turn = 'X'

	def __str__(self):
		tmpstr = '|'
		for row in range(len(self.board)):
			for col in range(len(self.board)):
				tmpstr += self.board[row][col] + '|'

			if row != len(self.board) - 1:
				tmpstr += '\n|'

		return tmpstr

	def setAt(self, row, col):
		self.board[row][col] = self.active_turn
		if self.active_turn == 'X':
			self.active_turn = 'O'
		else:
			self.active_turn = 'X'

	def board_full(self):
		for row in self.board:
			for col in row:
				if col == ' ':
					return False
		return True

	def over(self):
		if self.win('X') or self.win('O') or self.board_full():
			return True
		return False

	def win(self, player='X'):

		# check rows
		for row in self.board:
			playerWin = True
			for col in row:
				if col != player:
					playerWin = False
					break

			if playerWin:
				return True

		# check columns
		for col in range(len(self.board)):
			playerWin = True
			for row in range(len(self.board)):
				if self.board[row][col] != player:
					playerWin = False
					break

			if playerWin:
				return True

		# check diagonals
		playerWin = True
		for i in range(len(self.board)):
			if self.board[i][i] != player:
				playerWin = False
				break

		if playerWin:
			return True

		playerWin = True
		for i in range(len(self.board)):
			if self.board[i][len(self.board) - 1 - i] != player:
				playerWin = False
				break

		if playerWin:
			return True

		return False

	def get_new_state(self, move):
		new_game = Game(len(self.board))
		new_game.active_turn = self.active_turn
		new_game.board = [list(x) for x in self.board]
		new_game.setAt(*move)

		return new_game

	def get_available_moves(self):
		moves = []
		for row in range(len(self.board)):
			for col in range(len(self.board)):
				if self.board[row][col] == ' ':
					moves.append((row, col))

		return moves

def score(game, depth=0):
	if game.win('X'):
		return 10 - depth
	elif game.win('O'):
		return depth - 10
	else:
		return 0

def minimax(game, depth=0):
	global choice

	if game.over():
		return score(game, depth)

	depth += 1
	scores = []
	moves = []

	for move in game.get_available_moves():
		possible_game = game.get_new_state(move)
		scores.append(minimax(possible_game, depth))
		moves.append(move)

	if game.active_turn == 'X':
		max_score_index = scores.index(max(scores))
		choice = moves[max_score_index]
		return scores[max_score_index]
	else:
		min_score_index = scores.index(min(scores))
		choice = moves[min_score_index]
		return scores[min_score_index]


game = Game(3)
choice = None

while not game.over():
	print(game)
	print()
	minimax(game)
	game.setAt(*choice)
print(game)
