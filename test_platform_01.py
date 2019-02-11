import utilityFunctions as utilityFunctions

inputs = (
	("Design platfrom", "label"),
	("Creator: Daniel Lundin", "label"),
)


def perform(level, box, options):
	generatePillars(level, box)
	generateCeiling(level, box)


class Section:
	def __init__(self, minx, maxx, minz, maxz, miny, maxy):
		self.minx = minx
		self.maxx = maxx
		self.minz = minz
		self.maxz = maxz
		self.miny = miny
		self.maxy = maxy


def generatePillars(level, box):
	fillSection(level, (1, 0), Section(
			box.minx,
			box.minx + 1,
			box.minz,
			box.minz + 1,
			box.miny + 1,
      box.miny + 17))
	fillSection(level, (1, 0), Section(
			box.minx + 31,
			box.minx + 32,
			box.minz,
			box.minz + 1,
			box.miny + 1,
      box.miny + 17))
	fillSection(level, (1, 0), Section(
			box.minx,
			box.minx + 1,
			box.minz + 31,
			box.minz + 32,
			box.miny + 1,
      box.miny + 17))
	fillSection(level, (1, 0), Section(
			box.minx + 31,
			box.minx + 32,
			box.minz + 31,
			box.minz + 32,
			box.miny + 1,
      box.miny + 17))


def generateCeiling(level, box):
	fillSection(level, (1, 0), Section(
			box.minx,
			box.minx + 32,
			box.minz,
			box.minz + 32,
			box.miny + 16,
      box.miny + 17))
	fillSection(level, (2, 0), Section(
			box.minx + 1,
			box.minx + 31,
			box.minz + 1,
			box.minz + 31,
			box.miny + 16,
      box.miny + 17))


def fillSection(level, blockType, section):
	for x in range(section.minx, section.maxx):
		for z in range(section.minz, section.maxz):
			for y in range(section.miny, section.maxy):
				utilityFunctions.setBlock(level, blockType, x, y, z)
