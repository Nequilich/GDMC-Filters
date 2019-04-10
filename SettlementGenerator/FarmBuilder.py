from Common import setBlock

def buildPatch(level, surface, prop):
	for x in range(prop.xStart, prop.xEnd):
		for z in range(prop.zStart, prop.zEnd):
			y = surface.surfaceMap[x][z].height + 1
			setBlock(level, surface, x, y, z, 4)