import random
import math
import time
from logo import print_logo
###############################################################################
def nqueens(n):
	start = time.time()
	show(min_conflicts(list(range(n)), n), n)
	print("==================================================================")
	end = time.time()
	print("time to solve is : ",end - start)
###############################################################################
def show(indiv, n):
	print(indiv)
	for i in range(n):
		row = ['~'] * n
		for column in range(n):
			if indiv[column] == n - 1 - i:
				row[column] = 'Q'
		print(''.join(row))
###############################################################################
def min_conflicts(indiv, n, iters=10000):
	def random_pos(list, filter):
		return random.choice([i for i in range(n) if filter(list[i])])

	for k in range(iters):
		confs = find_conflicts(indiv, n)
		#age tedad barkhord ha 0 bod chapesh kon
		if sum(confs) == 0:
			return indiv

		def filter1(sas):
			return sas == sas>0
		column = random_pos(confs, filter1)

		vconfs = []
		for row in range(n):
			vconfs.append(hits(indiv,n,column,row))

		def filter2(sh):
			return sh ==  min(vconfs)
		indiv[column] = random_pos(vconfs,filter2)

	raise Exception("Incomplete:please try again with more iteration.")
###############################################################################

def find_conflicts(indiv, n):
	return [hits(indiv, n, column, indiv[column]) for column in range(n)]

###############################################################################

def hits(indiv, n, column, row):
	total = 0
	for i in range(n):
		if i == column:
			continue
		if (indiv[i] == row) or (math.fabs(i - column) == math.fabs(indiv[i] - row)):
			total += 1
	return total

###############################################################################

if __name__ == '__main__':
	print_logo(self=0)
	print("Starting N-Queen solver with min-conflict algoritm:")
	boardsize = int(input("please set the board size : "))
	print("    board size      : ", boardsize)
	print("    iteration size  : ", 10000)
	print("==================================================================")

	nqueens(boardsize)
