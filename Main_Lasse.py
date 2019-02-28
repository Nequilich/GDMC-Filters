from GetSurfaceAdv import getSurface
from Common import setBlock

def perform(level, box, options):
	surface = getSurface(level, box)

	for x in range(surface.x):
		for z in range(surface.z):
			y = surface.surface[x][z].height
			setBlock(level, x + box.minx, y + 1, z + box.minz, 20)

	surface.setSteepness()
	printSurfaceSteepness(surface)

def printSurfaceSteepness(surface):
	for x in range(surface.x):
		s = ""
		for z in range(surface.z):
			s += str(surface.surface[x][z].steepness) + " "
		print(s)