import utilityFunctions as utilityFunctions


def createPlateform(level, minx, maxx, minz, maxz, baseHeight):
	generatePillars(level, minx, maxx, minz, maxz, baseHeight)
	generateCeiling(level, minx, maxx, minz, maxz, baseHeight)


class Section:
	def __init__(self, minx, maxx, minz, maxz, miny, maxy):
		self.minx = minx
		self.maxx = maxx
		self.minz = minz
		self.maxz = maxz
		self.miny = miny
		self.maxy = maxy


def generatePillars(level, minx, maxx, minz, maxz, baseHeight):
	fillSection(level, (1, 0), Section(
			minx,
			minx + 1,
			minz,
			minz + 1,
			baseHeight + 1,
      baseHeight + 17))
	fillSection(level, (1, 0), Section(
			minx + 31,
			minx + 32,
			minz,
			minz + 1,
			baseHeight + 1,
      baseHeight + 17))
	fillSection(level, (1, 0), Section(
			minx,
			minx + 1,
			minz + 31,
			minz + 32,
			baseHeight + 1,
      baseHeight + 17))
	fillSection(level, (1, 0), Section(
			minx + 31,
			minx + 32,
			minz + 31,
			minz + 32,
			baseHeight + 1,
      baseHeight + 17))


def generateCeiling(level, minx, maxx, minz, maxz, baseHeight):
	fillSection(level, (1, 0), Section(
			minx,
			minx + 32,
			minz,
			minz + 32,
			baseHeight + 16,
      baseHeight + 17))
	fillSection(level, (2, 0), Section(
			minx + 1,
			minx + 31,
			minz + 1,
			minz + 31,
			baseHeight + 16,
      baseHeight + 17))


def fillSection(level, blockType, section):
	for x in range(section.minx, section.maxx):
		for z in range(section.minz, section.maxz):
			for y in range(section.baseHeight, section.maxy):
				utilityFunctions.setBlock(level, blockType, x, y, z)
