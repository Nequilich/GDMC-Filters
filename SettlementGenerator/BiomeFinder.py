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