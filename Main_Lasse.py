from GetSurfaceAdv import getSurface
from GetArea import getArea
from Common import setBlock

def perform(level, box, options):
	surface = getSurface(level, box)

	for x in range(surface.x):
		for z in range(surface.z):
			y = surface.surface[x][z].height
			setBlock(level, x + box.minx, y + 1, z + box.minz, 20)

	area = getArea(surface, int(surface.x / 2), int(surface.z / 2))