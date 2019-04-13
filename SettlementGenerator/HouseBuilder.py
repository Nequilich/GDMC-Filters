from BiomeMaterials import get_biome_materials
from Common import setBlock
from RemoveTree import removeTree

def buildHouse(level, surface, prop):
	if prop.xLength < 7 or prop.zLength < 7:
		return
	getMaterials(surface, prop)
	buildFloor(level, surface, prop)
	buildWalls(level, surface, prop)
	if prop.doorDirection == "NORTH" or prop.doorDirection == "SOUTH":
		buildRoofNS(level, surface, prop)
	else:
		buildRoofEW(level, surface, prop)
	buildDoor(level, surface, prop)
	buildWindows(level, surface, prop)

def clearHouseProperty(level, surface, prop):
	for x in range(prop.xStart, prop.xEnd):
		for z in range(prop.zStart, prop.zEnd):
			for y in range(prop.height + 2, prop.height + 7):
				removeTree(level, x + surface.xStart, y, z + surface.zStart)
				setBlock(level, surface, x, y, z, 0)

def buildFloor(level, surface, prop):
	for x in range(prop.xStart + 1, prop.xEnd - 1):
		for z in range(prop.zStart + 1, prop.zEnd - 1):
			setBlock(level, surface, x, prop.height + 1, z, materials["stone"]["default"][0], materials["stone"]["default"][1])

def buildWalls(level, surface, prop):
	# North and south walls
	for x in range(prop.xStart + 2, prop.xEnd - 2):
		for y in range(prop.height + 2, prop.height + 5):
			setBlock(level, surface, x, y, prop.zStart + 1, materials["wood_planks"]["default"][0], materials["door"]["directions"]["south"]["bottom"][1])
			setBlock(level, surface, x, y, prop.zEnd - 2, materials["wood_planks"]["default"][0], materials["door"]["directions"]["south"]["bottom"][1])
	# East and west walls
	for z in range(prop.zStart + 2, prop.zEnd - 2):
		for y in range(prop.height + 2, prop.height + 5):
			setBlock(level, surface, prop.xStart + 1, y, z, materials["wood_planks"]["default"][0], materials["door"]["directions"]["south"]["bottom"][1])
			setBlock(level, surface, prop.xEnd - 2, y, z, materials["wood_planks"]["default"][0], materials["door"]["directions"]["south"]["bottom"][1])
	# Corners
	for y in range(prop.height + 2, prop.height + 5):
		setBlock(level, surface, prop.xStart + 1, y, prop.zStart + 1, materials["wood"]["default"][0], materials["wood"]["default"][1])
		setBlock(level, surface, prop.xStart + 1, y, prop.zEnd - 2, materials["wood"]["default"][0], materials["wood"]["default"][1])
		setBlock(level, surface, prop.xEnd - 2, y, prop.zStart + 1, materials["wood"]["default"][0], materials["wood"]["default"][1])
		setBlock(level, surface, prop.xEnd - 2, y, prop.zEnd - 2, materials["wood"]["default"][0], materials["wood"]["default"][1])

def buildRoofNS(level, surface, prop):
	y = prop.height + 5
	for x in range(prop.xStart + 2, prop.xEnd - 2):
		setBlock(level, surface, x, y, prop.zStart + 1, materials["wood"]["directions"]["east"]["top"][0], materials["wood"]["directions"]["east"]["top"][1])
		setBlock(level, surface, x, y, prop.zEnd - 2, materials["wood"]["directions"]["east"]["top"][0], materials["wood"]["directions"]["east"]["top"][1])

	for z in range(prop.zStart, prop.zEnd):
		setBlock(level, surface, prop.xStart, y, z, materials["wood_planks"]["directions"]["east"]["bottom"][0], materials["wood_planks"]["directions"]["east"]["bottom"][1])
		setBlock(level, surface, prop.xStart + 1, y + 1, z, materials["wood_planks"]["directions"]["east"]["bottom"][0], materials["wood_planks"]["directions"]["east"]["bottom"][1])
		setBlock(level, surface, prop.xStart + 1, y, z, materials["wood"]["directions"]["north"]["top"][0], materials["wood"]["directions"]["north"]["top"][1])
		setBlock(level, surface, prop.xEnd - 1, y, z, materials["wood_planks"]["directions"]["west"]["bottom"][0], materials["wood_planks"]["directions"]["west"]["bottom"][1])
		setBlock(level, surface, prop.xEnd - 2, y + 1, z, materials["wood_planks"]["directions"]["west"]["bottom"][0], materials["wood_planks"]["directions"]["west"]["bottom"][1])
		setBlock(level, surface, prop.xEnd - 2, y, z, materials["wood"]["directions"]["north"]["top"][0], materials["wood"]["directions"]["north"]["top"][1])
		for x in range(prop.xStart + 2, prop.xEnd - 2):
			setBlock(level, surface, x, y + 1, z, materials["wood_planks"]["default"][0], materials["door"]["directions"]["south"]["bottom"][1])

