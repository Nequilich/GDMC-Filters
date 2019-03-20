import heapq

def getMinimumSpanningTree(vertexData, edges):
	minimumSpanningTree = []
	vertices = getVertices(vertexData)
	numberOfSets = len(vertices)
	print("START")
	print(numberOfSets)
	printVertexSets(vertices)
	while numberOfSets > 1:
		edge = heapq.heappop(edges) # pops shortest edge
		vertexOne = getVertex(edge[1][0], vertices)
		vertexTwo = getVertex(edge[1][1], vertices)
		if edgeVerticesInSameSet(vertexOne, vertexTwo):
			continue
		print("V1 SetID: " + str(vertexOne.setId) + ", V2 SetID: " + str(vertexTwo.setId))
		setTwoId = vertexTwo.setId
		for vertex in vertices: # Merge sets of the two vertices
			if vertex.setId == setTwoId:
				vertex.setId = vertexOne.setId
		numberOfSets -= 1
		print(numberOfSets)
		printVertexSets(vertices)
		minimumSpanningTree.append((vertexOne.data, vertexTwo.data))
	return minimumSpanningTree

def printVertexSets(vertices):
	strings = []
	for i in range(len(vertices)):
		strings.append("Set " + str(i) + ": ")
	for v in vertices:
		strings[v.setId] += str(v.id) + " "
	for s in strings:
		print(s)

def getVertices(vertexData):
	vertices = []
	for i, data in enumerate(vertexData):
		vertices.append(Vertex(i, i, data)) # each vertex starts in their own set
	return vertices

def getVertex(vertexData, vertices):
	for vertex in vertices:
		if vertex.data == vertexData:
			return vertex

def edgeVerticesInSameSet(vertexOne, vertexTwo):
	return vertexOne.setId == vertexTwo.setId

class Vertex:
	def __init__(self, id, setId, data):
		self.id = id
		self.setId = setId
		self.data = data