def getRectangle(surface, xFirst, zFirst, heightRange):
	rec = Rectangle(xFirst, zFirst, xFirst + 1, zFirst + 1)
	height = surface.surfaceMap[xFirst][zFirst].height
	continueUp = True
	continueRight = True
	continueDown = True
	continueLeft = True
	while continueUp or continueRight or continueDown or continueLeft:
		if continueUp:
			continueUp = isValidHorizontalArea(surface, rec.xStart, rec.xEnd, rec.zEnd, surface.zLength, height, heightRange)
			if continueUp:
				rec.zEnd += 1
		if continueRight:
			continueRight = isValidVerticalArea(surface, rec.zStart, rec.zEnd, rec.xEnd, surface.xLength, height, heightRange)
			if continueRight:
				rec.xEnd += 1
		if continueDown:
			continueDown = isValidHorizontalArea(surface, rec.xStart, rec.xEnd, rec.zStart - 1, -1, height, heightRange)
			if continueDown:
				rec.zStart -= 1
		if continueLeft:
			continueLeft = isValidVerticalArea(surface, rec.zStart, rec.zEnd, rec.xStart - 1, -1, height, heightRange)
			if continueLeft:
				rec.xStart -= 1
	return rec

def isValidHorizontalArea(surface, xStart, xEnd, z, zBorder, height, heightRange):
	if z == zBorder:
		return False
	for x in range(xStart, xEnd):
		if surface.surfaceMap[x][z].height < height or surface.surfaceMap[x][z].height > height + heightRange or surface.surfaceMap[x][z].isOccupied:
			return False
	return True

def isValidVerticalArea(surface, zStart, zEnd, x, xBorder, height, heightRange):
	if x == xBorder:
		return False
	for z in range(zStart, zEnd):
		if surface.surfaceMap[x][z].height < height or surface.surfaceMap[x][z].height > height + heightRange or surface.surfaceMap[x][z].isOccupied:
			return False
	return True

class Rectangle:

	def __init__(self, xStart, zStart, xEnd, zEnd):
		self.xStart = xStart
		self.zStart = zStart
		self.xEnd = xEnd
		self.zEnd = zEnd