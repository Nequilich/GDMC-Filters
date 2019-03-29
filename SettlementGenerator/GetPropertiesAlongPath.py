from GetRectangle import getRectangle

gap = 10
lengthFromCenter = 8
def getPropertiesAlongPath(surface, path):
	properties = []
	for i, point in enumerate(path):
		if i % gap != 0:
			continue
		for p in [(point.x + lengthFromCenter, point.z, "WEST"), (point.x - lengthFromCenter, point.z, "EAST"), (point.x, point.z + lengthFromCenter, "SOUTH"), (point.x, point.z - lengthFromCenter, "NORTH")]:
			x = p[0]
			z = p[1]
			if not isWithinBorder(surface, x, z) or surface.surfaceMap[x][z].isOccupied or surface.surfaceMap[x][z].isWater:
				continue
			prop = getProperty(surface, x, z, p[2], point.x, point.z)
			if prop:
				properties.append(prop)
				occupyArea(surface, prop.xStart, prop.zStart, prop.xEnd, prop.zEnd)
	return properties

def isWithinBorder(surface, x, z):
	return x >= 0 and x < surface.xLength and z >= 0 and z < surface.zLength

propertyMinWidth = 7
propertyMaxWidth = 11
def getProperty(surface, x, z, doorDirection, xPathwayEnd, zPathwayEnd):
	rec = getRectangle(surface, x, z, 1, propertyMaxWidth)
	if rec.xLength >= propertyMinWidth and rec.zLength >= propertyMinWidth:
		height = surface.surfaceMap[x][z].height
		return Property(rec.xStart, rec.zStart, rec.xEnd, rec.zEnd, height, doorDirection, xPathwayEnd, zPathwayEnd)
	return None

def occupyArea(surface, xStart, zStart, xEnd, zEnd):
	for x in range(xStart, xEnd):
		for z in range(zStart, zEnd):
			surface.surfaceMap[x][z].isOccupied = True

class Property:

	def __init__(self, xStart, zStart, xEnd, zEnd, height, doorDirection, xPathwayEnd, zPathwayEnd):
		self.xStart = xStart
		self.zStart = zStart
		self.xEnd = xEnd
		self.zEnd = zEnd
		self.xLength = xEnd - xStart
		self.zLength = zEnd - zStart
		self.height = height
		self.doorDirection = doorDirection
		self.xPathwayEnd = xPathwayEnd
		self.zPathwayEnd = zPathwayEnd