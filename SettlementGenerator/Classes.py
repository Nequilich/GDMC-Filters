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

class SurfaceSpot:

	def __init__(self, height = 0, steepness = 0):
		self.height = height
		self.steepness = steepness