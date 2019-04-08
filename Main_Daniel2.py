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
	sections = calculateSections(surface, 1, 24)

	landSections = []
	waterSections = []
	for section in sections:
		calculateSectionMid(surface, section)
		if section.layerDepth < 3:
			continue
		if section.isWater:
			waterSections.append(section)
		else:
			landSections.append(section)
	
	averageSurfaceHeight = calculateAverageSurfaceHeight(surface)

	for section in landSections:
		averageSectionHeight = calculateAverageSectionHeight(surface, section)
		if averageSectionHeight < averageSurfaceHeight:
			continue
		
		highestHeight = 0
		highestPoint = None

		for point in section.points:
			surfacePoint = surface.surfaceMap[point.x][point.z]
			height = surfacePoint.height
			if surfacePoint.layer == 2 and height > highestHeight:
				highestHeight = height
				highestPoint = point
		setBlock(level, surface.xStart + highestPoint.x, highestHeight + 1, surface.zStart + highestPoint.z, 57)

def calculateAverageSurfaceHeight(surface):
	cumulativeHeight = 0
	for x in range(surface.xLength):
		for z in range(surface.zLength):
			cumulativeHeight += surface.surfaceMap[x][z].height
	return cumulativeHeight / (surface.xLength * surface.zLength)

def calculateAverageSectionHeight(surface, section):
	cumulativeHeight = 0
	for point in section.points:
		x = point.x
		z = point.z
		cumulativeHeight += surface.surfaceMap[x][z].height
	return cumulativeHeight / len(section.points)