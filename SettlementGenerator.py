from Classes import Surface
from Common import setBlock
from FarmBuilder import buildPatch
from FarmBuilder import clearPatchProperty
from GetPath import getPath
from GetPropertiesAlongPath import getPropertiesAlongPath
from HouseBuilder import buildHouse
from HouseBuilder import clearHouseProperty
from PathManager import getPathsBetweenSections
from PathManager import getPathsInSection
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
	sections = calculateSections(surface, 1, 100)
	landSections = []
	for section in sections:
		if not section.isWater:
			calculateSectionMid(surface, section)
			landSections.append(section)
	paths = getPathsBetweenSections(surface, landSections)

	for section in landSections:
		paths.extend(getPathsInSection(surface, section))

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

	# Builds patches
	patchProperties = []
	for path in paths:
		patchProperties.extend(getPropertiesAlongPath(surface, path, 5, 11, 16))

	for p in patchProperties:
		clearPatchProperty(level, surface, p)

	for p in patchProperties:
		buildPatch(level, surface, p)

def buildPathway(level, surface, xStart, zStart, xEnd, zEnd):
	path = getPath(surface, xStart, zStart, xEnd, zEnd)
	for p in path:
		if surface.surfaceMap[p.x][p.z].isOccupied:
			continue
		height = surface.surfaceMap[p.x][p.z].height
		setBlock(level, surface, p.x, height, p.z, 4)