#level.blockAt(x, y, z)
#level.setBlockAt(x, y, z, id)

def perform(level, box, options):
	for x in range(box.minx, box.maxx):
		for z in range(box.minz, box.maxz):
			surfaceIsFound = False
			y = level.Height
			while (not surfaceIsFound):
				if (level.blockAt(x, y, z) != 0):
					surfaceIsFound = True
				else:
					y -= 1
			level.setBlockAt(x, y + 1, z, 20)