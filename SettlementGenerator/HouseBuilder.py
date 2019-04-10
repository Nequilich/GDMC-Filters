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
	buildWindows(level, surface, prop)

def buildFloor(level, surface, prop):
	for x in range(prop.xStart + 1, prop.xEnd - 1):
		for z in range(prop.zStart + 1, prop.zEnd - 1):
			setBlock(level, surface, x, prop.height + 1, z, 4)

def buildWalls(level, surface, prop):
	for x in range(prop.xStart + 2, prop.xEnd - 2):
		for y in range(prop.height + 2, prop.height + 5):
			setBlock(level, surface, x, y, prop.zStart + 1, 5)
			setBlock(level, surface, x, y, prop.zEnd - 2, 5)
	for z in range(prop.zStart + 2, prop.zEnd - 2):
		for y in range(prop.height + 2, prop.height + 5):
			setBlock(level, surface, prop.xStart + 1, y, z, 5)
			setBlock(level, surface, prop.xEnd - 2, y, z, 5)
	for y in range(prop.height + 2, prop.height + 5):
		setBlock(level, surface, prop.xStart + 1, y, prop.zStart + 1, 17)
		setBlock(level, surface, prop.xStart + 1, y, prop.zEnd - 2, 17)
		setBlock(level, surface, prop.xEnd - 2, y, prop.zStart + 1, 17)
		setBlock(level, surface, prop.xEnd - 2, y, prop.zEnd - 2, 17)

def buildCeiling(level, surface, prop):
	y = prop.height + 5
	for x in range(prop.xStart + 2, prop.xEnd - 2):
		for z in range(prop.zStart + 2, prop.zEnd - 2):
			setBlock(level, surface, x, y, z, 5)

def buildRoofNS(level, surface, prop):
	y = prop.height + 5
	for x in range(prop.xStart + 1, prop.xEnd - 1):
		setBlock(level, surface, x, y, prop.zStart + 1, 17, 4)
		setBlock(level, surface, x, y, prop.zEnd - 2, 17, 4)
	y = prop.height + 6
	for x in range(prop.xStart + 2, prop.xEnd - 2):
		setBlock(level, surface, x, y, prop.zStart + 1, 17, 4)
		setBlock(level, surface, x, y, prop.zEnd - 2, 17, 4)
	
	y = prop.height + 5
	for z in range(prop.zStart + 1, prop.zEnd - 1):
		setBlock(level, surface, prop.xStart, y, z, 17, 8)
		setBlock(level, surface, prop.xStart + 1, y + 1, z, 17, 8)
		setBlock(level, surface, prop.xEnd - 1, y, z, 17, 8)
		setBlock(level, surface, prop.xEnd - 2, y + 1, z, 17, 8)
		for x in range(prop.xStart + 2, prop.xEnd - 2):
			setBlock(level, surface, x, y + 2, z, 17, 8)

def buildRoofEW(level, surface, prop):
	y = prop.height + 5
	for z in range(prop.zStart + 1, prop.zEnd - 1):
		setBlock(level, surface, prop.xStart + 1, y, z, 17, 8)
		setBlock(level, surface, prop.xEnd - 2, y, z, 17, 8)
	y = prop.height + 6
	for z in range(prop.zStart + 2, prop.zEnd - 2):
		setBlock(level, surface, prop.xStart + 1, y, z, 17, 8)
		setBlock(level, surface, prop.xEnd - 2, y, z, 17, 8)
	
	y = prop.height + 5
	for x in range(prop.xStart + 1, prop.xEnd - 1):
		setBlock(level, surface, x, y, prop.zStart, 17, 4)
		setBlock(level, surface, x, y + 1, prop.zStart + 1, 17, 4)
		setBlock(level, surface, x, y, prop.zEnd - 1, 17, 4)
		setBlock(level, surface, x, y + 1, prop.zEnd - 2, 17, 4)
		for z in range(prop.zStart + 2, prop.zEnd - 2):
			setBlock(level, surface, x, y + 2, z, 17, 4)

