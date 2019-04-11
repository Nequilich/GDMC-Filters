from random import randint
from Classes import Edge
from Classes import Node
from Classes import Point
from Classes import Surface
from Common import getEuclideanDistance
from Common import setBlock
from FarmBuilder import buildPatch
from FarmBuilder import clearPatchProperty
from GetPath import getPath
from GetPathBetweenSections import getPathBetweenSections
from GetPropertiesAlongPath import getPropertiesAlongPath
from HouseBuilder import buildHouse
from HouseBuilder import clearHouseProperty
from Kruskal import getMinimumSpanningTree
from RemoveTree import removeTree
from RoadBuilder import buildTestRoad
from SurfaceManager import calculateHeightMapAdv
from SurfaceManager import calculateSteepnessMap
from SurfaceManager import calculateWaterPlacement
from SurfaceManager import calculateSections
from SurfaceManager import calculateSectionMid

def perform(level, box, options):
	surface = Surface(box.minx, box.minz, box.maxx, box.maxz)
	calculateHeightMapAdv(level, surface)
	calculateSteepnessMap(surface)
	calculateWaterPlacement(level, surface)
	sections = calculateSections(surface, 1, 100)
	landSections = []
	for section in sections:
		if not section.isWater:
			calculateSectionMid(surface, section)
			landSections.append(section)
	paths = getPathBetweenSections(surface, landSections)

	for section in landSections:
		paths.extend(getPathsInSection(surface, section))

	for path in paths:
		buildTestRoad(level, surface, path)

	# Builds houses
	houseProperties = []
	for path in paths:
		houseProperties.extend(getPropertiesAlongPath(surface, path, 7, 11, 7))

	for p in houseProperties:
		clearHouseProperty(level, surface, p)

	for p in houseProperties:
		buildHouse(level, surface, p)
		buildPathway(level, surface, p.xPathwayStart, p.zPathwayStart, p.xPathwayEnd, p.zPathwayEnd)

	# Builds patches
	patchProperties = []
	for path in paths:
		patchProperties.extend(getPropertiesAlongPath(surface, path, 5, 11, 16))

	for p in patchProperties:
		clearPatchProperty(level, surface, p)

	for p in patchProperties:
		buildPatch(level, surface, p)

def getPathsInSection(surface, section):
	amountOfPoints = len(section.points)
	amountOfNewNodes = amountOfPoints / 5000 - 1
	if amountOfNewNodes < 1:
		return []
	points = [Point(section.xMid, section.zMid)]
	for _ in range(amountOfNewNodes):
		i = randint(0, amountOfPoints - 1)
		p = section.points[i]
		points.append(Point(p.x, p.z))

	nodes = []
	for i, point in enumerate(points):
		nodes.append(Node(i, point))

	edges = []
	for node in nodes:
		for otherNode in nodes:
			if otherNode.id <= node.id:
				continue
			point1 = node.data
			point2 = otherNode.data
			cost = getEuclideanDistance(surface, point1, point2)
			edges.append(Edge(cost, node.id, otherNode.id))

	minimumSpanningTree = getMinimumSpanningTree(nodes, edges)

	paths = []
	for edge in minimumSpanningTree:
		point1 = getNode(nodes, edge.nodeId1).data
		point2 = getNode(nodes, edge.nodeId2).data
		path = getPath(surface, point1.x, point1.z, point2.x, point2.z)
		paths.append(path)
	return paths

def getNode(nodes, id):
	for node in nodes:
		if node.id == id:
			return node
	return None

def buildPathway(level, surface, xStart, zStart, xEnd, zEnd):
	path = getPath(surface, xStart, zStart, xEnd, zEnd)
	for p in path:
		if surface.surfaceMap[p.x][p.z].isOccupied:
			continue
		height = surface.surfaceMap[p.x][p.z].height
		setBlock(level, surface, p.x, height, p.z, 4)