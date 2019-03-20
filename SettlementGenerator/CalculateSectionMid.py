from collections import deque
from Classes import Point
from Common import getMatrix

def calculateSectionMid(surface, section):
	surfaceInfo = newSurfaceInfo(surface, section)
	setOutsideSectionAsComplete(surface, section, surfaceInfo)

	for x in range(surfaceInfo.xLength):
		for z in range(surfaceInfo.zLength):
			if surfaceInfo.surfaceMap[x][z].isComplete:
				continue
			layer = getNeighborLayer(surfaceInfo, x, z) + 1
			findLayer(surfaceInfo, x, z, layer)
	setSectionMid(section, surfaceInfo)

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
	return SurfaceInfo(xStart, zStart, xEnd + 1, zEnd + 1)

def setOutsideSectionAsComplete(surface, section, surfaceInfo):
	for x in range(surfaceInfo.xLength):
		for z in range(surfaceInfo.zLength):
			if section.id != surface.surfaceMap[x + surfaceInfo.xStart][z + surfaceInfo.zStart].sectionId:
				surfaceInfo.surfaceMap[x][z].isComplete = True
				surfaceInfo.surfaceMap[x][z].layer = -1

def getNeighborLayer(surfaceInfo, x, z):
	for xNeighbor in [x - 1, x, x + 1]:
		for zNeighbor in [z - 1, z, z + 1]:
			if xNeighbor == x and zNeighbor == z:
				continue
			if xNeighbor < 0 or xNeighbor >= surfaceInfo.xLength or zNeighbor < 0 or zNeighbor >= surfaceInfo.zLength:
				continue
			if surfaceInfo.surfaceMap[xNeighbor][zNeighbor].isComplete:
				return surfaceInfo.surfaceMap[xNeighbor][zNeighbor].layer
	return -1

def findLayer(surfaceInfo, x, z, layer):
	queue = deque()
	queue.append(Point(x, z))
	while queue:
		point = queue.popleft()
		if addPointToLayer(surfaceInfo, point.x, point.z, layer):
			addNeighborPointsToQueue(surfaceInfo, point.x, point.z, layer, queue)

def addPointToLayer(surfaceInfo, x, z, layer):
	for xNeighbor in [x - 1, x, x + 1]:
		for zNeighbor in [z - 1, z, z + 1]:
			if xNeighbor == x and zNeighbor == z:
				continue
			if not isWithinBorder(surfaceInfo, xNeighbor, zNeighbor) or surfaceInfo.surfaceMap[xNeighbor][zNeighbor].layer == layer - 1:
				surfaceInfo.surfaceMap[x][z].layer = layer
				surfaceInfo.surfaceMap[x][z].isComplete = True
				return True

def isWithinBorder(surfaceInfo, x, z):
	return 0 <= x and x < surfaceInfo.xLength and 0 <= z and z < surfaceInfo.zLength

def addNeighborPointsToQueue(surfaceInfo, x, z, layer, queue):
	for xNeighbor in [x - 1, x, x + 1]:
		for zNeighbor in [z - 1, z, z + 1]:
			if xNeighbor == x and zNeighbor == z or not isWithinBorder(surfaceInfo, xNeighbor, zNeighbor):
				continue
			if not surfaceInfo.surfaceMap[xNeighbor][zNeighbor].isComplete and surfaceInfo.surfaceMap[xNeighbor][zNeighbor].isCheckedByLayer != layer:
				surfaceInfo.surfaceMap[xNeighbor][zNeighbor].isCheckedByLayer = layer
				queue.append(Point(xNeighbor, zNeighbor))

def setSectionMid(section, surfaceInfo):
	xMid = 0
	zMid = 0
	layer = -2
	for x in range(surfaceInfo.xLength):
		for z in range(surfaceInfo.zLength):
			if layer < surfaceInfo.surfaceMap[x][z].layer:
				xMid = x
				zMid = z
				layer = surfaceInfo.surfaceMap[x][z].layer
	section.xMid = xMid + surfaceInfo.xStart
	section.zMid = zMid + surfaceInfo.zStart

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
		for _ in range(self.xLength):
			row = []
			for _ in range(self.zLength):
				row.append(PointInfo())
			surfaceMap.append(row)
		return surfaceMap

class PointInfo:

	def __init__(self):
		self.layer = -2 # -2 is for uncompleted points, -1 is for outside the section, 0+ is for the actual layers
		self.isComplete = False
		self.isCheckedByLayer = -1

def printSurfaceInfo(surfaceInfo):
	for x in range(surfaceInfo.xLength):
		s = ""
		for z in range(surfaceInfo.zLength):
			if surfaceInfo.surfaceMap[x][z].layer < 0 or surfaceInfo.surfaceMap[x][z].layer > 9:
				s += str(surfaceInfo.surfaceMap[x][z].layer) + " "
			else:
				s += " " + str(surfaceInfo.surfaceMap[x][z].layer) + " "
		print(s)
