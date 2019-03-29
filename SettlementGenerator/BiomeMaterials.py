from MaterialSets import *

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


biomeMaterials = {
    1: plains
}

def getBiomeMaterials(biomeID):
    # Merges the default materials with the biome materials.
    materials = addDefaultMaterials(biomeMaterials[biomeID])

    return materials

def testMaterials():
    materials = getBiomeMaterials(1)
    print(materials.keys())

def addDefaultMaterials(materials):
    dflt = default.copy()
    dflt.update(materials)
    return dflt