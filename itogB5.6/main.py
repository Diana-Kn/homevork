# игра в крестики нолики
board = list(range(1,10))
def draw(board):
	print("-" * 12)
	for i in range(3):
		print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
		print("-" * 12)

def d_input(player):
	valid = False
	while not valid:
		player_answ = input("куда поставим " + player+"? ")
		try:
			player_answ = int(player_answ)
		except:
			print("некорректрый ввод")
			continue
		if player_answ >= 1 and player_answ <= 9:
			if(str(board[player_answ-1]) not in "XO"):
				board[player_answ-1] = player
				valid = True
			else:
				print("занято")
		else:
			print("некоректный ввод")

def wic(board):
	w = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
	for s in w:
		if board[s[0]] == board[s[1]] == board[s[2]]:
			return board[s[0]]
	return False

def m(board):
	count = 0
	win = False
	while not win:
		draw(board)
		if count % 2 == 0:
			d_input("X")
		else:
			d_input("O")
		count += 1
		if count > 4:
			tmp = wic(board)
			if tmp:
				print(tmp, "victory!")
				win = True
				break
		if count == 9:
			print("dead heat!")
			break
	draw(board)
m(board)
