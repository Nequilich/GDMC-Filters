from Classes import Surface
from SurfaceManager import calculateHeightMapAdv
from SurfaceManager import calculateSteepnessMap
from SurfaceManager import calculateWaterPlacement

def perform(level, box, options):
	surface = Surface(box.minx, box.minz, box.maxx, box.maxz)
	calculateHeightMapAdv(level, surface)
	calculateSteepnessMap(surface)
	calculateWaterPlacement(level, surface)
	simpleSurface = SimpleSurface(box.minx, box.minz, box.maxx, box.maxz)

	for x in range(surface.xLength):
		for z in range(surface.zLength):
			height = surface.surfaceMap[x][z].height
			simpleHeight = simpleSurface.surfaceMap[x / 3][z / 3]
			if simpleHeight < height:
				simpleSurface.surfaceMap[x / 3][z / 3] = height

class SimpleSurface:

	def __init__(self, xStart, zStart, xEnd, zEnd):
		self.xStart = xStart + 3 - xStart % 3
		self.zStart = zStart + 3 - zStart % 3
		self.xEnd = xEnd - xEnd % 3
		self.zEnd = zEnd - zEnd % 3
		self.xLength = self.xEnd - self.xStart
		self.zLength = self.zEnd - self.zStart
		self.xMapLength = self.xLength / 3
		self.zMapLength = self.zLength / 3
		self.surfaceMap = self.getNewSurfaceMap(self.xMapLength, self.zMapLength)

	def getNewSurfaceMap(self, xLength, zLength):
		surfaceMap = []
		for x in range(xLength):
			row = []
			for z in range(zLength):
				row.append(0)
			surfaceMap.append(row)
		return surfaceMap