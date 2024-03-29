import json
import BlockDictionary

inputs = (
	("Create JSON file of selection", "label"),
	("Path: GDMC/stock-filters/selection_dump.json", "label"),
	("Include air blocks", False),
	("JSON Indents:", 2),
	("Creator: Daniel Lundin", "label"),
)


def perform(level, box, options):
	layers = readSelection(level, box)
	blocks = getBlocks(layers, options['Include air blocks'])
	blocks = addBlockInformation(blocks)

	writeToJSONFile('./stock-filters', 'selection_dump', blocks, options)


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


def getBlocks(layers, includeAir):
	blocks = []
	for y, layer in enumerate(layers):
		for x, line in enumerate(layer):
			for z, block in enumerate(line):
				if(includeAir or block[0] != 0):
					blocks.append({'id': 0 + block[0], 'data': 0 + block[1], 'x': 0 + x, 'y': 0 + y, 'z': 0 + z})
	return blocks


def addBlockInformation(blocks):
	data = []
	for mcBlock in blocks:
		block = BlockDictionary.getBlock(mcBlock['id'], mcBlock['data'])
		if block == None:
			data.append({'type': None, 'direction': None, 'verticalAllignment': None, 'id': mcBlock['id'], 'data': mcBlock['data'], 'x': mcBlock['x'], 'y': mcBlock['y'], 'z': mcBlock['z']})
			continue
		data.append({'type': block.type, 'direction': block.direction, 'verticalAllignment': block.verticalAllignment, 'id': mcBlock['id'], 'data': mcBlock['data'], 'x': mcBlock['x'], 'y': mcBlock['y'], 'z': mcBlock['z']})
	return data


def writeToJSONFile(path, fileName, data, options):
	filePath = path + '/' + fileName + '.json'
	with open(filePath, 'w') as f:
		json.dump(data, f, indent=options['JSON Indents:'], sort_keys=True)