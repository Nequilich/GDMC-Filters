from random import randint
import random

def perform(level, box, options):
	goal = "unicorn"
	size = 100
	mutationRate = 0.02
	population = Population(size)
	createRandomPopulation(population)
	print("Start:")
	generation = 1
	generationEnd = 1000
	stop = False
	while generation <= generationEnd and not stop:
		calculateFitness(population, goal)
		printPopulation(population, generation)
		stop = goalIsFound(population, goal)
		population = createNewPopulation(population, mutationRate)
		generation += 1
	print("Generation: " + str(generation - 1))

def createRandomPopulation(population):
	for i in range(population.size):
		s = ""
		for j in range(7):
			s += getRandomChar()
		population.elements.append(Element(s))

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
def getRandomChar():
	return chars[randint(0, 52)]

def calculateFitness(population, goal):
	for element in population.elements:
		fitness = 1
		for i in range(7):
			if goal[i] == element.body[i]:
				fitness += 5
		element.fitness = fitness

def createNewPopulation(population, mutationRate):
	newPopulation = Population(population.size)
	for element in population.elements:
		parents = selectParents(population)
		s = ""
		for i in range(7):
			isMutating = random.uniform(0.0, 1.0) <= mutationRate
			if isMutating:
				s += getRandomChar()
			else:
				r = randint(0, 1)
				s += parents[r].body[i]
		newPopulation.elements.append(Element(s))
	return newPopulation

def selectParents(population):
	parents = []
	totalFitness = 0
	for element in population.elements:
		totalFitness += element.fitness

	r = randint(0, totalFitness - 1)
	firstParentIndex = 0
	f = 0
	i = 0
	while i < population.size:
		element = population.elements[i]
		f += element.fitness
		if r < f:
			totalFitness -= element.fitness
			firstParentIndex = i
			parents.append(element)
			break
		i += 1

	r = randint(0, totalFitness - 1)
	f = 0
	i = 0
	while i < population.size:
		if i == firstParentIndex:
			i += 1
			continue
		element = population.elements[i]
		f += element.fitness
		if r < f:
			parents.append(element)
			break
		i += 1
	return parents

def printPopulation(population, generation):
	s = "Generation " + str(generation) + ": "
	for element in population.elements:
		s += "(" + element.body + ", " + str(element.fitness) + "), "
	print(s[:-2])

def goalIsFound(population, goal):
	for element in population.elements:
		if element.body == goal:
			return True
	return False

class Population:

	def __init__(self, size):
		self.size = size
		self.elements = []

class Element:

	def __init__(self, body):
		self.body = body
		self.fitness = 0