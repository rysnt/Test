def exhaustive(graph, startnode, endnode):
    maxdist = -1
    stack = [([startnode], 0)]
    while stack:
        cpath, cdist = stack.pop()
        cnode = cpath[-1]
        if cnode == endnode:
          if cdist > maxdist:
              maxdist = cdist
              maxpath = cpath
          continue
        for nbr, nbrdist in graph[cnode]:
            stack.append( (cpath+[nbr], nbrdist+cdist) )
    return maxdist, maxpath
def getGraph(startnode, listVertices, listEdge, tempVertices):
  for k,v in listVertices.items():
      for j in listEdge:
        if(k == j[0]):
          weight = 0
          for i in tempVertices:
            if(startnode == j[0] and i[0] == j[0]):
              weight += int(i[-1])
            if(j[-1] == i[0]):
              weight += int(i[-1])
          listVertices[k].append((j[-1], weight))
  return listVertices

def main():
    vertices = input("input n vertices: ")
    tempVertices = []
    for i in range(0,vertices):
      weight = raw_input("name and weight vertices: ")
      tempVertices.append(weight)
    listVertices = {}
    for i in tempVertices:
      listVertices[i[0]] = []
    edge = input("input m edge: ")
    listEdge = []
    for i in range(0,edge):
      edges = raw_input("input from and to edge with koma 'ex: A,B': ")
      listEdge.append(edges)
    startnode, endnode = raw_input("Enter start and endnode 'ex: A C': ").split()

    graph = getGraph(startnode, listVertices, listEdge, tempVertices)
    maxdist, maxpath = exhaustive(graph, startnode, endnode)
    print("Maxdist is %d, maxpath is %s" % (maxdist, maxpath))

if __name__ == "__main__":
    main()
