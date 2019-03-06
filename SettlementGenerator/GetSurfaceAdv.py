from collections import deque
from Classes import Surface

def getSurface(level, xStart, zStart, xEnd, zEnd):
	surface = Surface(xStart, zStart, xEnd, zEnd)
	suggestedHeights = []
	for x in range(surface.xLength):
		row = []
		for z in range(surface.zLength):
			row.append(0)
		suggestedHeights.append(row)
	unresolvedSurfacePoints = deque() #Surface points which surface height needs to be calculate

	#Adds the center surface point as the first unresolved surface point
	xCenter = int((surface.xLength) / 2)
	zCenter = int((surface.zLength) / 2)
	suggestedHeights[xCenter][zCenter] = level.Height
	unresolvedSurfacePoints.append((xCenter, zCenter, level.Height))

	while unresolvedSurfacePoints:
		nextSurfacePoint = unresolvedSurfacePoints.popleft()
		x = nextSurfacePoint[0]
		z = nextSurfacePoint[1]
		suggestedHeight = nextSurfacePoint[2]
		if suggestedHeight < suggestedHeights[x][z]:
			continue
		height = getSurfacePointHeight(level, x + surface.xStart, z + surface.zStart, suggestedHeight)

		#Returns if calculated is not higher than previous recorded height
		if surface.surface[x][z].height < height:
			surface.surface[x][z].height = height
			tryAddSurfacePointToQueue(surface, suggestedHeights, unresolvedSurfacePoints, x + 1, z, height)
			tryAddSurfacePointToQueue(surface, suggestedHeights, unresolvedSurfacePoints, x - 1, z, height)
			tryAddSurfacePointToQueue(surface, suggestedHeights, unresolvedSurfacePoints, x, z + 1, height)
			tryAddSurfacePointToQueue(surface, suggestedHeights, unresolvedSurfacePoints, x, z - 1, height)
	return surface

aboveSurfaceBlocks = [0, 6, 17, 18, 31, 32, 37, 38, 39, 40, 59, 78, 81, 83, 99, 100, 103, 104, 105, 106, 111, 141, 142, 161, 162, 175]
def isSurfaceBlock(level, x, y, z):
		for block in aboveSurfaceBlocks:
			if level.blockAt(x, y, z) == block:
				return False
		return True

def getSurfacePointHeight(level, x, z, suggestedHeight):
	y = suggestedHeight + 1
	isAboveSurface = not isSurfaceBlock(level, x, y, z)
	if isAboveSurface:
		y -= 1
		while not isSurfaceBlock(level, x, y, z):
			y -= 1
		return y
	else:
		y += 1
		while isSurfaceBlock(level, x, y, z):
			y += 1
		return y - 1

def tryAddSurfacePointToQueue(surface, suggestedHeights, queue, x, z, suggestedHeight):
	#Checks if surface point is within surface border
	if x < 0 or x >= surface.xLength or z < 0 or z >= surface.zLength:
		return

	#Checks if this height has been suggested before
	if suggestedHeights[x][z] < suggestedHeight:
		suggestedHeights[x][z] = suggestedHeight
		queue.append((x, z, suggestedHeight))