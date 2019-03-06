class Surface:

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
				row.append(SurfacePoint())
			surfaceMap.append(row)
		return surfaceMap

	def updateSteepness(self):	
		for x in range(self.xLength):
			for z in range(self.zLength):
				self.surfaceMap[x][z].steepness = self.updatePointSteepness(x, z)

	def updatePointSteepness(self, x, z):
		heights = []
		if x + 1 < self.xLength:
			heights.append(self.surfaceMap[x + 1][z].height)
		if x - 1 >= 0:
			heights.append(self.surfaceMap[x - 1][z].height)
		if z + 1 < self.zLength:
			heights.append(self.surfaceMap[x][z + 1].height)
		if z - 1 >= 0:
			heights.append(self.surfaceMap[x][z - 1].height)

		minHeight = self.surfaceMap[x][z].height
		maxHeight = self.surfaceMap[x][z].height
		for h in heights:
			if h < minHeight:
				minHeight = h
			elif h > maxHeight:
				maxHeight = h
		return maxHeight - minHeight

	def updateWater(self, level):
		for x in range(self.xLength):
			for z in range(self.zLength):
				y = self.surfaceMap[x][z].height
				self.surfaceMap[x][z].isWater = (level.blockAt(x + self.xStart, y, z + self.zStart) == 9)

class SurfacePoint:

	def __init__(self, height = 0):
		self.height = height
		self.steepness = 0
		self.isWater = False
		self.sectionId = -1
		self.isOccupied = False

class Section:

	def __init__(self, id):
		self.id = id
		self.points = []
		self.size = 0

class Point:

	def __init__(self, x, z):
		self.x = x
		self.z = z