from Classes import Edge
from Classes import Node
from Classes import Point
from Common import getEuclideanDistance
from GetPath import getPath
from Kruskal import getMinimumSpanningTree

def getPathBetweenSections(surface, sections):
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
	return paths

def getNode(nodes, id):
	for node in nodes:
		if node.id == id:
			return node
	return None