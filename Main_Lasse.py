from Classes import Surface
from Common import setBlock
from GetPath import getPath
from PathManager import getPathsBetweenSections
from PathManager import getPathsInSection
from GetPropertiesAlongPath import getPropertiesAlongPath
from HouseBuilder import buildHouse
from SurfaceManager import calculateHeightMapAdv
from SurfaceManager import calculateSteepnessMap
from SurfaceManager import calculateWaterPlacement
from SurfaceManager import calculateSections
from SurfaceManager import calculateSectionMid

def perform(level, box, options):
	surface = Surface(box.minx, box.minz, box.maxx, box.maxz)
	calculateHeightMapAdv(level, surface)
	calculateSteepnessMap(surface)
	calculateWaterPlacement(level, surface)
	sections = calculateSections(surface, 1, 250)
	landSections = []
	for section in sections:
		if not section.isWater:
			calculateSectionMid(surface, section)
			landSections.append(section)
	bigPaths = getPathsBetweenSections(surface, landSections)
	smallPaths = []
	for section in landSections:
		smallPaths.extend(getPathsInSection(surface, section))

	for x in range(surface.xLength):
		for z in range(surface.zLength):
			height = surface.surfaceMap[x][z].height
			if surface.surfaceMap[x][z].isWater:	
				setBlock(level, surface, x, height, z, 22)
			elif surface.surfaceMap[x][z].sectionId == -1:	
				setBlock(level, surface, x, height, z, 35, 15)
			else:
				i = surface.surfaceMap[x][z].sectionId
				setBlock(level, surface, x, height, z, 35, i % 15)

	for path in smallPaths:
		for p in path:
			height = surface.surfaceMap[p.x][p.z].height
			setBlock(level, surface, p.x, height, p.z, 41)

	for path in bigPaths:
		for p in path:
			height = surface.surfaceMap[p.x][p.z].height
			setBlock(level, surface, p.x, height, p.z, 57)