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
			placeHeightBlocks(level, surface, x, z)

d = [
	(35, 11),
	(35, 9),
	(35, 3),
	(2, 0),
	(35, 0),
	(41, 0),
	(35, 1),
	(100, 0)
	]
length = len(d)

def placeHeightBlocks(level, surface, x, z):
	height = surface.surfaceMap[x][z].height
	i = (height - 60) / 7
	if i < 0:
		i = 0
	elif i >= length:
		i = length - 1
	setBlock(level, surface, x, 250, z, d[i])

def test(level, surface):
	length = len(d)
	for i in range(length):
		setBlock(level, surface, i, 80, 0, d[i])