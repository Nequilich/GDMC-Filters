from BiomeFinder import findBiomes
from Classes import Surface
from Common import setBlock
from SurfaceManager import calculateHeightMapAdv
from SurfaceManager import calculateSteepnessMap

def perform(level, box, options):
	surface = Surface(box.minx, box.minz, box.maxx, box.maxz)
	calculateHeightMapAdv(level, surface)
	calculateSteepnessMap(surface)
	findBiomes(level, surface)

	for x in range(surface.xLength):
		for z in range(surface.zLength):
			placeBiomeBlocks(level, surface, x, z)

d = {
	0: (9, 0),
	1: (2, 0),
	2: (12, 0),
	3: (35, 7),
	4: (18, 0),
	5: (18, 1),
	6: (35, 13),
	7: (35, 3),
	16: (19, 0),
	17: (24, 0),
	18: (18, 0),
	19: (18, 1),
	20: (35, 7),
	21: (18, 3),
	22: (18, 3),
	23: (18, 3),
	24: (9, 0),
	25: (19, 0),
	27: (18, 2),
	28: (18, 2)
	}
def placeBiomeBlocks(level, surface, x, z):
	biomeId = surface.surfaceMap[x][z].biomeId
	blockType = d.get(biomeId, (35, 15))
	setBlock(level, surface, x, 250, z, blockType)