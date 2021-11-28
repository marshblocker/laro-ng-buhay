import os
import time
from random import choice

CELL_CHAR = '*'
BOARD_WIDTH = 100
BOARD_HEIGHT = 15

def will_live(rc: tuple[int, int], board: list[list[bool]]) -> bool:
	r, c = rc	
	alive_neighbors = 0

	if r != 0:
		for i in range(3):
			try:
				alive_neighbors += board[r-1][c-1+i]
			except IndexError:
				pass 
	if c != 0:
		alive_neighbors += board[r][c-1]
	if c != BOARD_WIDTH-1:
		alive_neighbors += board[r][c+1]
	if r != BOARD_HEIGHT-1:
		for i in range(3):
			try:
				alive_neighbors += board[r+1][c-1+i]
			except IndexError:
				pass 

	return alive_neighbors == 3 or \
		   alive_neighbors == 2 and board[r][c]


def next_state(curr_board: list[list[bool]]) -> list[list[bool]]:
	new_board: list[list[bool]] = [[False for _ in range(BOARD_WIDTH)]
								   for _ in range(BOARD_HEIGHT)]

	for r in range(BOARD_HEIGHT):
		for c in range(BOARD_WIDTH):
			new_board[r][c] = will_live((r,c), curr_board)

	return new_board


def board_init() -> list[list[bool]]:
	yesno: list[bool] = [True, False]
	starting_board: list[list[bool]] = \
		[[choice(yesno) for _ in range(BOARD_WIDTH)] 
			for _ in range(BOARD_HEIGHT)]

	return starting_board


def clear_screen() -> None:
	os.system('cls')


def print_board(board: list[list[bool]], gen: int) -> None:
	print(f"Generation: {gen}")
	board_str: str = \
		"\n".join(["".join([CELL_CHAR if elem else " " for elem in row]) 
						for row in board])
	print(board_str)

	time.sleep(0.05)
	clear_screen()
	

def main() -> None:
	gen: int = 0
	board: list[list[bool]] = board_init()

	clear_screen()
	while True:
		print_board(board, gen)
		board = next_state(board)
		gen += 1


if __name__ == "__main__":
	main()



