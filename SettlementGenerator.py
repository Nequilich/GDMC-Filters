from GetSurfaceAdv import getSurface
from Common import setBlock

def perform(level, box, options):
	surface = getSurface(level, box.minx, box.minz, box.maxx, box.maxz)

	for x in range(surface.xLength):
		for z in range(surface.zLength):
			y = surface.surface[x][z].height
			setBlock(level, x + surface.xStart, y + 1, z + surface.zStart, 20)