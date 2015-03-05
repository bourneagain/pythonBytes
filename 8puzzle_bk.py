import sys
import Queue
import time
import copy
# import heaq
class Board():
	def __init__(self, x):
		self.board_array = x
	def __eq__(self, other):
		return self.board_array == other.board_array
	def __hash__(self):
		a=0
		i=0
		for n in self.board_array:
			a+=n*(3**i)
			i+=1
		return hash(a)

	def generate_swap_boards(self):
		neighbor_index = self.findNeighbours()
		print neighbor_index
		boards = []
		init_board = self.printb()
		zero_index = init_board.index(0)
		for i in neighbor_index:
			temp = copy.deepcopy(init_board)
			t = temp[i]
			temp[i] = 0
			temp[zero_index] = t
			boards.append(Board(temp))
		return boards
	
	def get_greedy_manhattan(self, board_list):
		min_path = sys.maxint
		min_board = None
		for i in board_list:
			temp_board = copy.deepcopy(i)
			min_temp = self.get_manhattan(i)
			if  min_temp < min_path:
				min_board = temp_board
				min_path = min_temp
		return min_board,min_path	

	def getMinGasnik(self, board_list):
		min_path = sys.maxint
		min_board = None
		for i in board_list:
			temp_board = copy.deepcopy(i)
			min_temp = self.gashnik(i)
			if  min_temp < min_path:
				min_board = temp_board
				min_path = min_temp
		return min_board,min_path

	def findNeighbours(self):
		source_index = self.board_array.index(0)
		source_col = source_index%3
		source_row = source_index//3
		x = []
        # //down
		x.append((source_col,source_row+1))
        # //up
		x.append((source_col,source_row-1))
        # //right
		x.append((source_col+1,source_row))
        # //left
		x.append((source_col-1,source_row))
		return_index = []
		for col,row in x:
			if row>=0 and row<=2 and col>=0 and col<=2 :
				return_index.append(row*3+col)
		return return_index

	def printb(self):
		return self.board_array
	def print_matrix(self):
		for i in range(3):
			for j in range(3):
				print self.board_array[i*3+j],
			print ""
		print "----"

	def is_reached(self):
		for index, i  in enumerate(self.board_array):
			if index != i:
				return False
		return True
	def find_missed_value(self, skip):
		res = []
		for index,i in enumerate(self.board_array):
			if skip and i == 0:
				continue
			if index != i:
				res.append(i)
		return res
	def a_star(self, type):
		if type == "MANHATTAN":
            pass
			
	def get_misplaced_tile_score(self):
		return len(self.find_missed_value())

	def gashnik(self, board ):
		result = []
		res = board.find_missed_value(1)
		res.sort()
		path_cost = 0
		while not board.is_reached():
			# time.sleep(1)
			# print "RES", res0, 1, 2, 3, 4, 5, 6, 8, 7
			# print "BOARD",board.printb()
			path_cost+=1
			zero_index = board.board_array.index(0)
			if zero_index != 0 :
				# assume board 6 3 5 2 1 50 4 8 7 
				# index of 0 = 5
				# index of 5 = 2 
				# swap a[2] and a[5] 
				# remove 5 ; index of 0 initially from res
				# case where the 0 is not in the right place
				to_swap = board.board_array.index(zero_index)
				# print "TOSWAP" , zero_index
				# to_swap contains the index of 0 
				board.board_array[to_swap],board.board_array[zero_index] = board.board_array[zero_index], board.board_array[to_swap]
				del res[res.index(zero_index)]
				
			else:
				# case where 0 is in the right place
				# take first of the res
				# swap 
				checkVal = res[0]
				to_swap = board.board_array.index(checkVal)
				# print "TO SWAP -- ", to_swap
				board.board_array[0] = checkVal
				board.board_array[to_swap] = 0
				# self.board_array[self.board_array.index(0)], self.board_array[to_swap] = to_swap, self.board_array[to_swap]
		return path_cost

	def get_manhattan(self, board):
		man_score = 0
		for index, i in enumerate(board.board_array):
			des_row = i//3
			des_col = i%3
			cur_row = index//3
			cur_col = index%3
			man_score+=abs(cur_row - des_row) + abs(cur_col - des_col)
		return man_score




A =[0, 1, 2, 3, 4, 5, 6, 8, 7]
A = [6,3,5,2,1,0,4,8,7]
a = Board(A)		
print a.get_manhattan(a)
# a.print_matrix()
# # a.gashnik(a)
# board_list = a.generate_swap_boards()
# min_board = a.getMinGasnik(board_list)
# print min_board[0].print_matrix()
# print min_board[1]





