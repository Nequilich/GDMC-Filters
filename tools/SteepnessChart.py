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
	
	blockDatas = [5, 4, 1, 14]

	for x in range(surface.xLength):
		for z in range(surface.zLength):
			if surface.surfaceMap[x][z].isWater:
				setBlock(level, surface.xStart + x, 160, surface.zStart + z, 35, 15)
				continue
			steepness = surface.surfaceMap[x][z].steepness
			setBlock(level, surface.xStart + x, 160, surface.zStart + z, 35, blockDatas[min(steepness, 3)])
