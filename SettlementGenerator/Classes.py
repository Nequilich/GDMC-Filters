from collections import deque

class Surface:
	aboveSurfaceBlocks = [0, 6, 17, 18, 31, 32, 37, 38, 39, 40, 59, 78, 81, 83, 99, 100, 103, 104, 105, 106, 111, 141, 142, 161, 162, 175]

	def __init__(self, level, xStart, zStart, xEnd, zEnd):
		self.xStart = xStart
		self.zStart = zStart
		self.xEnd = xEnd
		self.zEnd = zEnd
		self.xLength = xEnd - xStart
		self.zLength = zEnd - zStart
		self.surfaceMap = self.getNewSurfaceMap()
		self.updateHeights(level)
		self.updateWater(level)
		self.updateSteepness()

	def getNewSurfaceMap(self):
		surfaceMap = []
		for _ in range(self.xLength):
			row = []
			for _ in range(self.zLength):
				row.append(SurfacePoint())
			surfaceMap.append(row)
		return surfaceMap

	def updateHeights(self, level):
		suggestedHeights = []
		for x in range(self.xLength):
			row = []
			for z in range(self.zLength):
				row.append(0)
			suggestedHeights.append(row)
		unresolvedSurfacePoints = deque() #Surface points which surface height needs to be calculate

		#Adds the center surface point as the first unresolved surface point
		xCenter = int((self.xLength) / 2)
		zCenter = int((self.zLength) / 2)
		suggestedHeights[xCenter][zCenter] = level.Height
		unresolvedSurfacePoints.append((xCenter, zCenter, level.Height))

		while unresolvedSurfacePoints:
			nextSurfacePoint = unresolvedSurfacePoints.popleft()
			x = nextSurfacePoint[0]
			z = nextSurfacePoint[1]
			suggestedHeight = nextSurfacePoint[2]
			if suggestedHeight < suggestedHeights[x][z]:
				continue
			height = self.getSurfacePointHeight(level, x + self.xStart, z + self.zStart, suggestedHeight)

			#Returns if calculated is not higher than previous recorded height
			if self.surfaceMap[x][z].height < height:
				self.surfaceMap[x][z].height = height
				self.tryAddSurfacePointToQueue(suggestedHeights, unresolvedSurfacePoints, x + 1, z, height)
				self.tryAddSurfacePointToQueue(suggestedHeights, unresolvedSurfacePoints, x - 1, z, height)
				self.tryAddSurfacePointToQueue(suggestedHeights, unresolvedSurfacePoints, x, z + 1, height)
				self.tryAddSurfacePointToQueue(suggestedHeights, unresolvedSurfacePoints, x, z - 1, height)

	def isSurfaceBlock(self, level, x, y, z):
			for block in self.aboveSurfaceBlocks:
				if level.blockAt(x, y, z) == block:
					return False
			return True

	def getSurfacePointHeight(self, level, x, z, suggestedHeight):
		y = suggestedHeight + 1
		isAboveSurface = not self.isSurfaceBlock(level, x, y, z)
		if isAboveSurface:
			y -= 1
			while not self.isSurfaceBlock(level, x, y, z):
				y -= 1
			return y
		else:
			y += 1
			while self.isSurfaceBlock(level, x, y, z):
				y += 1
			return y - 1

	def tryAddSurfacePointToQueue(self, suggestedHeights, queue, x, z, suggestedHeight):
		#Checks if surface point is within surface border
		if x < 0 or x >= self.xLength or z < 0 or z >= self.zLength:
			return

		#Checks if this height has been suggested before
		if suggestedHeights[x][z] < suggestedHeight:
			suggestedHeights[x][z] = suggestedHeight
			queue.append((x, z, suggestedHeight))

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
				self.surfaceMap[x][z].isWater = (level.blockAt(x + self.xStart, y, z + self.zStart) == 9 and level.blockDataAt(x + self.xStart, y, z + self.zStart) == 0)

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