from collections import deque

def getSurface(level, box):
	surface = []
	surfaceExtra = []
	for x in range(box.minx, box.maxx):
		row = []
		rowExtra = []
		for z in range(box.minz, box.maxz):
			row.append(Block(0))
			rowExtra.append(BlockExtra(0))
		surface.append(row)
		surfaceExtra.append(rowExtra)
	
	surfacePoints = deque()
	xMid = int(box.minx + (box.maxx - box.minx) / 2)
	zMid = int(box.minz + (box.maxz - box.minz) / 2)
	surfaceExtra[xMid - box.minx][zMid - box.minz].suggestedHeight = level.Height
	surfacePoints.append(SurfacePoint(xMid, zMid, level.Height))

	while (surfacePoints):
		nextSurfacePoint = surfacePoints.popleft()
		x = nextSurfacePoint.x
		z = nextSurfacePoint.z
		suggestedHeight = nextSurfacePoint.suggestedHeight
		height = getSurfaceBlockHeightViaStartPoint(level, x, z, suggestedHeight)
		block = surface[x - box.minx][z - box.minz]
		if (block.height < height):
			block.height = height
			if (x + 1 < box.maxx and surface[x + 1 - box.minx][z - box.minz].height < height and surfaceExtra[x + 1 - box.minx][z - box.minz].suggestedHeight < height):
				surfaceExtra[x + 1 - box.minx][z - box.minz].suggestedHeight = height
				surfacePoints.append(SurfacePoint(x + 1, z, height))
			if (x - 1 >= box.minx and surface[x - 1 - box.minx][z - box.minz].height < height and surfaceExtra[x - 1 - box.minx][z - box.minz].suggestedHeight < height):
				surfaceExtra[x - 1 - box.minx][z - box.minz].suggestedHeight = height
				surfacePoints.append(SurfacePoint(x - 1, z, height))
			if (z + 1 < box.maxz and surface[x - box.minx][z + 1 - box.minz].height < height and surfaceExtra[x - box.minx][z + 1 - box.minz].suggestedHeight < height):
				surfaceExtra[x - box.minx][z + 1 - box.minz].suggestedHeight = height
				surfacePoints.append(SurfacePoint(x, z + 1, height))
			if (z - 1 >= box.minz and surface[x - box.minx][z - 1 - box.minz].height < height and surfaceExtra[x - box.minx][z - 1 - box.minz].suggestedHeight < height):
				surfaceExtra[x - box.minx][z - 1 - box.minz].suggestedHeight = height
				surfacePoints.append(SurfacePoint(x, z - 1, height))
	return surface

def setBlock(level, x, y, z, block, data = 0):
	level.setBlockAt(x, y, z, block)
	level.setBlockDataAt(x, y, z, data)

aboveSurfaceBlocks = [0, 6, 17, 18, 31, 32, 37, 38, 39, 40, 59, 78, 81, 83, 99, 100, 103, 104, 105, 106, 111, 141, 142, 161, 162, 175]
def isSurfaceBlock(level, x, y, z):
		for block in aboveSurfaceBlocks:
			if (level.blockAt(x, y, z) == block):
				return False
		return True

def getSurfaceBlockHeightViaStartPoint(level, x, z, suggestedHeight):
	isAboveSurface = not isSurfaceBlock(level, x, suggestedHeight, z)
	surfaceIsFound = False
	y = suggestedHeight
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

class Block:

	def __init__(self, height):
		self.height = height

class BlockExtra:

	def __init__(self, suggestedHeight):
		self.suggestedHeight = suggestedHeight

class SurfacePoint:

	def __init__(self, x, z, suggestedHeight):
		self.x = x
		self.z = z
		self.suggestedHeight = suggestedHeight