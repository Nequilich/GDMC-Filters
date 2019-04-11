import BlockDictionary
import json
import math
from Classes import Point
from Common import setBlock

directions = ['north', 'east', 'south', 'west']

def buildMediumTower(level, point, baseHeight, direction='north', applyBiomeChanges=True, specialBiomeChanges=None, biome='plains'):
	buildFoundation(level, point, baseHeight, 7)
	point = Point(point.x - 5, point.z - 5)
	filePath = "./stock-filters/SettlementGenerator/structures/medium_tower.json"
	blockRegister = loadBlockRegisterFromFile(filePath)
	blockRegister = rotateRegister(blockRegister, directions.index(direction))
	if applyBiomeChanges and biome != 'plains':
		blockRegister = calculateBiomeChanges(blockRegister, specialBiomeChanges, biome)
	build(level, point, baseHeight, blockRegister)

def buildFoundation(level, point, height, size):
	cornerPoint = Point(point.x - int(size/2), point.z - int(size/2))
	for x in range(cornerPoint.x, cornerPoint.x + size):
		for z in range(cornerPoint.z, cornerPoint.z + size):
			i = 1
			while not isSurfaceBlock(level, x, height - i, z):
				blockId = 1
				if i == 1:
					blockId = 98
				if (x == cornerPoint.x or x == cornerPoint.x + size - 1) and (z == cornerPoint.z or z == cornerPoint.z + size - 1):
					blockId = 98
				setBlock(level, None, x, height - i, z, blockId)
				i += 1

aboveSurfaceBlocks = [0, 2, 3, 6, 17, 18, 31, 32, 37, 38, 39, 40, 59, 78, 81, 83, 99, 100, 103, 104, 105, 106, 111, 141, 142, 161, 162, 175]
def isSurfaceBlock(level, x, y, z):
	for block in aboveSurfaceBlocks:
		if level.blockAt(x, y, z) == block:
			return False
	return True

def loadBlockRegisterFromFile(filePath):
	with open(filePath) as f:
		return json.load(f)

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
	biomeChanges = getBiomeChanges(specialBiomeChanges, biome)
	for block in blockRegister:
		if biomeChanges.get(block['type']):
			block['type'] = biomeChanges[block['type']]
	return blockRegister

def getBiomeChanges(specialBiomeChanges, biome):
	biomeChanges = specialBiomeChanges.get(biome)
	if not biomeChanges:
		print('getdefaultbiomechanges')
	return biomeChanges

def build(level, point, baseHeight, blockRegister):
	for block in blockRegister:
		x = point.x
		z = point.z
		b = None
		if block.get('type'):
			b = BlockDictionary.Block(block['type'], block['direction'], block['verticalAllignment'])
		else:
			b = BlockDictionary.getBlock(block['id'], block['data'])
		if not b:
			setBlock(level, None, x + int(block['x']), baseHeight + int(block['y']), z + int(block['z']), block['id'], block['data'])
		else:
			blockIdentifier = BlockDictionary.getBlockIdentifier(b)
			setBlock(level, None, x + int(block['x']), baseHeight + int(block['y']), z + int(block['z']), blockIdentifier[0], blockIdentifier[1])