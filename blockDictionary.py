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

def getBlock(id, data):
	identifier = (id, data)
	for _, blockType in blockTypes.iteritems():
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
'stone_brick': {
	'type': 'stone_brick',
	'default': (98, 0),
	'directions': {
		'north': {
			'top': (109, 7),
			'bottom': (109, 3)
		},
		'east': {
			'top': (109, 4),
			'bottom': (109, 0)
		},
		'south': {
			'top': (109, 6),
			'bottom': (109, 2)
		},
		'west': {
			'top': (109, 5),
			'bottom': (109, 1)
		}
	},
	'slabs': {
		'top': (44, 13),
		'bottom': (44, 5)
	}
},
'brick': {
	'type': 'brick',
	'default': (45, 0),
	'directions': {
		'north': {
			'top': (108, 7),
			'bottom': (108, 3)
		},
		'east': {
			'top': (108, 4),
			'bottom': (108, 0)
		},
		'south': {
			'top': (108, 6),
			'bottom': (108, 2)
		},
		'west': {
			'top': (108, 5),
			'bottom': (108, 1)
		}
	},
	'slabs': {
		'top': (44, 12),
		'bottom': (44, 4)
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
},
'spruce_wood': {
	'type': 'spruce_wood',
	'default': (17, 1),
	'directions': {
		'north': {
			'top': (17, 9),
			'bottom': (17, 9)
		},
		'east': {
			'top': (17, 5),
			'bottom': (17, 5)
		},
		'south': {
			'top': (17, 9),
			'bottom': (17, 9)
		},
		'west': {
			'top': (17, 5),
			'bottom': (17, 5)
		}
	},
	'slabs': {
		'top': (17, 1),
		'bottom': (17, 1)
	}
},
'birch_wood': {
	'type': 'birch_wood',
	'default': (17, 2),
	'directions': {
		'north': {
			'top': (17, 10),
			'bottom': (17, 10)
		},
		'east': {
			'top': (17, 6),
			'bottom': (17, 6)
		},
		'south': {
			'top': (17, 10),
			'bottom': (17, 10)
		},
		'west': {
			'top': (17, 6),
			'bottom': (17, 6)
		}
	},
	'slabs': {
		'top': (17, 2),
		'bottom': (17, 2)
	}
},
'jungle_wood': {
	'type': 'jungle_wood',
	'default': (17, 3),
	'directions': {
		'north': {
			'top': (17, 11),
			'bottom': (17, 11)
		},
		'east': {
			'top': (17, 7),
			'bottom': (17, 7)
		},
		'south': {
			'top': (17, 11),
			'bottom': (17, 11)
		},
		'west': {
			'top': (17, 7),
			'bottom': (17, 7)
		}
	},
	'slabs': {
		'top': (17, 3),
		'bottom': (17, 3)
	}
},
'acacia_wood': {
	'type': 'acacia_wood',
	'default': (162, 0),
	'directions': {
		'north': {
			'top': (162, 8),
			'bottom': (162, 8)
		},
		'east': {
			'top': (162, 4),
			'bottom': (162, 4)
		},
		'south': {
			'top': (162, 8),
			'bottom': (162, 8)
		},
		'west': {
			'top': (162, 4),
			'bottom': (162, 4)
		}
	},
	'slabs': {
		'top': (162, 0),
		'bottom': (162, 0)
	}
},
'dark_oak_wood': {
	'type': 'dark_oak_wood',
	'default': (162, 1),
	'directions': {
		'north': {
			'top': (162, 9),
			'bottom': (162, 9)
		},
		'east': {
			'top': (162, 5),
			'bottom': (162, 5)
		},
		'south': {
			'top': (162, 9),
			'bottom': (162, 9)
		},
		'west': {
			'top': (162, 5),
			'bottom': (162, 5)
		}
	},
	'slabs': {
		'top': (162, 1),
		'bottom': (162, 1)
	}
},
'oak_wood_planks': {
	'type': 'oak_wood_planks',
	'default': (5, 0),
	'directions': {
		'north': {
			'top': (53, 7),
			'bottom': (53, 3)
		},
		'east': {
			'top': (53, 4),
			'bottom': (53, 0)
		},
		'south': {
			'top': (53, 6),
			'bottom': (53, 2)
		},
		'west': {
			'top': (53, 5),
			'bottom': (53, 1)
		}
	},
	'slabs': {
		'top': (126, 8),
		'bottom': (126, 0)
	}
},
'spruce_wood_planks': {
	'type': 'spruce_wood_planks',
	'default': (5, 1),
	'directions': {
		'north': {
			'top': (134, 7),
			'bottom': (134, 3)
		},
		'east': {
			'top': (134, 4),
			'bottom': (134, 0)
		},
		'south': {
			'top': (134, 6),
			'bottom': (134, 2)
		},
		'west': {
			'top': (134, 5),
			'bottom': (134, 1)
		}
	},
	'slabs': {
		'top': (126, 9),
		'bottom': (126, 1)
	}
},
'birch_wood_planks': {
	'type': 'birch_wood_planks',
	'default': (5, 2),
	'directions': {
		'north': {
			'top': (135, 7),
			'bottom': (135, 3)
		},
		'east': {
			'top': (135, 4),
			'bottom': (135, 0)
		},
		'south': {
			'top': (135, 6),
			'bottom': (135, 2)
		},
		'west': {
			'top': (135, 5),
			'bottom': (135, 1)
		}
	},
	'slabs': {
		'top': (126, 10),
		'bottom': (126, 2)
	}
},
'jungle_wood_planks': {
	'type': 'jungle_wood_planks',
	'default': (5, 3),
	'directions': {
		'north': {
			'top': (136, 7),
			'bottom': (136, 3)
		},
		'east': {
			'top': (136, 4),
			'bottom': (136, 0)
		},
		'south': {
			'top': (136, 6),
			'bottom': (136, 2)
		},
		'west': {
			'top': (136, 5),
			'bottom': (136, 1)
		}
	},
	'slabs': {
		'top': (126, 11),
		'bottom': (126, 3)
	}
},
'acacia_wood_planks': {
	'type': 'acacia_wood_planks',
	'default': (5, 4),
	'directions': {
		'north': {
			'top': (163, 7),
			'bottom': (163, 3)
		},
		'east': {
			'top': (163, 4),
			'bottom': (163, 0)
		},
		'south': {
			'top': (163, 6),
			'bottom': (163, 2)
		},
		'west': {
			'top': (163, 5),
			'bottom': (163, 1)
		}
	},
	'slabs': {
		'top': (126, 12),
		'bottom': (126, 4)
	}
},
'dark_oak_wood_planks': {
	'type': 'dark_oak_wood_planks',
	'default': (5, 5),
	'directions': {
		'north': {
			'top': (164, 7),
			'bottom': (164, 3)
		},
		'east': {
			'top': (164, 4),
			'bottom': (164, 0)
		},
		'south': {
			'top': (164, 6),
			'bottom': (164, 2)
		},
		'west': {
			'top': (164, 5),
			'bottom': (164, 1)
		}
	},
	'slabs': {
		'top': (126, 13),
		'bottom': (126, 5)
	}
}}