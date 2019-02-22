def perform(level, box, options):
	surface = getSurface(level, box)
	setSteepness(box, surface)
	print("Height:")
	printSurfaceHeight(box, surface)
	print("Steepness:")
	printSurfaceSteepness(box, surface)
	for x in range(0, box.maxx - box.minx):
		for z in range(0, box.maxz - box.minz):
			setBlock(level, x + box.minx, surface[x][z].height + 1, z + box.minz, 20)

aboveSurfaceBlocks = [0, 6, 17, 18, 31, 32, 37, 38, 39, 40, 59, 78, 81, 83, 99, 100, 103, 104, 105, 106, 111, 141, 142, 161, 162, 175]
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

def getSurface(level, box):
	surface = []
	neighborHeightAtRowStart = 256
	for x in range(box.minx, box.maxx):
		y = getSurfaceBlockHeightViaStartPoint(level, x, box.minz, neighborHeightAtRowStart)
		row = [Block(y)]
		neighborHeight = y
		neighborHeightAtRowStart = y
		for z in range(box.minz + 1, box.maxz):
			y = getSurfaceBlockHeightViaStartPoint(level, x, z, neighborHeight)
			row.append(Block(y))
			neighborHeight = y
		surface.append(row)
	return surface

class Block:

	def __init__(self, height, steepness = 0):
		self.height = height
		self.steepness = steepness

def getSteepness(box, surface, x, z):
	blocks = []
	if (x + 1 < box.maxx - box.minx):
		blocks.append(surface[x + 1][z])
	if (z + 1 < box.maxz - box.minz):
		blocks.append(surface[x][z + 1])
	if (x - 1 >= 0):
		blocks.append(surface[x - 1][z])
	if (z - 1 >= 0):
		blocks.append(surface[x][z - 1])
	
	minHeight = surface[x][z].height
	maxHeight = surface[x][z].height
	for block in blocks:
		h = block.height
		if (h < minHeight):
			minHeight = h
		if (h > maxHeight):
			maxHeight = h
	return maxHeight - minHeight

def setSteepness(box, surface):
	for x in range(0, box.maxx - box.minx):
		for z in range(0, box.maxz - box.minz):
			surface[x][z].steepness = getSteepness(box, surface, x, z)

def printSurfaceHeight(box, surface):
	for x in range(0, box.maxx - box.minx):
		s = ""
		for z in range(0, box.maxz - box.minz):
			s += str(surface[x][z].height) + " "
		print(s)

def printSurfaceSteepness(box, surface):
	for x in range(0, box.maxx - box.minx):
		s = ""
		for z in range(0, box.maxz - box.minz):
			s += str(surface[x][z].steepness) + " "
		print(s)