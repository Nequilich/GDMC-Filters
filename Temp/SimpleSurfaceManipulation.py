from random import randint
from Classes import Surface
from Classes import SimpleSurface
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
		registerAsOccupied(surface, rec)
		registerHouse(surface, rec, houseId)
		houseId += 1
		createPyramid(level, rec.xStart + 2 + box.minx, rec.xEnd - 2 + box.minx, rec.zStart + 2 + box.minz, rec.zEnd - 2 + box.minz, surface.surfaceMap[x][z].height)

	simpleSurface = SimpleSurface(box.minx, box.minz, box.maxx, box.maxz)
	calculateAttributes(simpleSurface, surface)
	printAttributes(simpleSurface)

def isValidRectangle(rec):
	xLength = rec.xEnd - rec.xStart
	zLength = rec.zEnd - rec.zStart
	if xLength >= 8 and zLength >= 8 or xLength >= 8 and zLength >= 8:
		return True
	return False

def registerAsOccupied(surface, rec):
	for x in range(rec.xStart, rec.xEnd):
		for z in range(rec.zStart, rec.zEnd):
			surface.surfaceMap[x][z].isOccupied = True

def registerHouse(surface, rec, houseId):
	for x in range(rec.xStart + 2, rec.xEnd - 2):
		for z in range(rec.zStart + 2, rec.zEnd - 2):
			surface.surfaceMap[x][z].houseId = houseId

def calculateAttributes(simpleSurface, surface):
	for xSimple in range(simpleSurface.xLength):
		for zSimple in range(simpleSurface.zLength):
			xMid = simpleSurface.toSurfaceX(surface, xSimple)
			zMid = simpleSurface.toSurfaceZ(surface, zSimple)
			for x in [xMid - 1, xMid, xMid + 1]:
				for z in [zMid - 1, zMid, zMid + 1]:
					if simpleSurface.surfaceMap[xSimple][zSimple].height < surface.surfaceMap[x][z].height:
						simpleSurface.surfaceMap[xSimple][zSimple].height = surface.surfaceMap[x][z].height
					if surface.surfaceMap[x][z].isWater:
						simpleSurface.surfaceMap[xSimple][zSimple].isWater = True
					if surface.surfaceMap[x][z].houseId != -1:
						simpleSurface.surfaceMap[xSimple][zSimple].houseId = surface.surfaceMap[x][z].houseId

def printAttributes(simpleSurface):
	print("Heights:")
	for x in range(simpleSurface.xLength):
		s = ""
		for z in range(simpleSurface.zLength):
			surfaceArea = simpleSurface.surfaceMap[x][z]
			s += str(surfaceArea.height) + " "
		print(s[:-1])
	print("")
	print("Water:")
	for x in range(simpleSurface.xLength):
		s = ""
		for z in range(simpleSurface.zLength):
			surfaceArea = simpleSurface.surfaceMap[x][z]
			if surfaceArea.isWater:
				s += "W "
			else:
				s += "- "
		print(s[:-1])
	print("")
	print("Houses:")
	for x in range(simpleSurface.xLength):
		s = ""
		for z in range(simpleSurface.zLength):
			surfaceArea = simpleSurface.surfaceMap[x][z]
			if surfaceArea.houseId == -1:
				s += "- "
			else:
				s += str(surfaceArea.houseId) + " "
		print(s[:-1])