def buildRoofEW(level, surface, prop):
	y = prop.height + 5
	for z in range(prop.zStart + 2, prop.zEnd - 2):
		setBlock(level, surface, prop.xStart + 1, y, z, materials["wood"]["directions"]["north"]["top"][0], materials["wood"]["directions"]["north"]["top"][1])
		setBlock(level, surface, prop.xEnd - 2, y, z, materials["wood"]["directions"]["north"]["top"][0], materials["wood"]["directions"]["north"]["top"][1])

	for x in range(prop.xStart, prop.xEnd):
		setBlock(level, surface, x, y, prop.zStart, materials["wood_planks"]["directions"]["south"]["bottom"][0], materials["wood_planks"]["directions"]["south"]["bottom"][1])
		setBlock(level, surface, x, y + 1, prop.zStart + 1, materials["wood_planks"]["directions"]["south"]["bottom"][0], materials["wood_planks"]["directions"]["south"]["bottom"][1])
		setBlock(level, surface, x, y, prop.zStart + 1, materials["wood"]["directions"]["east"]["top"][0], materials["wood"]["directions"]["east"]["top"][1])
		setBlock(level, surface, x, y, prop.zEnd - 1, materials["wood_planks"]["directions"]["north"]["bottom"][0], materials["wood_planks"]["directions"]["north"]["bottom"][1])
		setBlock(level, surface, x, y + 1, prop.zEnd - 2, materials["wood_planks"]["directions"]["north"]["bottom"][0], materials["wood_planks"]["directions"]["north"]["bottom"][1])
		setBlock(level, surface, x, y, prop.zEnd - 2, materials["wood"]["directions"]["east"]["top"][0], materials["wood"]["directions"]["east"]["top"][1])
		for z in range(prop.zStart + 2, prop.zEnd - 2):
			setBlock(level, surface, x, y + 1, z, materials["wood_planks"]["default"][0], materials["wood_planks"]["default"][1])

