from Common import setBlock
from GetRectangle import getRectangle
from GetSurfaceAdv import getSurface

def perform(level, box, options):
	surface = getSurface(level, box.minx, box.minz, box.maxx, box.maxz)
	for x in range(surface.xLength):
		for z in range(surface.zLength):
			y = surface.surface[x][z].height
			setBlock(level, x + surface.xStart, y + 1, z + surface.zStart, 20)

	rec = getRectangle(surface, int(surface.xLength / 2), int(surface.zLength / 2), 1)
	for x in range(rec.xStart, rec.xEnd):
		for z in range(rec.zStart, rec.zEnd):
			y = surface.surface[x][z].height
			setBlock(level, x + surface.xStart, y + 1, z + surface.zStart, 95, 3)