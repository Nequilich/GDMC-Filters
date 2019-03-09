from Classes import Surface
from Common import setBlock
from SurfaceManager import calculateHeightMapAdv
from GetRectangle import getRectangle

def perform(level, box, options):
	surface = Surface(box.minx, box.minz, box.maxx, box.maxz)
	calculateHeightMapAdv(level, surface)
	for x in range(surface.xLength):
		for z in range(surface.zLength):
			y = surface.surfaceMap[x][z].height
			setBlock(level, x + surface.xStart, y + 1, z + surface.zStart, 20)

	rec = getRectangle(surface, int(surface.xLength / 2), int(surface.zLength / 2), 1)
	for x in range(rec.xStart, rec.xEnd):
		for z in range(rec.zStart, rec.zEnd):
			y = surface.surfaceMap[x][z].height
			setBlock(level, x + surface.xStart, y + 1, z + surface.zStart, 95, 3)