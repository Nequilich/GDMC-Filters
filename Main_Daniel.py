from Classes import Surface
from Common import setBlock
from GetPath import getPath
from SurfaceManager import calculateHeightMapAdv
from SurfaceManager import calculateWaterPlacement

def perform(level, box, options):
	surface = Surface(box.minx, box.minz, box.maxx, box.maxz)
	calculateHeightMapAdv(level, surface)
	calculateWaterPlacement(level, surface)

	path = getPath(surface, 0, 0, surface.xLength - 1, surface.zLength - 1)

	for p in path:
		y = surface.surfaceMap[p.x][p.z].height
		setBlock(level, p.x + surface.xStart, y, p.z + surface.zStart, 57, 0)