import graph_tool.all as gt
from graph_tool import Graph
from header import *
from math import *
from decimal import *

def onegrade_property(g):
    graph_weight = g.new_edge_property("float") #graph tool property for edges
    g.ep.weight_high = graph_weight             #adding a high priority weight
    graph_weight = g.new_edge_property("float") 
    g.ep.weight_primary = graph_weight              #adding a low priority weight
    graph_counter = g.new_edge_property("int")
    g.ep.counter_channels = graph_counter
    graph_pred_tree = g.new_vertex_property("int")  #graph tool for vertex property to know previous vertex (used for getting edges)
    pred_tree = graph_pred_tree                 #adding predecessor vertex of tree
    edge_flags = {}                           #various flags for edges
    available_wavelengths_high = {}
    available_wavelengths_low = {}
    available_wavelengths_alt = {}

    for e in g.edges():                         
        flags_of_edges = []
        flags_of_edges1 = []
        flags_of_edges2 = []
        flags_of_backup = []
        for i in range(int(number_wavelengths)):
            flags_of_edges.append(1)
            flags_of_edges1.append(1)
            flags_of_edges2.append(1)
        for i in range(int(number_wavelengths)):
            #flags_of_edges.append(1)
            flags_of_edges.append(1)
            flags_of_edges.append(1)
            flags_of_edges1.append(1)
            flags_of_edges2.append(1)
            flags_of_backup.append(1)
        edge_flags[str(e.source()) + " --> " + str(e.target())] = flags_of_edges
        available_wavelengths_high[str(e.source()) + " --> " + str(e.target())] = flags_of_edges1
        edge_flags[str(e.target()) + " --> " + str(e.source())] = flags_of_edges
        available_wavelengths_high[str(e.target()) + " --> " + str(e.source())] = flags_of_edges1
        available_wavelengths_alt[str(e.source()) + " --> " + str(e.target())] = flags_of_backup
        available_wavelengths_alt[str(e.target()) + " --> " + str(e.source())] = flags_of_backup
        available_wavelengths_low[str(e.source()) + " --> " + str(e.target())] = flags_of_edges2
        available_wavelengths_low[str(e.target()) + " --> " + str(e.source())] = flags_of_edges2

        g.ep.weight_primary[e] = 1
        g.ep.weight_high[e] = 1
        g.ep.counter_channels[e] = number_wavelengths

    return (available_wavelengths_low,available_wavelengths_alt,available_wavelengths_high,edge_flags,g.ep.weight_primary,g.ep.weight_high,g.ep.counter_channels)

def twograde_property(g):
    graph_weight = g.new_edge_property("float") #graph tool property for edges
    g.ep.weight_high = graph_weight             #adding a high priority weight
    graph_weight1 = g.new_edge_property("float") 
    g.ep.weight_low = graph_weight1         #adding a low priority weight   
    graph_counter = g.new_edge_property("int")
    g.ep.counter_high = graph_counter
    graph_counter2 = g.new_edge_property("int")
    g.ep.counter_low = graph_counter2
    graph_counter3 = g.new_edge_property("int")
    g.ep.counter_alt = graph_counter3

    graph_pred_tree = g.new_vertex_property("int")  #graph tool for vertex property to know previous vertex (used for getting edges)
    pred_tree = graph_pred_tree                 #adding predecessor vertex of tree
    edge_flags = {}                         #various flags for edges
    available_wavelengths = {}
    available_wavelengths_alt = {}
    channels_high = ceil(0.70*number_wavelengths)
    channels_low = floor(0.30*number_wavelengths)

    for e in g.edges():                         
        flags_of_edges = []
        flags_of_backup = []
        for i in range(number_wavelengths):
            flags_of_edges.append(1)
            flags_of_edges.append(1)
        for i in range(number_wavelengths):
            flags_of_edges.append(1)
            flags_of_backup.append(1)
        edge_flags[str(e.source()) + " --> " + str(e.target())] = flags_of_edges
        available_wavelengths[str(e.source()) + " --> " + str(e.target())] = flags_of_edges
        edge_flags[str(e.target()) + " --> " + str(e.source())] = flags_of_edges
        available_wavelengths[str(e.target()) + " --> " + str(e.source())] = flags_of_edges
        available_wavelengths_alt[str(e.source()) + " --> " + str(e.target())] = flags_of_backup
        available_wavelengths_alt[str(e.target()) + " --> " + str(e.source())] = flags_of_backup

        g.ep.weight_low[e] = 1
        g.ep.weight_high[e] = 1
        #g.ep.weight_temp[e] = 1
        g.ep.counter_high[e] = ceil(0.70*number_wavelengths)
        g.ep.counter_low[e] = floor(0.30*number_wavelengths)
        g.ep.counter_alt[e] = floor(0.30*number_wavelengths)
        
    return (available_wavelengths_alt,available_wavelengths,edge_flags,g.ep.weight_high,g.ep.weight_low,g.ep.counter_high,g.ep.counter_alt,channels_high,channels_low)

