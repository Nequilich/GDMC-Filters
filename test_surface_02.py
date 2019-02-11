def perform(level, box, options):
	for x in range(box.minx, box.maxx):
		for z in range(box.minz, box.maxz):
			surfaceIsFound = False
			y = level.Height
			while (not surfaceIsFound):
				if (isSurfaceBlock(level, x, y, z)):
					surfaceIsFound = True
				else:
					y -= 1
			setBlock(level, x, y + 1, z, 20)

aboveSurfaceBlocks = [0, 6, 17, 18, 31, 32, 37, 38, 39, 40, 59]
def isSurfaceBlock(level, x, y, z):
		for block in aboveSurfaceBlocks:
			if (level.blockAt(x, y, z) == block):
				return False
		return True

def setBlock(level, x, y, z, block, data = 0):
	level.setBlockAt(x, y, z, block)
	level.setBlockDataAt(x, y, z, data)