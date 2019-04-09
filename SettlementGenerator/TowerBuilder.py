import blockDictionary
import json
import math
from Classes import Point
from Common import setBlock

directions = ['north', 'east', 'south', 'west']

def buildMediumTower(level, surface, point, baseHeight, direction):
	point = Point(point.x - 5, point.z - 5)
	# buildFoundation(level, surface, point, baseHeight, 7)
	filePath = "./stock-filters/SettlementGenerator/structures/medium_tower.json"
	blockRegister = loadBlockRegisterFromFile(filePath)
	blockRegister = rotateRegister(blockRegister, directions.index(direction))
	build(level, surface, point, baseHeight, blockRegister)

def buildFoundation(level, surface, point, height, size):
	for x in range(point.x - int(size/2), point.x + int(size/2) + 2):
		for z in range(point.z - int(size/2), point.z + int(size/2) + 2):
			for y in range (height - 5, height):
				setBlock(level, surface.xStart + x, y, surface.zStart + z, 57)

def loadBlockRegisterFromFile(filePath):
	with open(filePath) as f:
		return json.load(f)

def rotateRegister(blockRegister, rotations):
	rotations = rotations % 4
	rotatedRegister = []
	for block in blockRegister:
		np = rotateBlock(0, 0, 1.57079632679 * rotations, (block['x'], block['z']))
		if not block['type'] or not block['direction']:
			rotatedRegister.append({'type': None, 'direction': None, 'verticalAllignment': None, 'id': block['id'], 'data': block['data'], 'x': np[0], 'y': block['y'], 'z': np[1]})
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
	directions = ['north', 'east', 'south', 'west']
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

def build(level, surface, point, baseHeight, blockRegister):
	for block in blockRegister:
		x = point.x
		z = point.z
		if block['type'] == None:
			setBlock(level, surface.xStart + x + int(block['x']), baseHeight + int(block['y']), surface.zStart + z + int(block['z']), block['id'], block['data'])
		else:
			b = blockDictionary.Block(block['type'], block['direction'], block['verticalAllignment'])
			blockIdentifier = blockDictionary.getBlockIdentifier(b)
			setBlock(level, surface.xStart + x + int(block['x']), baseHeight + int(block['y']), surface.zStart + z + int(block['z']), blockIdentifier[0], blockIdentifier[1])