from Classes import Point
from Classes import Property
from StructureBuilder import buildStructure

inputs = (
	("Build house (minimum 7x7)", "label"),
	("Direction:", ("north", "east", "south", "west")),
	("Biome:", ("plains", "forest", "birchForest", "darkForest", "swamp", "jungle", "riverBeach", "taiga", "snowyIcy", "mountains", "mushroom", "desert", "savanna", "badlands", "aquatic"))
)

def perform(level, box, options):
	if min([box.maxx - box.minx, box.maxz - box.minz]) < 7:
		return
	point = Point(box.minx, box.minz)
	property = Property(box.minx, box.minz, box.maxx, box.maxz, box.miny)
	property.doorDirection = options["Direction:"].upper()
	buildStructure(level, point, box.miny, "house", options["Direction:"], options["Biome:"], prop=property)
