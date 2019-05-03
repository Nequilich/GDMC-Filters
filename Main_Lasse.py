from BiomeFinder import findBiomes
from Biomes import getBiomeDict
from Classes import Surface
from Common import setBlock
from SurfaceManager import calculateHeightMapAdv
from SurfaceManager import calculateSections
from SurfaceManager import calculateSteepnessMap
from SurfaceManager import calculateWaterPlacement

def perform(level, box, options):
	surface = Surface(box.minx, box.minz, box.maxx, box.maxz)
	calculateHeightMapAdv(level, surface)
	calculateSteepnessMap(surface)
	calculateWaterPlacement(level, surface)
	findBiomes(level, surface)
	sections = calculateSections(surface, 1, 15)

	for x in range(surface.xLength):
		for z in range(surface.zLength):
			placeSteepnessBlocks(level, surface, x, 250, z)
			placeBiomeBlocks(level, surface, x, 251, z)

d1 = {0: (35, 0), 1: (35, 8), 2: (35, 7)}
def placeSteepnessBlocks(level, surface, x, y, z):
	steepness = surface.surfaceMap[x][z].steepness
	blockType = d1.get(steepness, (35, 15))
	setBlock(level, surface, x, y, z, blockType)

d2 = {
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
	27: (18, 2),
	28: (18, 2)
	}
def placeBiomeBlocks(level, surface, x, y, z):
	biomeId = surface.surfaceMap[x][z].biomeId
	blockType = d2.get(biomeId, (35, 15))
	setBlock(level, surface, x, y, z, blockType)