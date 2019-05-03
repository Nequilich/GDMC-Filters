from Classes import Surface
from Common import setBlock
from SurfaceManager import calculateHeightMapAdv
from SurfaceManager import calculateSteepnessMap

def perform(level, box, options):
	surface = Surface(box.minx, box.minz, box.maxx, box.maxz)
	calculateHeightMapAdv(level, surface)
	calculateSteepnessMap(surface)

	for x in range(surface.xLength):
		for z in range(surface.zLength):
			placeSteepnessBlocks(level, surface, x, z)

d = {
	0: (35, 0),
	1: (35, 8),
	2: (1, 3),
	3: (4, 0),
	4: (7, 0)
	}
def placeSteepnessBlocks(level, surface, x, z):
	steepness = surface.surfaceMap[x][z].steepness
	blockType = d.get(steepness, (35, 15))
	setBlock(level, surface, x, 250, z, blockType)