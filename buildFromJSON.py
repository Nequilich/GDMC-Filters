import json
import utilityFunctions as utilityFunctions
import blockDictionary


def perform(level, box, options):
	filePath = "./stock-filters/selection_dump.json"
	blockRegister = loadBlockRegisterFromFile(filePath)
	build(level, box.minx, box.minz, box.miny, blockRegister)


def loadBlockRegisterFromFile(filePath):
	with open(filePath) as f:
		return json.load(f)


def build(level, xStart, zStart, baseHeight, blockRegister):
	for block in blockRegister:
		if block['type'] == None:
			utilityFunctions.setBlock(level, (block['id'], block['data']), xStart + block['x'], baseHeight + block['y'], zStart + block['z'])
		else:
			b = blockDictionary.Block(block['type'], block['direction'], block['verticalAllignment'])
			blockIdentifier = blockDictionary.getBlockIdentifier(b)
			utilityFunctions.setBlock(level, (blockIdentifier[0], blockIdentifier[1]), xStart + block['x'], baseHeight + block['y'], zStart + block['z'])