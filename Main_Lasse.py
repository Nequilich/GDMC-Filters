from Classes import Surface
from Common import setBlock
from GetPath import getPath
from SurfaceManager import calculateHeightMapAdv
from SurfaceManager import calculateSteepnessMap
from SurfaceManager import calculateWaterPlacement

def perform(level, box, options):
	surface = Surface(box.minx, box.minz, box.maxx, box.maxz)
	calculateHeightMapAdv(level, surface)
	calculateSteepnessMap(surface)
	calculateWaterPlacement(level, surface)

	path = getPath(surface, 10, 10, surface.xLength - 11, surface.zLength - 11)

	for point in path:
		buildRoadPoint(level, surface, point.x, point.z)

def buildRoadPoint(level, surface, x, z):
	for p in [(x, z), (x + 1, z), (x - 1, z), (x, z + 1), (x, z - 1)]:
		if not isWithinBorder(surface, p[0], p[1]) or surface.surfaceMap[p[0]][p[1]].isOccupied or isGreatHeightDifference(surface, x, z, p[0], p[1]):
			continue
		height = surface.surfaceMap[p[0]][p[1]].height
		setBlock(level, surface.xStart + p[0], height, surface.zStart + p[1], 4)
		surface.surfaceMap[p[0]][p[1]].isOccupied = True

def isWithinBorder(surface, x, z):
	return x >= 0 and x < surface.xLength and z >= 0 and z < surface.zLength

def isGreatHeightDifference(surface, x1, z1, x2, z2):
	heigth1 = surface.surfaceMap[x1][z1].height
	heigth2 = surface.surfaceMap[x2][z2].height
	difference = heigth1 - heigth2
	return difference > 1 or difference < -1