from BlockRegisterRotater import rotateRegister
from Classes import Base
from Classes import Blueprint
from Classes import Point
from Common import loadFile

directions = ['NORTH', 'EAST', 'SOUTH', 'WEST']

def getHouseBlueprint(point, prop):
	blockRegister = []
	base = Base(point.x, point.z, prop.xLength, prop.zLength)
	blueprint = Blueprint(point, blockRegister, prop.height + 1, base, True)
	addFloor(point, prop, blueprint)
	addWall(point, prop, blueprint.blockRegister)
	return blueprint

def addFloor(point, prop, blueprint):
	for x in range(2, prop.xLength - 2):
		for z in range(2, prop.zLength - 2):
			blueprint.blockRegister.append({'type': 'oak_wood_planks', 'direction': None, 'verticalAllignment': None, 'id': 5, 'data': 0, 'x': x, 'y': 0, 'z': z})

def addWall(point, prop, blockRegister):
	y = 0
	isDoorPlaced = False
	doorPoint = None
	# North and South default wall segments
	segmentRegister = loadSegmentRegister('wall_default')
	for x in range(2, prop.xLength - 2, 2):
		for block in segmentRegister:
			appendAdjustedBlockToRegister(blockRegister, block, x, y, 1)
			appendAdjustedBlockToRegister(blockRegister, block, prop.xLength - 1 - x, y, prop.zLength - 2)
			if x == prop.xLength - 4:
				appendAdjustedBlockToRegister(blockRegister, block, x + 1, y, 1)
				appendAdjustedBlockToRegister(blockRegister, block, prop.xLength - 2 - x, y, prop.zLength - 2)
	# East and West default wall segments
	for z in range(2, prop.zLength - 2, 2):
		for block in segmentRegister:
			appendAdjustedBlockToRegister(blockRegister, block, 1, y, z)
			appendAdjustedBlockToRegister(blockRegister, block, prop.xLength - 2, y, prop.zLength - 1 - z)
			if z == prop.zLength - 4:
				appendAdjustedBlockToRegister(blockRegister, block, 1, y, z + 1)
				appendAdjustedBlockToRegister(blockRegister, block, prop.xLength - 2, y, prop.zLength - 2 - z)
	segmentRegister = loadSegmentRegister('wall_window')
	# North and South windows and maybe door
	for x in range(3, prop.xLength - 3, 2):
		skipNorth = False
		skipSouth = False
		if not isDoorPlaced:
			if prop.doorDirection == 'NORTH':
				skipNorth = True
			if prop.doorDirection == 'SOUTH':
				skipSouth = True
		if skipNorth:
			doorPoint = Point(x, 1)
			isDoorPlaced = True
		if skipSouth:
			doorPoint = Point(prop.xLength - 1 - x, prop.zLength - 2)
			isDoorPlaced = True
		for block in segmentRegister:
			if not skipNorth:
				appendAdjustedBlockToRegister(blockRegister, block, x, y, 1)
			if not skipSouth:
				appendAdjustedBlockToRegister(blockRegister, block, prop.xLength - 1 - x, y, prop.zLength - 2)
	# East and West windows and maybe door
	for z in range(3, prop.zLength - 3, 2):
		skipEast = False
		skipWest = False
		if not isDoorPlaced:
			if prop.doorDirection == 'EAST':
				skipEast = True
			if prop.doorDirection == 'WEST':
				skipWest = True
		if skipEast:
			doorPoint = Point(prop.xLength - 2, prop.zLength - 1 - z)
			isDoorPlaced = True
		if skipWest:
			doorPoint = Point(1, z)
			isDoorPlaced = True
		for block in segmentRegister:
			if not skipWest:
				appendAdjustedBlockToRegister(blockRegister, block, 1, y, z)
			if not skipEast:
				appendAdjustedBlockToRegister(blockRegister, block, prop.xLength - 2, y, prop.zLength - 1 - z)
	# Corners
	segmentRegister = loadSegmentRegister('wall_corner')
	for block in segmentRegister:
		appendAdjustedBlockToRegister(blockRegister, block, 1, y, 1)
		appendAdjustedBlockToRegister(blockRegister, block, prop.xLength - 2, y, 1)
		appendAdjustedBlockToRegister(blockRegister, block, 1, y, prop.zLength - 2)
		appendAdjustedBlockToRegister(blockRegister, block, prop.xLength - 2, y, prop.zLength - 2)
	# Door
	segmentRegister = loadSegmentRegister('wall_door')
	segmentRegister = rotateRegister(segmentRegister, directions.index(prop.doorDirection))
	for block in segmentRegister:
		appendAdjustedBlockToRegister(blockRegister, block, doorPoint.x, y, doorPoint.z)

def loadSegmentRegister(segment):
	filePath = './stock-filters/SettlementGenerator/StructureBuilder/structures/house/' + segment + '.json'
	return loadFile(filePath)

def appendAdjustedBlockToRegister(register, block, x, y, z):
	register.append({
		'type': block['type'],
		'direction': block['direction'],
		'verticalAllignment': block['verticalAllignment'],
		'id': block['id'],
		'data': block['data'],
		'x': x + block['x'],
		'y': y + block['y'],
		'z': z + block['z']})