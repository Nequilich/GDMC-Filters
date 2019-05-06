from Classes import Surface
from Common import setBlock
from SurfaceManager import calculateHeightMapAdv
from SurfaceManager import calculateSectionMid
from SurfaceManager import calculateSections
from SurfaceManager import calculateSteepnessMap
from SurfaceManager import calculateWaterPlacement

# layerBlocks = [(35, 13), (18, 1), (2, 0), (19, 0), (41, 0), (35, 1), (35, 14), (35, 12)]
layerBlocks = [
	(35, 13),
	(18, 1),
	(2, 0),
	(19, 0),
	(41, 0),
	(35, 1),
	(35, 14),
	(35, 12)
]

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
			# block = layerBlocks[min([layer + 1, len(layerBlocks) - 1])]
			block = layerBlocks[(layer + 1) % len(layerBlocks)]
			if surface.surfaceMap[x][z].isWater or surface.surfaceMap[x][z].sectionId == -1:
				block = (35, 15)
			setBlock(level, surface, x, 249, z, 2, 0)
			setBlock(level, surface, x, 250, z, block)
