from Classes import Edge
from Classes import Node
from Classes import Point
from Classes import Surface
from Common import getEuclideanDistance
from Common import setBlock
from GetPath import getPath
from Kruskal2 import getMinimumSpanningTree
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
	sectionsIncludingWater = calculateSections(surface, 1, 40)
	sections = []
	for section in sectionsIncludingWater:
		if not section.isWater:
			calculateSectionMid(surface, section)
			sections.append(section)

	nodes = []
	for section in sections:
		nodes.append(Node(section.id, section))

	edges = []
	for node in nodes:
		for otherNode in nodes:
			if otherNode.id <= node.id:
				continue
			section1 = node.data
			section2 = otherNode.data
			point1 = Point(section1.xMid, section1.zMid)
			point2 = Point(section2.xMid, section2.zMid)
			cost = getEuclideanDistance(surface, point1, point2)
			edges.append(Edge(cost, node.id, otherNode.id))

	minimumSpanningTree = getMinimumSpanningTree(nodes, edges)

	paths = []
	for edge in minimumSpanningTree:
		section1 = getNode(nodes, edge.nodeId1).data
		section2 = getNode(nodes, edge.nodeId2).data
		path = getPath(surface, section1.xMid, section1.zMid, section2.xMid, section2.zMid)
		paths.append(path)

	for path in paths:
		buildRoad(level, surface, path)

def getNode(nodes, id):
	for node in nodes:
		if node.id == id:
			return node
	return None

def buildRoad(level, surface, path):
	for point in path:
		buildRoadPoint(level, surface, point.x, point.z)

def buildRoadPoint(level, surface, x, z):
	for p in [(x, z), (x + 1, z), (x - 1, z), (x, z + 1), (x, z - 1)]:
		if not isWithinBorder(surface, p[0], p[1]) or surface.surfaceMap[p[0]][p[1]].isOccupied or isGreatHeightDifference(surface, x, z, p[0], p[1]):
			continue
		height = surface.surfaceMap[p[0]][p[1]].height
		setBlock(level, surface.xStart + p[0], height, surface.zStart + p[1], 4)
		setBlock(level, surface.xStart + p[0], height - 1, surface.zStart + p[1], 4)
		surface.surfaceMap[p[0]][p[1]].isOccupied = True

def isWithinBorder(surface, x, z):
	return x >= 0 and x < surface.xLength and z >= 0 and z < surface.zLength

def isGreatHeightDifference(surface, x1, z1, x2, z2):
	heigth1 = surface.surfaceMap[x1][z1].height
	heigth2 = surface.surfaceMap[x2][z2].height
	difference = heigth1 - heigth2
	return difference > 1 or difference < -1