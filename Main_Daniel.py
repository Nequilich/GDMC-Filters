from Classes import Point
from Classes import Surface
from Common import getEuclideanDistance
from Common import setBlock
from GetPath import getPath
import heapq
from Kruskal import getMinimumSpanningTree
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
		calculateSectionMid(surface, section)

	distances = [] # Tuples: (distance, (section1, section2))
	sectionIds = []
	for section in sections:
		height = surface.surfaceMap[section.xMid][section.zMid].height
		setBlock(level, surface.xStart + section.xMid, height + 2, surface.zStart + section.zMid, 41)
		sectionIds.append(section.id)
		for otherSection in sections:
			if (otherSection.id <= section.id):
				continue
			sectionMidPoint = Point(section.xMid, section.zMid)
			otherSectionMidPoint = Point(otherSection.xMid, otherSection.zMid)
			heapq.heappush(distances, (getEuclideanDistance(surface, sectionMidPoint, otherSectionMidPoint), (section.id, otherSection.id)))
	
	minimumSpanningTree = getMinimumSpanningTree(sectionIds, distances)
	roads = [] # Tuples: (point1, point2)
	for connection in minimumSpanningTree:
		section1 = getSection(sections, connection[0])
		section2 = getSection(sections, connection[1])
		startPoint = Point(section1.xMid, section1.zMid)
		endPoint = Point(section2.xMid, section2.zMid)
		roads.append((startPoint, endPoint))
	paths = []
	for road in roads:
		paths.append(getPath(surface, road[0].x, road[0].z, road[1].x, road[1].z))
	for path in paths:
		for p in path:
			y = surface.surfaceMap[p.x][p.z].height
			setBlock(level, p.x + surface.xStart, y + 1, p.z + surface.zStart, 57, 0)

def getSection(sections, id):
	for section in sections:
		if section.id == id:
			return section
	return None