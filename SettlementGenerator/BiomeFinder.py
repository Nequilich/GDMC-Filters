from pymclevel.biome_types import biome_types  # Converts biome id to its name.
from pymclevel.infiniteworld import AnvilChunk
from Common import convertChunkBlockCoordinate
from Common import setBlock

def findBiomes(level, box, surface):
    biomesFound = set()

    for cPos in box.chunkPositions:
        chunk = level.getChunk(cPos[0], cPos[1])

        chunkBiomeData = chunk.root_tag["Level"]["Biomes"].value
        # print(type(chunk))

        # property_names=[p for p in dir(AnvilChunk) if isinstance(getattr(AnvilChunk,p),property)]
        # print(property_names)
        # print("Blocks", chunk.Blocks)
        # print("HeightMap", chunk.HeightMap)
        # print("bounds", chunk.bounds)
        # print(chunk.bounds.minx)

        for i in range(chunkBiomeData.size):
            blockCoordinate = convertChunkBlockCoordinate(cPos[0], cPos[1], i)
            if(blockCoordinate[0] < surface.xStart or blockCoordinate[0] >= surface.xEnd or blockCoordinate[1] < surface.zStart or blockCoordinate[1] >= surface.zEnd):
                # print("ree")
                continue
            
            x = blockCoordinate[0] - surface.xStart
            z = blockCoordinate[1] - surface.zStart
            
            surface.surfaceMap[x][z].biomeId = chunkBiomeData[i]
            # print(blockCoordinate[0], blockCoordinate[1], surface.surfaceMap[x][z].biomeId)

        # biomes = chunk.root_tag["Level"]["Biomes"].value
        # biomesFound.update(biomes)
        
        # Marks river biome with yellow wool.
        # for i in range(biomes.size):
        #     if biomes[i] == 7:  # River
        #         blockXZ = convertChunkBlockCoordinate(cPos[0], cPos[1], i)
        #         blockX = blockXZ[0]
        #         blockZ = blockXZ[1]
        #         surfaceX = blockX - box.minx
        #         surfaceZ = blockZ - box.minz
        #         setBlock(level, blockX, surface.surfaceMap[surfaceX][surfaceZ].height, blockZ, 35, 4)

    # Prints the names of the different biomes found.
    # print("Biomes found:")
    # for biome in biomesFound:
    #     print(biome_types[biome])

    return biomesFound