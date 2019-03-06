from Common import setBlock
from GetSurfaceAdv import getSurface
from UpdateSections import updateSections

def perform(level, box, options):
	surface = getSurface(level, box.minx, box.minz, box.maxx, box.maxz)
	surface.updateSteepness()
	surface.updateWater(level)
	sections = updateSections(surface, 1, 30)

	for x in range(surface.xLength):
		for z in range(surface.zLength):
			y = surface.surfaceMap[x][z].height
			id = surface.surfaceMap[x][z].sectionId
			if (id == -1):
				setBlock(level, x + surface.xStart, y + 1, z + surface.zStart, 20)
			else:
				setBlock(level, x + surface.xStart, y + 1, z + surface.zStart, 95, id % 15 + 1)