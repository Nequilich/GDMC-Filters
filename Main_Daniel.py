from BridgeBuilder import buildBridge
from Classes import Point
from Classes import Surface
from Common import getEuclideanDistance
from Common import setBlock
from GetPath import getPath
import heapq
from Kruskal import getMinimumSpanningTree
from SurfaceManager import calculateHeightMapAdv
from SurfaceManager import calculateSectionMid
from SurfaceManager import calculateSections
from SurfaceManager import calculateSteepnessMap
from SurfaceManager import calculateWaterPlacement

def perform(level, box, options):
	surface = Surface(box.minx, box.minz, box.maxx, box.maxz)
	calculateHeightMapAdv(level, surface)
	calculateSteepnessMap(surface)
	calculateWaterPlacement(level, surface)
	sections = calculateSections(surface, 1, 40)

	newSections = []
	for section in sections:
		if section.isWater:
			continue
		newSections.append(section)
	sections = newSections

	for section in sections:
		calculateSectionMid(surface, section)

	useAStar = False
	distances = [] # Tuples: (distance, (section1, section2))
	sectionIds = []
	for section in sections:
		height = surface.surfaceMap[section.xMid][section.zMid].height
		setBlock(level, surface.xStart + section.xMid, height + 2, surface.zStart + section.zMid, 41)
		sectionIds.append(section.id)
		for otherSection in sections:
			if (otherSection.id <= section.id):
				continue
			if useAStar:
				pathLength = len(getPath(surface, section.xMid, section.zMid, otherSection.xMid, otherSection.zMid))
				heapq.heappush(distances, (pathLength, (section.id, otherSection.id)))
			else:
				sectionMidPoint = Point(section.xMid, section.zMid)
				otherSectionMidPoint = Point(otherSection.xMid, otherSection.zMid)
				heapq.heappush(distances, (getEuclideanDistance(surface, sectionMidPoint, otherSectionMidPoint), (section.id, otherSection.id)))
	
	minimumSpanningTree = getMinimumSpanningTree(sectionIds, distances)
	roads = [] # Tuples: (point1, point2)
	for connection in minimumSpanningTree:
		section1 = getSection(sections, connection[0])
		section2 = getSection(sections, connection[1])
		startPoint = Point(section1.xMid, section1.zMid)
		endPoint = Point(section2.xMid, section2.zMid)
		roads.append((startPoint, endPoint))
	paths = []
	for road in roads:
		paths.append(getPath(surface, road[0].x, road[0].z, road[1].x, road[1].z))
	
	bridges = []
	newPaths = []
	for path in paths:
		bridge = []
		newPath = []
		for p in path:
			if surface.surfaceMap[p.x][p.z].isWater:
				bridge.append(p)
				if newPath:
					newPaths.append(newPath)
					newPath = []
			else:
				newPath.append(p)
				if bridge:
					bridges.append(bridge)
					bridge = []
		if newPath:
			newPaths.append(newPath)
		if bridge:
			bridges.append(bridge)

	paths = newPaths

	for path in paths:
		for p in path:
			y = surface.surfaceMap[p.x][p.z].height
			point = Point(p.x + surface.xStart, p.z + surface.zStart)
			buildPathPoint(level, point, y)

	oakMaterial = {
    "normal": (17, 0),
    "upper slab": (126, 8),
    "lower slab": (126, 0),
    "fence": 85.0,
    "torch": 50
	}
	
	for bridge in bridges:
		startPoint = bridge[0]
		endPoint = bridge[len(bridge) - 1]
		height = surface.surfaceMap[startPoint.x][startPoint.z].height
		startPointTuple = (startPoint.x + surface.xStart, startPoint.z + surface.zStart)
		endPointTuple = (endPoint.x + surface.xStart, endPoint.z + surface.zStart)
		buildBridge(level, startPointTuple, endPointTuple, height, 4, oakMaterial)

def getSection(sections, id):
	for section in sections:
		if section.id == id:
			return section
	return None

def findBridges(surface, paths):
	bridges = []
	newPaths = []
	for path in paths:
		bridge = []
		newPath = []
		for p in path:
			if surface.surfaceMap[p.x][p.z].isWater:
				bridge.append(p)
				if newPath:
					newPaths.append(newPath)
					newPath = []
			else:
				newPath.append(p)
				if bridge:
					bridges.append(bridge)
					bridge = []
	paths = newPaths
	return bridges


def buildPathPoint(level, point, height):
	buildCenterPathTile(level, point, height)
	for p in [(point.x - 1, point.z), (point.x + 1, point.z), (point.x, point.z - 1), (point.x, point.z + 1)]:
		buildOuterPathTile(level, Point(p[0], p[1]), height)

def buildCenterPathTile(level, point, height):
	setBlock(level, point.x, height, point.z, 43, 0)
	clearAboveTile(level, point, height)

def buildOuterPathTile(level, point, height):
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
	while(level.blockAt(point.x, height - i, point.z) == 0):
		setBlock(level, point.x, height - i, point.z, 98, 0)
		i += 1

def clearAboveTile(level, point, height):
	for i in range(1, 6):
		setBlock(level, point.x, height + i, point.z, 0, 0)
	