import heapq

from Classes import Point
from Classes import Surface
from Common import getEuclideanDistance
from Common import setBlock
from PathManager import getPathsBetweenSections
from PathManager import getPathsInSections
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
	calculateSectionMids(surface, sections)
	
	smallLandSections = []
	mediumLandSections = []
	bigLandSections = []
	waterSections = []

	arrangeSections(sections, waterSections, bigLandSections, mediumLandSections, smallLandSections)

	paintSections(level, surface, smallLandSections, mediumLandSections, bigLandSections, waterSections)

	averageSurfaceHeight = calculateAverageSurfaceHeight(surface)
	calculateAverageSectionHeights(surface, sections)

	towerSections = getTowerSections(surface, averageSurfaceHeight, bigLandSections, mediumLandSections, smallLandSections)

	habitatSections = getHabitatSections(towerSections, mediumLandSections, bigLandSections)

	paths = getPathsInSections(surface, bigLandSections)

	paintPathPoints(level, surface, habitatSections)
	paintPaths(level, surface, paths, (35, 8))

	intersectionPaths = getPathsBetweenSections(surface, habitatSections)
	paths.extend(intersectionPaths)

	paintPaths(level, surface, intersectionPaths, (35, 2))

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

def paintSections(level, surface, smallLandSections, mediumLandSections, bigLandSections, waterSections):
	for x in range(surface.xLength):
		for z in range(surface.zLength):
			setBlock(level, surface, x, 250, z, 35, 15)

	for s in smallLandSections:
		for p in s.points:
			setBlock(level, surface, p.x, 250, p.z, 35, 5)

	for s in mediumLandSections:
		for p in s.points:
			setBlock(level, surface, p.x, 250, p.z, 2)

	for s in bigLandSections:
		for p in s.points:
			setBlock(level, surface, p.x, 250, p.z, 35, 13)

	for s in waterSections:
		for p in s.points:
			setBlock(level, surface, p.x, 250, p.z, 35, 11)

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
	maxAmount = (surface.xLength * surface.zLength) / 25000 + 1
	sectionHeap = heapifySectionsByAverageHeight(smallLandSections)
	towerSections = []
	for i, element in enumerate(sectionHeap):
		if i >= maxAmount:
			break
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
		if distance < 100:
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

def paintPathPoints(level, surface, habitatSections):
	for section in habitatSections:
		for x in [section.xMid - 1, section.xMid, section.xMid + 1]:
			for z in [section.zMid - 1, section.zMid, section.zMid + 1]:
				setBlock(level, surface, x, 251, z, 2)
				setBlock(level, surface, x, 252, z, 38)

		for p in section.pathConnectionPoints:
			for x in [p.x - 1, p.x, p.x + 1]:
				for z in [p.z - 1, p.z, p.z + 1]:
					setBlock(level, surface, x, 251, z, 35, 1)

def paintPaths(level, surface, paths, blockType):
	for path in paths:
		for point in path:
			setBlock(level, surface, point.x, 250, point.z, blockType)