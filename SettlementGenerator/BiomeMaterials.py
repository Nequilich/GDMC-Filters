from MaterialSets import *
from Biomes import getBiomeDict

default = {
    "torch": (50, 0),
    "window": (102, 0)
}

plains = {
    "foundation": stone["normal"],
    "wood beam": oak["normal"],
    "plank": oak["secondary"],
    "fence": oak["fence"],
    "fence gate": oak["fence gate"],
    "door": oak["door"]
}

def getBiomeMaterials(biomeID = 1):
    biomeID = 1  # TODO Remove line when implementing more material sets.
    # Merges the default materials with the biome materials.
    materials = addDefaultMaterials(biomeMaterials[biomeID])

    return materials

def testMaterials():
    global biomeMaterials
    biomeMaterials = getBiomeDict()
    # materials = getBiomeMaterials(1)
    # print(materials.keys())
    print(biomeMaterials[1])

def addDefaultMaterials(materials):
    dflt = default.copy()
    dflt.update(materials)
    return dflt