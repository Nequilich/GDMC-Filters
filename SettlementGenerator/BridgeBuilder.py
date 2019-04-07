from Common import setBlock
from Classes import Surface

materials = {}


def buildBridge(level, startPoint, endPoint, bridgeY, width, blocks):
    global materials
    materials = blocks

    # Sets the direction variables
    setBridgeDirections(startPoint, endPoint)

    # # Offsets the start and end points to center bridge.
    # startPoint = (startPoint[0]-((width/2)*bridgeSecondaryDirectionX),
    #               startPoint[1]-((width/2)*bridgeSecondaryDirectionZ))
    # endPoint = (endPoint[0]-((width/2)*bridgeSecondaryDirectionX),
    #             endPoint[1]-((width/2)*bridgeSecondaryDirectionZ))

    # Offset variables
    offsetNext = False
    offsetInterval = bridgeLength/float(bridgeSkew)
    currentOffset = 0
    # TODO handle offset intervals smaller than 2.

    # place bridge heads
    if (offsetInterval >= 2):
        headLength = 3

        placeOrthogonalBridgeHead(
            level, startPoint[0], bridgeY, startPoint[1], width, headLength)  # Start of bridge
        placeOrthogonalBridgeHead(
            level, endPoint[0], bridgeY, endPoint[1], width, headLength, True)  # End of bridge

        startPoint = ((startPoint[0] + headLength * bridgeMainDirectionX),
                      (startPoint[1] + headLength * bridgeMainDirectionZ))
        endPoint = ((endPoint[0] + headLength * bridgeMainDirectionX * -1),
                    (endPoint[1] + headLength * bridgeMainDirectionZ * -1))

    else:
        placeDiagonalBridgeHead(
            level, startPoint[0], bridgeY, startPoint[1], width)  # Start of bridge
        placeDiagonalBridgeHead(
            level, endPoint[0], bridgeY, endPoint[1], width, True)  # End of bridge

    # Update offset variables after placing bridgeheads
    setBridgeDirections(startPoint, endPoint)
    offsetInterval = bridgeLength/float(bridgeSkew)

    # place main part of bridge
    # for i in range(1, bridgeLength-1):
    #     x = startPoint[0]+(i*bridgeMainDirectionX) + \
    #         (currentOffset*bridgeSecondaryDirectionX)
    #     z = startPoint[1]+(i*bridgeMainDirectionZ) + \
    #         (currentOffset*bridgeSecondaryDirectionZ)
    #     if ((i+1) % offsetInterval < 1):
    #         if (offsetNext == True):
    #             placeBridgeSection(level, x, bridgeY, z, width+2, True, True)
    #             currentOffset += 1
    #         else:
    #             placeBridgeSection(level, x, bridgeY, z, width+1, False, True)
    #         offsetNext = True
    #     elif (offsetNext == True):
    #         placeBridgeSection(level, x, bridgeY, z, width+1, True, False)
    #         offsetNext = False
    #         currentOffset += 1
    #     else:
    #         placeBridgeSection(level, x, bridgeY, z, width, False, False)


def placeBridgeSection(level, x, y, z, width, extraFenceLeft=False, extraFenceRight=False):
    # Place main part of bridge
    for i in range(width):
        setBlock(level, x+i*bridgeSecondaryDirectionX, y, z+i*bridgeSecondaryDirectionZ,
                 materials["upper slab"][0], materials["upper slab"][1])

    # Place fencing
    setBlock(level, x, y+1, z, materials["fence"])
    setBlock(level, x+(width-1)*bridgeSecondaryDirectionX, y+1, z +
             (width-1)*bridgeSecondaryDirectionZ, materials["fence"])
    if (extraFenceLeft):
        setBlock(level, x+bridgeSecondaryDirectionX, y+1, z +
                 bridgeSecondaryDirectionZ, materials["fence"])
    elif (extraFenceRight):
        setBlock(level, x+(width-2)*bridgeSecondaryDirectionX, y+1, z +
                 (width-2)*bridgeSecondaryDirectionZ, materials["fence"])


