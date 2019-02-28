def getFlatAreas(surface, allowedSteepness = 0):
	#isVisitedList = [[False] * surface.zLength] * surface.xLength
	isVisitedList = []
	for x in range(surface.xLength):
		row = []
		for z in range(surface.zLength):
			row.append(False)
		isVisitedList.append(row)

	flatAreas = []
	for x in range(surface.xLength):
		for z in range(surface.zLength):
			if (isVisitedList[x][z]):
				continue
			if (surface.surface[x][z].steepness == 0):
				flatAreas.append(getArea(x, z, surface, isVisitedList, allowedSteepness))
			isVisitedList[x][z] = True
	return flatAreas


def getArea(x, z, surface, isVisitedList, allowedSteepness):
	area = []
	pointsToCheck = [(x, z)]
	isVisitedList[0][0] = True
	while (pointsToCheck):
		point = pointsToCheck.pop(0)
		cx = point[0] # current x
		cz = point[1] # current z
		if surface.surface[cx][cz].steepness <= allowedSteepness:
			area.append((cx, cz))
			pointsToCheck.extend(getNeighboursToCheck(cx, cz, surface, isVisitedList))
	return area


def getNeighboursToCheck(x, z, surface, isVisitedList):
	neighboursToCheck = []
	if (x + 1) < surface.xLength and not isVisitedList[x + 1][z]:
		isVisitedList[x + 1][z] = True
		neighboursToCheck.append((x + 1, z))
	if (z + 1) < surface.zLength and not isVisitedList[x][z + 1]:
		isVisitedList[x][z + 1] = True
		neighboursToCheck.append((x, z + 1))
	if (x - 1) >= 0 and not isVisitedList[x - 1][z]:
		isVisitedList[x - 1][z] = True
		neighboursToCheck.append((x - 1, z))
	if (z - 1) >= 0 and not isVisitedList[x][z - 1]:
		isVisitedList[x][z - 1] = True
		neighboursToCheck.append((x, z - 1))
	return neighboursToCheck
