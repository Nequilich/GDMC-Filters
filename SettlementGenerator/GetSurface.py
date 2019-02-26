from Classes import Surface

def getSurface(level, box):
	surface = Surface(box.maxx - box.minx, box.maxz - box.minz)
	for x in range(surface.x):
		for z in range(surface.z):
			height = getSurfaceSpotHeight(level, x + box.minx, z + box.minz)
			surface.surface[x][z].height = height
	return surface

def getSurfaceSpotHeight(level, x, z):
	heightIsFound = False
	y = 128
	while (not heightIsFound):
		if (isSurfaceBlock(level, x, y, z)):
			heightIsFound = True
		else:
			y -= 1
	return y

aboveSurfaceBlocks = [0, 6, 17, 18, 31, 32, 37, 38, 39, 40, 59, 78, 81, 83, 99, 100, 103, 104, 105, 106, 111, 141, 142, 161, 162, 175]
def isSurfaceBlock(level, x, y, z):
		for block in aboveSurfaceBlocks:
			if (level.blockAt(x, y, z) == block):
				return False
		return True