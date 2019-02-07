from pymclevel import alphaMaterials

import utilityFunctions as utilityFunctions

inputs = (
	("Daniel Test Filter 1", "label"),
	("Material", alphaMaterials.Cobblestone), # main material
	("Creator: Daniel Lundin", "label"),
)

def perform(level, box, options):
	for x in range(box.minx, box.maxx):
		for z in range(box.minz, box.maxz):
			print(level.blockAt(x, box.maxy, z))
			utilityFunctions.setBlock(level, (options["Material"].ID, 0), x, box.maxy - 1, z)
