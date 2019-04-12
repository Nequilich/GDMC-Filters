from Classes import Point
from Classes import Surface
from SurfaceManager import calculateHeightMapAdv
from TowerBuilder import buildMediumTower
from Biomes import biomes, getBiomeDict
from BiomeFinder import findBiomes

# inputs = (
# 	("Biome", tuple(biomes.keys())),
# )

def perform(level, box, options):
	surface = Surface(box.minx, box.minz, box.maxx, box.maxz)
	calculateHeightMapAdv(level, surface)
	findBiomes(level, surface)

	point = Point(box.minx, box.minz)
	surfaceX = point.x - surface.xStart
	surfaceZ = point.z - surface.zStart

	specialBiomeChanges = {
		'jungle': {
			'cobblestone': 'brick',
			'oak_wood': 'acacia_wood',
			'oak_wood_planks': 'acacia_wood_planks'
		}
	}

	# biome = options["Biome"]
	biomeDict = getBiomeDict()
	biome = biomeDict[surface.surfaceMap[surfaceX][surfaceZ].biomeId]

	buildMediumTower(level, point, box.miny, 'east', True, None, biome)