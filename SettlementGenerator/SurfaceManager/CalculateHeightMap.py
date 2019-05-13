from Common import isSurfaceBlock

def calculateHeightMap(level, surface):
	for x in range(surface.xLength):
		for z in range(surface.zLength):
			height = calculateSurfacePointHeight(level, x + surface.xStart, z + surface.zStart)
			surface.surfaceMap[x][z].height = height

def calculateSurfacePointHeight(level, x, z):
	heightIsFound = False
	y = 128
	while not heightIsFound:
		if isSurfaceBlock(level, x, y, z):
			heightIsFound = True
		else:
			y -= 1
	return y