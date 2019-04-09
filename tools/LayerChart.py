from Classes import Surface
from Common import setBlock
from SurfaceManager import calculateHeightMapAdv
from SurfaceManager import calculateSectionMid
from SurfaceManager import calculateSections
from SurfaceManager import calculateSteepnessMap
from SurfaceManager import calculateWaterPlacement

def perform(level, box, options):
	surface = Surface(box.minx, box.minz, box.maxx, box.maxz)
	calculateHeightMapAdv(level, surface)
	calculateSteepnessMap(surface)
	calculateWaterPlacement(level, surface)
	sections = calculateSections(surface, 1, 15)
	
	for section in sections:
		calculateSectionMid(surface, section)
	
	for x in range(surface.xLength):
		for z in range(surface.zLength):
			layer = surface.surfaceMap[x][z].layer
			setBlock(level, surface.xStart + x, 159, surface.zStart + z, 251)
			setBlock(level, surface.xStart + x, 160, surface.zStart + z, 95, ((layer + 1) % 15) + 1)
