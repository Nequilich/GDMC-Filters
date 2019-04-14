from BiomeFinder import findBiomes
from Classes import Surface
from Common import setBlock
from FarmBuilder import buildFarm
from FarmBuilder import clearFarmProperty
from GetPath import getPath
from GetPropertiesAlongPath import getPropertiesAlongPath
from HouseBuilder import buildHouse
from HouseBuilder import clearHouseProperty
from PathManager import getPathsBetweenSections
from PathManager import getPathsInSections
from RoadBuilder import buildTestRoad
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
	findBiomes(level, surface)
	sections = calculateSections(surface, 1, 100)

	landSections = []
	for section in sections:
		if not section.isWater:
			calculateSectionMid(surface, section)
			landSections.append(section)

	paths = getPathsInSections(surface, landSections)
	paths.extend(getPathsBetweenSections(surface, landSections))

	for path in paths:
		buildTestRoad(level, surface, path)

	# Builds houses
	houseProperties = []
	for path in paths:
		houseProperties.extend(getPropertiesAlongPath(surface, path, 7, 11, 7))

	for p in houseProperties:
		clearHouseProperty(level, surface, p)

	for p in houseProperties:
		buildHouse(level, surface, p)
		buildPathway(level, surface, p.xPathwayStart, p.zPathwayStart, p.xPathwayEnd, p.zPathwayEnd)

	# Builds farms
	patchProperties = []
	for path in paths:
		patchProperties.extend(getPropertiesAlongPath(surface, path, 7, 11, 16))

	for p in patchProperties:
		clearFarmProperty(level, surface, p)

	for p in patchProperties:
		buildFarm(level, surface, p)

def buildPathway(level, surface, xStart, zStart, xEnd, zEnd):
	path = getPath(surface, xStart, zStart, xEnd, zEnd)
	for p in path:
		height = surface.surfaceMap[p.x][p.z].height
		setBlock(level, surface, p.x, height + 1, p.z, 0)
		setBlock(level, surface, p.x, height + 2, p.z, 0)
		if not surface.surfaceMap[p.x][p.z].isOccupied:
			setBlock(level, surface, p.x, height, p.z, 4)