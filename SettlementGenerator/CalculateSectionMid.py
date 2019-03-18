from collections import deque
from Classes import Point
from Common import getMatrix
from Common import setBlock

def calculateSectionMid(surface, section, level):
	visitedPoints = []
	unvisitedPoints =  section.points
	unresolvedPoints = deque()
	surfaceInfo = newSurfaceInfo(surface, section)

	addToQueue(unresolvedPoints, surfaceInfo, section.points[0])
	layer = 0
	while unresolvedPoints:
		point = removeFromQueue(unresolvedPoints, surfaceInfo)
		if isPartOfLayer(surfaceInfo, point, layer):
			addPointToLayer(visitedPoints, unvisitedPoints, surfaceInfo, point, layer)
			addNeighborsToQueue(unresolvedPoints, surfaceInfo, point)

	for x in range(surfaceInfo.xLength):
		for z in range(surfaceInfo.zLength):
			if surfaceInfo.surfaceMap[x][z].layer == 0:
				height = surface.surfaceMap[x + surfaceInfo.xStart][z + surfaceInfo.zStart].height
				xReal = x + surfaceInfo.xStart + surface.xStart
				zReal = z + surfaceInfo.zStart + surface.zStart
				setBlock(level, xReal, height + 1, zReal, 41)

def newSurfaceInfo(surface, section):
	xStart = section.points[0].x
	xEnd = section.points[0].x
	zStart = section.points[0].z
	zEnd = section.points[0].z
	for point in section.points:
		if point.x < xStart:
			xStart = point.x
		elif point.x > xEnd:
			xEnd = point.x
		if point.z < zStart:
			zStart = point.z
		elif point.z > zEnd:
			zEnd = point.z
	
	surfaceInfo = SurfaceInfo(xStart - 1, zStart - 1, xEnd + 1, zEnd + 1)
	for x in range(surfaceInfo.xLength):
		for z in range(surfaceInfo.zLength):
			if surface.surfaceMap[x + surfaceInfo.xStart][z + surfaceInfo.zStart].sectionId != section.id:
				surfaceInfo.surfaceMap[x][z].isDetermined = True
	return surfaceInfo

def addToQueue(queue, surfaceInfo, point):
	queue.append(point)
	x = point.x - surfaceInfo.xStart
	z = point.z - surfaceInfo.zStart
	surfaceInfo.surfaceMap[x][z].isQueued = True

def removeFromQueue(queue, surfaceInfo):
	point = queue.popleft()
	x = point.x - surfaceInfo.xStart
	z = point.z - surfaceInfo.zStart
	surfaceInfo.surfaceMap[x][z].isQueued = False
	return point

def isPartOfLayer(surfaceInfo, point, layer):
	for x in [point.x - 1, point.x, point.x + 1]:
		for z in [point.z - 1, point.z, point.z + 1]:
			pointInfo = surfaceInfo.surfaceMap[x + surfaceInfo.xStart][z + surfaceInfo.zStart]
			if pointInfo.isDetermined and pointInfo.layer == layer - 1:
				return True
	return False

def addPointToLayer(visitedPoints, unvisitedPoints, surfaceInfo, point, layer):
	visitedPoints.append(point)
	for i, p in enumerate(unvisitedPoints):
		if point.x == p.x and point.z == p.z:
			unvisitedPoints.pop(i)
			break
	x = point.x - surfaceInfo.xStart
	z = point.z - surfaceInfo.zStart
	surfaceInfo.surfaceMap[x][z].layer = layer
	surfaceInfo.surfaceMap[x][z].isDetermined = True

def addNeighborsToQueue(queue, surfaceInfo, point):
	for x in [point.x - 1, point.x, point.x + 1]:
		for z in [point.z - 1, point.z, point.z + 1]:
			pointInfo = surfaceInfo.surfaceMap[x + surfaceInfo.xStart][z + surfaceInfo.zStart]
			if not pointInfo.isQueued and not pointInfo.isDetermined:
				addToQueue(queue, surfaceInfo, Point(x, z))

class SurfaceInfo:

	def __init__(self, xStart, zStart, xEnd, zEnd):
		self.xStart = xStart
		self.zStart = zStart
		self.xEnd = xEnd
		self.zEnd = zEnd
		self.xLength = xEnd - xStart
		self.zLength = zEnd - zStart
		self.surfaceMap = self.getNewSurfaceMap()

	def getNewSurfaceMap(self):
		surfaceMap = []
		for x in range(self.xLength):
			row = []
			for z in range(self.zLength):
				row.append(PointInfo())
			surfaceMap.append(row)
		return surfaceMap

class PointInfo:

	def __init__(self):
		self.layer = -1
		self.isDetermined = False
		self.isQueued = False