import utilityFunctions as utilityFunctions

inputs = (
	("Daniel Test Filter 2", "label"),
	("Only build within selection", False),
	("Creator: Daniel Lundin", "label"),
)

def perform(level, box, options):
	if(box.maxx - box.minx < 3 or box.maxz - box.minz < 3 or box.maxy - box.miny < 4):
		raise ValueError("Selection must be of size 3*3*4 (x*z*y) or bigger")
	sections = []
	if(options["Only build within selection"]):
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
	currentminx = box.minx
	currentmaxx = box.maxx
	currentminz = box.minz
	currentmaxz = box.maxz
	currentminy = box.miny + 1
	currentmaxy = box.miny + 4
	while(currentmaxy <= maxHeight and currentmaxx - currentminx >= 3 and currentmaxz - currentminz >= 3):
		sections.append(Section(currentminx, currentmaxx, currentminz, currentmaxz, currentminy, currentmaxy))
		currentminx += 1
		currentmaxx -= 1
		currentminz += 1
		currentmaxz -= 1
		currentminy += 3
		currentmaxy += 3
	return sections

def generateFloor(level, box):
	fillArea(level, (4, 0), box.minx, box.maxx, box.minz, box.maxz, box.miny, box.miny + 1)

def generateSections(level, sections):
	for section in sections:
		clearSection(level, section)
		fillArea(level, (43, 5), section.minx, section.maxx, section.minz, section.maxz, section.miny, section.maxy)

def clearSection(level, section):
	clearArea(level, section.minx, section.maxx, section.minz, section.maxz, section.miny, section.maxy)

def clearArea(level, minx, maxx, minz, maxz, miny, maxy):
	fillArea(level, (0, 0), minx, maxx, minz, maxz, miny, maxy)

def fillArea(level, blockType, minx, maxx, minz, maxz, miny, maxy):
	for x in range(minx, maxx):
		for z in range(minz, maxz):
			for y in range(miny, maxy):
					utilityFunctions.setBlock(level, blockType, x, y, z)