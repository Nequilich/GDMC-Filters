from pymclevel import alphaMaterials

import utilityFunctions as utilityFunctions

inputs = (
	("Daniel Test Filter 1", "label"),
	("Top Material", alphaMaterials.Glass), # top material
	("Middle Material", alphaMaterials.Stone), # middle material
	("Bottom Material", alphaMaterials.Cobblestone), # bottom material
	("Creator: Daniel Lundin", "label"),
)

def perform(level, box, options):
	for x in range(box.minx, box.maxx):
		for z in range(box.minz, box.maxz):
			utilityFunctions.setBlock(level, (options["Top Material"].ID, 0), x, box.maxy - 1, z)
			utilityFunctions.setBlock(level, (options["Middle Material"].ID, 0), x, box.maxy - 2, z)
			utilityFunctions.setBlock(level, (options["Bottom Material"].ID, 0), x, box.maxy - 3, z)
