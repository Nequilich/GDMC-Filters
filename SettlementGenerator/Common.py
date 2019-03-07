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