import MaterialSets
from BiomeChanges import defaultBiomeChanges
from Biomes import getBiomeDict
from BlockDictionary import blockTypes

def get_biome_materials(biomeId = 1):
	biome_dict = getBiomeDict()
	biome_name = biome_dict[biomeId]
	materials = apply_biome_changes_to_material_set(
		MaterialSets.default.copy(), biome_name)

	return materials

def apply_biome_changes_to_material_set(materialSet, biome):
	biomeChanges = defaultBiomeChanges[biome]
	returnMaterials = {}

	for key, value in materialSet.items():
		if biomeChanges.get(value['type']):
			value = blockTypes[biomeChanges[value['type']]]
		returnMaterials[key] = value

	return returnMaterials