def placeOrthogonalBridgeHead(level, x, y, z, width, headLength, flipped=False):
    placePillarWithTorch(level, x, y, z)

    for i in range(1, width-1):
        setBlock(level, x+i*bridgeSecondaryDirectionX, y, z+i*bridgeSecondaryDirectionZ,
                 materials["lower slab"][0], materials["lower slab"][1])

    placePillarWithTorch(level, x+(width-1)*bridgeSecondaryDirectionX,
                         y, z+(width-1)*bridgeSecondaryDirectionZ)

    if not flipped:
        rangeList = range(1, headLength+1)
    else:
        rangeList = range(-1, (headLength+1)*-1, -1)

    for i in rangeList:
        sectionX = x + (i*bridgeMainDirectionX)
        sectionZ = z + (i*bridgeMainDirectionZ)
        placeBridgeSection(level, sectionX, y, sectionZ, width)


def placePillarWithTorch(level, x, y, z):
    setBlock(level, x, y, z, materials["normal"][0], materials["normal"][1])
    setBlock(level, x, y+1, z, materials["normal"][0], materials["normal"][1])
    setBlock(level, x, y+2, z, materials["torch"])


def placeDiagonalBridgeHead(level, x, y, z, width, flipped=False):
    pass  # TODO implement diagonal bridge terminals
    if not flipped:
        placePillarWithTorch(level, (x + 2*(bridgeMainDirectionX + bridgeSecondaryDirectionX)),
                            y, (z + -1*(bridgeMainDirectionZ + bridgeSecondaryDirectionZ)))
        placePillarWithTorch(level, (x + -1*(bridgeMainDirectionZ + bridgeSecondaryDirectionZ)),
                            y, (z + 2*(bridgeMainDirectionZ + bridgeSecondaryDirectionZ)))
        setBlock(level, x+(bridgeMainDirectionX + bridgeSecondaryDirectionX), y, z,
                 materials["lower slab"][0], materials["lower slab"][1])
        setBlock(level, x, y, z+(bridgeMainDirectionZ + bridgeSecondaryDirectionZ),
                 materials["lower slab"][0], materials["lower slab"][1])

    else:
        placePillarWithTorch(level, (x + -2*(bridgeMainDirectionX + bridgeSecondaryDirectionX)),
                            y, (z + 1*(bridgeMainDirectionZ + bridgeSecondaryDirectionZ)))
        placePillarWithTorch(level, (x + 1*(bridgeMainDirectionZ + bridgeSecondaryDirectionZ)),
                            y, (z + -2*(bridgeMainDirectionZ + bridgeSecondaryDirectionZ)))

def setBridgeDirections(startPoint, endPoint):
    xLength = abs(endPoint[0] - startPoint[0])+1
    zLength = abs(endPoint[1] - startPoint[1])+1
    # bridgeLength = max(xLength, xLength)

    global bridgeMainDirectionX
    global bridgeMainDirectionZ
    global bridgeSecondaryDirectionX
    global bridgeSecondaryDirectionZ
    global bridgeLength
    global bridgeSkew

    if(xLength > zLength):  # Main direction is east or west, positive/negative X
        bridgeLength = xLength
        bridgeSkew = zLength
        bridgeMainDirectionZ = 0
        bridgeSecondaryDirectionX = 0
        if (startPoint[0] <= endPoint[0]):  # Main east
            bridgeMainDirectionX = 1
        else:  # Main west
            bridgeMainDirectionX = -1
        if (startPoint[1] <= endPoint[1]):  # Secondary south
            bridgeSecondaryDirectionZ = 1
        else:  # Secondary north
            bridgeSecondaryDirectionZ = -1

    else:  # Main direction is north or south, negative/positive Z
        bridgeLength = zLength
        bridgeSkew = xLength
        bridgeMainDirectionX = 0
        bridgeSecondaryDirectionZ = 0
        if (startPoint[1] <= endPoint[1]):  # Main south
            bridgeMainDirectionZ = 1
        else:  # Main north
            bridgeMainDirectionZ = -1
        if (startPoint[0] <= endPoint[0]):  # Secondary east
            bridgeSecondaryDirectionX = 1
        else:  # Secondary west
            bridgeSecondaryDirectionX = -1
