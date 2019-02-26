from Common import setBlock

treeBlocks = [17, 18, 99, 100, 161, 162]
def isTreeBlock(level, x, y, z):
		for block in treeBlocks:
			if (level.blockAt(x, y, z) == block):
				return True
		return False

def removeTree(level, x, y, z):
	setBlock(level, x, y, z, 0)

	#Removes snow layer
	if (level.blockAt(x, y + 1, z) == 78):
		setBlock(level, x, y + 1, z, 0)

	#Checks if neighbor blocks are parts of the tree
	neighborBlocks = [Block(x + 1, y, z), Block(x - 1, y, z), Block(x, y + 1, z), Block(x, y - 1, z), Block(x, y, z + 1), Block(x, y, z - 1)]
	for block in neighborBlocks:
		if (isTreeBlock(level, block.x, block.y, block.z)):
			removeTree(level, block.x, block.y, block.z)

class Block:

	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z