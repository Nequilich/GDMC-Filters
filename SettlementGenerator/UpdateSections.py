from collections import deque
from Classes import Point
from Classes import Section

def updateSections(surface, allowedSteepness = 0, minSize = 1):
	sections = []
	isChecked = [] #A matrix the keeps track of which points are checked
	for x in range(surface.xLength):
		row = []
		for z in range(surface.zLength):
			row.append(False)
		isChecked.append(row)

	id = 0
	for x in range(surface.xLength):
		for z in range(surface.zLength):
			if (isChecked[x][z]):
				continue
			if (surface.surface[x][z].steepness <= allowedSteepness):
				section = getSection(id, Point(x, z), surface, isChecked, allowedSteepness)
				if (section.size >= minSize):
					registerIdsOnSurface(surface, section)
					sections.append(section)
					id += 1
			isChecked[x][z] = True
	print(str(id))
	return sections

def registerIdsOnSurface(surface, section):
	for point in section.points:
		surface.surface[point.x][point.z].sectionId = section.id

def getSection(id, startPoint, surface, isChecked, allowedSteepness):
	section = Section(id)
	isWaterSection = surface.surface[startPoint.x][startPoint.z].isWater
	pointsToCheck = deque()
	pointsToCheck.append(startPoint)
	isChecked[0][0] = True
	while (pointsToCheck):
		nextPoint = pointsToCheck.popleft()
		x = nextPoint.x
		z = nextPoint.z
		if surface.surface[x][z].isWater == isWaterSection and surface.surface[x][z].steepness <= allowedSteepness:
			section.points.append(nextPoint)
			pointsToCheck.extend(getNeighboursToCheck(nextPoint, surface, isChecked))
	section.size = len(section.points)
	return section

def getNeighboursToCheck(point, surface, isChecked):
	neighboursToCheck = []
	x = point.x
	z = point.z
	if (x + 1) < surface.xLength and not isChecked[x + 1][z]:
		isChecked[x + 1][z] = True
		neighboursToCheck.append(Point(x + 1, z))
	if (z + 1) < surface.zLength and not isChecked[x][z + 1]:
		isChecked[x][z + 1] = True
		neighboursToCheck.append(Point(x, z + 1))
	if (x - 1) >= 0 and not isChecked[x - 1][z]:
		isChecked[x - 1][z] = True
		neighboursToCheck.append(Point(x - 1, z))
	if (z - 1) >= 0 and not isChecked[x][z - 1]:
		isChecked[x][z - 1] = True
		neighboursToCheck.append(Point(x, z - 1))
	return neighboursToCheck