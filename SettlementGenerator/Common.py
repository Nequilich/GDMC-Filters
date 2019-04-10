import math

def setBlock(level, x, y, z, block, data = 0):
	level.setBlockAt(x, y, z, block)
	level.setBlockDataAt(x, y, z, data)

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

# Converts a chunk coordinate and the blocks position in the chunk to a real coordinate.    
def convertChunkBlockCoordinate(cPosX, CPosZ, chunkBlockPosition):
    chunkBlockPositionX = (chunkBlockPosition / 16)
    chunkBlockPositionZ = chunkBlockPosition % 16

    realPosX = cPosX*16 + chunkBlockPositionX
    realPosZ = CPosZ*16 + chunkBlockPositionZ

    return (realPosX, realPosZ)

def calculateAverage(list):
	total = 0
	for n in list:
		total += n
	return total / len(list)