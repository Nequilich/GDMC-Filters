import math
import json

def setBlock(level, surface, x, y, z, block, data = 0):
	if type(block) is tuple:
		data = block[1]
		block = block[0]
	if surface == None:
		level.setBlockAt(x, y, z, block)
		level.setBlockDataAt(x, y, z, data)
	else:
		level.setBlockAt(x + surface.xStart, y, z + surface.zStart, block)
		level.setBlockDataAt(x + surface.xStart, y, z + surface.zStart, data)

def isWithinBorder(surface, x, z):
	return x >= 0 and x < surface.xLength and z >= 0 and z < surface.zLength

def getMatrix(height, width, defaultValue):
	matrix = []
	for _ in range(height):
		row = []
		for _ in range(width):
			row.append(defaultValue)
		matrix.append(row)
	return matrix

def getEuclideanDistance(surface, point1, point2):
	p1Height = surface.surfaceMap[point1.x][point1.z].height
	p2Height = surface.surfaceMap[point2.x][point2.z].height
	return math.sqrt(math.pow(point2.x - point1.x, 2) + math.pow(point2.z - point1.z, 2) + math.pow((p2Height - p1Height), 2))

def calculateAverage(list):
	total = 0
	for n in list:
		total += n
	return total / len(list)

def loadFile(filePath):
	with open(filePath) as f:
		return json.load(f)

aboveSurfaceBlocks = [0, 6, 8, 10, 17, 18, 31, 32, 37, 38, 39, 40, 59, 78, 81, 83, 99, 100, 103, 104, 105, 106, 111, 141, 142, 161, 162, 175]
def isSurfaceBlock(level, x, y, z):
	for block in aboveSurfaceBlocks:
		if level.blockAt(x, y, z) == block:
			return False
	return True

def removeTree(level, x, y, z):
	blocks = [Block(x, y, z)]
	while blocks:
		nextBlock = blocks.pop()
		x = nextBlock.x
		y = nextBlock.y
		z = nextBlock.z

		if not isTreeBlock(level, x, y, z):
			continue

		setBlock(level, None, x, y, z, 0)

		#Removes snow layer
		if level.blockAt(x, y + 1, z) == 78:
			setBlock(level, None, x, y + 1, z, 0)

		# Adds neighbors to stack
		blocks.extend([Block(x + 1, y, z), Block(x - 1, y, z), Block(x, y + 1, z), Block(x, y - 1, z), Block(x, y, z + 1), Block(x, y, z - 1)])
		blocks.extend([Block(x + 1, y + 1, z), Block(x - 1, y + 1, z), Block(x, y + 1, z + 1), Block(x, y + 1, z - 1)])
		blocks.extend([Block(x + 1, y - 1, z), Block(x - 1, y - 1, z), Block(x, y - 1, z + 1), Block(x, y - 1, z - 1)])

treeBlocks = [17, 18, 99, 100, 106, 161, 162]
def isTreeBlock(level, x, y, z):
		for block in treeBlocks:
			if level.blockAt(x, y, z) == block:
				return True
		return False

class Block:

	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z