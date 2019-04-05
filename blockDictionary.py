class Block:

	def __init__(self, type, direction = None, verticalAllignment = None):
		self.type = type
		self.direction = direction
		self.verticalAllignment = verticalAllignment

def getBlockIdentifier(block):
	if not block.direction and not block.verticalAllignment:
		return blockTypes[block.type]['default']
	elif not block.direction and block.verticalAllignment:
		return blockTypes[block.type]['slabs'][block.verticalAllignment]
	return blockTypes[block.type]['directions'][block.direction][block.verticalAllignment]

def getBlock(identifier):
	for blockType in blockTypes:
		# checking default
		if blockType['default'] == identifier:
			return Block(blockType['type'], None, None)
		# checking slabs
		if blockType['slabs']['top'] == identifier:
			return Block(blockType['type'], None, 'top')
		if blockType['slabs']['bottom'] == identifier:
			return Block(blockType['type'], None, 'bottom')
		# checking directions
		# north
		if blockType['directions']['north']['top'] == identifier:
			return Block(blockType['type'], 'north', 'top')
		if blockType['directions']['north']['bottom'] == identifier:
			return Block(blockType['type'], 'north', 'bottom')
		# east
		if blockType['directions']['east']['top'] == identifier:
			return Block(blockType['type'], 'east', 'top')
		if blockType['directions']['east']['bottom'] == identifier:
			return Block(blockType['type'], 'east', 'bottom')
		# south
		if blockType['directions']['south']['top'] == identifier:
			return Block(blockType['type'], 'south', 'top')
		if blockType['directions']['south']['bottom'] == identifier:
			return Block(blockType['type'], 'south', 'bottom')
		# west
		if blockType['directions']['west']['top'] == identifier:
			return Block(blockType['type'], 'west', 'top')
		if blockType['directions']['west']['bottom'] == identifier:
			return Block(blockType['type'], 'west', 'bottom')
	return None

blockTypes = {
	'stone': {
	'type': 'stone',
	'default': (1, 0),
	'directions': {
		'north': {
			'top': (1, 0),
			'bottom': (1, 0)
		},
		'east': {
			'top': (1, 0),
			'bottom': (1, 0)
		},
		'south': {
			'top': (1, 0),
			'bottom': (1, 0)
		},
		'west': {
			'top': (1, 0),
			'bottom': (1, 0)
		}
	},
	'slabs': {
		'top': (44, 8),
		'bottom': (44, 0)
	}
},
'cobblestone': {
	'type': 'cobblestone',
	'default': (4, 0),
	'directions': {
		'north': {
			'top': (67, 7),
			'bottom': (67, 3)
		},
		'east': {
			'top': (67, 4),
			'bottom': (67, 0)
		},
		'south': {
			'top': (67, 6),
			'bottom': (67, 2)
		},
		'west': {
			'top': (67, 5),
			'bottom': (67, 1)
		}
	},
	'slabs': {
		'top': (44, 11),
		'bottom': (44, 3)
	}
},
'oak_wood': {
	'type': 'oak_wood',
	'default': (17, 0),
	'directions': {
		'north': {
			'top': (17, 8),
			'bottom': (17, 8)
		},
		'east': {
			'top': (17, 4),
			'bottom': (17, 4)
		},
		'south': {
			'top': (17, 8),
			'bottom': (17, 8)
		},
		'west': {
			'top': (17, 4),
			'bottom': (17, 4)
		}
	},
	'slabs': {
		'top': (17, 0),
		'bottom': (17, 0)
	}
}}