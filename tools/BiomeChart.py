from Common import setBlock
from Classes import Surface
from SurfaceManager import calculateHeightMapAdv
from BiomeFinder import findBiomes
import Biomes
import time

inputs = (
	("Chart height", 100),
)

def perform(level, box, options):
	surface = Surface(box.minx, box.minz, box.maxx, box.maxz)
	calculateHeightMapAdv(level, surface)

	# BiomeFinder adds biome data to surfaceMap
	findBiomes(level, surface)

	# Makes a colored map of biomes in the sky
	height = options["Chart height"]
	biomeIds = Biomes.getBiomeDict()
	biomeNameList = Biomes.biomes.keys()
	for x in range(surface.xLength):
		for z in range(surface.zLength):
			biomeName = biomeIds[surface.surfaceMap[x][z].biomeId]

			for i in range(len(biomeNameList)):
				if biomeName == biomeNameList[i]:
					setBlock(level, surface, x, height, z, 35, i)