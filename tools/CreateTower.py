from Classes import Point
from Classes import Surface
from SurfaceManager import calculateHeightMapAdv
from TowerBuilder import buildMediumTower

def perform(level, box, options):
	surface = Surface(box.minx, box.minz, box.maxx, box.maxz)
	calculateHeightMapAdv(level, surface)

	buildMediumTower(level, Point(box.minx, box.minz), box.miny)