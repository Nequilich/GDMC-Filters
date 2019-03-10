from Common import getMatrix

class Surface:

	def __init__(self, xStart, zStart, xEnd, zEnd):
		self.xStart = xStart
		self.zStart = zStart
		self.xEnd = xEnd
		self.zEnd = zEnd
		self.xLength = xEnd - xStart
		self.zLength = zEnd - zStart
		self.surfaceMap = getNewSurfaceMap(self.xLength, self.zLength)

def getNewSurfaceMap(xLength, zLength):
	surfaceMap = []
	for x in range(xLength):
		row = []
		for z in range(zLength):
			row.append(SurfacePoint())
		surfaceMap.append(row)
	return surfaceMap

class SurfacePoint:

	def __init__(self):
		self.height = 0
		self.steepness = 0
		self.isWater = False
		self.sectionId = -1
		self.isOccupied = False

class Section:

	def __init__(self, id):
		self.id = id
		self.points = []
		self.size = 0
		self.isWater = False

class Point:

	def __init__(self, x, z):
		self.x = x
		self.z = z