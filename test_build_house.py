import json
import utilityFunctions as utilityFunctions

inputs = (
  ("Build house", "label"),
  ("Size", ("regular", "small", "tiny")),
  ("Creator: Daniel Lundin", "label"),
)


def perform(level, box, options):
  filePath = "./stock-filters/test_build_house/house_" + options['Size'] + ".json"
  houseRegister = loadHouseRegisterFromFile(filePath)
  buildHouse(level, box, houseRegister)


def loadHouseRegisterFromFile(filePath):
  with open(filePath) as f:
    return json.load(f)


def buildHouse(level, box, houseRegister):
  for block in houseRegister:
    utilityFunctions.setBlock(level, (block['id'], block['data']), box.minx + block['x'], box.miny + block['y'], box.minz + block['z'])