def buildDoor(level, surface, prop):
	if prop.doorDirection == "NORTH":
		x = prop.xStart + prop.xLength / 2
		# Stair
		if isSurfaceBlock(level, x + surface.xStart, prop.height + 1, prop.zStart - 1 + surface.zStart):
			setBlock(level, surface, x, prop.height + 1, prop.zStart, 4)
		else:
			setBlock(level, surface, x, prop.height + 1, prop.zStart, 67, 2)
		# Door
		setBlock(level, surface, x, prop.height + 2, prop.zStart + 1, 64, 1)
		setBlock(level, surface, x, prop.height + 3, prop.zStart + 1, 64, 9)
		# Torch
		setBlock(level, surface, x + 1, prop.height + 3, prop.zStart + 2, 50, 3)
		setBlock(level, surface, x - 1, prop.height + 3, prop.zStart + 2, 50, 3)
	elif prop.doorDirection == "EAST":
		z = prop.zStart + prop.zLength / 2
		# Stair
		if isSurfaceBlock(level, prop.xEnd + surface.xStart, prop.height + 1, z + surface.zStart):
			setBlock(level, surface, prop.xEnd - 1, prop.height + 1, z, 4)
		else:
			setBlock(level, surface, prop.xEnd - 1, prop.height + 1, z, 67, 1)
		# Door
		setBlock(level, surface, prop.xEnd - 2, prop.height + 2, z, 64, 2)
		setBlock(level, surface, prop.xEnd - 2, prop.height + 3, z, 64, 9)
		# Torch
		setBlock(level, surface, prop.xEnd - 3, prop.height + 3, z + 1, 50, 2)
		setBlock(level, surface, prop.xEnd - 3, prop.height + 3, z - 1, 50, 2)
	elif prop.doorDirection == "SOUTH":
		x = prop.xStart + prop.xLength / 2
		# Stair
		if isSurfaceBlock(level, x + surface.xStart, prop.height + 1, prop.zEnd + surface.zStart):
			setBlock(level, surface, x, prop.height + 1, prop.zEnd - 1, 4)
		else:
			setBlock(level, surface, x, prop.height + 1, prop.zEnd - 1, 67, 3)
		# Door
		setBlock(level, surface, x, prop.height + 2, prop.zEnd - 2, 64, 3)
		setBlock(level, surface, x, prop.height + 3, prop.zEnd - 2, 64, 9)
		# Torch
		setBlock(level, surface, x + 1, prop.height + 3, prop.zEnd - 3, 50, 4)
		setBlock(level, surface, x - 1, prop.height + 3, prop.zEnd - 3, 50, 4)
	elif prop.doorDirection == "WEST":
		z = prop.zStart + prop.zLength / 2
		# Stair
		if isSurfaceBlock(level, prop.xStart - 1 + surface.xStart, prop.height + 1, z + surface.zStart):
			setBlock(level, surface, prop.xStart, prop.height + 1, z, 4)
		else:
			setBlock(level, surface, prop.xStart, prop.height + 1, z, 67, 0)
		# Door
		setBlock(level, surface, prop.xStart + 1, prop.height + 2, z, 64, 0)
		setBlock(level, surface, prop.xStart + 1, prop.height + 3, z, 64, 9)
		# Torch
		setBlock(level, surface, prop.xStart + 2, prop.height + 3, z + 1, 50, 1)
		setBlock(level, surface, prop.xStart + 2, prop.height + 3, z - 1, 50, 1)

aboveSurfaceBlocks = [0, 6, 17, 18, 31, 32, 37, 38, 39, 40, 59, 78, 81, 83, 99, 100, 103, 104, 105, 106, 111, 141, 142, 161, 162, 175]
def isSurfaceBlock(level, x, y, z):
	for block in aboveSurfaceBlocks:
		if level.blockAt(x, y, z) == block:
			return False
	return True

def buildWindows(level, surface, prop):
	if prop.doorDirection != "NORTH":
		x = prop.xStart + 3
		i = 0
		while x < prop.xEnd - 3:
			if i % 2 == 0:
				setBlock(level, surface, x, prop.height + 3, prop.zStart + 1, 102)
			x += 1
			i += 1
	if prop.doorDirection != "EAST":
		z = prop.zStart + 3
		i = 0
		while z < prop.zEnd - 3:
			if i % 2 == 0:
				setBlock(level, surface, prop.xEnd - 2, prop.height + 3, z, 102)
			z += 1
			i += 1
	if prop.doorDirection != "SOUTH":
		x = prop.xStart + 3
		i = 0
		while x < prop.xEnd - 3:
			if i % 2 == 0:
				setBlock(level, surface, x, prop.height + 3, prop.zEnd - 2, 102)
			x += 1
			i += 1
	if prop.doorDirection != "WEST":
		z = prop.zStart + 3
		i = 0
		while z < prop.zEnd - 3:
			if i % 2 == 0:
				setBlock(level, surface, prop.xStart + 1, prop.height + 3, z, 102)
			z += 1
			i += 1