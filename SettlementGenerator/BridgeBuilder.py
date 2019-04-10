from Common import setBlock as setBlockWithSurface
from Classes import Surface


def buildBridge(level, startPoint, endPoint, bridgeY, width, blocks):
    global materials
    materials = blocks

    # Sets the direction variables
    setBridgeDirections(startPoint, endPoint)

    # Builds small bridge if distance is short.
    if (bridgeLength < 6):
        buildSmallBridge(level, startPoint, endPoint, bridgeY, width, blocks)
        return

    # Offset variables
    offsetNext = False
    offsetInterval = bridgeLength/float(bridgeSkew)
    currentOffset = 0
    # TODO WIP handle offset intervals smaller than 2.

    # place bridge heads
    if (offsetInterval >= 2):
        diagonal = False
        headLength = width/2

        # Offset points of bridge to center.
        startPoint = (startPoint[0]-((width/2)*bridgeSecondaryDirectionX),
                      startPoint[1]-((width/2)*bridgeSecondaryDirectionZ))
        endPoint = (endPoint[0]-((width/2)*bridgeSecondaryDirectionX),
                    endPoint[1]-((width/2)*bridgeSecondaryDirectionZ))

        placeOrthogonalBridgeHead(
            level, startPoint[0], bridgeY, startPoint[1], width, headLength)  # Start of bridge
        placeOrthogonalBridgeHead(
            level, endPoint[0], bridgeY, endPoint[1], width, headLength, True)  # End of bridge

        # Offsets points of bridge to edge of platform.
        startPoint = ((startPoint[0] + (headLength-1) * bridgeMainDirectionX),
                      (startPoint[1] + (headLength-1) * bridgeMainDirectionZ))
        endPoint = ((endPoint[0] + (headLength-1) * bridgeMainDirectionX * -1),
                    (endPoint[1] + (headLength-1) * bridgeMainDirectionZ * -1))

    else:
        diagonal = True
        tempWidth = width/2
        placeDiagonalBridgeHead(
            level, startPoint[0], bridgeY, startPoint[1], width)  # Start of bridge
        placeDiagonalBridgeHead(
            level, endPoint[0], bridgeY, endPoint[1], width, True)  # End of bridge

        offsetMain = tempWidth
        offsetSecondaryStart = tempWidth-2
        offsetSecondaryEnd = tempWidth + int(tempWidth / offsetInterval)
        startPoint = ((startPoint[0] + offsetMain*bridgeMainDirectionX + offsetSecondaryStart*bridgeSecondaryDirectionX),
                      (startPoint[1] + offsetMain*bridgeMainDirectionZ + offsetSecondaryStart*bridgeSecondaryDirectionZ))
        endPoint = ((endPoint[0] + (offsetMain*bridgeMainDirectionX + offsetSecondaryEnd*bridgeSecondaryDirectionX) * -1),
                    (endPoint[1] + (offsetMain*bridgeMainDirectionZ + offsetSecondaryEnd*bridgeSecondaryDirectionZ) * -1))

        # Marks the new points
        # setBlock(level, startPoint[0], bridgeY, startPoint[1],
        #          materials["normal"][0], materials["normal"][1])
        # setBlock(level, endPoint[0], bridgeY, endPoint[1],
        #          materials["normal"][0], materials["normal"][1])

    # Update offset variables after placing bridgeheads
    setBridgeDirections(startPoint, endPoint)
    offsetInterval = bridgeLength/float(bridgeSkew)
    # place main part of bridge
    if (diagonal):
        if offsetInterval < 2:
            offsetNext = True
            # if offsetInterval >' 1:
            #     width = width+1'
    for i in range(1, bridgeLength-1):
        x = startPoint[0]+(i*bridgeMainDirectionX) + \
            (currentOffset*bridgeSecondaryDirectionX)
        z = startPoint[1]+(i*bridgeMainDirectionZ) + \
            (currentOffset*bridgeSecondaryDirectionZ)
        if ((i+1) % offsetInterval < 1):
            if (offsetNext == True):
                placeBridgeSection(level, x, bridgeY, z, width+2,
                                   materials["upper slab"], True, True)
                currentOffset += 1
            else:
                placeBridgeSection(level, x, bridgeY, z, width+1,
                                   materials["upper slab"], False, True)
            offsetNext = True
        elif (offsetNext == True):
            placeBridgeSection(level, x, bridgeY, z, width+1,
                               materials["upper slab"], True, False)
            offsetNext = False
            currentOffset += 1
        else:
            placeBridgeSection(level, x, bridgeY, z, width,
                               materials["upper slab"], False, False)


