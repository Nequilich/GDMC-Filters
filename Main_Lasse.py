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
	sections = calculateSections(surface, 1, 40)

	for x in range(surface.xLength):
		for z in range(surface.zLength):
			height = surface.surfaceMap[x][z].height
			sectionId = surface.surfaceMap[x][z].sectionId
			if sectionId == -1:
				setBlock(level, surface.xStart + x, height + 1, surface.zStart + z, 20)
			else:
				setBlock(level, surface.xStart + x, height + 1, surface.zStart + z, 95, sectionId % 15 + 1)

	for section in sections:
		calculateSectionMid(surface, section, level)

	for section in sections:
		height = surface.surfaceMap[section.xMid][section.zMid].height
		setBlock(level, surface.xStart + section.xMid, height + 2, surface.zStart + section.zMid, 57)