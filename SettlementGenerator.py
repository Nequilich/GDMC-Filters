from GetSurfaceAdv import getSurface
from Common import setBlock
from GetFlatAreas import getFlatAreas
from random import randint
from GetRectangle import getRectangle

def perform(level, box, options):
	surface = getSurface(level, box.minx, box.minz, box.maxx, box.maxz)
	surface.setSteepness()
	areas = getFlatAreas(surface, 1)

	length = len(areas)
	i = 0
	while(i < length):
		if (len(areas[i]) < 35):
			areas.pop(i)
			length -= 1
		else:
			i += 1

	for x in range(surface.xLength):
		for z in range(surface.zLength):
			y = surface.surface[x][z].height
			setBlock(level, x + surface.xStart, y + 1, z + surface.zStart, 20)
	for a, area in enumerate(areas):
		for point in area:
			y = surface.surface[point[0]][point[1]].height
			setBlock(level, surface.xStart + point[0], y + 1, surface.zStart + point[1], 95, a % 15 + 1)
	
	combinedArea = []
	for area in areas:
		for spot in area:
			combinedArea.append(spot)
	
	length = len(combinedArea)
	counter = 0
	for s in range(10):
		i = randint(0, length - 1)
		x = combinedArea[i][0]
		z = combinedArea[i][1]
		rec = getRectangle(surface, x, z, 1)
		if (not isValidRectangle(rec)):
			continue
		counter += 1
	print(str(counter))

def isValidRectangle(rec):
	xLength = rec.xEnd - rec.xStart
	zLength = rec.zEnd - rec.zStart
	if (xLength >= 5 and zLength >= 7 or xLength >= 7 and zLength >= 5):
		return True
	return False