def threegrade_property(g):

    graph_weight = g.new_edge_property("float") #graph tool property for edges
    g.ep.weight_high = graph_weight             #adding a high priority weight
    graph_weight1 = g.new_edge_property("float") 
    g.ep.weight_low = graph_weight1         #adding a low priority weight
    graph_weight2 = g.new_edge_property("float")
    g.ep.weight_med = graph_weight2 
    graph_counter = g.new_edge_property("int")
    g.ep.counter_high = graph_counter
    graph_counter2 = g.new_edge_property("int")
    g.ep.counter_low = graph_counter2
    graph_counter4 = g.new_edge_property("int")
    g.ep.counter_med = graph_counter4
    graph_counter3 = g.new_edge_property("int")
    g.ep.counter_alt = graph_counter3
   
    graph_pred_tree = g.new_vertex_property("int")  #graph tool for vertex property to know previous vertex (used for getting edges)
    pred_tree = graph_pred_tree                 #adding predecessor vertex of tree
    edge_flags = {}                         #various flags for edges
    available_wavelengths = {}
    available_wavelengths_alt = {}
    channels_high = ceil(0.45*number_wavelengths)
    channels_med = ceil(0.25*number_wavelengths)
    channels_low = floor(0.30*number_wavelengths)

    for e in g.edges():                         
        flags_of_edges = []
        flags_of_backup = []
        for i in range(number_wavelengths):
            flags_of_edges.append(1)
            flags_of_edges.append(1)
        for i in range(number_wavelengths):
            flags_of_edges.append(1)
            flags_of_backup.append(1)
        edge_flags[str(e.source()) + " --> " + str(e.target())] = flags_of_edges
        available_wavelengths[str(e.source()) + " --> " + str(e.target())] = flags_of_edges
        edge_flags[str(e.target()) + " --> " + str(e.source())] = flags_of_edges
        available_wavelengths[str(e.target()) + " --> " + str(e.source())] = flags_of_edges
        available_wavelengths_alt[str(e.source()) + " --> " + str(e.target())] = flags_of_backup
        available_wavelengths_alt[str(e.target()) + " --> " + str(e.source())] = flags_of_backup

        g.ep.weight_low[e] = 1
        g.ep.weight_high[e] = 1
        g.ep.weight_med[e] = 1
        #g.ep.weight_temp[e] = 1
        g.ep.counter_high[e] = ceil(0.45*number_wavelengths)
        g.ep.counter_med[e] = ceil(0.25*number_wavelengths)
        g.ep.counter_low[e] = floor(0.30*number_wavelengths)
        g.ep.counter_alt[e] = floor(0.30 * number_wavelengths)
    return (available_wavelengths_alt,available_wavelengths,edge_flags,g.ep.weight_high,g.ep.weight_low,g.ep.weight_med,g.ep.counter_high,g.ep.counter_alt,g.ep.counter_med,channels_high,channels_low,channels_med)
