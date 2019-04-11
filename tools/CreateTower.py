from Classes import Point
from Classes import Surface
from SurfaceManager import calculateHeightMapAdv
from TowerBuilder import buildMediumTower

def perform(level, box, options):
	surface = Surface(box.minx, box.minz, box.maxx, box.maxz)
	calculateHeightMapAdv(level, surface)

	specialBiomeChanges = {
		'jungle': {
			'cobblestone': 'brick',
			'oak_wood': 'acacia_wood',
			'oak_wood_planks': 'acacia_wood_planks'
		}
	}

	buildMediumTower(level, Point(box.minx, box.minz), box.miny, 'east', True, specialBiomeChanges, 'jungle')