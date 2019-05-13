import random

class SeededRandom:
	__instance = None

	@staticmethod
	def getInstance():
		if SeededRandom.__instance == None:
			rng = random.Random()
			rng.seed(12345)
			SeededRandom.__instance = rng
		return SeededRandom.__instance