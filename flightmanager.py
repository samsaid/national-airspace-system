# this file calculates the maximum flow of the graph
import csv
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

flight_source_graph = {}      #source airports: departure times
flight_dest_graph = {}        #arrival airports: arrival times

with open('flights.csv') as csvfile:
  reader = csv.reader(csvfile, delimiter=',')
  next(reader, None)
  for row in reader:
    flight_source = row[0]
    flight_dep_time = row[2]
    
    flight_dest = row[1]
    flight_arr_time = row[3]
    flight_cap = row[4]

    #departure information
    if flight_source in flight_source_graph:
      flight_source_graph[flight_source].append((int(flight_dep_time),int(flight_arr_time),flight_dest,int(flight_cap)))
    else:
      flight_source_graph[flight_source] = [(int(flight_dep_time),int(flight_arr_time),flight_dest,int(flight_cap))]

from_verts = []
to_verts = []
  
  #   key = source airport
  #   i = departure time
  #   j = arrival time
  #   k = destination airport
  #   l = flight capacity 
  
  #python lists order of elements are preserved
capacity = []
for key,value in flight_source_graph.items():
  for i,j,k,l in value:
    from_verts.append((key,i))
    to_verts.append((k,j))
    capacity.append(l)
  
  df = pd.DataFrame(
    {'from': from_verts, 'to': to_verts,'capacity': capacity})
    
G = nx.MultiDiGraph()
G = nx.from_pandas_edgelist(df,source='from',target='to',edge_attr='capacity',create_using=nx.MultiDiGraph())
  
node_color=[]
for node in G.nodes(data=True):
  if 'LAX' in node[0]:
    node_color.append('green')  #source node
  elif 'JFK' in node[0]:
    node_color.append('red')    #sink node
  else:
    node_color.append('skyblue')   #internal nodes

#print(nx.get_edge_attributes(G,'capacity'))
#labels = {['capacity'] for e in G.edges}
edge_labels = nx.get_edge_attributes(G,'capacity')

#print(edge_labels)
p = nx.spring_layout(G, k=0.22, iterations=20)
#nx.draw_networkx_edge_labels(G,p,edge_labels=True,font_size=6)
     
nx.draw(G,
        with_labels=True,
        node_size=30,
        arrows=True,
        node_color=node_color,
        font_size=8,
        edge_color="black",
        width=0.8,          
        pos = p
        )
print(G.edges())
print("Number of edges:",len(G.edges()))
print("Number of nodes:",len(G.nodes()))

plt.show()
plt.savefig("filename.png",bbox_inches="tight")

def find_all_paths(graph, source, destination):
    path = path + [start]
    if start == end:
      return [path]
    if start not in graph:
      return []
    paths = []
    for key,value in flight_source_graph.items():
      for i,j,k,l in value:
        if key not in path:
          newpaths = find_all_paths(graph,key,end,path)
          for newpath in newpaths:
            paths.append(newpath)
    return paths


def ford_fulkerson(self):
  max_flow = 0  #initialize flow to 0
  for path in find_all_paths(graph,source,destination):
    new_p = []
    for j in range(1, len(path)):
      new_p.append()
      max_flow += new_p   
  return max_flow
  
  #calculate the bottleneck capacity
  cap = nx.get_edge_attributes(G,'capacity')
  (list(cap))
  for u,v in list(G.edges()):
    print(G[u][v].get('capacity'))

