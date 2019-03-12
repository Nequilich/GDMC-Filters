from Classes import Surface
from Common import setBlock
from SurfaceManager import calculateHeightMapAdv
from SurfaceManager import calculateSteepnessMap
from SurfaceManager import calculateWaterPlacement

def perform(level, box, options):
	surface = Surface(box.minx, box.minz, box.maxx, box.maxz)
	calculateHeightMapAdv(level, surface)
	calculateSteepnessMap(surface)
	calculateWaterPlacement(level, surface)
	simpleSurface = SimpleSurface(box.minx, box.minz, box.maxx, box.maxz)

	xStart = simpleSurface.xStart - surface.xStart
	zStart = simpleSurface.zStart - surface.zStart
	xLength = simpleSurface.xEnd - simpleSurface.xStart
	zLength = simpleSurface.zEnd - simpleSurface.zStart
	for x in range(xStart, xStart + xLength):
		for z in range(zStart, zStart + zLength):
			height = surface.surfaceMap[x][z].height
			xSimple = (x - xStart) / 3
			zSimple = (z - zStart) / 3
			simpleHeight = simpleSurface.surfaceMap[xSimple][zSimple]
			if simpleHeight < height:
				simpleSurface.surfaceMap[xSimple][zSimple] = height

	for x in range(surface.xLength):
		for z in range(surface.zLength):
			height = surface.surfaceMap[x][z].height
			setBlock(level, surface.xStart + x, height + 8, surface.zStart + z, 1)

	for x in range(simpleSurface.xMapLength):
		for z in range(simpleSurface.zMapLength):
			height = simpleSurface.surfaceMap[x][z]
			xReal = simpleSurface.xStart + x * 3
			zReal = simpleSurface.zStart + z * 3
			setBlock(level, xReal, height + 12, zReal, 20)
			setBlock(level, xReal + 1, height + 12, zReal, 20)
			setBlock(level, xReal + 2, height + 12, zReal, 20)
			setBlock(level, xReal, height + 12, zReal + 1, 20)
			setBlock(level, xReal + 1, height + 12, zReal + 1, 20)
			setBlock(level, xReal + 2, height + 12, zReal + 1, 20)
			setBlock(level, xReal, height + 12, zReal + 2, 20)
			setBlock(level, xReal + 1, height + 12, zReal + 2, 20)
			setBlock(level, xReal + 2, height + 12, zReal + 2, 20)

class SimpleSurface:

	def __init__(self, xStart, zStart, xEnd, zEnd):
		self.xStart = xStart + (3 - xStart % 3) % 3
		self.zStart = zStart + (3 - zStart % 3) % 3
		self.xEnd = xEnd - xEnd % 3
		self.zEnd = zEnd - zEnd % 3
		self.xLength = self.xEnd - self.xStart
		self.zLength = self.zEnd - self.zStart
		self.xMapLength = self.xLength / 3
		self.zMapLength = self.zLength / 3
		print("xStart: " + str(xStart) + ", zStart: " + str(zStart) + ", xEnd: " + str(xEnd) + ", zEnd: " + str(zEnd))
		print("xStart: " + str(self.xStart) + ", zStart: " + str(self.zStart) + ", xEnd: " + str(self.xEnd) + ", zEnd: " + str(self.zEnd))
		print("xLength: " + str(self.xLength) + ", zLength: " + str(self.zLength) + ", xMapLength: " + str(self.xMapLength) + ", zMapLength: " + str(self.zMapLength))
		self.surfaceMap = self.getNewSurfaceMap(self.xMapLength, self.zMapLength)

	def getNewSurfaceMap(self, xLength, zLength):
		surfaceMap = []
		for x in range(xLength):
			row = []
			for z in range(zLength):
				row.append(0)
			surfaceMap.append(row)
		return surfaceMap