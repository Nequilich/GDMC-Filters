from collections import deque

def perform(level, box, options):
	surface = getSurface(level, box)
	for x in range(0, box.maxx - box.minx):
		for z in range(0, box.maxz - box.minz):
			setBlock(level, x + box.minx, surface[x][z].height + 1, z + box.minz, 20)

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

def getSurface(level, box):
	surface = []
	for x in range(box.minx, box.maxx):
		row = []
		for z in range(box.minz, box.maxz):
			row.append(Block(0))
		surface.append(row)
	
	surfacePoints = deque()
	xMid = int(box.minx + (box.maxx - box.minx) / 2)
	zMid = int(box.minz + (box.maxz - box.minz) / 2)
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
			if (x + 1 < box.maxx and surface[x + 1 - box.minx][z - box.minz].height < height):
				surfacePoints.append(SurfacePoint(x + 1, z, height))
			if (x - 1 >= box.minx and surface[x - 1 - box.minx][z - box.minz].height < height):
				surfacePoints.append(SurfacePoint(x - 1, z, height))
			if (z + 1 < box.maxz and surface[x - box.minx][z + 1 - box.minz].height < height):
				surfacePoints.append(SurfacePoint(x, z + 1, height))
			if (z - 1 >= box.minz and surface[x - box.minx][z - 1 - box.minz].height < height):
				surfacePoints.append(SurfacePoint(x, z - 1, height))
	return surface

class Block:

	def __init__(self, height, steepness = 0):
		self.height = height
		self.steepness = steepness

class SurfacePoint:

	def __init__(self, x, z, suggestedHeight):
		self.x = x
		self.z = z
		self.suggestedHeight = suggestedHeight

class Area:

	def __init__(self, x1, z1, x2, z2):
		self.x1 = x1
		self.z1 = z1
		self.x2 = x2
		self.z2 = z2

def getArea(level, box, surface, x, z):
	area = Area(x, z, x + 1, z + 1)
	canContinueUp = True
	canContinueRight = True
	canContinueDown = True
	canContinueLeft = True
	while(canContinueUp or canContinueRight or canContinueDown or canContinueLeft):
		if (canContinueUp):
			print("do stuff")
		if (canContinueRight):
			print("do stuff")
		if (canContinueDown):
			print("do stuff")
		if (canContinueLeft):
			print("do stuff")
	return area