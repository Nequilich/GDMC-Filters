from random import randint
from Classes import Edge
from Classes import Node
from Classes import Point
from Common import getEuclideanDistance
from GetPath import getPath
from Kruskal import getMinimumSpanningTree

def getPathsBetweenSections(surface, sections):
	points = []
	for section in sections:
		points.append(Point(section.xMid, section.zMid))
	return getPathBetweenPoints(surface, points)

def getPathsInSection(surface, section):
	points = [Point(section.xMid, section.zMid)]
	pointPool = section.points
	poolSize = len(pointPool)
	expectedPoints = poolSize / 4000 - 1

	if expectedPoints < 1:
		return []

	while expectedPoints > 0:
		p = getUniquePoint(pointPool, poolSize, points)
		points.append(p)
		expectedPoints -= 1
	
	return getPathBetweenPoints(surface, points)

def getUniquePoint(pointPool, poolSize, points):
	i = randint(0, poolSize - 1)
	p = pointPool[i]
	while contain(points, p):
		i = randint(0, poolSize - 1)
		p = pointPool[i]
	return p

def contain(points, point):
	for p in points:
		if p.x == point.x and p.z == point.z:
			return True
	return False

def getPathBetweenPoints(surface, points):
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