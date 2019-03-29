from Common import setBlock
from Classes import Surface
from SurfaceManager import calculateHeightMapAdv
from BridgeBuilder import buildBridge
from BiomeFinder import findBiomes
from SurfaceManager import calculateSteepnessMap
from SurfaceManager import calculateWaterPlacement
from SurfaceManager import calculateSections
from VillagerSpawner import spawnVillager
from BiomeMaterials import testMaterials

inputs = (
    ("Width", 4),
    ("Material", ("Oak", "Cobblestone", "Birch")),
    ("Creator: Jungne Losang", "label")
)

oakMaterial = {
    "normal": (17, 0),
    "upper slab": (126, 8),
    "lower slab": (126, 0),
    "fence": 85.0,
    "torch": 50
}

cobblestoneMaterial = {
    "normal": (4, 0),
    "upper slab": (44, 11),
    "lower slab": (44, 3),
    "fence": 139,
    "torch": 50
}

birchMaterial = {
    "normal": (17, 2),
    "upper slab": (126, 10),
    "lower slab": (126, 2),
    "fence": 189,
    "torch": 50
}

glass = {
    "green": (95, 5),
    "yellow": (95, 4),
    "orange": (95, 1),
    "red": (95, 14),
    "blue": (95, 11)
}


def perform(level, box, options):

    testMaterials()


    #spawnVillager(level, box)
    
    
    # BridgeBuilder
    # bridgeWidth = options["Width"]

    # surface = Surface(box.minx, box.minz, box.maxx, box.maxz)
    # calculateHeightMapAdv(level, surface)
    # startPoint = (box.minx, box.minz)
    # endPoint = (box.maxx-1, box.maxz-1)
    # bridgeY = surface.surfaceMap[0][0].height + 1  #+1 to raise above the surface

    # chosenMaterial = options["Material"]
    # if (chosenMaterial == "Oak"):
    #   materials = oakMaterial
    # elif (chosenMaterial == "Cobblestone"):
    #   materials = cobblestoneMaterial
    # elif (chosenMaterial == "Birch"):
    #   materials = birchMaterial
    # else:
    #   materials = oakMaterial

    # buildBridge(level, startPoint, endPoint, bridgeY, bridgeWidth, materials)

    # BiomeFinder
    # biomes = findBiomes(level, box, surface)

    # Topographic marker
    # surface = Surface(box.minx, box.minz, box.maxx, box.maxz)
    # calculateHeightMapAdv(level, surface)
    # calculateSteepnessMap(surface)
    # calculateWaterPlacement(level, surface)

    # sections = calculateSections(surface, 1, 40)

    # minHeight = 255
    # maxHeight = 0

    # for x in range(surface.xLength):
    #     for z in range(surface.zLength):
    #         height = surface.surfaceMap[x][z].height

    #         if (height < minHeight):
    #             minHeight = height
    #         if (height > maxHeight):
    #             maxHeight = height

    # heightRange = maxHeight - minHeight
    # heigthInterval = heightRange / 4

    # for x in range(surface.xLength):
    #     for z in range(surface.zLength):
    #         height = surface.surfaceMap[x][z].height
    #         if (surface.surfaceMap[x][z].isWater):
    #           setBlock(level, surface.xStart + x,
    #                      height + 1, surface.zStart + z, glass["blue"][0], glass["blue"][1])
    #         elif (height <= minHeight + heigthInterval):
    #             setBlock(level, surface.xStart + x,
    #                      height + 1, surface.zStart + z, glass["green"][0], glass["green"][1])
    #         elif (height <= minHeight + heigthInterval * 2):
    #             setBlock(level, surface.xStart + x,
    #                      height + 1, surface.zStart + z, glass["yellow"][0], glass["yellow"][1])
    #         elif (height <= minHeight + heigthInterval * 3):
    #             setBlock(level, surface.xStart + x,
    #                      height + 1, surface.zStart + z, glass["orange"][0], glass["orange"][1])
    #         else:
    #             setBlock(level, surface.xStart + x,
    #                      height + 1, surface.zStart + z, glass["red"][0], glass["red"][1])
