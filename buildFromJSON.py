import json
import math
import utilityFunctions as utilityFunctions
import blockDictionary


inputs = (
	('rotations:', 0),
)

def perform(level, box, options):
	filePath = "./stock-filters/selection_dump.json"
	blockRegister = loadBlockRegisterFromFile(filePath)
	blockRegister = rotateRegister(blockRegister, options['rotations:'])
	moveToPositive(blockRegister)
	build(level, box.minx, box.minz, box.miny, blockRegister)


def loadBlockRegisterFromFile(filePath):
	with open(filePath) as f:
		return json.load(f)

halfPi = math.pi/2
def rotateRegister(blockRegister, rotations):
	rotations = rotations % 4
	rotatedRegister = []
	for block in blockRegister:
		np = rotateBlock(0, 0, halfPi * rotations, (block['x'], block['z']))
		if not block['type'] or not block['direction']:
			rotatedRegister.append({'type': None, 'direction': None, 'verticalAllignment': None, 'id': block['id'], 'data': block['data'], 'x': np[0], 'y': block['y'], 'z': np[1]})
			continue
		rotatedRegister.append({'type': block['type'], 'direction': changeDirection(block['direction'], rotations), 'verticalAllignment': block['verticalAllignment'], 'id': block['id'], 'data': block['data'], 'x': np[0], 'y': block['y'], 'z': np[1]})
	return rotatedRegister

def rotateBlock(cx, cz, angle, p):
	s = round(math.sin(angle))
	c = round(math.cos(angle))

	p = (p[0] - cx, p[1] - cz)

	nx = p[0] * c - p[1] * s
	nz = p[0] * s + p[1] * c

	p = (nx + cx, nz + cz)
	return p

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


def changeDirection(direction, rotations):
	directions = ['north', 'east', 'south', 'west']
	i = (directions.index(direction) + rotations) % 4
	return directions[i]


def build(level, xStart, zStart, baseHeight, blockRegister):
	for block in blockRegister:
		if block['type'] == None:
			utilityFunctions.setBlock(level, (block['id'], block['data']), xStart + block['x'], baseHeight + block['y'], zStart + block['z'])
		else:
			b = blockDictionary.Block(block['type'], block['direction'], block['verticalAllignment'])
			blockIdentifier = blockDictionary.getBlockIdentifier(b)
			utilityFunctions.setBlock(level, (blockIdentifier[0], blockIdentifier[1]), xStart + block['x'], baseHeight + block['y'], zStart + block['z'])