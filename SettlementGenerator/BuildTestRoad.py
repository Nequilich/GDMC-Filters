from Classes import Point
from Common import setBlock
from RemoveTree import isTreeBlock
from RemoveTree import removeTree

def buildTestRoad(level, surface, path):
	for point in path:
		y = surface.surfaceMap[point.x][point.z].height
		point = Point(point.x + surface.xStart, point.z + surface.zStart)
		buildPathPoint(level, surface, point, y)

def buildPathPoint(level, surface, point, height):
	buildCenterPathTile(level, surface, point, height)
	for p in [(point.x - 1, point.z), (point.x + 1, point.z), (point.x, point.z - 1), (point.x, point.z + 1)]:
		buildOuterPathTile(level, surface, Point(p[0], p[1]), height)

def buildCenterPathTile(level, surface, point, height):
	surface.surfaceMap[point.x - surface.xStart][point.z - surface.zStart].isOccupied = True
	setBlock(level, point.x, height, point.z, 43, 0)
	clearAboveTile(level, point, height)

def buildOuterPathTile(level, surface, point, height):
	if point.x >= 0 and point.x < surface.xLength and point.z >= 0 and point.z < surface.zLength:
		surface.surfaceMap[point.x - surface.xStart][point.z - surface.zStart].isOccupied = True
	if level.blockAt(point.x, height, point.z) == 43:
		return
	if level.blockAt(point.x, height, point.z) == 0:
		i = 0
		while level.blockAt(point.x, height - i, point.z) == 0:
			if level.blockAt(point.x, height - 1 - i, point.z) == 43:
				return
			i += 1
	
	if level.blockAt(point.x, height + 1, point.z) == 4:
		setBlock(level, point.x, height + 1, point.z, 44, 3)
	if level.blockAt(point.x, height - 1, point.z) == 4:
		setBlock(level, point.x, height, point.z, 44, 3)
	else:
		setBlock(level, point.x, height, point.z, 4, 0)
	
	i = 1
	while level.blockAt(point.x, height - i, point.z) == 0:
		setBlock(level, point.x, height - i, point.z, 98, 0)
		i += 1

def clearAboveTile(level, point, height):
	for i in range(1, 9):
		setBlock(level, point.x, height + i, point.z, 0, 0)
		#if isTreeBlock(level, point.x, height + i, point.z):
		#	removeTree(level, point.x, height + i, point.z)
		#else:
		#	setBlock(level, point.x, height + i, point.z, 0, 0)