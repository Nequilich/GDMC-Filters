from Common import convertChunkBlockCoordinate
from Common import getMatrix
from pymclevel.box import BoundingBox

def findBiomes(level, surface):
	box = BoundingBox((surface.xStart, 0, surface.zStart), (surface.xLength, 256, surface.zLength))
	for cPos in box.chunkPositions:
		chunk = level.getChunk(cPos[0], cPos[1])
		chunkBiomeData = chunk.root_tag["Level"]["Biomes"].value

		for i in range(chunkBiomeData.size):
			blockCoordinate = convertChunkBlockCoordinate(cPos[0], cPos[1], i)

			if blockCoordinate[0] < surface.xStart or blockCoordinate[0] >= surface.xEnd or blockCoordinate[1] < surface.zStart or blockCoordinate[1] >= surface.zEnd:
				continue

			x = blockCoordinate[0] - surface.xStart
			z = blockCoordinate[1] - surface.zStart            
			surface.surfaceMap[x][z].biomeId = chunkBiomeData[i]

def findBiomes2(level, surface):
	chunks = getMatrix(surface.xLength / 16 + 1, surface.zLength / 16 + 1, None)
	xDiff = surface.xStart % 16
	zDiff = surface.zStart % 16
	for x in range(surface.xLength):
		for z in range(surface.zLength):
			xIndex = (x + xDiff) / 16
			zIndex = (z + zDiff) / 16
			xReal = x + surface.xStart
			zReal = z + surface.zStart
			chunk = chunks[xIndex][zIndex]
			if chunk == None:
				chunks[xIndex][zIndex] = level.getChunk(xReal, zReal)
				chunk = chunks[xIndex][zIndex]
			chunkBiomeData = chunk.root_tag["Level"]["Biomes"].value
			surface.surfaceMap[x][z].biomeId = chunkBiomeData[(xReal % 16) * 16 + zReal % 16]