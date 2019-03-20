from Common import setBlock
from Classes import Surface

materials = {}

def buildBridge(level, startPoint, endPoint, bridgeY, width, blocks):
    global materials
    materials = blocks
    
    xLength = abs(endPoint[0] - startPoint[0])+1
    zLength = abs(endPoint[1] - startPoint[1])+1
    bridgeLength = min(xLength, xLength)

    if(xLength > zLength):  #Main direction is east, positive X
        bridgeLength = xLength
        bridgeSkew = zLength
        bridgeMainDirectionX = 1
        bridgeMainDirectionZ = 0
        bridgeSecondaryDirectionX = 0
        bridgeSecondaryDirectionZ = 1
    else:  #Main direction is south, positive Z
        bridgeLength = zLength        
        bridgeSkew = xLength
        bridgeMainDirectionX = 0
        bridgeMainDirectionZ = 1
        bridgeSecondaryDirectionX = 1
        bridgeSecondaryDirectionZ = 0

    #Offsets the start and end points to center bridge.
    startPoint = (startPoint[0]-((width/2)*bridgeSecondaryDirectionX), startPoint[1]-((width/2)*bridgeSecondaryDirectionZ))
    endPoint = (endPoint[0]-((width/2)*bridgeSecondaryDirectionX), endPoint[1]-((width/2)*bridgeSecondaryDirectionZ))
     
    #Offset variables
    offsetNext = False
    offsetInterval = bridgeLength/float(bridgeSkew)
    currentOffset = 0
    #TODO handle offset intervals smaller than 2.

    #place start of bridge
    placeBridgeStartOrEnd(level, startPoint[0], bridgeY, startPoint[1], bridgeSecondaryDirectionX, bridgeSecondaryDirectionZ, width)

    #place main part of bridge
    for i in range(1, bridgeLength-1):
        x = startPoint[0]+(i*bridgeMainDirectionX)+(currentOffset*bridgeSecondaryDirectionX)
        z = startPoint[1]+(i*bridgeMainDirectionZ)+(currentOffset*bridgeSecondaryDirectionZ)
        if ((i+1) % offsetInterval < 1):
            if (offsetNext == True):
                placeBridgeSection(level, x, bridgeY, z, bridgeSecondaryDirectionX, bridgeSecondaryDirectionZ, width+2, True, True)
                currentOffset += 1
            else :
                placeBridgeSection(level, x, bridgeY, z, bridgeSecondaryDirectionX, bridgeSecondaryDirectionZ, width+1, False, True)
            offsetNext = True
        elif (offsetNext == True):
            placeBridgeSection(level, x, bridgeY, z, bridgeSecondaryDirectionX, bridgeSecondaryDirectionZ, width+1, True, False)
            offsetNext = False
            currentOffset += 1
        else :
            placeBridgeSection(level, x, bridgeY, z, bridgeSecondaryDirectionX, bridgeSecondaryDirectionZ, width, False, False)

    #place end of bridge
    placeBridgeStartOrEnd(level, endPoint[0], bridgeY, endPoint[1], bridgeSecondaryDirectionX, bridgeSecondaryDirectionZ, width)

def placeBridgeSection(level, x, y, z, directionX, directionZ, width, extraFenceLeft, extraFenceRight):
    #Place main part of bridge
    for i in range(width):
        setBlock(level, x+i*directionX, y, z+i*directionZ, materials["upper slab"][0], materials["upper slab"][1])

    #Place fencing
    setBlock(level, x, y+1, z, materials["fence"])
    setBlock(level, x+(width-1)*directionX, y+1, z+(width-1)*directionZ, materials["fence"])
    if (extraFenceLeft):
        setBlock(level, x+directionX, y+1, z+directionZ, materials["fence"])
    elif (extraFenceRight):
        setBlock(level, x+(width-2)*directionX, y+1, z+(width-2)*directionZ, materials["fence"])

def placeBridgeStartOrEnd(level, x, y, z, directionX, directionZ, width):
    placePillarWithTorch(level, x, y, z)

    for i in range(1, width-1):
        setBlock(level, x+i*directionX, y, z+i*directionZ, materials["lower slab"][0], materials["lower slab"][1])
    placePillarWithTorch(level, x+(width-1)*directionX, y, z+(width-1)*directionZ)

def placePillarWithTorch(level, x, y, z):
    setBlock(level, x, y, z, materials["normal"][0], materials["normal"][1])
    setBlock(level, x, y+1, z, materials["normal"][0], materials["normal"][1])
    setBlock(level, x, y+2, z, materials["torch"])