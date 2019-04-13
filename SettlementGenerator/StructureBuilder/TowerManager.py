import json

from StructureBuilder import Base
from StructureBuilder import Blueprint

def getTowerBlueprint(point, baseHeight):
	filePath = "./stock-filters/SettlementGenerator/StructureBuilder/structures/tower_medium.json"
	blockRegister = loadFile(filePath)
	base = Base(point.x + 2, point.z + 2, 7, 7, baseHeight)
	return Blueprint(point, blockRegister, baseHeight, base, True)

def loadFile(filePath):
	with open(filePath) as f:
		return json.load(f)