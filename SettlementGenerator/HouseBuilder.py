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

def buildFloor(level, surface, prop):
	for x in range(prop.xStart + 1, prop.xEnd - 1):
		for z in range(prop.zStart + 1, prop.zEnd - 1):
			setBlock(level, x + surface.xStart, prop.height, z + surface.zStart, 4)

def buildWalls(level, surface, prop):
	for x in range(prop.xStart + 2, prop.xEnd - 2):
		for y in range(prop.height + 1, prop.height + 4):
			setBlock(level, x + surface.xStart, y, prop.zStart + 1 + surface.zStart, 5)
			setBlock(level, x + surface.xStart, y, prop.zEnd - 2 + surface.zStart, 5)
	for z in range(prop.zStart + 2, prop.zEnd - 2):
		for y in range(prop.height + 1, prop.height + 4):
			setBlock(level, prop.xStart + 1 + surface.xStart, y, z + surface.zStart, 5)
			setBlock(level, prop.xEnd - 2 + surface.xStart, y, z + surface.zStart, 5)
	for y in range(prop.height + 1, prop.height + 4):
		setBlock(level, prop.xStart + 1 + surface.xStart, y, prop.zStart + 1 + surface.zStart, 17)
		setBlock(level, prop.xStart + 1 + surface.xStart, y, prop.zEnd - 2 + surface.zStart, 17)
		setBlock(level, prop.xEnd - 2 + surface.xStart, y, prop.zStart + 1 + surface.zStart, 17)
		setBlock(level, prop.xEnd - 2 + surface.xStart, y, prop.zEnd - 2 + surface.zStart, 17)

def buildCeiling(level, surface, prop):
	y = prop.height + 4
	for x in range(prop.xStart + 2, prop.xEnd - 2):
		for z in range(prop.zStart + 2, prop.zEnd - 2):
			setBlock(level, x + surface.xStart, y, z + surface.zStart, 5)

def buildRoofNS(level, surface, prop):
	y = prop.height + 4
	for x in range(prop.xStart + 1, prop.xEnd - 1):
		setBlock(level, x + surface.xStart, y, prop.zStart + 1 + surface.zStart, 17, 4)
		setBlock(level, x + surface.xStart, y, prop.zEnd - 2 + surface.zStart, 17, 4)
	y = prop.height + 5
	for x in range(prop.xStart + 2, prop.xEnd - 2):
		setBlock(level, x + surface.xStart, y, prop.zStart + 1 + surface.zStart, 17, 4)
		setBlock(level, x + surface.xStart, y, prop.zEnd - 2 + surface.zStart, 17, 4)
	
	y = prop.height + 4
	for z in range(prop.zStart + 1, prop.zEnd - 1):
		setBlock(level, prop.xStart + surface.xStart, y, z + surface.zStart, 17, 8)
		setBlock(level, prop.xStart + 1 + surface.xStart, y + 1, z + surface.zStart, 17, 8)
		setBlock(level, prop.xEnd - 1 + surface.xStart, y, z + surface.zStart, 17, 8)
		setBlock(level, prop.xEnd - 2 + surface.xStart, y + 1, z + surface.zStart, 17, 8)
		for x in range(prop.xStart + 2, prop.xEnd - 2):
			setBlock(level, x + surface.xStart, y + 2, z + surface.zStart, 17, 8)

def buildRoofEW(level, surface, prop):
	y = prop.height + 4
	for z in range(prop.zStart + 1, prop.zEnd - 1):
		setBlock(level, prop.xStart + 1 + surface.xStart, y, z + surface.zStart, 17, 8)
		setBlock(level, prop.xEnd - 2 + surface.xStart, y, z + surface.zStart, 17, 8)
	y = prop.height + 5
	for z in range(prop.zStart + 2, prop.zEnd - 2):
		setBlock(level, prop.xStart + 1 + surface.xStart, y, z + surface.zStart, 17, 8)
		setBlock(level, prop.xEnd - 2 + surface.xStart, y, z + surface.zStart, 17, 8)
	
	y = prop.height + 4
	for x in range(prop.xStart + 1, prop.xEnd - 1):
		setBlock(level, x + surface.xStart, y, prop.zStart + surface.zStart, 17, 4)
		setBlock(level, x + surface.xStart, y + 1, prop.zStart + 1 + surface.zStart, 17, 4)
		setBlock(level, x + surface.xStart, y, prop.zEnd - 1 + surface.zStart, 17, 4)
		setBlock(level, x + surface.xStart, y + 1, prop.zEnd - 2 + surface.zStart, 17, 4)
		for z in range(prop.zStart + 2, prop.zEnd - 2):
			setBlock(level, x + surface.xStart, y + 2, z + surface.zStart, 17, 4)