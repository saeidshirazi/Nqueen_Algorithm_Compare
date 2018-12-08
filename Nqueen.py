#!/usr/bin/python3
import sys
import copy
import math
import random
from logo import print_logo
from GA import *
import time
###############################################################################
class Board:
    def __init__(self, board_size, goal):
        self.board_size = board_size
        self.goal = goal
        self.fitness = 0
        # first item
        self.queens = list(range(self.board_size))
        # random switch
        self.switch(self.board_size / 2)
###############################################################################
    def switch(self, count):
        count = int(count)
        for i in range(count):
            j = random.randint(0, self.board_size - 1)
            k = random.randint(0, self.board_size - 1)
            self.queens[j], self.queens[k] = self.queens[k], self.queens[j]
        self.compute_fitness()
###############################################################################
    def mutation(self):
        # randomly switch 2 itmes
        self.switch(2)
        # age adad random to baze ma nbod 1 bezare!
        if random.uniform(0, 1) < 0.25:
            self.switch(1)
###############################################################################
    def compute_fitness(self):
        #harchi fitness bishtar behtar:)
        self.fitness = self.goal
        for i in range(self.board_size):
            for j in range(i + 1, self.board_size):
                if math.fabs(self.queens[i] - self.queens[j]) == j - i:
                    # baraye mohafezat az q yeki hardafe az fitness kam mikonim!
                    self.fitness -= 1
###############################################################################
    def print_board(self):
        for row in range(self.board_size):
            print("", end="|")
            queen = self.queens.index(row)
            for col in range(self.board_size):
                if col == queen:
                    print("Q", end="|")
                else:
                    print("_", end="|")
            print("")
###############################################################################
if __name__ == '__main__':
    print_logo(self=0)
    boardsize = input("please set the board size : ")
    board_size = int(boardsize)
    pop_size = 8
    # inghad edame bede ta javab ro peyda kone:)
    gen_size = -1
    print("Starting N-Queen solver with GA algoritm:")
    print("    board size      : ", board_size)
    print("    population size : ", pop_size)
    print("    generation size : ", gen_size)
    print("==================================================================")
    start = time.time()
    GaQueens(board_size, pop_size, gen_size)
    print("==================================================================")
    end = time.time()
    print("time to solve is : ",end - start)
