from BiomeMaterials import get_biome_materials
from Common import setBlock
from RemoveTree import removeTree

def buildPatch(level, surface, prop):
	if prop.xLength < 5 or prop.zLength < 5 or prop.height > 90:
		return

	getMaterials(surface, prop)
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
		setBlock(level, surface, p[0], y, p[1], materials["wood"]["default"][0], materials["wood"]["default"][1])
		setBlock(level, surface, p[0], y + 1, p[1], materials["wood"]["default"][0], materials["wood"]["default"][1])
		setBlock(level, surface, p[0], y + 2, p[1], materials["torch"]["default"][0], materials["torch"]["default"][1])

	buildNorthSide(level, surface, prop)
	buildEastSide(level, surface, prop)
	buildSouthSide(level, surface, prop)
	buildWestSide(level, surface, prop)

def buildNorthSide(level, surface, prop):
	y = prop.height + 1
	if prop.doorDirection == "NORTH":
		setBlock(level, surface, prop.xStart + 1, y, prop.zStart, materials["wood_planks"]["default"][0], materials["wood_planks"]["default"][1])
		setBlock(level, surface, prop.xStart + 1, y + 1, prop.zStart, materials["fence"]["default"][0], materials["fence"]["default"][1])
		setBlock(level, surface, prop.xEnd - 2, y, prop.zStart, materials["wood_planks"]["default"][0], materials["wood_planks"]["default"][1])
		setBlock(level, surface, prop.xEnd - 2, y + 1, prop.zStart, materials["fence"]["default"][0], materials["fence"]["default"][1])
		for x in range(prop.xStart + 2, prop.xEnd - 2):
			if isSurfaceBlock(level, x + surface.xStart, y, prop.zStart - 1 + surface.zStart):
				setBlock(level, surface, x, y, prop.zStart, materials["wood_planks"]["default"][0], materials["wood_planks"]["default"][1])
			else:
				setBlock(level, surface, x, y, prop.zStart, materials["wood_planks"]["directions"]["south"]["bottom"][0], materials["wood_planks"]["directions"]["south"]["bottom"][1])
	else:
		for x in range(prop.xStart + 1, prop.xEnd - 1):
			setBlock(level, surface, x, y, prop.zStart, materials["wood_planks"]["default"][0], materials["wood_planks"]["default"][1])
			setBlock(level, surface, x, y + 1, prop.zStart, materials["fence"]["default"][0], materials["fence"]["default"][1])

def buildEastSide(level, surface, prop):
	y = prop.height + 1
	if prop.doorDirection == "EAST":
		setBlock(level, surface, prop.xEnd - 1, y, prop.zStart + 1, materials["wood_planks"]["default"][0], materials["wood_planks"]["default"][1])
		setBlock(level, surface, prop.xEnd - 1, y + 1, prop.zStart + 1, materials["fence"]["default"][0], materials["fence"]["default"][1])
		setBlock(level, surface, prop.xEnd - 1, y, prop.zEnd - 2, materials["wood_planks"]["default"][0], materials["wood_planks"]["default"][1])
		setBlock(level, surface, prop.xEnd - 1, y + 1, prop.zEnd - 2, materials["fence"]["default"][0], materials["fence"]["default"][1])
		for z in range(prop.zStart + 2, prop.zEnd - 2):
			if isSurfaceBlock(level, prop.xEnd + surface.xStart, y, z + surface.zStart):
				setBlock(level, surface, prop.xEnd - 1, y, z, materials["wood_planks"]["default"][0], materials["wood_planks"]["default"][1])
			else:
				setBlock(level, surface, prop.xEnd - 1, y, z, materials["wood_planks"]["directions"]["west"]["bottom"][0], materials["wood_planks"]["directions"]["west"]["bottom"][1])
	else:
		for z in range(prop.zStart + 1, prop.zEnd - 1):
			setBlock(level, surface, prop.xEnd - 1, y, z, materials["wood_planks"]["default"][0], materials["wood_planks"]["default"][1])
			setBlock(level, surface, prop.xEnd - 1, y + 1, z, materials["fence"]["default"][0], materials["fence"]["default"][1])

def buildSouthSide(level, surface, prop):
	y = prop.height + 1
	if prop.doorDirection == "SOUTH":
		setBlock(level, surface, prop.xStart + 1, y, prop.zEnd - 1, materials["wood_planks"]["default"][0], materials["wood_planks"]["default"][1])
		setBlock(level, surface, prop.xStart + 1, y + 1, prop.zEnd - 1, materials["fence"]["default"][0], materials["fence"]["default"][1])
		setBlock(level, surface, prop.xEnd - 2, y, prop.zEnd - 1, materials["wood_planks"]["default"][0], materials["wood_planks"]["default"][1])
		setBlock(level, surface, prop.xEnd - 2, y + 1, prop.zEnd - 1, materials["fence"]["default"][0], materials["fence"]["default"][1])
		for x in range(prop.xStart + 2, prop.xEnd - 2):
			if isSurfaceBlock(level, x + surface.xStart, y, prop.zEnd + surface.zStart):
				setBlock(level, surface, x, y, prop.zEnd - 1, materials["wood_planks"]["default"][0], materials["wood_planks"]["default"][1])
			else:
				setBlock(level, surface, x, y, prop.zEnd - 1, materials["wood_planks"]["directions"]["north"]["bottom"][0], materials["wood_planks"]["directions"]["north"]["bottom"][1])
	else:
		for x in range(prop.xStart + 1, prop.xEnd - 1):
			setBlock(level, surface, x, y, prop.zEnd - 1, materials["wood_planks"]["default"][0], materials["wood_planks"]["default"][1])
			setBlock(level, surface, x, y + 1, prop.zEnd - 1, materials["fence"]["default"][0], materials["fence"]["default"][1])

