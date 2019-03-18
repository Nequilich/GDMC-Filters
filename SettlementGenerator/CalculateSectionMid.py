def calculateSectionMid(surface, section):
	xTotal = 0
	zTotal = 0
	for point in section.points:
		xTotal += point.x
		zTotal += point.z
	section.xMid = xTotal / section.size
	section.zMid = zTotal / section.size