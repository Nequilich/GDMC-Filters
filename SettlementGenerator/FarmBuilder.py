from Common import setBlock
from RemoveTree import removeTree

def buildPatch(level, surface, prop):
	if prop.xLength < 5 or prop.zLength < 5 or prop.height > 90:
		return
	buildField(level, surface, prop)
	buildSides(level, surface, prop)

def clearPatchProperty(level, surface, prop):
	for x in range(prop.xStart, prop.xEnd):
		for z in range(prop.zStart, prop.zEnd):
			for y in range(prop.height + 2, prop.height + 4):
				removeTree(level, x + surface.xStart, y, z + surface.zStart)
				setBlock(level, surface, x, y, z, 0)

def buildField(level, surface, prop):
	y = prop.height + 1
	for x in range(prop.xStart + 1, prop.xEnd - 1):
		for z in range(prop.zStart + 1, prop.zEnd - 1):
			setBlock(level, surface, x, y, z, 60)
			setBlock(level, surface, x, y + 1, z, 59, 7)

	setBlock(level, surface, prop.xStart + prop.xLength / 2, y, prop.zStart + prop.zLength / 2, 9)
	setBlock(level, surface, prop.xStart + prop.xLength / 2, y + 1, prop.zStart + prop.zLength / 2, 0)

def buildSides(level, surface, prop):
	# Corners
	y = prop.height + 1
	for p in [(prop.xStart, prop.zStart), (prop.xStart, prop.zEnd - 1), (prop.xEnd - 1, prop.zStart), (prop.xEnd - 1, prop.zEnd - 1)]:
		setBlock(level, surface, p[0], y, p[1], 17)
		setBlock(level, surface, p[0], y + 1, p[1], 17)
		setBlock(level, surface, p[0], y + 2, p[1], 50, 5)

	buildNorthSide(level, surface, prop)
	buildEastSide(level, surface, prop)
	buildSouthSide(level, surface, prop)
	buildWestSide(level, surface, prop)

def buildNorthSide(level, surface, prop):
	y = prop.height + 1
	if prop.doorDirection == "NORTH":
		setBlock(level, surface, prop.xStart + 1, y, prop.zStart, 5)
		setBlock(level, surface, prop.xStart + 1, y + 1, prop.zStart, 85)
		setBlock(level, surface, prop.xEnd - 2, y, prop.zStart, 5)
		setBlock(level, surface, prop.xEnd - 2, y + 1, prop.zStart, 85)
		for x in range(prop.xStart + 2, prop.xEnd - 2):
			if isSurfaceBlock(level, x + surface.xStart, y, prop.zStart - 1 + surface.zStart):
				setBlock(level, surface, x, y, prop.zStart, 5)
			else:
				setBlock(level, surface, x, y, prop.zStart, 53, 2)
	else:
		for x in range(prop.xStart + 1, prop.xEnd - 1):
			setBlock(level, surface, x, y, prop.zStart, 5)
			setBlock(level, surface, x, y + 1, prop.zStart, 85)

def buildEastSide(level, surface, prop):
	y = prop.height + 1
	if prop.doorDirection == "EAST":
		setBlock(level, surface, prop.xEnd - 1, y, prop.zStart + 1, 5)
		setBlock(level, surface, prop.xEnd - 1, y + 1, prop.zStart + 1, 85)
		setBlock(level, surface, prop.xEnd - 1, y, prop.zEnd - 2, 5)
		setBlock(level, surface, prop.xEnd - 1, y + 1, prop.zEnd - 2, 85)
		for z in range(prop.zStart + 2, prop.zEnd - 2):
			if isSurfaceBlock(level, prop.xEnd + surface.xStart, y, z + surface.zStart):
				setBlock(level, surface, prop.xEnd - 1, y, z, 5)
			else:
				setBlock(level, surface, prop.xEnd - 1, y, z, 53, 1)
	else:
		for z in range(prop.zStart + 1, prop.zEnd - 1):
			setBlock(level, surface, prop.xEnd - 1, y, z, 5)
			setBlock(level, surface, prop.xEnd - 1, y + 1, z, 85)

def buildSouthSide(level, surface, prop):
	y = prop.height + 1
	if prop.doorDirection == "SOUTH":
		setBlock(level, surface, prop.xStart + 1, y, prop.zEnd - 1, 5)
		setBlock(level, surface, prop.xStart + 1, y + 1, prop.zEnd - 1, 85)
		setBlock(level, surface, prop.xEnd - 2, y, prop.zEnd - 1, 5)
		setBlock(level, surface, prop.xEnd - 2, y + 1, prop.zEnd - 1, 85)
		for x in range(prop.xStart + 2, prop.xEnd - 2):
			if isSurfaceBlock(level, x + surface.xStart, y, prop.zEnd + surface.zStart):
				setBlock(level, surface, x, y, prop.zEnd - 1, 5)
			else:
				setBlock(level, surface, x, y, prop.zEnd - 1, 53, 3)
	else:
		for x in range(prop.xStart + 1, prop.xEnd - 1):
			setBlock(level, surface, x, y, prop.zEnd - 1, 5)
			setBlock(level, surface, x, y + 1, prop.zEnd - 1, 85)

def buildWestSide(level, surface, prop):
	y = prop.height + 1
	if prop.doorDirection == "WEST":
		setBlock(level, surface, prop.xStart, y, prop.zStart + 1, 5)
		setBlock(level, surface, prop.xStart, y + 1, prop.zStart + 1, 85)
		setBlock(level, surface, prop.xStart, y, prop.zEnd - 2, 5)
		setBlock(level, surface, prop.xStart, y + 1, prop.zEnd - 2, 85)
		for z in range(prop.zStart + 2, prop.zEnd - 2):
			if isSurfaceBlock(level, prop.xStart - 1 + surface.xStart, y, z + surface.zStart):
				setBlock(level, surface, prop.xStart, y, z, 5)
			else:
				setBlock(level, surface, prop.xStart, y, z, 53, 0)
	else:
		for z in range(prop.zStart + 1, prop.zEnd - 1):
			setBlock(level, surface, prop.xStart, y, z, 5)
			setBlock(level, surface, prop.xStart, y + 1, z, 85)

aboveSurfaceBlocks = [0, 6, 17, 18, 31, 32, 37, 38, 39, 40, 59, 78, 81, 83, 99, 100, 103, 104, 105, 106, 111, 141, 142, 161, 162, 175]
def isSurfaceBlock(level, x, y, z):
	for block in aboveSurfaceBlocks:
		if level.blockAt(x, y, z) == block:
			return False
	return True