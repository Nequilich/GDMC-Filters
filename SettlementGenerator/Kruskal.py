import heapq

def getMinimumSpanningTree(vertexData, edges):
	minimumSpanningTree = []
	vertices = getVertices(vertexData)
	numberOfSets = len(vertices)
	while numberOfSets > 1:
		edge = heapq.heappop(edges) # pops shortest edge
		if edgeVerticesInSameSet(edge, vertices):
			continue
		for vertex in vertices:
			if vertex.setId == vertices[edge[1][1]].setId:
				vertex.setId = vertices[edge[1][0]].setId
		numberOfSets -= 1
		minimumSpanningTree.append((edge[1][0], edge[1][1]))
	return minimumSpanningTree

def getVertices(vertexData):
	vertices = []
	for i, data in enumerate(vertexData):
		vertices.append(Vertex(i, i, data)) # each vertex starts in their own set
	return vertices

def edgeVerticesInSameSet(edge, vertices):
	return vertices[edge[1][0]].setId == vertices[edge[1][1]].setId

class Vertex:
	def __init__(self, id, setId, data):
		self.id = id
		self.setId = setId
		self.data = data