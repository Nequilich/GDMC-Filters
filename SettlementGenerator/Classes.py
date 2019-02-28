class Surface:

	def __init__(self, x, z):
		self.x = x
		self.z = z
		self.surface = self.getNewSurface()

	def getNewSurface(self):
		surface = []
		for x in range(self.x):
			row = []
			for z in range(self.z):
				row.append(SurfaceSpot())
			surface.append(row)
		return surface

	def setSteepness(self):	
		for x in range(self.x):
			for z in range(self.z):
				self.surface[x][z].steepness = self.getSteepness(x, z)

	def getSteepness(self, x, z):
		heights = []
		if (x + 1 < self.x):
			heights.append(self.surface[x + 1][z].height)
		if (x - 1 >= 0):
			heights.append(self.surface[x - 1][z].height)
		if (z + 1 < self.z):
			heights.append(self.surface[x][z + 1].height)
		if (z - 1 >= 0):
			heights.append(self.surface[x][z - 1].height)

		minHeight = self.surface[x][z].height
		maxHeight = self.surface[x][z].height
		for h in heights:
			if (h < minHeight):
				minHeight = h
			elif (h > maxHeight):
				maxHeight = h
		return maxHeight - minHeight

class SurfaceSpot:

	def __init__(self, height = 0, steepness = 0):
		self.height = height
		self.steepness = steepness