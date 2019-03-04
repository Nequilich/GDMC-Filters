from random import randint
from Common import setBlock
from CreatePyramid import createPyramid
from GetFlatAreas import getFlatAreas
from GetRectangle import getRectangle
from GetSurfaceAdv import getSurface

def perform(level, box, options):
	surface = getSurface(level, box.minx, box.minz, box.maxx, box.maxz)
	surface.setSteepness()
	areas = getFlatAreas(surface, 1)

	length = len(areas)
	i = 0
	while i < length:
		if len(areas[i]) < 35:
			areas.pop(i)
			length -= 1
		else:
			i += 1

	combinedArea = []
	for area in areas:
		for spot in area:
			combinedArea.append(spot)

	length = len(combinedArea)
	for s in range(100):
		i = randint(0, length - 1)
		x = combinedArea[i][0]
		z = combinedArea[i][1]
		rec = getRectangle(surface, x, z, 1)
		if not isValidRectangle(rec):
			continue
		occupyArea(surface, rec)
		createPyramid(level, rec.xStart + box.minx, rec.xEnd + box.minx, rec.zStart + box.minz, rec.zEnd + box.minz, surface.surface[x][z].height)

def isValidRectangle(rec):
	xLength = rec.xEnd - rec.xStart
	zLength = rec.zEnd - rec.zStart
	if xLength >= 5 and zLength >= 7 or xLength >= 7 and zLength >= 5:
		return True
	return False

def occupyArea(surface, rec):
	for x in range(rec.xStart, rec.xEnd):
		for z in range(rec.zStart, rec.zEnd):
			surface.surface[x][z].isOccupied = True