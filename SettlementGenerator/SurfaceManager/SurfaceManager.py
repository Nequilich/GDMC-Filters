from CalculateBiomeMap import calculateBiomeMap as CBM
from CalculateHeightMap import calculateHeightMap as CHM
from CalculateHeightMapAdv import calculateHeightMap as CHMA
from CalculateSteepnessMap import calculateSteepnessMap as CSM
from CalculateSections import calculateSections as CS
from CalculateSectionMid import calculateSectionMid as CSMid

def calculateBiomeMap(level, surface):
	CBM(level, surface)

def calculateHeightMap(level, surface):
	CHM(level, surface)

def calculateHeightMapAdv(level, surface):
	CHMA(level, surface)

def calculateSteepnessMap(surface):
	CSM(surface)

def calculateSections(surface, allowedSteepness = 0, minSize = 1):
	return CS(surface, allowedSteepness, minSize)

def calculateSectionMid(surface, section):
	CSMid(surface, section)

def calculateWaterPlacement(level, surface):
	for x in range(surface.xLength):
		for z in range(surface.zLength):
			y = surface.surfaceMap[x][z].height
			isWater = level.blockAt(x + surface.xStart, y, z + surface.zStart) == 9 and level.blockDataAt(x + surface.xStart, y, z + surface.zStart) == 0
			isLava = level.blockAt(x + surface.xStart, y, z + surface.zStart) == 11 and level.blockDataAt(x + surface.xStart, y, z + surface.zStart) == 0
			surface.surfaceMap[x][z].isWater = isWater or isLava