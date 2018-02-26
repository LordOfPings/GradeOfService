import graph_tool.all as gt
from graph_tool import Graph

def creation(g,nodes):
    
    vList = g.add_vertex(nodes)
     ## Creating the USIP network ##

    '''
    e01 = g.add_edge(g.vertex_index[0], g.vertex_index[1])
    e04 = g.add_edge(g.vertex_index[0], g.vertex_index[4])
    e02 = g.add_edge(g.vertex_index[0], g.vertex_index[2])
    e12 = g.add_edge(g.vertex_index[1], g.vertex_index[2])
    e15 = g.add_edge(g.vertex_index[1], g.vertex_index[5])
    e16 = g.add_edge(g.vertex_index[1], g.vertex_index[6])
    e23 = g.add_edge(g.vertex_index[2], g.vertex_index[3])
    e27 = g.add_edge(g.vertex_index[2], g.vertex_index[7])
    e34 = g.add_edge(g.vertex_index[3], g.vertex_index[4])
    e37 = g.add_edge(g.vertex_index[3], g.vertex_index[7])
    e56 = g.add_edge(g.vertex_index[5], g.vertex_index[6])
    e67 = g.add_edge(g.vertex_index[6], g.vertex_index[7])
    e68 = g.add_edge(g.vertex_index[6], g.vertex_index[8])
    e69 = g.add_edge(g.vertex_index[6], g.vertex_index[9])
    e79 = g.add_edge(g.vertex_index[7], g.vertex_index[9])
    e710 = g.add_edge(g.vertex_index[7], g.vertex_index[10])
    e89 = g.add_edge(g.vertex_index[8], g.vertex_index[9])
    e812 = g.add_edge(g.vertex_index[8], g.vertex_index[12])
    e911 = g.add_edge(g.vertex_index[9], g.vertex_index[11])
    e912 = g.add_edge(g.vertex_index[9], g.vertex_index[12])
    e1013 = g.add_edge(g.vertex_index[10], g.vertex_index[13])
    e1112 = g.add_edge(g.vertex_index[11], g.vertex_index[12])
    e1113 = g.add_edge(g.vertex_index[11], g.vertex_index[13])
    e1214 = g.add_edge(g.vertex_index[12], g.vertex_index[14])
    e1215 = g.add_edge(g.vertex_index[12], g.vertex_index[15])
    e1315 = g.add_edge(g.vertex_index[13], g.vertex_index[15])
    e1316 = g.add_edge(g.vertex_index[13], g.vertex_index[16])
    e1418 = g.add_edge(g.vertex_index[14], g.vertex_index[18])
    e1517 = g.add_edge(g.vertex_index[15], g.vertex_index[17])
    e1518 = g.add_edge(g.vertex_index[15], g.vertex_index[18])
    e1519 = g.add_edge(g.vertex_index[15], g.vertex_index[19])
    e1617 = g.add_edge(g.vertex_index[16], g.vertex_index[17])
    e1720 = g.add_edge(g.vertex_index[17], g.vertex_index[20])
    e1819 = g.add_edge(g.vertex_index[18], g.vertex_index[19])
    e1920 = g.add_edge(g.vertex_index[19], g.vertex_index[20])


    e01 = g.add_edge(g.vertex_index[0], g.vertex_index[1])
    e02 = g.add_edge(g.vertex_index[0], g.vertex_index[2])
    e12 = g.add_edge(g.vertex_index[1], g.vertex_index[2])
    e13 = g.add_edge(g.vertex_index[1], g.vertex_index[3])
    e24 = g.add_edge(g.vertex_index[2], g.vertex_index[4])
    e34 = g.add_edge(g.vertex_index[3], g.vertex_index[4])
    e35 = g.add_edge(g.vertex_index[3], g.vertex_index[5])
    e45 = g.add_edge(g.vertex_index[4], g.vertex_index[5])

    '''
    
    e01 = g.add_edge(g.vertex_index[0], g.vertex_index[1])
    e12 = g.add_edge(g.vertex_index[1], g.vertex_index[2])
    e23 = g.add_edge(g.vertex_index[2], g.vertex_index[3])
    e03 = g.add_edge(g.vertex_index[0], g.vertex_index[3])

    e45 = g.add_edge(g.vertex_index[4], g.vertex_index[5])
    e56 = g.add_edge(g.vertex_index[5], g.vertex_index[6])
    e67 = g.add_edge(g.vertex_index[6], g.vertex_index[7])
    e47 = g.add_edge(g.vertex_index[4], g.vertex_index[7])

    e89 = g.add_edge(g.vertex_index[8], g.vertex_index[9])
    e910 = g.add_edge(g.vertex_index[9], g.vertex_index[10])
    e1011 = g.add_edge(g.vertex_index[10], g.vertex_index[11])
    e811 = g.add_edge(g.vertex_index[8], g.vertex_index[11])

    e1213 = g.add_edge(g.vertex_index[12], g.vertex_index[13])
    e1314 = g.add_edge(g.vertex_index[13], g.vertex_index[14])
    e1415 = g.add_edge(g.vertex_index[14], g.vertex_index[15])
    e1215 = g.add_edge(g.vertex_index[12], g.vertex_index[15])

    e04 = g.add_edge(g.vertex_index[0], g.vertex_index[4])
    e48 = g.add_edge(g.vertex_index[4], g.vertex_index[8])
    e812 = g.add_edge(g.vertex_index[8], g.vertex_index[12])
    e012 = g.add_edge(g.vertex_index[0], g.vertex_index[12])

    e15 = g.add_edge(g.vertex_index[1], g.vertex_index[5])
    e59 = g.add_edge(g.vertex_index[5], g.vertex_index[9])
    e913 = g.add_edge(g.vertex_index[9], g.vertex_index[13])
    e113 = g.add_edge(g.vertex_index[1], g.vertex_index[13])

    e26 = g.add_edge(g.vertex_index[2], g.vertex_index[6])
    e610 = g.add_edge(g.vertex_index[6], g.vertex_index[10])
    e1014 = g.add_edge(g.vertex_index[10], g.vertex_index[14])
    e214 = g.add_edge(g.vertex_index[2], g.vertex_index[14])

    e37 = g.add_edge(g.vertex_index[3], g.vertex_index[7])
    e711 = g.add_edge(g.vertex_index[7], g.vertex_index[11])
    e1115 = g.add_edge(g.vertex_index[11], g.vertex_index[15])
    e315 = g.add_edge(g.vertex_index[3], g.vertex_index[15])




