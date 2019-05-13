from collections import deque
from Common import getMatrix
from Common import isSurfaceBlock

def calculateHeightMap(level, surface):
	suggestedHeights = getMatrix(surface.xLength, surface.zLength, 0) #Matrix of the highest suggested height for each surface point
	unresolvedSurfacePoints = deque() #Surface points which surface height needs to be calculated

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
		height = calculateSurfacePointHeight(level, x + surface.xStart, z + surface.zStart, suggestedHeight)

		#Returns if calculated is not higher than previous recorded height
		if surface.surfaceMap[x][z].height < height:
			surface.surfaceMap[x][z].height = height
			if x + 1 < surface.xLength:
				pushToQueue(unresolvedSurfacePoints, suggestedHeights, x + 1, z, height)
			if x - 1 >= 0:
				pushToQueue(unresolvedSurfacePoints, suggestedHeights, x - 1, z, height)
			if z + 1 < surface.zLength:
				pushToQueue(unresolvedSurfacePoints, suggestedHeights, x, z + 1, height)
			if z - 1 >= 0:
				pushToQueue(unresolvedSurfacePoints, suggestedHeights, x, z - 1, height)
	return surface

def calculateSurfacePointHeight(level, x, z, suggestedHeight):
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

def pushToQueue(queue, suggestedHeights, x, z, suggestedHeight):
	#Checks if this height has been suggested before
	if suggestedHeights[x][z] < suggestedHeight:
		suggestedHeights[x][z] = suggestedHeight
		queue.append((x, z, suggestedHeight))