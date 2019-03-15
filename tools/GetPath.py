import heapq as heapq
import math as math


def getPath(surface, xStart, zStart, xEnd, zEnd):
  return getAStarPath(surface, xStart, zStart, xEnd, zEnd)


def getAStarPath(surface, xSource, zSource, xTarget, zTarget):
  closedSet = []
  openSet = []
  initializedNodes = []
  for _ in range(surface.xLength):
    row = []
    for _ in range(surface.zLength):
      row.append(None)
    initializedNodes.append(row)

  targetNode = Node(surface, xTarget, zTarget, None)

  sourceNode = Node(surface, xSource, zSource, targetNode)
  sourceNode.heuristicCostToTargetEstimate = getEuclideanHeuristicCostEstimate(surface, sourceNode, targetNode)
  sourceNode.gScore = 0
  sourceNode.fScore = sourceNode.heuristicCostToTargetEstimate

  initializedNodes[sourceNode.x][sourceNode.z] = sourceNode
  initializedNodes[targetNode.x][targetNode.z] = targetNode

  heapq.heappush(openSet, (sourceNode.fScore, sourceNode))

  while(len(openSet) > 0):
    currentNode = heapq.heappop(openSet)[1]
    
    if (currentNode.isEqual(targetNode)):
      return reconstructPath(currentNode)
    
    closedSet.append(currentNode)

    for neighbourNode in getNeighbourNodes(surface, currentNode, initializedNodes, targetNode):
      if neighbourNode in closedSet:
        continue
      waterCostModifier = 1
      if (surface.surfaceMap[neighbourNode.x][neighbourNode.z].isWater):
        waterCostModifier = 2
      tentativeGSCore = currentNode.gScore + getEuclideanHeuristicCostEstimate(surface, currentNode, neighbourNode) * waterCostModifier
      if (tentativeGSCore >= neighbourNode.gScore):
        continue
      neighbourNode.gScore = tentativeGSCore
      neighbourNode.fScore = tentativeGSCore + neighbourNode.heuristicCostToTargetEstimate
      neighbourNode.cameFrom = currentNode
      if (neighbourNode.fScore, neighbourNode) not in openSet:
        heapq.heappush(openSet, (neighbourNode.fScore, neighbourNode))

  return None


def getNeighbourNodes(surface, node, initializedNodes, targetNode):
  neighbourNodes = []
  for x in range(node.x - 1, node.x + 2):
    if (x < 0 or x >= surface.xLength):
      continue
    for z in range(node.z - 1, node.z + 2):
      if (z < 0 or z >= surface.zLength):
        continue
      if (x == node.x and z == node.z):
        continue
      neighbourNode = None
      if (initializedNodes[x][z] == None):
        initializedNodes[x][z] = Node(surface, x, z, targetNode)
      neighbourNode = initializedNodes[x][z]
      neighbourNodes.append(neighbourNode)
  return neighbourNodes


def reconstructPath(node):
  path = []
  currentNode = node
  path.insert(0, currentNode)
  while(currentNode.cameFrom != None):
    currentNode = currentNode.cameFrom
    path.insert(0, currentNode)
  return path


def getEuclideanHeuristicCostEstimate(surface, node, targetNode):
  hcm = 4 # height cost modifier
  return math.sqrt(math.pow(targetNode.x - node.x, 2) + math.pow(targetNode.z - node.z, 2) + math.pow((targetNode.y - node.y) * hcm, 2))

c1 = math.sqrt(2)
c2 = math.sqrt(3)
def getHeuristicCostEstimate(surface, node, targetNode):
  # hcm = 1 # height cost modifier
  # return math.sqrt(math.pow(targetNode.x - node.x, 2) + math.pow(targetNode.z - node.z, 2) + math.pow((targetNode.y - node.y) * hcm, 2))
  minimumDistance = 0
  xLength = abs(targetNode.x - node.x)
  zLength = abs(targetNode.z - node.z)
  yLength = abs(targetNode.y - node.y)
  longHorizontalLength = max(xLength, zLength)
  shortHorizontalLength = min(xLength, zLength)
  height = yLength
  if(height > longHorizontalLength):
    return math.sqrt(math.pow(targetNode.x - node.x, 2) + math.pow(targetNode.z - node.z, 2) + math.pow((targetNode.y - node.y), 2))
  if (shortHorizontalLength > height):
    minimumDistance = height * c2 + (shortHorizontalLength - height) * c1 + longHorizontalLength - shortHorizontalLength
  else:
    minimumDistance = shortHorizontalLength * c2 + (height - shortHorizontalLength) * c1 + longHorizontalLength - height
  return minimumDistance


def getSimpleHeuristicCostEstimate(surface, node, targetNode):
  heightCost = 4
  xLength = abs(targetNode.x - node.x)
  zLength = abs(targetNode.z - node.z)
  yLength = abs(targetNode.y - node.y)
  longHorizontalLength = max(xLength, zLength)
  shortHorizontalLength = min(xLength, zLength)
  minimumDistance = shortHorizontalLength * c1 + (longHorizontalLength - shortHorizontalLength)
  cost = minimumDistance + yLength * heightCost
  return cost


def getStepCost(surface, node, neighbourNode):
  heightCost = 4
  waterCost = 4
  isWater = 0
  if (surface.surfaceMap[neighbourNode.x][neighbourNode.z].isWater):
    isWater = 1
  xLength = abs(neighbourNode.x - node.x)
  zLength = abs(neighbourNode.z - node.z)
  yLength = abs(neighbourNode.y - node.y)
  if (xLength + zLength == 2):
    return c2 + yLength * heightCost + isWater * waterCost
  elif (xLength + zLength == 1):
    return 1 + yLength * heightCost + isWater * waterCost
  else:
    print('this step should not happen')
    return 0


def getPointHeight(surface, x, z):
  return surface.surfaceMap[x][z].height

class Node:

  def __init__(self, surface, x, z, targetNode):
    self.x = x
    self.y = getPointHeight(surface, x, z)
    self.z = z
    self.gScore = float('inf')
    self.fScore = float('inf')
    self.cameFrom = None
    self.targetNode = targetNode
    if (targetNode == None):
      self.heuristicCostToTargetEstimate = 0
    else:
      self.heuristicCostToTargetEstimate = getEuclideanHeuristicCostEstimate(surface, self, targetNode)
  
  def isEqual(self, node):
    if (node == None):
      return False
    return (self.x == node.x and self.z == node.z)