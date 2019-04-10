import heapq
from Classes import Point
from Classes import Surface
from Common import getEuclideanDistance
from SurfaceManager import calculateHeightMapAdv
from SurfaceManager import calculateSectionMid
from SurfaceManager import calculateSections
from SurfaceManager import calculateSteepnessMap
from SurfaceManager import calculateWaterPlacement
from TowerBuilder import buildMediumTower

def perform(level, box, options):
	surface = Surface(box.minx, box.minz, box.maxx, box.maxz)
	calculateHeightMapAdv(level, surface)
	calculateSteepnessMap(surface)
	calculateWaterPlacement(level, surface)
	sections = calculateSections(surface, 1, 15)

	landSections = []
	waterSections = []
	for section in sections:
		calculateSectionMid(surface, section)
		if section.layerDepth < 2:
			continue
		if section.isWater:
			waterSections.append(section)
		else:
			landSections.append(section)
	
	averageSurfaceHeight = calculateAverageSurfaceHeight(surface)

	sectionHeap = []
	largestTuples = []
	for section in landSections:
		averageSectionHeight = calculateAverageSectionHeight(surface, section)
		heapq.heappush(sectionHeap, (averageSectionHeight, section))
	
	n = int(len(sectionHeap)/5)
	for sectionTuple in heapq.nlargest(n, sectionHeap):
		section = sectionTuple[1]
		if sectionTuple[0] < averageSurfaceHeight:
			continue
		
		pointHeap = []		
		for point in section.points:
			surfacePoint = surface.surfaceMap[point.x][point.z]
			if surfacePoint.layer == 1:
				heapq.heappush(pointHeap, (surfacePoint.height, point))
		
		largestTuple = heapq.nlargest(1, pointHeap)[0]
		largestTuples.append(largestTuple)
	
	ltHeap = []
	towers = []
	for t in largestTuples:
		heapq.heappush(ltHeap, (-t[0], t[1]))
	while ltHeap:
		t = heapq.heappop(ltHeap)
		tooClose = False
		point = t[1]
		height = -t[0]
		for p in towers:
			distance = getEuclideanDistance(surface, point, p)
			if distance < 40:
				tooClose = True
		if not tooClose:
			buildMediumTower(level, Point(surface.xStart + point.x, surface.zStart + point.z), height, 'north')
			towers.append(point)

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