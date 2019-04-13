from Classes import Point
from Classes import Surface
from SurfaceManager import calculateHeightMapAdv
from StructureBuilder import buildStructure
from Biomes import biomes, getBiomeDict
from BiomeFinder import findBiomes

def perform(level, box, options):
	surface = Surface(box.minx, box.minz, box.maxx, box.maxz)
	calculateHeightMapAdv(level, surface)
	findBiomes(level, surface)

	point = Point(box.minx, box.minz)
	surfaceX = point.x - surface.xStart
	surfaceZ = point.z - surface.zStart

	# biome = options["Biome"]
	biomeDict = getBiomeDict()
	biome = biomeDict[surface.surfaceMap[surfaceX][surfaceZ].biomeId]

	buildStructure(level, Point(point.x - 5, point.z - 5), box.miny, 'tower', 'east', True, None, biome)