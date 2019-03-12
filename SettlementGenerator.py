from random import randint
from Classes import Surface
from CreatePyramid import createPyramid
from GetRectangle import getRectangle
from SurfaceManager import calculateHeightMapAdv
from SurfaceManager import calculateSections
from SurfaceManager import calculateSteepnessMap
from SurfaceManager import calculateWaterPlacement

def perform(level, box, options):
	surface = Surface(box.minx, box.minz, box.maxx, box.maxz)
	calculateHeightMapAdv(level, surface)
	calculateSteepnessMap(surface)
	calculateWaterPlacement(level, surface)
	sections = calculateSections(surface, 1, 40)

	allPoints = []
	for section in sections:
		if section.isWater:
			continue
		for point in section.points:
			allPoints.append(point)

	length = len(allPoints)
	houseId = 0
	for s in range(100):
		i = randint(0, length - 1)
		x = allPoints[i].x
		z = allPoints[i].z
		rec = getRectangle(surface, x, z, 1)
		if not isValidRectangle(rec):
			continue
		houseId += 1
		registerHouse(surface, rec, houseId)
		registerAsOccupied(surface, rec)
		createPyramid(level, rec.xStart + 2 + box.minx, rec.xEnd - 2 + box.minx, rec.zStart + 2 + box.minz, rec.zEnd - 2 + box.minz, surface.surfaceMap[x][z].height)

def isValidRectangle(rec):
	xLength = rec.xEnd - rec.xStart
	zLength = rec.zEnd - rec.zStart
	if xLength >= 8 and zLength >= 8 or xLength >= 8 and zLength >= 8:
		return True
	return False

def registerHouse(surface, rec, houseId):
	for x in range(rec.xStart + 2, rec.xEnd - 2):
		for z in range(rec.zStart + 2, rec.zEnd - 2):
			surface.surfaceMap[x][z].houseId = houseId

def registerAsOccupied(surface, rec):
	for x in range(rec.xStart, rec.xEnd):
		for z in range(rec.zStart, rec.zEnd):
			surface.surfaceMap[x][z].isOccupied = True