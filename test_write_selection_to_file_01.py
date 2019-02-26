import json
import utilityFunctions as utilityFunctions

inputs = (
  ("Write selection to file", "label"),
  ("Include air blocks", False),
  ("Creator: Daniel Lundin", "label"),
)


def perform(level, box, options):
  layers = readSelection(level, box)
  blocks = getBlocks(layers)

  writeToJSONFile('./', 'test_write_selection_to_file_01-dump', blocks)


def readSelection(level, box):
  layers = []
  for y in range(box.miny, box.maxy):
    layer = []
    for x in range(box.minx, box.maxx):
      line = []
      for z in range(box.minz, box.maxz):
        line.append((level.blockAt(x, y, z), level.blockDataAt(x, y, z)))
      layer.append(line)
    layers.append(layer)
  return layers


def getBlocks(layers):
  blocks = []
  for y, layer in enumerate(layers):
    for x, line in enumerate(layer):
      for z, block in enumerate(line):
        if(block[0] != 0):
          blocks.append({'id': 0 + block[0], 'data': 0 + block[1], 'x': 0 + x, 'y': 0 + y, 'z': 0 + z})
  return blocks


def writeToJSONFile(path, fileName, data):
    filePath = path + '/' + fileName + '.json'
    with open(filePath, 'w') as f:
        json.dump(data, f, indent=2)