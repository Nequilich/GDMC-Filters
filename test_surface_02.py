def perform(level, box, options):
	neighborHeightAtRowStart = 256
	for x in range(box.minx, box.maxx):
		y = getSurfaceBlockHeightViaStartPoint(level, x, box.minz, neighborHeightAtRowStart)
		setBlock(level, x, y + 1, box.minz, 20)
		neighborHeight = y
		neighborHeightAtRowStart = y
		for z in range(box.minz + 1, box.maxz):
			y = getSurfaceBlockHeightViaStartPoint(level, x, z, neighborHeight)
			setBlock(level, x, y + 1, z, 20)
			neighborHeight = y

aboveSurfaceBlocks = [0, 6, 17, 18, 31, 32, 37, 38, 39, 40, 59, 81, 83, 99, 100, 103, 104, 105, 106, 111, 141, 142, 161, 162, 175]
def isSurfaceBlock(level, x, y, z):
		for block in aboveSurfaceBlocks:
			if (level.blockAt(x, y, z) == block):
				return False
		return True

def setBlock(level, x, y, z, block, data = 0):
	level.setBlockAt(x, y, z, block)
	level.setBlockDataAt(x, y, z, data)

def getSurfaceBlockHeight(level, x, z):
	surfaceIsFound = False
	y = level.Height
	while (not surfaceIsFound):
		if (isSurfaceBlock(level, x, y, z)):
			surfaceIsFound = True
		else:
			y -= 1
	return y

def getSurfaceBlockHeightViaStartPoint(level, x, z, startHeight):
	isAboveSurface = not isSurfaceBlock(level, x, startHeight, z)
	surfaceIsFound = False
	y = startHeight
	if (isAboveSurface):
		while (not surfaceIsFound):
			if (isSurfaceBlock(level, x, y, z)):
				surfaceIsFound = True
			else:
				y -= 1
		return y
	else:
		while (not surfaceIsFound):
			if (isSurfaceBlock(level, x, y, z)):
				y += 1
			else:
				surfaceIsFound = True
		return y - 1