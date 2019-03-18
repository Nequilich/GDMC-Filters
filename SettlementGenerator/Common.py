import math

def setBlock(level, x, y, z, block, data = 0):
	level.setBlockAt(x, y, z, block)
	level.setBlockDataAt(x, y, z, data)

def getMatrix(height, width, defaultValue):
	matrix = []
	for x in range(height):
		row = []
		for z in range(width):
			row.append(defaultValue)
		matrix.append(row)
	return matrix

def getEuclideanDistance(surface, point1, point2):
	p1Height = surface.surfaceMap[point1.x][point1.z].height
	p2Height = surface.surfaceMap[point2.x][point2.z].height
	return math.sqrt(math.pow(point2.x - point1.x, 2) + math.pow(point2.z - point1.z, 2) + math.pow((p2Height - p1Height), 2))