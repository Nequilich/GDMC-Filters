def perform(level, box, options):
	removeTree(level, box.minx, box.miny, box.minz)

def setBlock(level, x, y, z, block, data = 0):
	level.setBlockAt(x, y, z, block)
	level.setBlockDataAt(x, y, z, data)

treeBlocks = [17, 18, 99, 100, 161, 162]
def isTreeBlock(level, x, y, z):
		for block in treeBlocks:
			if (level.blockAt(x, y, z) == block):
				return True
		return False

def removeTree(level, x, y, z):
	setBlock(level, x, y, z, 0)
	if (level.blockAt(x, y + 1, z) == 78): #Removes snow layer
		setBlock(level, x, y + 1, z, 0)
	neighborBlocks = [Block(x + 1, y, z), Block(x - 1, y, z), Block(x, y + 1, z), Block(x, y - 1, z), Block(x, y, z + 1), Block(x, y, z - 1)]
	for block in neighborBlocks:
		if (isTreeBlock(level, block.x, block.y, block.z)):
			removeTree(level, block.x, block.y, block.z)

class Block:

	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z