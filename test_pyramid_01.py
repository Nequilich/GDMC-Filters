import utilityFunctions as utilityFunctions

inputs = (
	("Daniel Test Filter 2", "label"),
	("Only build within selection", False),
	("Creator: Daniel Lundin", "label"),
)


def perform(level, box, options):
	if (box.maxx - box.minx < 3 or box.maxz - box.minz < 3
			or box.maxy - box.miny < 4):
		raise ValueError("Selection must be of size 3*3*4 (x*z*y) or bigger")
	sections = []
	if (options["Only build within selection"]):
		sections = getSections(box, box.maxy)
	else:
		sections = getSections(box, level.Height)
	generateFloor(level, box)
	generateSections(level, sections)


class Section:
	def __init__(self, minx, maxx, minz, maxz, miny, maxy):
		self.minx = minx
		self.maxx = maxx
		self.minz = minz
		self.maxz = maxz
		self.miny = miny
		self.maxy = maxy


def getSections(box, maxHeight):
	sections = []
	currentSection = Section(
		box.minx,
		box.maxx if (box.maxx - box.minx) % 2 == 1 else box.maxx - 1,
		box.minz,
		box.maxz if (box.maxz - box.minz) % 2 == 1 else box.maxz - 1,
		box.miny + 1,
		box.miny + 4)
	while (currentSection.maxy <= maxHeight
		   and currentSection.maxx - currentSection.minx >= 3
		   and currentSection.maxz - currentSection.minz >= 3):
		sections.append(currentSection)
		currentSection = Section(
			currentSection.minx + 1,
			currentSection.maxx - 1,
			currentSection.minz + 1,
			currentSection.maxz - 1,
			currentSection.miny + 3,
			currentSection.maxy + 3)
	return sections


def generateFloor(level, box):
	fillSection(
		level, (4, 0),
		Section(
			box.minx,
			box.maxx if (box.maxx - box.minx) % 2 == 1 else box.maxx - 1,
			box.minz,
			box.maxz if (box.maxz - box.minz) % 2 == 1 else box.maxz - 1,
			box.miny,
			box.miny + 1))


def generateSections(level, sections):
	for section in sections:
		clearSection(level, section)
		generatePillars(level, section)
		generateCeilings(level, section)


def generatePillars(level, section):
	for x in range(section.minx, section.maxx, 2):
		for z in range(section.minz, section.maxz, 2):
			utilityFunctions.setBlock(level, (43, 5), x, section.miny, z)
			utilityFunctions.setBlock(level, (43, 5), x, section.miny + 1, z)


def generateCeilings(level, section):
	fillSection(level, (43, 5),
		Section(
			section.minx,
			section.maxx,
			section.minz,
			section.maxz,
			section.maxy - 1, section.maxy))


def clearSection(level, section):
	fillSection(level, (0, 0), section)


def fillSection(level, blockType, section):
	for x in range(section.minx, section.maxx):
		for z in range(section.minz, section.maxz):
			for y in range(section.miny, section.maxy):
				utilityFunctions.setBlock(level, blockType, x, y, z)
