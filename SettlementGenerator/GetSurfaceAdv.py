from collections import deque
from Classes import Surface

def getSurface(level, box):
	surface = Surface(box.maxx - box.minx, box.maxz - box.minz)
	surfaceExtra = Surface(box.maxx - box.minx, box.maxz - box.minz) #Contains suggested heights
	unresolvedSurfaceSpots = deque() #Surface spots which surface height needs to be calculate

	#Adds the center surfacespot as the first unresolved surface spot
	xCenter = int((box.maxx - box.minx) / 2)
	zCenter = int((box.maxz - box.minz) / 2)
	surfaceExtra.surface[xCenter][zCenter].height = level.Height
	unresolvedSurfaceSpots.append(Arg(xCenter, zCenter, level.Height))

	while (unresolvedSurfaceSpots):
		nextSurfaceSpot = unresolvedSurfaceSpots.popleft()
		x = nextSurfaceSpot.x
		z = nextSurfaceSpot.z
		suggestedHeight = nextSurfaceSpot.suggestedHeight
		height = getSurfaceSpotHeight(level, x + box.minx, z + box.minz, suggestedHeight)

		#Returns if calculated is not higher than previous recorded height
		if (surface.surface[x][z].height < height):
			surface.surface[x][z].height = height
			tryAddSurfaceSpotToQueue(box, x + 1, z, height, surface, surfaceExtra, unresolvedSurfaceSpots)
			tryAddSurfaceSpotToQueue(box, x - 1, z, height, surface, surfaceExtra, unresolvedSurfaceSpots)
			tryAddSurfaceSpotToQueue(box, x, z + 1, height, surface, surfaceExtra, unresolvedSurfaceSpots)
			tryAddSurfaceSpotToQueue(box, x, z - 1, height, surface, surfaceExtra, unresolvedSurfaceSpots)
	return surface

aboveSurfaceBlocks = [0, 6, 17, 18, 31, 32, 37, 38, 39, 40, 59, 78, 81, 83, 99, 100, 103, 104, 105, 106, 111, 141, 142, 161, 162, 175]
def isSurfaceBlock(level, x, y, z):
		for block in aboveSurfaceBlocks:
			if (level.blockAt(x, y, z) == block):
				return False
		return True

def getSurfaceSpotHeight(level, x, z, suggestedHeight):
	isAboveSurface = not isSurfaceBlock(level, x, suggestedHeight, z)
	y = suggestedHeight + 2
	if (isAboveSurface):
		while (True):
			if (isSurfaceBlock(level, x, y, z)):
				return y
			else:
				y -= 1
	else:
		while (True):
			if (isSurfaceBlock(level, x, y, z)):
				y += 1
			else:
				return y - 1

def tryAddSurfaceSpotToQueue(box, x, z, suggestedHeight, surface, surfaceExtra, unresolvedSurfaceSpots):
	#Checks if surface spot is within surface border
	if (x + box.minx < box.minx or x + box.minx >= box.maxx or z + box.minz < box.minz or z + box.minz >= box.maxz):
		return

	#Checks if this height has been suggested before
	if (surfaceExtra.surface[x][z].height < suggestedHeight):
		surfaceExtra.surface[x][z].height = suggestedHeight
		unresolvedSurfaceSpots.append(Arg(x, z, suggestedHeight))

class Arg:

	def __init__(self, x, z, suggestedHeight):
		self.x = x
		self.z = z
		self.suggestedHeight = suggestedHeight