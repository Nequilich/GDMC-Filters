import BlockDictionary
import math

from BiomeChanges import defaultBiomeChanges
from Common import setBlock
from TowerManager import getTowerBlueprint

class Blueprint:

	def __init__(self, point, blockRegister, baseHeight, base = None, buildFoundation = False):
		self.point = point
		self.blockRegister = blockRegister
		self.baseHeight = baseHeight
		self.base = base
		self.buildFoundation = buildFoundation

class Base:
	
	def __init__(self, xStart, zStart, xLength, zLength, height):
		self.xStart = xStart
		self.zStart = zStart
		self.xLength = xLength
		self.zLength = zLength

directions = ['north', 'east', 'south', 'west']

def buildStructure(level, point, baseHeight, type='tower', direction='north', biome='plains', applyBiomeChanges=True, specialBiomeChanges=None):
	blueprint = getBlueprint(type, point, baseHeight)
	blueprint.blockRegister = rotateRegister(blueprint.blockRegister, directions.index(direction))
	if applyBiomeChanges and biome != 'plains':
		blueprint.blockRegister = calculateBiomeChanges(blueprint.blockRegister, specialBiomeChanges, biome)
	build(level, blueprint)

def getBlueprint(type, point, baseHeight):
	if type == 'tower':
		return getTowerBlueprint(point, baseHeight)

def rotateRegister(blockRegister, rotations):
	rotations = rotations % 4
	rotatedRegister = []
	for block in blockRegister:
		np = rotateBlock(0, 0, 1.57079632679 * rotations, (block['x'], block['z']))
		if not block.get('type') or not block.get('direction'):
			b = BlockDictionary.getBlock(block['id'], block['data'])
			if not b:
				rotatedRegister.append({'type': None, 'direction': None, 'verticalAllignment': None, 'id': block['id'], 'data': block['data'], 'x': np[0], 'y': block['y'], 'z': np[1]})
			else:
				rotatedRegister.append({'type': b.type, 'direction': changeDirection(b.direction, rotations), 'verticalAllignment': b.verticalAllignment, 'id': block['id'], 'data': block['data'], 'x': np[0], 'y': block['y'], 'z': np[1]})
			continue
		rotatedRegister.append({'type': block['type'], 'direction': changeDirection(block['direction'], rotations), 'verticalAllignment': block['verticalAllignment'], 'id': block['id'], 'data': block['data'], 'x': np[0], 'y': block['y'], 'z': np[1]})
	moveToPositive(rotatedRegister)
	return rotatedRegister

def rotateBlock(cx, cz, angle, p):
	s = round(math.sin(angle))
	c = round(math.cos(angle))

	p = (p[0] - cx, p[1] - cz)

	nx = p[0] * c - p[1] * s
	nz = p[0] * s + p[1] * c

	p = (nx + cx, nz + cz)
	return p

def changeDirection(direction, rotations):
	if not direction:
		return None
	i = (directions.index(direction) + rotations) % 4
	return directions[i]

def moveToPositive(blockRegister):
	xMin = 0
	zMin = 0
	for block in blockRegister:
		if block['x'] < xMin:
			xMin = block['x']
		if block['z'] < zMin:
			zMin = block['z']
	for block in blockRegister:
		block['x'] += abs(xMin)
		block['z'] += abs(zMin)

def calculateBiomeChanges(blockRegister, specialBiomeChanges, biome):
	for block in blockRegister:
		if specialBiomeChanges and specialBiomeChanges.get(biome) and specialBiomeChanges.get(biome).get(block['type']):
			block['type'] = specialBiomeChanges[block['type']]
			continue
		if defaultBiomeChanges.get(block['type']):
			block['type'] = defaultBiomeChanges[block['type']]
	return blockRegister

def build(level, blueprint):
	for block in blueprint.blockRegister:
		x = blueprint.point.x
		z = blueprint.point.z
		b = None
		if block.get('type'):
			b = BlockDictionary.Block(block['type'], block['direction'], block['verticalAllignment'])
		else:
			b = BlockDictionary.getBlock(block['id'], block['data'])
		if not b:
			setBlock(level, None, x + int(block['x']), blueprint.baseHeight + int(block['y']), z + int(block['z']), block['id'], block['data'])
		else:
			blockIdentifier = BlockDictionary.getBlockIdentifier(b)
			setBlock(level, None, x + int(block['x']), blueprint.baseHeight + int(block['y']), z + int(block['z']), blockIdentifier[0], blockIdentifier[1])
	if blueprint.buildFoundation:
		buildFoundation(level, blueprint)

def buildFoundation(level, blueprint):
	if not blueprint.base:
		return
	xStart = blueprint.base.xStart
	zStart = blueprint.base.zStart
	xEnd = blueprint.base.xStart + blueprint.base.xLength - 1
	zEnd = blueprint.base.zStart + blueprint.base.zLength - 1
	for x in range(xStart, xEnd + 1):
		for z in range(zStart, zEnd + 1):
			i = 1
			while not isSurfaceBlock(level, x, blueprint.baseHeight - i, z):
				blockId = 1
				if i == 1:
					blockId = 98
				if (x == xStart or x == xEnd) and (z == zStart or z == zEnd):
					blockId = 98
				setBlock(level, None, x, blueprint.baseHeight - i, z, blockId)
				i += 1

aboveSurfaceBlocks = [0, 2, 3, 6, 17, 18, 31, 32, 37, 38, 39, 40, 59, 78, 81, 83, 99, 100, 103, 104, 105, 106, 111, 141, 142, 161, 162, 175]
def isSurfaceBlock(level, x, y, z):
	for block in aboveSurfaceBlocks:
		if level.blockAt(x, y, z) == block:
			return False
	return True