def buildDoor(level, surface, prop):
	if prop.doorDirection == "NORTH":
		x = prop.xStart + prop.xLength / 2
		# Stair
		if isSurfaceBlock(level, x + surface.xStart, prop.height + 1, prop.zStart - 1 + surface.zStart):
			setBlock(level, surface, x, prop.height + 1, prop.zStart, materials["stone"]["default"][0], materials["stone"]["default"][1])
		else:
			setBlock(level, surface, x, prop.height + 1, prop.zStart, materials["stone"]["directions"]["south"]["bottom"][0], materials["stone"]["directions"]["south"]["bottom"][1])
		# Door
		setBlock(level, surface, x, prop.height + 2, prop.zStart + 1, materials["door"]["directions"]["south"]["bottom"][0], materials["door"]["directions"]["south"]["bottom"][1])
		setBlock(level, surface, x, prop.height + 3, prop.zStart + 1, materials["door"]["directions"]["south"]["top"][0], materials["door"]["directions"]["south"]["top"][1])
		# Torch
		setBlock(level, surface, x + 1, prop.height + 3, prop.zStart + 2, materials["torch"]["directions"]["south"]["top"][0], materials["torch"]["directions"]["south"]["top"][1])
		setBlock(level, surface, x - 1, prop.height + 3, prop.zStart + 2, materials["torch"]["directions"]["south"]["top"][0], materials["torch"]["directions"]["south"]["top"][1])
	elif prop.doorDirection == "EAST":
		z = prop.zStart + prop.zLength / 2
		# Stair
		if isSurfaceBlock(level, prop.xEnd + surface.xStart, prop.height + 1, z + surface.zStart):
			setBlock(level, surface, prop.xEnd - 1, prop.height + 1, z, materials["stone"]["default"][0], materials["stone"]["default"][1])
		else:
			setBlock(level, surface, prop.xEnd - 1, prop.height + 1, z, materials["stone"]["directions"]["west"]["bottom"][0], materials["stone"]["directions"]["west"]["bottom"][1])
		# Door
		setBlock(level, surface, prop.xEnd - 2, prop.height + 2, z, materials["door"]["directions"]["west"]["bottom"][0], materials["door"]["directions"]["west"]["bottom"][1])
		setBlock(level, surface, prop.xEnd - 2, prop.height + 3, z, materials["door"]["directions"]["west"]["top"][0], materials["door"]["directions"]["west"]["top"][1])
		# Torch
		setBlock(level, surface, prop.xEnd - 3, prop.height + 3, z + 1, materials["torch"]["directions"]["west"]["top"][0], materials["torch"]["directions"]["west"]["top"][1])
		setBlock(level, surface, prop.xEnd - 3, prop.height + 3, z - 1, materials["torch"]["directions"]["west"]["top"][0], materials["torch"]["directions"]["west"]["top"][1])
	elif prop.doorDirection == "SOUTH":
		x = prop.xStart + prop.xLength / 2
		# Stair
		if isSurfaceBlock(level, x + surface.xStart, prop.height + 1, prop.zEnd + surface.zStart):
			setBlock(level, surface, x, prop.height + 1, prop.zEnd - 1, materials["stone"]["default"][0], materials["stone"]["default"][1])
		else:
			setBlock(level, surface, x, prop.height + 1, prop.zEnd - 1, materials["stone"]["directions"]["north"]["bottom"][0], materials["stone"]["directions"]["north"]["bottom"][1])
		# Door
		setBlock(level, surface, x, prop.height + 2, prop.zEnd - 2, materials["door"]["directions"]["north"]["bottom"][0], materials["door"]["directions"]["north"]["bottom"][1])
		setBlock(level, surface, x, prop.height + 3, prop.zEnd - 2, materials["door"]["directions"]["north"]["top"][0], materials["door"]["directions"]["north"]["top"][1])
		# Torch
		setBlock(level, surface, x + 1, prop.height + 3, prop.zEnd - 3, materials["torch"]["directions"]["north"]["top"][0], materials["torch"]["directions"]["north"]["top"][1])
		setBlock(level, surface, x - 1, prop.height + 3, prop.zEnd - 3, materials["torch"]["directions"]["north"]["top"][0], materials["torch"]["directions"]["north"]["top"][1])
	elif prop.doorDirection == "WEST":
		z = prop.zStart + prop.zLength / 2
		# Stair
		if isSurfaceBlock(level, prop.xStart - 1 + surface.xStart, prop.height + 1, z + surface.zStart):
			setBlock(level, surface, prop.xStart, prop.height + 1, z, materials["stone"]["default"][0], materials["stone"]["default"][1])
		else:
			setBlock(level, surface, prop.xStart, prop.height + 1, z, materials["stone"]["directions"]["east"]["bottom"][0], materials["stone"]["directions"]["east"]["bottom"][1])
		# Door
		setBlock(level, surface, prop.xStart + 1, prop.height + 2, z, materials["door"]["directions"]["east"]["bottom"][0], materials["door"]["directions"]["east"]["bottom"][1])
		setBlock(level, surface, prop.xStart + 1, prop.height + 3, z, materials["door"]["directions"]["east"]["top"][0], materials["door"]["directions"]["east"]["top"][1])
		# Torch
		setBlock(level, surface, prop.xStart + 2, prop.height + 3, z + 1, materials["torch"]["directions"]["east"]["top"][0], materials["torch"]["directions"]["east"]["top"][1])
		setBlock(level, surface, prop.xStart + 2, prop.height + 3, z - 1, materials["torch"]["directions"]["east"]["top"][0], materials["torch"]["directions"]["east"]["top"][1])

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
				setBlock(level, surface, x, prop.height + 3, prop.zStart + 1, materials["glass_pane"]["default"][0], materials["glass_pane"]["default"][1])
			x += 1
			i += 1
	if prop.doorDirection != "EAST":
		z = prop.zStart + 3
		i = 0
		while z < prop.zEnd - 3:
			if i % 2 == 0:
				setBlock(level, surface, prop.xEnd - 2, prop.height + 3, z, materials["glass_pane"]["default"][0], materials["glass_pane"]["default"][1])
			z += 1
			i += 1
	if prop.doorDirection != "SOUTH":
		x = prop.xStart + 3
		i = 0
		while x < prop.xEnd - 3:
			if i % 2 == 0:
				setBlock(level, surface, x, prop.height + 3, prop.zEnd - 2, materials["glass_pane"]["default"][0], materials["glass_pane"]["default"][1])
			x += 1
			i += 1
	if prop.doorDirection != "WEST":
		z = prop.zStart + 3
		i = 0
		while z < prop.zEnd - 3:
			if i % 2 == 0:
				setBlock(level, surface, prop.xStart + 1, prop.height + 3, z, materials["glass_pane"]["default"][0], materials["glass_pane"]["default"][1])
			z += 1
			i += 1


def getMaterials(surface, prop):
	biomeId = surface.surfaceMap[prop.xStart][prop.zStart].biomeId

	global materials
	materials = get_biome_materials(biomeId)