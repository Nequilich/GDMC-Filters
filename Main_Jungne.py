from Biomes import biomes
from BiomeFinder import findBiomes
from BiomeMaterials import get_biome_materials
from BridgeBuilder import buildBridge
from Classes import Property
from Classes import Surface
from Common import setBlock
from HouseBuilder import buildHouse
from HouseBuilder import clearHouseProperty
from SurfaceManager import calculateHeightMapAdv
from SurfaceManager import calculateSections
from SurfaceManager import calculateSteepnessMap
from SurfaceManager import calculateWaterPlacement
from VillagerSpawner import spawnVillager
import time

inputs = (
    ("Width", 4),
    ("Biome", tuple(biomes.keys())),
    ("Creator: Jungne Losang", "label")
)


def perform(level, box, options):
    startTime = time.time()

    # testMaterials()

    # spawnVillager(level, box)

    # # BridgeBuilder
    # bridgeWidth = options["Width"]

    surface = Surface(box.minx, box.minz, box.maxx, box.maxz)
    calculateHeightMapAdv(level, surface)
    calculateSteepnessMap(surface)
    calculateWaterPlacement(level, surface)
    findBiomes(level, surface)
    sections = calculateSections(surface, 1, 100)

    prop = Property(2, 2, surface.xLength-2, surface.zLength-2, surface.surfaceMap[0][0].height)
    prop.doorDirection = "SOUTH"
    print(surface.xStart, surface.zStart, prop.xStart, prop.zStart)
    buildHouse(level, surface, prop)

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

    # # BiomeFinder adds biome data to surfaceMap
    # findBiomes(level, surface)
    # # Test of biome material changes.
    # biomeId = surface.surfaceMap[0][0].biomeId

    # buildBridge(level, startPoint, endPoint, bridgeY, bridgeWidth, biomeId)

    # # Makes a colored map of biomes in the sky
    # biomeIds = Biomes.getBiomeDict()
    # biomeNameList = Biomes.biomes.keys()
    # for x in range(surface.xLength):
    #     for z in range(surface.zLength):
    #         biomeName = biomeIds[surface.surfaceMap[x][z].biomeId]

    #         for i in range(len(biomeNameList)):
    #             if (biomeName == biomeNameList[i]):
    #                 setBlock(level, surface, x, 100, z, 35, i)

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
    endTime = time.time()

    print("Runtime: ", endTime-startTime)
