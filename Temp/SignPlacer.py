from pymclevel import TAG_Byte, TAG_Short, TAG_Int, TAG_Compound, TAG_List, TAG_String, TAG_Double, TAG_Float

def placeSectionSigns(sections):
	for section in sections:
		pass

def placeSign(level, surface, x, y, z, rotation, text1, text2, text3, text4):
	level.setBlockAt(x, y, z, 63)

	sign = TAG_Compound()
	sign["id"] = TAG_String('minecraft:sign')
	sign["x"] = TAG_Int(x)
	sign["y"] = TAG_Int(y)
	sign["z"] = TAG_Int(z)
	sign["Text1"] = TAG_String("{'text':''}")
	sign["Text2"] = TAG_String("{'text':''}")
	sign["Text3"] = TAG_String("{'text':''}")
	sign["Text4"] = TAG_String("{'text':''}")
    
	chunk = level.getChunk(x / 16, z / 16)
	chunk.Entities.append(sign)
	chunk.dirty = True