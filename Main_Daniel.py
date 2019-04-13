import heapq
from Classes import Point
from Classes import Surface
from Common import getEuclideanDistance
from Common import setBlock
from PathManager import getPathsBetweenSections
from PathManager import getPathsInSection
from SurfaceManager import calculateHeightMapAdv
from SurfaceManager import calculateSectionMid
from SurfaceManager import calculateSections
from SurfaceManager import calculateSteepnessMap
from SurfaceManager import calculateWaterPlacement
from TowerBuilder import buildMediumTower

from RoadBuilder import buildTestRoad
from GetPropertiesAlongPath import getPropertiesAlongPath
from RemoveTree import removeTree
from HouseBuilder import buildHouse
from HouseBuilder import clearHouseProperty
from FarmBuilder import buildPatch
from FarmBuilder import clearPatchProperty
from GetPath import getPath

def perform(level, box, options):
	surface = Surface(box.minx, box.minz, box.maxx, box.maxz)
	calculateHeightMapAdv(level, surface)
	calculateSteepnessMap(surface)
	calculateWaterPlacement(level, surface)

	sections = calculateSections(surface, 1, 15)
	calculateSectionMids(surface, sections)
	
	smallLandSections = []
	mediumLandSections = []
	bigLandSections = []
	waterSections = []

	arrangeSections(sections, waterSections, bigLandSections, mediumLandSections, smallLandSections)

	averageSurfaceHeight = calculateAverageSurfaceHeight(surface)
	calculateAverageSectionHeights(surface, sections)

	towerSections = getTowerSections(surface, averageSurfaceHeight, bigLandSections, mediumLandSections, smallLandSections)
	
	habitatSections = getHabitatSections(towerSections, mediumLandSections, bigLandSections)
	
	paths = getPathsBetweenSections(surface, habitatSections)
	paths.extend(getPathsInSections(surface, bigLandSections))
	buildPaths(level, surface, paths)

	properties = getProperties(surface, paths)
	clearHouseProperties(level, surface, properties)
	buildProperties(level, surface, properties)

	buildTowers(level, surface, towerSections)

	patchProperties = getPatchProperties(surface, paths)
	clearPatchProperties(level, surface, patchProperties)
	buildPatchProperties(level, surface, patchProperties)



def calculateSectionMids(surface, sections):
	for section in sections:
		calculateSectionMid(surface, section)

def arrangeSections(sections, waterSections, bigLandSections, mediumLandSections, smallLandSections):
	for section in sections:
		if section.layerDepth < 2:
			continue
		if section.isWater:
			waterSections.append(section)
			continue
		if len(section.points) < 250:
			smallLandSections.append(section)
			continue
		if len(section.points) < 1000:
			mediumLandSections.append(section)
			continue
		bigLandSections.append(section)

def calculateAverageSurfaceHeight(surface):
	cumulativeHeight = 0
	for x in range(surface.xLength):
		for z in range(surface.zLength):
			cumulativeHeight += surface.surfaceMap[x][z].height
	return cumulativeHeight / (surface.xLength * surface.zLength)

def calculateAverageSectionHeights(surface, sections):
	for section in sections:
		section.averageHeight = calculateAverageSectionHeight(surface, section)

def calculateAverageSectionHeight(surface, section):
	cumulativeHeight = 0
	for point in section.points:
		x = point.x
		z = point.z
		cumulativeHeight += surface.surfaceMap[x][z].height
	return cumulativeHeight / len(section.points)

def heapifySectionsByAverageHeight(sections):
	heap = []
	for section in sections:
		heapq.heappush(heap, (-section.averageHeight, section))
	return heap

def getTowerSections(surface, averageSurfaceHeight, bigLandSections, mediumLandSections, smallLandSections):
	sectionHeap = heapifySectionsByAverageHeight(smallLandSections)
	towerSections = []
	for element in sectionHeap:
		section = element[1]
		averageSectionHeight = section.averageHeight
		if averageSectionHeight < averageSurfaceHeight:
			break
		sectionMid = Point(section.xMid, section.zMid)
		if tooCloseToOtherTowers(surface, sectionMid, towerSections) or tooCloseToBiggerHigherSections(surface, sectionMid, averageSectionHeight, bigLandSections, mediumLandSections):
			continue
		towerSections.append(section)
	return towerSections

def tooCloseToOtherTowers(surface, sectionMid, towerSections):
	for towerSection in towerSections:
		towerSectionMid = Point(towerSection.xMid, towerSection.zMid)
		distance = getEuclideanDistance(surface, towerSectionMid, sectionMid)
		if distance < 50:
			return True
	return False

def tooCloseToBiggerHigherSections(surface, sectionMid, averageSectionHeight, bigLandSections, mediumLandSections):
	biggerSections = []
	biggerSections.extend(bigLandSections)
	biggerSections.extend(mediumLandSections)
	for s in biggerSections:
		if s.averageHeight < averageSectionHeight + 10:
			continue
		for p in s.points:
			if surface.surfaceMap[p.x][p.z].layer != 0:
				continue
			distance = getEuclideanDistance(surface, p, sectionMid)
			if distance < 30:
				return True
	return False

def getHabitatSections(towerSections, mediumLandSections, bigLandSections):
	habitatSections = []
	habitatSections.extend(towerSections)
	habitatSections.extend(mediumLandSections)
	habitatSections.extend(bigLandSections)
	return habitatSections

def buildPaths(level, surface, paths):
	for path in paths:
		buildTestRoad(level, surface, path)

def buildTowers(level, surface, towerSections):
	for section in towerSections:
		height = surface.surfaceMap[section.xMid][section.zMid].height
		buildMediumTower(level, Point(surface.xStart + section.xMid, surface.zStart + section.zMid), height, 'north')











def getPathsInSections(surface, bigLandSections):
	paths = []
	for section in bigLandSections:
		paths.extend(getPathsInSection(surface, section))
	return paths

def getProperties(surface, paths):
	properties = []
	for path in paths:
		properties.extend(getPropertiesAlongPath(surface, path, 7, 11, 7))
	return properties

def clearHouseProperties(level, surface, houseProperties):
	for p in houseProperties:
		clearHouseProperty(level, surface, p)

def buildProperties(level, surface, properties):
	for p in properties:
		buildHouse(level, surface, p)
		buildPathway(level, surface, p.xPathwayStart, p.zPathwayStart, p.xPathwayEnd, p.zPathwayEnd)

def getPatchProperties(surface, paths):
	patchProperties = []
	for path in paths:
		patchProperties.extend(getPropertiesAlongPath(surface, path, 5, 11, 16))
	return patchProperties

def clearPatchProperties(level, surface, patchProperties):
	for p in patchProperties:
		clearPatchProperty(level, surface, p)

def buildPatchProperties(level, surface, patchProperties):
	for p in patchProperties:
		buildPatch(level, surface, p)

# fra Lasse

def buildPathway(level, surface, xStart, zStart, xEnd, zEnd):
	path = getPath(surface, xStart, zStart, xEnd, zEnd)
	for p in path:
		if surface.surfaceMap[p.x][p.z].isOccupied:
			continue
		height = surface.surfaceMap[p.x][p.z].height
		setBlock(level, surface, p.x, height, p.z, 4)

def removeTrees(level, surface, prop):
	for x in range(prop.xStart, prop.xEnd):
		for z in range(prop.zStart, prop.zEnd):
			y = surface.surfaceMap[x][z].height + 2
			removeTree(level, x + surface.xStart, y, z + surface.zStart)