from Classes import Property
from Common import setBlock

def buildHouse(level, surface, prop):
	if prop.xLength < 7 or prop.zLength < 7:
		return
	buildFloor(level, surface, prop)
	buildWalls(level, surface, prop)
	buildCeiling(level, surface, prop)
	if prop.doorDirection == "NORTH" or prop.doorDirection == "SOUTH":
		buildRoofNS(level, surface, prop)
	else:
		buildRoofEW(level, surface, prop)
	buildDoor(level, surface, prop)

def buildFloor(level, surface, prop):
	for x in range(prop.xStart + 1, prop.xEnd - 1):
		for z in range(prop.zStart + 1, prop.zEnd - 1):
			setBlock(level, x + surface.xStart, prop.height + 1, z + surface.zStart, 4)

def buildWalls(level, surface, prop):
	for x in range(prop.xStart + 2, prop.xEnd - 2):
		for y in range(prop.height + 2, prop.height + 5):
			setBlock(level, x + surface.xStart, y, prop.zStart + 1 + surface.zStart, 5)
			setBlock(level, x + surface.xStart, y, prop.zEnd - 2 + surface.zStart, 5)
	for z in range(prop.zStart + 2, prop.zEnd - 2):
		for y in range(prop.height + 2, prop.height + 5):
			setBlock(level, prop.xStart + 1 + surface.xStart, y, z + surface.zStart, 5)
			setBlock(level, prop.xEnd - 2 + surface.xStart, y, z + surface.zStart, 5)
	for y in range(prop.height + 2, prop.height + 5):
		setBlock(level, prop.xStart + 1 + surface.xStart, y, prop.zStart + 1 + surface.zStart, 17)
		setBlock(level, prop.xStart + 1 + surface.xStart, y, prop.zEnd - 2 + surface.zStart, 17)
		setBlock(level, prop.xEnd - 2 + surface.xStart, y, prop.zStart + 1 + surface.zStart, 17)
		setBlock(level, prop.xEnd - 2 + surface.xStart, y, prop.zEnd - 2 + surface.zStart, 17)

def buildCeiling(level, surface, prop):
	y = prop.height + 5
	for x in range(prop.xStart + 2, prop.xEnd - 2):
		for z in range(prop.zStart + 2, prop.zEnd - 2):
			setBlock(level, x + surface.xStart, y, z + surface.zStart, 5)

def buildRoofNS(level, surface, prop):
	y = prop.height + 5
	for x in range(prop.xStart + 1, prop.xEnd - 1):
		setBlock(level, x + surface.xStart, y, prop.zStart + 1 + surface.zStart, 17, 4)
		setBlock(level, x + surface.xStart, y, prop.zEnd - 2 + surface.zStart, 17, 4)
	y = prop.height + 6
	for x in range(prop.xStart + 2, prop.xEnd - 2):
		setBlock(level, x + surface.xStart, y, prop.zStart + 1 + surface.zStart, 17, 4)
		setBlock(level, x + surface.xStart, y, prop.zEnd - 2 + surface.zStart, 17, 4)
	
	y = prop.height + 5
	for z in range(prop.zStart + 1, prop.zEnd - 1):
		setBlock(level, prop.xStart + surface.xStart, y, z + surface.zStart, 17, 8)
		setBlock(level, prop.xStart + 1 + surface.xStart, y + 1, z + surface.zStart, 17, 8)
		setBlock(level, prop.xEnd - 1 + surface.xStart, y, z + surface.zStart, 17, 8)
		setBlock(level, prop.xEnd - 2 + surface.xStart, y + 1, z + surface.zStart, 17, 8)
		for x in range(prop.xStart + 2, prop.xEnd - 2):
			setBlock(level, x + surface.xStart, y + 2, z + surface.zStart, 17, 8)

def buildRoofEW(level, surface, prop):
	y = prop.height + 5
	for z in range(prop.zStart + 1, prop.zEnd - 1):
		setBlock(level, prop.xStart + 1 + surface.xStart, y, z + surface.zStart, 17, 8)
		setBlock(level, prop.xEnd - 2 + surface.xStart, y, z + surface.zStart, 17, 8)
	y = prop.height + 6
	for z in range(prop.zStart + 2, prop.zEnd - 2):
		setBlock(level, prop.xStart + 1 + surface.xStart, y, z + surface.zStart, 17, 8)
		setBlock(level, prop.xEnd - 2 + surface.xStart, y, z + surface.zStart, 17, 8)
	
	y = prop.height + 5
	for x in range(prop.xStart + 1, prop.xEnd - 1):
		setBlock(level, x + surface.xStart, y, prop.zStart + surface.zStart, 17, 4)
		setBlock(level, x + surface.xStart, y + 1, prop.zStart + 1 + surface.zStart, 17, 4)
		setBlock(level, x + surface.xStart, y, prop.zEnd - 1 + surface.zStart, 17, 4)
		setBlock(level, x + surface.xStart, y + 1, prop.zEnd - 2 + surface.zStart, 17, 4)
		for z in range(prop.zStart + 2, prop.zEnd - 2):
			setBlock(level, x + surface.xStart, y + 2, z + surface.zStart, 17, 4)

