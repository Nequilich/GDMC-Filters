from Common import setBlock
from Classes import Surface
from SurfaceManager import calculateHeightMapAdv
from BridgeBuilder import buildBridge

inputs = (
  ("Width", 4),
  ("Creator: Jungne Losang", "label")
)

def perform(level, box, options):
    bridgeWidth = options["Width"]

    surface = Surface(box.minx, box.minz, box.maxx, box.maxz)
    calculateHeightMapAdv(level, surface)
    startPoint = (box.minx, box.minz)
    endPoint = (box.maxx-1, box.maxz-1)
    bridgeY = surface.surfaceMap[0][0].height + 1  #+1 to raise above the surface

    buildBridge(level, startPoint, endPoint, bridgeY, bridgeWidth)