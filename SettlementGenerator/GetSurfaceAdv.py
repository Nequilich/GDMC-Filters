from collections import deque
from Classes import Surface

def getSurface(level, box):
	surface = Surface(box.maxx - box.minx, box.maxz - box.minz)
	surfaceExtra = Surface(box.maxx - box.minx, box.maxz - box.minz) #Contains suggested heights
	unresolvedSurfaceSpots = deque() #Surfacespots which surface height needs to be calculated

	#Adds the center surfacespot as the first unresolved surfacespot
	xCenter = int(box.minx + (box.maxx - box.minx) / 2)
	zCenter = int(box.minz + (box.maxz - box.minz) / 2)
	surfaceExtra.surface[xCenter - box.minx][zCenter - box.minz].height = level.Height
	unresolvedSurfaceSpots.append(Arg(xCenter, zCenter, level.Height))

	while (unresolvedSurfaceSpots):
		nextSurfaceSpot = unresolvedSurfaceSpots.popleft()
		x = nextSurfaceSpot.x
		z = nextSurfaceSpot.z
		suggestedHeight = nextSurfaceSpot.suggestedHeight

		height = getSurfaceSpotHeight(level, x, z, suggestedHeight)
		block = surface[x - box.minx][z - box.minz]
		if (block.height < height):
			block.height = height
			if (x + 1 < box.maxx and surface[x + 1 - box.minx][z - box.minz].height < height and surfaceExtra[x + 1 - box.minx][z - box.minz].suggestedHeight < height):
				surfaceExtra[x + 1 - box.minx][z - box.minz].suggestedHeight = height
				unresolvedSurfaceSpots.append(Arg(x + 1, z, height))
			if (x - 1 >= box.minx and surface[x - 1 - box.minx][z - box.minz].height < height and surfaceExtra[x - 1 - box.minx][z - box.minz].suggestedHeight < height):
				surfaceExtra[x - 1 - box.minx][z - box.minz].suggestedHeight = height
				unresolvedSurfaceSpots.append(Arg(x - 1, z, height))
			if (z + 1 < box.maxz and surface[x - box.minx][z + 1 - box.minz].height < height and surfaceExtra[x - box.minx][z + 1 - box.minz].suggestedHeight < height):
				surfaceExtra[x - box.minx][z + 1 - box.minz].suggestedHeight = height
				unresolvedSurfaceSpots.append(Arg(x, z + 1, height))
			if (z - 1 >= box.minz and surface[x - box.minx][z - 1 - box.minz].height < height and surfaceExtra[x - box.minx][z - 1 - box.minz].suggestedHeight < height):
				surfaceExtra[x - box.minx][z - 1 - box.minz].suggestedHeight = height
				unresolvedSurfaceSpots.append(Arg(x, z - 1, height))
	return surface

aboveSurfaceBlocks = [0, 6, 17, 18, 31, 32, 37, 38, 39, 40, 59, 78, 81, 83, 99, 100, 103, 104, 105, 106, 111, 141, 142, 161, 162, 175]
def isSurfaceBlock(level, x, y, z):
		for block in aboveSurfaceBlocks:
			if (level.blockAt(x, y, z) == block):
				return False
		return True

def getSurfaceSpotHeight(level, x, z, suggestedHeight):
	isAboveSurface = not isSurfaceBlock(level, x, suggestedHeight, z)
	heightIsFound = False
	y = suggestedHeight + 2
	if (isAboveSurface):
		while (not heightIsFound):
			if (isSurfaceBlock(level, x, y, z)):
				heightIsFound = True
			else:
				y -= 1
		return y
	else:
		while (not heightIsFound):
			if (isSurfaceBlock(level, x, y, z)):
				y += 1
			else:
				heightIsFound = True
		return y - 1

class Arg:

	def __init__(self, x, z, suggestedHeight):
		self.x = x
		self.z = z
		self.suggestedHeight = suggestedHeight