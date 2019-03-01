from Common import setBlock

blocks = {
    "wood": 17.0,
    "wood slab": 126.0,
    "fence": 85.0,
    "torch": 50
}

inputs = (
  ("Width", 4),
  ("Creator: Jungne Losang", "label")
)



def perform(level, box, options):
    bridgeWidth = options["Width"]
    pointA = (box.minx, box.minz)
    pointB = (box.maxx, box.maxz)
    heightA = getSurfaceSpotHeight(level, pointA[0], pointA[1]) + 1
    heightB = getSurfaceSpotHeight(level, pointB[0], pointB[1]) + 1
    xLength = box.maxx - box.minx
    zLength = box.maxz - box.minz
    bridgeLength = min(xLength, xLength)

    if(xLength > zLength):
        bridgeLength = xLength
        bridgeMainDirection = "east" #east is positive x
    else:
        bridgeLength = zLength
        bridgeMainDirection = "south" #south is positive z

    #place start of bridge
    placeBridgeStartEnd(level, pointA[0], heightA, pointA[1], bridgeMainDirection, bridgeWidth)

    #place main part of bridge
    for i in range(bridgeLength-2):
        print("hey")
    #place end of bridge


def getSurfaceSpotHeight(level, x, z):
    heightIsFound = False
    y = 128
    while (not heightIsFound):
        if (isSurfaceBlock(level, x, y, z)):
            heightIsFound = True
        else:
            y -= 1
    return y


aboveSurfaceBlocks = [0, 6, 17, 18, 31, 32, 37, 38, 39, 40, 59, 78,
                      81, 83, 99, 100, 103, 104, 105, 106, 111, 141, 142, 161, 162, 175]


def isSurfaceBlock(level, x, y, z):
    for block in aboveSurfaceBlocks:
        if (level.blockAt(x, y, z) == block):
            return False
    return True

def placeBridgeSection(level, x, y, z, mainDirection, width):
    level.setBlockAt

def placeBridgeStartEnd(level, x, y, z, mainDirection, width):
    placePillarWithTorch(level, x, y, z)
    for i in range(width-2):
            level.setBlockAt(x, y, z+i+1, blocks["wood slab"])
    placePillarWithTorch(level, x, y, z+(width-1))

def placePillarWithTorch(level, x, y, z):
    setBlock(level, x, y, z, 17)
    setBlock(level, x, y+1, z, 17)
    setBlock(level, x, y+2, z, blocks["torch"])