def placeBridgeSection(level, x, y, z, width, bridgeMaterial, extraFenceLeft=False, extraFenceRight=False, placeFence=True):
    # Place main part of bridge
    for i in range(width):
        setBlock(level, x+i*bridgeSecondaryDirectionX, y, z+i*bridgeSecondaryDirectionZ,
                 bridgeMaterial[0], bridgeMaterial[1])

    # Place fencing
    if (placeFence):
        setBlock(level, x, y+1, z, materials["fence"])
        setBlock(level, x+(width-1)*bridgeSecondaryDirectionX, y+1, z +
                 (width-1)*bridgeSecondaryDirectionZ, materials["fence"])
        if (extraFenceLeft):
            setBlock(level, x+bridgeSecondaryDirectionX, y+1, z +
                     bridgeSecondaryDirectionZ, materials["fence"])
        if (extraFenceRight):
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
    tempWidth = width/2  # Halved and truncated
    if not flipped:
        flipped = 1
    else:
        flipped = -1

    # Pillars with torches TODO scale with width
    placePillarWithTorch(level, (x + flipped*2*(bridgeMainDirectionX + bridgeSecondaryDirectionX)),
                         y, (z + flipped*-1*(bridgeMainDirectionZ + bridgeSecondaryDirectionZ)))
    placePillarWithTorch(level, (x + flipped*-1*(bridgeMainDirectionX + bridgeSecondaryDirectionX)),
                         y, (z + flipped*2*(bridgeMainDirectionZ + bridgeSecondaryDirectionZ)))

    # Steps
    setBlock(level, x+flipped*-1*(bridgeMainDirectionX + bridgeSecondaryDirectionX), y, z+flipped*(bridgeMainDirectionZ + bridgeSecondaryDirectionZ),
             materials["lower slab"][0], materials["lower slab"][1])
    for i in range(tempWidth):
        for j in range(2):
            setBlock(level, x+i*flipped*(bridgeMainDirectionX + bridgeSecondaryDirectionX), y, z+(j*flipped*(bridgeMainDirectionZ + bridgeSecondaryDirectionZ))-i*flipped,
                     materials["lower slab"][0], materials["lower slab"][1])

    # Platform

    # Primary platform
    offsetMain = -1*(tempWidth-2)
    offsetSecondary = tempWidth
    for i in range(2*tempWidth-1):
        tempX = x + flipped*(i * bridgeMainDirectionX +
                             offsetSecondary * bridgeSecondaryDirectionX)
        tempZ = z + flipped*(i * bridgeMainDirectionZ +
                             offsetSecondary * bridgeSecondaryDirectionZ)
        for j in range(i, -1, -1):
            setBlock(level, tempX+flipped*(-1*j*bridgeSecondaryDirectionX+offsetMain*bridgeMainDirectionX), y, tempZ+flipped*(-1*j*bridgeSecondaryDirectionZ + offsetMain * bridgeMainDirectionZ),
                     materials["upper slab"][0], materials["upper slab"][1])
    setBlock(level, x + flipped*tempWidth, y+1, z, materials["fence"])
    setBlock(level, x, y+1, z + flipped*tempWidth, materials["fence"])

    # Priming platform for main part of bridge
    offsetMain = -1*(tempWidth-2)
    offsetSecondary = tempWidth+1
    offsetInterval = bridgeLength / float(bridgeSkew)  # Yes, redundant code.
    flapSize = 0
    extraFence = False
    for i in range(width-1):
        tempX = x + flipped*(i * bridgeMainDirectionX +
                             offsetSecondary * bridgeSecondaryDirectionX)
        tempZ = z + flipped*(i * bridgeMainDirectionZ +
                             offsetSecondary * bridgeSecondaryDirectionZ)

        if (((i+1) % offsetInterval) < 1):
            flapSize = flapSize + 1
            extraFence = True

        for j in range(flapSize):
            if (j == flapSize-1):
                setBlock(level, tempX+flipped*(j*bridgeSecondaryDirectionX+offsetMain*bridgeMainDirectionX), y+1,
                         tempZ+flipped*(j*bridgeSecondaryDirectionZ + offsetMain * bridgeMainDirectionZ), materials["fence"])
                if (extraFence):
                    setBlock(level, tempX+flipped*((j-1)*bridgeSecondaryDirectionX+offsetMain*bridgeMainDirectionX), y+1,
                             tempZ+flipped*((j-1)*bridgeSecondaryDirectionZ + offsetMain * bridgeMainDirectionZ), materials["fence"])
                    extraFence = False
            setBlock(level, tempX+flipped*(j*bridgeSecondaryDirectionX+offsetMain*bridgeMainDirectionX), y, tempZ+flipped*(j*bridgeSecondaryDirectionZ + offsetMain * bridgeMainDirectionZ),
                     materials["upper slab"][0], materials["upper slab"][1])


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


def buildSmallBridge(level, startPoint, endPoint, bridgeY, width, blocks):
    width = 3
    currentOffset = 0
    offsetInterval = bridgeLength/float(bridgeSkew)
    offsetNext = False

    # Offset points of bridge to center.
    startPoint = (startPoint[0]-((width/2)*bridgeSecondaryDirectionX),
                  startPoint[1]-((width/2)*bridgeSecondaryDirectionZ))
    endPoint = (endPoint[0]-((width/2)*bridgeSecondaryDirectionX),
                endPoint[1]-((width/2)*bridgeSecondaryDirectionZ))

    for i in range(bridgeLength):
        x = startPoint[0]+(i*bridgeMainDirectionX) + \
            (currentOffset*bridgeSecondaryDirectionX)
        z = startPoint[1]+(i*bridgeMainDirectionZ) + \
            (currentOffset*bridgeSecondaryDirectionZ)
        if ((i+1) % offsetInterval < 1):
            placeBridgeSection(level, x, bridgeY, z, width+1, materials["lower slab"],
                               False, False, False)
            currentOffset += 1
        else:
            placeBridgeSection(level, x, bridgeY, z, width, materials["lower slab"],
                               False, False, False)

def setBlock(level, x, y , z, block, data = 0):
    setBlockWithSurface(level, None, x, y, z, block, data)