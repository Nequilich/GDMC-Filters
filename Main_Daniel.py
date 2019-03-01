from GetSurfaceAdv import getSurface
from Common import setBlock
from GetFlatAreas import getFlatAreas

def perform(level, box, options):
	surface = getSurface(level, box.minx, box.minz, box.maxx, box.maxz)

	for x in range(surface.xLength):
		for z in range(surface.zLength):
			y = surface.surface[x][z].height
			setBlock(level, x + surface.xStart, y + 1, z + surface.zStart, 20)

	surface.setSteepness()
	flatAreas = getFlatAreas(surface, 0)
	for a, area in enumerate(flatAreas):
		for point in area:
			y = surface.surface[point[0]][point[1]].height
			setBlock(level, surface.xStart + point[0], y + 1, surface.zStart + point[1], 95, a % 16)