from BridgeBuilder import buildBridge
from Classes import Point
from Common import isWithinBorder
from Common import setBlock
from RemoveTree import isTreeBlock
from RemoveTree import removeTree

def buildTestRoad(level, surface, path):
	roads = []
	bridges = []
	findRoadsAndBridges(surface, path, roads, bridges)
	buildRoads(level, surface, roads)
	buildBridges(level, surface, bridges)

def findRoadsAndBridges(surface, path, roads, bridges):
	bridge = []
	road = []
	for p in path:
		if surface.surfaceMap[p.x][p.z].isWater:
			bridge.append(p)
			if road:
				roads.append(road)
				road = []
		else:
			road.append(p)
			if bridge:
				bridges.append(bridge)
				bridge = []
	if road:
		roads.append(road)
	if bridge:
		bridges.append(bridge)

def buildRoads(level, surface, roads):
	for road in roads:
		for point in road:
			y = surface.surfaceMap[point.x][point.z].height
			point = Point(point.x + surface.xStart, point.z + surface.zStart)
			buildPathPoint(level, surface, point, y)

def buildBridges(level, surface, bridges):
	oakMaterial = {
    "normal": (17, 0),
    "upper slab": (126, 8),
    "lower slab": (126, 0),
    "fence": 85.0,
    "torch": (50, 5)
	}
	for bridge in bridges:
		startPoint = bridge[0]
		endPoint = bridge[len(bridge) - 1]
		height = surface.surfaceMap[startPoint.x][startPoint.z].height + 1
		startPointTuple = (startPoint.x + surface.xStart, startPoint.z + surface.zStart)
		endPointTuple = (endPoint.x + surface.xStart, endPoint.z + surface.zStart)
		buildBridge(level, startPointTuple, endPointTuple, height, 4, oakMaterial)

def buildPathPoint(level, surface, point, height):
	buildCenterPathTile(level, surface, point, height)
	for p in [(point.x - 1, point.z), (point.x + 1, point.z), (point.x, point.z - 1), (point.x, point.z + 1)]:
		buildOuterPathTile(level, surface, Point(p[0], p[1]), height)

def buildCenterPathTile(level, surface, point, height):
	surface.surfaceMap[point.x - surface.xStart][point.z - surface.zStart].isOccupied = True
	setBlock(level, None, point.x, height, point.z, 43, 0)
	clearAboveTile(level, point, height)

def buildOuterPathTile(level, surface, point, height):
	if not isWithinBorder(surface, point.x - surface.xStart, point.z - surface.zStart):
		return
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
		setBlock(level, None, point.x, height + 1, point.z, 44, 3)
	if level.blockAt(point.x, height - 1, point.z) == 4:
		setBlock(level, None, point.x, height, point.z, 44, 3)
	else:
		setBlock(level, None, point.x, height, point.z, 4, 0)
	
	i = 1
	while level.blockAt(point.x, height - i, point.z) == 0:
		setBlock(level, None, point.x, height - i, point.z, 98, 0)
		i += 1

def clearAboveTile(level, point, height):
	for i in range(1, 3):
		removeTree(level, point.x, height + i, point.z)