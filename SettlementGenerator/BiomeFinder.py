from pymclevel.biome_types import biome_types  # Converts biome id to its name.
from Common import convertChunkBlockCoordinate

def findBiomes(level, box):
    biomesFound = set()

    for cPos in box.chunkPositions:
        chunk = level.getChunk(cPos[0], cPos[1])
        biomes = chunk.root_tag["Level"]["Biomes"].value
        biomesFound.update(biomes)

    # Prints the names of the different biomes found.
    print("Biomes found:")
    for biome in biomesFound:
        print(biome_types[biome])

    return biomesFound