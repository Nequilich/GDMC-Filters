from Classes import Surface
from Classes import SimpleSurface
from Common import setBlock
from SurfaceManager import calculateHeightMapAdv
from SurfaceManager import calculateSteepnessMap
from SurfaceManager import calculateWaterPlacement

def perform(level, box, options):
	surface = Surface(box.minx, box.minz, box.maxx, box.maxz)
	calculateHeightMapAdv(level, surface)
	calculateSteepnessMap(surface)
	calculateWaterPlacement(level, surface)
	simpleSurface = SimpleSurface(box.minx, box.minz, box.maxx, box.maxz)

	xDif = simpleSurface.xStart - surface.xStart
	zDif = simpleSurface.zStart - surface.zStart
	for x in range(xDif, xDif + simpleSurface.xRealLength):
		for z in range(zDif, zDif + simpleSurface.zRealLength):
			height = surface.surfaceMap[x][z].height
			xSimple = surface.toSimpleSurfaceX(simpleSurface, x)
			zSimple = surface.toSimpleSurfaceZ(simpleSurface, z)
			if simpleSurface.surfaceMap[xSimple][zSimple].height < height:
				simpleSurface.surfaceMap[xSimple][zSimple].height = height

	for x in range(surface.xLength):
		for z in range(surface.zLength):
			height = surface.surfaceMap[x][z].height
			setBlock(level, surface.xStart + x, height + 8, surface.zStart + z, 1)

	for x in range(simpleSurface.xLength):
		for z in range(simpleSurface.zLength):
			height = simpleSurface.surfaceMap[x][z].height
			xReal = simpleSurface.toRealX(x)
			zReal = simpleSurface.toRealZ(z)
			for xn in [-1, 0, 1]:
				for zn in [-1, 0, 1]:
					setBlock(level, xReal + xn, height + 12, zReal + zn, 20)