def buildWestSide(level, surface, prop):
	y = prop.height + 1
	if prop.doorDirection == "WEST":
		setBlock(level, surface, prop.xStart, y, prop.zStart + 1, materials["wood_planks"]["default"][0], materials["wood_planks"]["default"][1])
		setBlock(level, surface, prop.xStart, y + 1, prop.zStart + 1, materials["fence"]["default"][0], materials["fence"]["default"][1])
		setBlock(level, surface, prop.xStart, y, prop.zEnd - 2, materials["wood_planks"]["default"][0], materials["wood_planks"]["default"][1])
		setBlock(level, surface, prop.xStart, y + 1, prop.zEnd - 2, materials["fence"]["default"][0], materials["fence"]["default"][1])
		for z in range(prop.zStart + 2, prop.zEnd - 2):
			if isSurfaceBlock(level, prop.xStart - 1 + surface.xStart, y, z + surface.zStart):
				setBlock(level, surface, prop.xStart, y, z, materials["wood_planks"]["default"][0], materials["wood_planks"]["default"][1])
			else:
				setBlock(level, surface, prop.xStart, y, z, materials["wood_planks"]["directions"]["east"]["bottom"][0], materials["wood_planks"]["directions"]["east"]["bottom"][1])
	else:
		for z in range(prop.zStart + 1, prop.zEnd - 1):
			setBlock(level, surface, prop.xStart, y, z, materials["wood_planks"]["default"][0], materials["wood_planks"]["default"][1])
			setBlock(level, surface, prop.xStart, y + 1, z, materials["fence"]["default"][0], materials["fence"]["default"][1])

aboveSurfaceBlocks = [0, 6, 17, 18, 31, 32, 37, 38, 39, 40, 59, 78, 81, 83, 99, 100, 103, 104, 105, 106, 111, 141, 142, 161, 162, 175]
def isSurfaceBlock(level, x, y, z):
	for block in aboveSurfaceBlocks:
		if level.blockAt(x, y, z) == block:
			return False
	return True

def getMaterials(surface, prop):
	biomeId = surface.surfaceMap[prop.xStart][prop.zStart].biomeId

	global materials
	materials = get_biome_materials(biomeId)

def buildAnimalPen(level, surface, prop):
	# Grass
	y = prop.height + 1
	for x in range(prop.xStart + 1, prop.xEnd - 1):
		for z in range(prop.zStart + 1, prop.zEnd - 1):
			setBlock(level, surface, x, y, z, 2)
	# Fence
	for x in range(prop.xStart, prop.xEnd):
		setBlock(level, surface, x, y, prop.zStart, 4)
		setBlock(level, surface, x, y + 1, prop.zStart, 85)
		setBlock(level, surface, x, y, prop.zEnd - 1, 4)
		setBlock(level, surface, x, y + 1, prop.zEnd - 1, 85)
	for z in range(prop.zStart + 1, prop.zEnd - 1):
		setBlock(level, surface, prop.xStart, y, z, 4)
		setBlock(level, surface, prop.xStart, y + 1, z, 85)
		setBlock(level, surface, prop.xEnd - 1, y, z, 4)
		setBlock(level, surface, prop.xEnd - 1, y + 1, z, 85)
	# Torches
	setBlock(level, surface, prop.xStart, y + 2, prop.zStart, 50, 5)
	setBlock(level, surface, prop.xStart, y + 2, prop.zEnd - 1, 50, 5)
	setBlock(level, surface, prop.xEnd - 1, y + 2, prop.zStart, 50, 5)
	setBlock(level, surface, prop.xEnd - 1, y + 2, prop.zEnd - 1, 50, 5)
	# Gate
	if prop.doorDirection == "North":
		x = prop.xStart + prop.xLength / 2
		setBlock(level, surface, x, y + 1, prop.zStart, 107, 0)
		if isSurfaceBlock(level, x + surface.xStart, y, prop.zStart - 1 + surface.zStart):
			setBlock(level, surface, x, y, prop.zStart, 4)
		else:
			setBlock(level, surface, x, y, prop.zStart, 67, 0)
	if prop.doorDirection == "East":
		z = prop.zStart + prop.zLength / 2
		setBlock(level, surface, prop.xEnd - 1, y + 1, z, 107, 1)
		if isSurfaceBlock(level, prop.xEnd + surface.xStart, y, z + surface.zStart):
			setBlock(level, surface, prop.xEnd - 1, y, z, 4)
		else:
			setBlock(level, surface, prop.xEnd - 1, y, z, 67, 1)
	if prop.doorDirection == "South":
		x = prop.xStart + prop.xLength / 2
		setBlock(level, surface, x, y + 1, prop.zEnd - 1, 107, 2)
		if isSurfaceBlock(level, x + surface.xStart, y, prop.zEnd + surface.zStart):
			setBlock(level, surface, x, y, prop.zEnd - 1, 4)
		else:
			setBlock(level, surface, x, y, prop.zEnd - 1, 67, 3)
	if prop.doorDirection == "West":
		z = prop.zStart + prop.zLength / 2
		setBlock(level, surface, prop.xEnd - 1, y + 1, z, 107, 1)
		if isSurfaceBlock(level, prop.xEnd + surface.xStart, y, z + surface.zStart):
			setBlock(level, surface, prop.xEnd - 1, y, z, 4)
		else:
			setBlock(level, surface, prop.xEnd - 1, y, z, 67, 1)