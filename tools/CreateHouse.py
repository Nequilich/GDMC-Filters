import json
import utilityFunctions as utilityFunctions


def createHouse(level, xStart, zStart, xEnd, zEnd, baseHeight):
  houseSize = ""
  xLength = xEnd - xStart
  zLength = zEnd - zStart
  if (xLength >= 7 and zLength >= 5):
    houseSize = "tiny"
  if (xLength >= 11 and zLength >= 7):
    houseSize = "small"
  if (xLength >= 11 and zLength >= 19):
    houseSize = "regular"
  if (houseSize == ""):
    return
  filePath = "./stock-filters/houses/house_" + houseSize + ".json"
  houseRegister = loadHouseRegisterFromFile(filePath)
  buildHouse(level, xStart, zStart, baseHeight, houseRegister)


def loadHouseRegisterFromFile(filePath):
  with open(filePath) as f:
    return json.load(f)


def buildHouse(level, xStart, zStart, baseHeight, houseRegister):
  for block in houseRegister:
    utilityFunctions.setBlock(level, (block['id'], block['data']), xStart + block['x'], baseHeight + block['y'], zStart + block['z'])