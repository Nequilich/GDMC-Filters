def getSurface(level, box):
	surface = []
	for x in range(box.minx, box.maxx):
		row = []
		for z in range(box.minz, box.maxz):
			surfaceIsFound = False
			y = 128
			while (not surfaceIsFound):
				if (isSurfaceBlock(level, x, y, z)):
					surfaceIsFound = True
				else:
					y -= 1
			row.append(Block(y))
		surface.append(row)
	return surface

aboveSurfaceBlocks = [0, 6, 17, 18, 31, 32, 37, 38, 39, 40, 59, 78, 81, 83, 99, 100, 103, 104, 105, 106, 111, 141, 142, 161, 162, 175]
def isSurfaceBlock(level, x, y, z):
		for block in aboveSurfaceBlocks:
			if (level.blockAt(x, y, z) == block):
				return False
		return True

def setBlock(level, x, y, z, block, data = 0):
	level.setBlockAt(x, y, z, block)
	level.setBlockDataAt(x, y, z, data)

class Block:

	def __init__(self, height):
		self.height = height