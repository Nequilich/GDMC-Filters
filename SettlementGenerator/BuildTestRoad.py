from Biomes import biomes
from BridgeBuilder import buildBridge
from Classes import Bridge
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
	biomeId = 1
	for i, p in enumerate(path):
		if surface.surfaceMap[p.x][p.z].biomeId not in biomes["riverBeach"] and surface.surfaceMap[p.x][p.z].biomeId not in biomes["aquatic"]:
			biomeId = surface.surfaceMap[p.x][p.z].biomeId
		if surface.surfaceMap[p.x][p.z].isWater:
			if not bridge and i > 0:
				bridge.append(path[i-1])
			bridge.append(p)
			if road:
				roads.append(road)
				road = []
		else:
			road.append(p)
			if bridge:
				bridge.append(p)
				bridges.append(Bridge(bridge, biomeId))
				bridge = []
	if road:
		roads.append(road)
	if bridge:
		bridges.append(Bridge(bridge, biomeId))

def buildRoads(level, surface, roads):
	streetLightInterval = 8
	for road in roads:
		streetLightCounter = 0
		for point in road:
			y = surface.surfaceMap[point.x][point.z].height
			point = Point(point.x + surface.xStart, point.z + surface.zStart)
			buildPathPoint(level, surface, point, y)
			if (streetLightCounter % streetLightInterval == 0):
				for p in [(point.x - 2, point.z), (point.x + 2, point.z), (point.x, point.z - 2), (point.x, point.z + 2)]:
					placeStreetLight(level, surface, Point(p[0], p[1]), y)
			streetLightCounter += 1

def buildBridges(level, surface, bridges):
	for bridge in bridges:
		print(bridge.biomeId)
		startPoint = bridge.bridgePoints[0]
		endPoint = bridge.bridgePoints[-1]
		height = surface.surfaceMap[startPoint.x][startPoint.z].height + 1
		startPointTuple = (startPoint.x + surface.xStart, startPoint.z + surface.zStart)
		endPointTuple = (endPoint.x + surface.xStart, endPoint.z + surface.zStart)
		buildBridge(level, startPointTuple, endPointTuple, height, 4, bridge.biomeId)

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
		return False
	surface.surfaceMap[point.x - surface.xStart][point.z - surface.zStart].isOccupied = True
	if level.blockAt(point.x, height, point.z) == 43:
		return False
	if level.blockAt(point.x, height, point.z) == 0:
		i = 0
		while level.blockAt(point.x, height - i, point.z) == 0:
			if level.blockAt(point.x, height - 1 - i, point.z) == 43:
				return False
			i += 1
	
	if level.blockAt(point.x, height + 1, point.z) == 4:
		setBlock(level, None, point.x, height + 1, point.z, 44, 3)
	if level.blockAt(point.x, height - 1, point.z) == 4:
		setBlock(level, None, point.x, height, point.z, 44, 3)
	else:
		setBlock(level, None, point.x, height, point.z, 4, 0)
		clearAboveTile(level, point, height)
		
	i = 1
	while level.blockAt(point.x, height - i, point.z) == 0:
		setBlock(level, None, point.x, height - i, point.z, 98, 0)
		i += 1
	return True

def clearAboveTile(level, point, height):
	for i in range(1, 4):
		removeTree(level, point.x, height + i, point.z)
		setBlock(level, None, point.x, height + i, point.z, 0, 0)

def placeStreetLight(level, surface, point, height):
	buildablePoint = buildOuterPathTile(level, surface, point, height)
	if buildablePoint:  # Tries to place a tile and if successful place a street light.
		setBlock(level, None, point.x, height + 1, point.z, 139, 0)
		setBlock(level, None, point.x, height + 2, point.z, 50, 5)