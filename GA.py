import sys
import copy
import math
import random
import time
from Nqueen import *
class GaQueens:
    def __init__(self, board_size, pop_size, gen_size):

        self.board_size = board_size
        self.pop_size = pop_size
        self.gen_size = gen_size
        self.generation_count = 0
        # fitness for goal
        self.goal = int((self.board_size * (self.board_size - 1)) / 2)
		#populcation feli!
        self.population = []
        self.first_generation()
        while True:
			#age population be foal resid dg check nakone!
            if self.goal_find() == True:
                break
			#dige generation nasaze age barname be generation size resid!	
            if -1 < self.gen_size <= self.generation_count:
                break
            self.next_generation()
        if -1 < self.gen_size <= self.generation_count:
            print("result not find in %d generations" % self.generation_count)
        elif self.goal_find():
            print("result find in %s" % self.generation_count)
            for population in self.population:
                if population.fitness == self.goal:
					#print toye yek list!
                    print(population.queens)
					#print be sorat safe shatranj
                    population.print_board()
    def goal_find(self):
        for population in self.population:
            if population.fitness == self.goal:
                return True
        return False
    def random_selection(self):
		#entekhab chand item az population feli baraye next generation  
		#k in selection ha bishtarin meghdar fitness ra daranad!
        population_list = []
        for i in range(len(self.population)):
            population_list.append((i, self.population[i].fitness))
        population_list.sort(key=lambda pop_item: pop_item[1], reverse=True)
        return population_list[:int(len(population_list) / 3)]

    def first_generation(self):
        for i in range(self.pop_size):
            self.population.append(Board(self.board_size, self.goal))

    def next_generation(self):
        self.generation_count += 1
        # random selection baraye sakht next generation
        selections = self.random_selection()
        new_population = []
        while len(new_population) < self.pop_size:
            sel = random.choice(selections)[0]
            new_population.append(copy.deepcopy(self.population[sel]))
        self.population = new_population
        for population in self.population:
            population.mutation()
