from Classes import Point
from Classes import Surface
from Common import getEuclideanDistance
from Common import setBlock
from GetPath import getPath
import heapq
from SurfaceManager import calculateHeightMapAdv
from SurfaceManager import calculateSectionMidSimple
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
		calculateSectionMidSimple(surface, section)

	distances = [] # Tuples: (distance, (section1, section2))
	for section in sections:
		height = surface.surfaceMap[section.xMid][section.zMid].height
		setBlock(level, surface.xStart + section.xMid, height + 2, surface.zStart + section.zMid, 41)
		for otherSection in sections:
			if (otherSection.id <= section.id):
				continue
			sectionMidPoint = Point(section.xMid, section.zMid)
			otherSectionMidPoint = Point(otherSection.xMid, otherSection.zMid)
			heapq.heappush(distances, (getEuclideanDistance(surface, sectionMidPoint, otherSectionMidPoint), (section.id, otherSection.id)))

	roads = [] # Tuples: (point1, point2)
	disjointSets = []
	for section in sections:
		tree = []
		tree.append(section.id)
		disjointSets.append(tree)
	print('start')
	while len(disjointSets) > 1:
		if not distances:
			break
		distance = heapq.heappop(distances)
		section1 = getSection(sections, distance[1][0])
		section2 = getSection(sections, distance[1][1])
		set1 = findSet(disjointSets, section1)
		set2 = findSet(disjointSets, section2)
		if set1 == None or set2 == None:
			break
		if set1 == set2:
			print("s1: " + str(set1) + " s2: " + str(set2))
			continue
		mergeSets(disjointSets, set1, set2)
		roads.append((Point(section1.xMid, section1.zMid), Point(section2.xMid, section2.zMid)))
	paths = []
	for road in roads:
		paths.append(getPath(surface, road[0].x, road[0].z, road[1].x, road[1].z))
	for path in paths:
		for p in path:
			y = surface.surfaceMap[p.x][p.z].height
			setBlock(level, p.x + surface.xStart, y, p.z + surface.zStart, 57, 0)

def findSet(sets, section):
	for s in sets:
		if section.id in s:
			return s
	return None

def mergeSets(sets, set1, set2):
	print(set1)
	print(set2)
	set1Index = -1
	set2Index = -1
	for i, s in enumerate(sets):
		if set1 == s:
			set1Index = i
		if set2 == s:
			set2Index = i
	sets.pop(set1Index)
	sets.pop(set2Index - 1)
	newSet = []
	for i in set1:
		newSet.append(i)
	for i in set2:
		newSet.append(i)
	sets.append(newSet)

def getSection(sections, id):
	for section in sections:
		if section.id == id:
			return section
	return None