def buildDoor(level, surface, prop):
	if prop.doorDirection == "NORTH":
		if isSurfaceBlock(level, prop.xStart + prop.xLength / 2 + surface.xStart, prop.height + 1, prop.zStart - 1 + surface.zStart):
			setBlock(level, prop.xStart + prop.xLength / 2 + surface.xStart, prop.height + 1, prop.zStart + surface.zStart, 4)
		else:
			setBlock(level, prop.xStart + prop.xLength / 2 + surface.xStart, prop.height + 1, prop.zStart + surface.zStart, 67, 2)
		setBlock(level, prop.xStart + prop.xLength / 2 + surface.xStart, prop.height + 2, prop.zStart + 1 + surface.zStart, 64, 1)
		setBlock(level, prop.xStart + prop.xLength / 2 + surface.xStart, prop.height + 3, prop.zStart + 1 + surface.zStart, 64, 9)
	elif prop.doorDirection == "EAST":
		if isSurfaceBlock(level, prop.xEnd + surface.xStart, prop.height + 1, prop.zStart + prop.zLength / 2 + surface.zStart):
			setBlock(level, prop.xEnd - 1 + surface.xStart, prop.height + 1, prop.zStart + prop.zLength / 2 + surface.zStart, 4)
		else:
			setBlock(level, prop.xEnd - 1 + surface.xStart, prop.height + 1, prop.zStart + prop.zLength / 2 + surface.zStart, 67, 1)
		setBlock(level, prop.xEnd - 2 + surface.xStart, prop.height + 2, prop.zStart + prop.zLength / 2 + surface.zStart, 64, 2)
		setBlock(level, prop.xEnd - 2 + surface.xStart, prop.height + 3, prop.zStart + prop.zLength / 2 + surface.zStart, 64, 9)
	elif prop.doorDirection == "SOUTH":
		if isSurfaceBlock(level, prop.xStart + prop.xLength / 2 + surface.xStart, prop.height + 1, prop.zEnd + surface.zStart):
			setBlock(level, prop.xStart + prop.xLength / 2 + surface.xStart, prop.height + 1, prop.zEnd - 1 + surface.zStart, 4)
		else:
			setBlock(level, prop.xStart + prop.xLength / 2 + surface.xStart, prop.height + 1, prop.zEnd - 1 + surface.zStart, 67, 3)
		setBlock(level, prop.xStart + prop.xLength / 2 + surface.xStart, prop.height + 2, prop.zEnd - 2 + surface.zStart, 64, 3)
		setBlock(level, prop.xStart + prop.xLength / 2 + surface.xStart, prop.height + 3, prop.zEnd - 2 + surface.zStart, 64, 9)
	elif prop.doorDirection == "WEST":
		if isSurfaceBlock(level, prop.xStart - 1 + surface.xStart, prop.height + 1, prop.zStart + prop.zLength / 2 + surface.zStart):
			setBlock(level, prop.xStart + surface.xStart, prop.height + 1, prop.zStart + prop.zLength / 2 + surface.zStart, 4)
		else:
			setBlock(level, prop.xStart + surface.xStart, prop.height + 1, prop.zStart + prop.zLength / 2 + surface.zStart, 67, 0)
		setBlock(level, prop.xStart + 1 + surface.xStart, prop.height + 2, prop.zStart + prop.zLength / 2 + surface.zStart, 64, 0)
		setBlock(level, prop.xStart + 1 + surface.xStart, prop.height + 3, prop.zStart + prop.zLength / 2 + surface.zStart, 64, 9)

aboveSurfaceBlocks = [0, 6, 17, 18, 31, 32, 37, 38, 39, 40, 59, 78, 81, 83, 99, 100, 103, 104, 105, 106, 111, 141, 142, 161, 162, 175]
def isSurfaceBlock(level, x, y, z):
	for block in aboveSurfaceBlocks:
		if level.blockAt(x, y, z) == block:
			return False
	return True