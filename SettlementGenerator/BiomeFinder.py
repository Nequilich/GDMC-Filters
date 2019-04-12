from Common import convertChunkBlockCoordinate

def findBiomes(level, box, surface):
    for cPos in box.chunkPositions:
        chunk = level.getChunk(cPos[0], cPos[1])
        chunkBiomeData = chunk.root_tag["Level"]["Biomes"].value

        for i in range(chunkBiomeData.size):
            blockCoordinate = convertChunkBlockCoordinate(cPos[0], cPos[1], i)

            if(blockCoordinate[0] < surface.xStart or blockCoordinate[0] >= surface.xEnd or blockCoordinate[1] < surface.zStart or blockCoordinate[1] >= surface.zEnd):
                continue
            
            x = blockCoordinate[0] - surface.xStart
            z = blockCoordinate[1] - surface.zStart            
            surface.surfaceMap[x][z].biomeId = chunkBiomeData[i]