import heapq
from Classes import Point
from Classes import Surface
from Common import getEuclideanDistance
from GetPathBetweenSections import getPathBetweenSections
from SurfaceManager import calculateHeightMapAdv
from SurfaceManager import calculateSectionMid
from SurfaceManager import calculateSections
from SurfaceManager import calculateSteepnessMap
from SurfaceManager import calculateWaterPlacement
from TowerBuilder import buildMediumTower

from Kruskal import getMinimumSpanningTree
from GetPath import getPath
from Classes import Node
from random import randint
from Classes import Edge
from RoadBuilder import buildTestRoad

def perform(level, box, options):
	surface = Surface(box.minx, box.minz, box.maxx, box.maxz)
	calculateHeightMapAdv(level, surface)
	calculateSteepnessMap(surface)
	calculateWaterPlacement(level, surface)

	sections = calculateSections(surface, 1, 15)
	calculateSectionMids(surface, sections)
	
	smallLandSections = []
	mediumLandSections = []
	bigLandSections = []
	waterSections = []

	arrangeSections(sections, waterSections, bigLandSections, mediumLandSections, smallLandSections)

	averageSurfaceHeight = calculateAverageSurfaceHeight(surface)
	calculateAverageSectionHeights(surface, sections)

	smallLandSectionHeap = heapifySectionsByAverageHeight(smallLandSections)

	towerSections = getTowerSections(surface, averageSurfaceHeight, smallLandSectionHeap)
	
	habitatSections = getHabitatSections(towerSections, mediumLandSections, bigLandSections)
	
	paths = getPathBetweenSections(surface, habitatSections)

	for section in bigLandSections:
		paths.extend(getPathsInSection(surface, section))

	buildPaths(level, surface, paths)

def calculateSectionMids(surface, sections):
	for section in sections:
		calculateSectionMid(surface, section)

def arrangeSections(sections, waterSections, bigLandSections, mediumLandSections, smallLandSections):
	for section in sections:
		if section.layerDepth < 2:
			continue
		if section.isWater:
			waterSections.append(section)
			continue
		if len(section.points) < 250:
			smallLandSections.append(section)
			continue
		if len(section.points) < 1000:
			mediumLandSections.append(section)
			continue
		bigLandSections.append(section)

def calculateAverageSurfaceHeight(surface):
	cumulativeHeight = 0
	for x in range(surface.xLength):
		for z in range(surface.zLength):
			cumulativeHeight += surface.surfaceMap[x][z].height
	return cumulativeHeight / (surface.xLength * surface.zLength)

def calculateAverageSectionHeights(surface, sections):
	for section in sections:
		section.averageHeight = calculateAverageSectionHeight(surface, section)

def calculateAverageSectionHeight(surface, section):
	cumulativeHeight = 0
	for point in section.points:
		x = point.x
		z = point.z
		cumulativeHeight += surface.surfaceMap[x][z].height
	return cumulativeHeight / len(section.points)

def heapifySectionsByAverageHeight(sections):
	heap = []
	for section in sections:
		heapq.heappush(heap, (-section.averageHeight, section))
	return heap

def getTowerSections(surface, averageSurfaceHeight, sectionHeap):
	towerSections = []
	for element in sectionHeap:
		section = element[1]
		if section.averageHeight < averageSurfaceHeight:
			break
		tooClose = False
		sectionMid = Point(section.xMid, section.zMid)
		for towerSection in towerSections:
			towerSectionMid = Point(towerSection.xMid, towerSection.zMid)
			distance = getEuclideanDistance(surface, towerSectionMid, sectionMid)
			if distance < 50:
				tooClose = True
		if tooClose:
			continue
		towerSections.append(section)
	return towerSections

def getHabitatSections(towerSections, mediumLandSections, bigLandSections):
	habitatSections = []
	habitatSections.extend(towerSections)
	habitatSections.extend(mediumLandSections)
	habitatSections.extend(bigLandSections)
	return habitatSections

def buildPaths(level, surface, paths):
	for path in paths:
		buildTestRoad(level, surface, path)








# fra Lasse

def getPathsInSection(surface, section):
	amountOfPoints = len(section.points)
	amountOfNewNodes = amountOfPoints / 4000 - 1
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