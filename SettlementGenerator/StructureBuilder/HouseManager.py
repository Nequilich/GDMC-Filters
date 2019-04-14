from Classes import Base
from Classes import Blueprint
from Common import loadFile

def getHouseBlueprint(point, prop):
	blockRegister = []
	base = Base(point.x, point.z, prop.xLength, prop.zLength)
	blueprint = Blueprint(point, blockRegister, prop.height + 5, base, True)
	addFloor(point, prop, blueprint)
	addWall(point, prop, blueprint.blockRegister)
	return blueprint

def addFloor(point, prop, blueprint):
	for x in range(1, prop.xLength - 1):
		for z in range(1, prop.zLength - 1):
			blueprint.blockRegister.append({'type': 'oak_wood_planks', 'direction': None, 'verticalAllignment': None, 'id': 5, 'data': 0, 'x': x, 'y': 1, 'z': z})

def addWall(point, prop, blockRegister):
	y = 2
	# North and south default wall segments
	segmentRegister = loadSegmentRegister('wall_default')
	for x in range(2, prop.xLength - 2, 2):
		for block in segmentRegister:
			appendAdjustedBlockToRegister(blockRegister, block, x, y, 1)
			appendAdjustedBlockToRegister(blockRegister, block, prop.xLength - 1 - x, y, prop.zLength - 2)
			if x == prop.xLength - 4:
				appendAdjustedBlockToRegister(blockRegister, block, x + 1, y, 1)
				appendAdjustedBlockToRegister(blockRegister, block, prop.xLength - 2 - x, y, prop.zLength - 2)
	# East and west walls
	for z in range(2, prop.zLength - 2, 2):
		for block in segmentRegister:
			appendAdjustedBlockToRegister(blockRegister, block, 1, y, z)
			appendAdjustedBlockToRegister(blockRegister, block, prop.xLength - 2, y, prop.zLength - 1 - z)
			if z == prop.zLength - 4:
				appendAdjustedBlockToRegister(blockRegister, block, 1, y, z + 1)
				appendAdjustedBlockToRegister(blockRegister, block, prop.xLength - 2, y, prop.zLength - 2 - z)
	segmentRegister = loadSegmentRegister('wall_window')
	# North and south windows
	for x in range(3, prop.xLength - 3, 2):
		for block in segmentRegister:
			appendAdjustedBlockToRegister(blockRegister, block, x, y, 1)
			appendAdjustedBlockToRegister(blockRegister, block, prop.xLength - 1 - x, y, prop.zLength - 2)
	# East and west windows
	for z in range(3, prop.zLength - 3, 2):
		for block in segmentRegister:
			appendAdjustedBlockToRegister(blockRegister, block, 1, y, z)
			appendAdjustedBlockToRegister(blockRegister, block, prop.xLength - 2, y, prop.zLength - 1 - z)
	# Corners
	segmentRegister = loadSegmentRegister('wall_corner')
	for block in segmentRegister:
		appendAdjustedBlockToRegister(blockRegister, block, 1, y, 1)
		appendAdjustedBlockToRegister(blockRegister, block, prop.xLength - 2, y, 1)
		appendAdjustedBlockToRegister(blockRegister, block, 1, y, prop.zLength - 2)
		appendAdjustedBlockToRegister(blockRegister, block, prop.xLength - 2, y, prop.zLength - 2)

def loadSegmentRegister(segment):
	filePath = './stock-filters/SettlementGenerator/StructureBuilder/structures/house/' + segment + '.json'
	return loadFile(filePath)

def appendAdjustedBlockToRegister(register, block, x, y, z):
	register.append({
		'type': block['type'],
		'direction': block['direction'],
		'verticalAllignment': block['verticalAllignment'],
		'data': block['data'],
		'x': x + block['x'],
		'y': y + block['y'],
		'z': z + block['z']})