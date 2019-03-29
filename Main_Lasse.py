from Classes import Surface
from Common import setBlock
from GetPathBetweenSections import getPathBetweenSections
from GetPropertiesAlongPath import getPropertiesAlongPath
from SurfaceManager import calculateHeightMapAdv
from SurfaceManager import calculateSteepnessMap
from SurfaceManager import calculateWaterPlacement
from SurfaceManager import calculateSections
from SurfaceManager import calculateSectionMid

def perform(level, box, options):
	surface = Surface(box.minx, box.minz, box.maxx, box.maxz)
	calculateHeightMapAdv(level, surface)
	calculateSteepnessMap(surface)
	calculateWaterPlacement(level, surface)
	sections = calculateSections(surface, 1, 40)
	landSections = []
	for section in sections:
		if not section.isWater:
			calculateSectionMid(surface, section)
			landSections.append(section)
	paths = getPathBetweenSections(surface, landSections)

	for path in paths:
		buildRoad(level, surface, path)

	properties = []
	for path in paths:
		properties.extend(getPropertiesAlongPath(surface, path))

	for p in properties:
		buildFloor(level, surface, p.xStart + 1, p.zStart + 1, p.xEnd - 1, p.zEnd - 1, p.height)
		buildDoor(level, surface, p.xStart + 1, p.zStart + 1, p.xEnd - 1, p.zEnd - 1, p.height, p.doorDirection)

def buildRoad(level, surface, path):
	for point in path:
		buildRoadPoint(level, surface, point.x, point.z)

def buildRoadPoint(level, surface, x, z):
	for p in [(x, z), (x + 1, z), (x - 1, z), (x, z + 1), (x, z - 1)]:
		if not isWithinBorder(surface, p[0], p[1]) or surface.surfaceMap[p[0]][p[1]].isOccupied or isGreatHeightDifference(surface, x, z, p[0], p[1]):
			continue
		height = surface.surfaceMap[p[0]][p[1]].height
		setBlock(level, surface.xStart + p[0], height, surface.zStart + p[1], 4)
		setBlock(level, surface.xStart + p[0], height - 1, surface.zStart + p[1], 4)
		surface.surfaceMap[p[0]][p[1]].isOccupied = True

def isWithinBorder(surface, x, z):
	return x >= 0 and x < surface.xLength and z >= 0 and z < surface.zLength

def isGreatHeightDifference(surface, x1, z1, x2, z2):
	heigth1 = surface.surfaceMap[x1][z1].height
	heigth2 = surface.surfaceMap[x2][z2].height
	difference = heigth1 - heigth2
	return difference > 1 or difference < -1

def buildFloor(level, surface, xStart, zStart, xEnd, zEnd, height):
	for x in range(xStart, xEnd):
		for z in range(zStart, zEnd):
			setBlock(level, surface.xStart + x, height + 1, surface.zStart + z, 41)

def buildDoor(level, surface, xStart, zStart, xEnd, zEnd, height, doorDirection):
	if doorDirection == "NORTH":
		setBlock(level, surface.xStart + xStart + (xEnd - xStart) / 2, height + 1, surface.zStart + zEnd, 57)
	elif doorDirection == "EAST":
		setBlock(level, surface.xStart + xEnd, height + 1, surface.zStart + zStart + (zEnd - zStart) / 2, 57)
	elif doorDirection == "SOUTH":
		setBlock(level, surface.xStart + xStart + (xEnd - xStart) / 2, height + 1, surface.zStart + zStart - 1, 57)
	elif doorDirection == "WEST":
		setBlock(level, surface.xStart + xStart - 1, height + 1, surface.zStart + zStart + (zEnd - zStart) / 2, 57)