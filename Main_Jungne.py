from Biomes import biomes, getBiomeDict
from BiomeMaterials import get_biome_materials
from BridgeBuilder import buildBridge
from Classes import Property
from Classes import Surface
from Common import setBlock
from HouseBuilder import buildHouse
from HouseBuilder import clearHouseProperty
from NameGenerator import getCityName
from SurfaceManager import calculateBiomeMap
from SurfaceManager import calculateHeightMapAdv
from SurfaceManager import calculateSections
from SurfaceManager import calculateSteepnessMap
from SurfaceManager import calculateWaterPlacement
from VillagerSpawner import spawnVillager
import time
from pymclevel import TAG_Byte, TAG_Short, TAG_Int, TAG_Compound, TAG_List, TAG_String, TAG_Double, TAG_Float
from pymclevel.entity import TileEntity

inputs = (
    ("Width", 4),
    ("Biome", tuple(biomes.keys())),
    ("Creator: Jungne Losang", "label")
)


def perform(level, box, options):
    startTime = time.time()

    # x = box.minx
    # y = box.miny
    # z = box.minz

    # level.setBlockAt(x, y, z, 63)
    
    # sign = TileEntity.Create("Sign", (x,y,z))
    # print(sign)

    # boat = TAG_Compound()
    # boat["id"] = TAG_String("boat")
    # boat["Pos"] = TAG_List([TAG_Double(x), TAG_Double(y), TAG_Double(z)])
    # boat["Motion"] = TAG_List([TAG_Double(0.0), TAG_Double(0.0), TAG_Double(0.0)])
    # boat["Rotation"] = TAG_List([TAG_Float(0.0), TAG_Float(0.0)])

    # # print(boat)
    # sign = TAG_Compound()
    # sign["id"] = TAG_String('minecraft:sign')
    # sign["x"] = TAG_Int(x)
    # sign["y"] = TAG_Int(y)
    # sign["z"] = TAG_Int(z)
    # sign["Text1"] = TAG_String("{'text':'hooohooo'}")
    # sign["Text2"] = TAG_String("{'text':'hooohooo'}")
    # sign["Text3"] = TAG_String("{'text':'hooohooo'}")
    # sign["Text4"] = TAG_String("{'text':'hooohooo'}")
    
    # chunk = level.getChunk(x / 16, z / 16)
    # chunk.TileEntities.append(sign)
    # chunk.dirty = True

    # print(chunk.TileEntities)
    # print(level.blockAt(x,y,z))
    # print(level.blockDataAt(x,y,z))


    for i in range(10):
        print(getCityName())

    # Places a boat 
    # boat = TAG_Compound()
    # boat["id"] = TAG_String("boat")
    # boat["Type"] = TAG_String("spruce")
    # boat["Pos"] = TAG_List([TAG_Double(box.minx), TAG_Double(box.miny), TAG_Double(box.minz)])
    # boat["Motion"] = TAG_List([TAG_Double(0.0), TAG_Double(0.0), TAG_Double(0.0)])
    # boat["Rotation"] = TAG_List([TAG_Float(0.0), TAG_Float(0.0)])
    
    # chunk = level.getChunk(box.minx / 16, box.minz / 16)
    # chunk.Entities.append(boat)
    # chunk.dirty = True


    # biomeList = []
    # biomeDict = getBiomeDict()
    # for key in biomeDict.keys():
    #     biomeList.append(key)
    # biomeList.sort()

    # missingBiomeIds = []

    # for i in range(biomeList[-1]+1):
    #     if i not in biomeList:
    #         missingBiomeIds.append(i)

    # print(missingBiomeIds)


    # testMaterials()

    # spawnVillager(level, box)

    # BridgeBuilder
    # bridgeWidth = options["Width"]

    # surface = Surface(box.minx, box.minz, box.maxx, box.maxz)
    # calculateHeightMapAdv(level, surface)
    # calculateSteepnessMap(surface)
    # calculateWaterPlacement(level, surface)
    # calculateBiomeMap(level, surface)
    # sections = calculateSections(surface, 1, 100)

    # prop = Property(2, 2, surface.xLength-2, surface.zLength-2, surface.surfaceMap[0][0].height)
    # prop.doorDirection = "SOUTH"
    # print(surface.xStart, surface.zStart, prop.xStart, prop.zStart)
    # buildHouse(level, surface, prop)

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
    # calculateBiomeMap(level, surface)
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
