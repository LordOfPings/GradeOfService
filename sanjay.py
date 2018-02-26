
import graph_tool.all as gt
from graph_tool import Graph
from random import randint

from AllConstants import *
from main import number_requests

#number_requests = 10

all_requests_with_primary_paths = {}
all_requests_with_alternative_paths = {}
all_requests_with_primary_frequency_channels = {}
all_requests_with_alternative_frequency_channels = {}
output = open(str(number_frequency_bands) + "_Channels_" + str(simulated_on_network) + "_Network_Blockings_log_Dijkstra.txt","a")

if simulated_on_network == 1:
    ## Network is USIP ##

    ## Creating the USIP network ##
    g = Graph(directed=False)
    vertices_set = g.add_vertex(24)
    '''
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
    e05 = g.add_edge(g.vertex_index[0], g.vertex_index[5])
    e12 = g.add_edge(g.vertex_index[1], g.vertex_index[2])
    e15 = g.add_edge(g.vertex_index[1], g.vertex_index[5])
    e23 = g.add_edge(g.vertex_index[2], g.vertex_index[3])
    e24 = g.add_edge(g.vertex_index[2], g.vertex_index[4])
    e26 = g.add_edge(g.vertex_index[2], g.vertex_index[6])
    e36 = g.add_edge(g.vertex_index[3], g.vertex_index[6])
    e34 = g.add_edge(g.vertex_index[3], g.vertex_index[4])
    e47 = g.add_edge(g.vertex_index[4], g.vertex_index[7])
    e56 = g.add_edge(g.vertex_index[5], g.vertex_index[6])
    e58 = g.add_edge(g.vertex_index[5], g.vertex_index[8])
    e510 = g.add_edge(g.vertex_index[5], g.vertex_index[10])
    e67 = g.add_edge(g.vertex_index[6], g.vertex_index[7])
    e68 = g.add_edge(g.vertex_index[6], g.vertex_index[8])
    e79 = g.add_edge(g.vertex_index[7], g.vertex_index[9])
    e89 = g.add_edge(g.vertex_index[8], g.vertex_index[9])
    e810 = g.add_edge(g.vertex_index[8], g.vertex_index[10])
    e811 = g.add_edge(g.vertex_index[8], g.vertex_index[11])
    e912 = g.add_edge(g.vertex_index[9], g.vertex_index[12])
    e913 = g.add_edge(g.vertex_index[9], g.vertex_index[13])
    e1011 = g.add_edge(g.vertex_index[10], g.vertex_index[11])
    e1014 = g.add_edge(g.vertex_index[10], g.vertex_index[14])
    e1018 = g.add_edge(g.vertex_index[10], g.vertex_index[18])
    e1112 = g.add_edge(g.vertex_index[11], g.vertex_index[12])
    e1115 = g.add_edge(g.vertex_index[11], g.vertex_index[15])
    e1213 = g.add_edge(g.vertex_index[12], g.vertex_index[13])
    e1216 = g.add_edge(g.vertex_index[12], g.vertex_index[16])
    e1317 = g.add_edge(g.vertex_index[13], g.vertex_index[17])
    e1415 = g.add_edge(g.vertex_index[14], g.vertex_index[15])
    e1419 = g.add_edge(g.vertex_index[14], g.vertex_index[19])
    e1516 = g.add_edge(g.vertex_index[15], g.vertex_index[16])
    e1520 = g.add_edge(g.vertex_index[15], g.vertex_index[20])
    e1521 = g.add_edge(g.vertex_index[15], g.vertex_index[21])
    e1617 = g.add_edge(g.vertex_index[16], g.vertex_index[17])
    e1621 = g.add_edge(g.vertex_index[16], g.vertex_index[21])
    e1622 = g.add_edge(g.vertex_index[16], g.vertex_index[22])
    e1723 = g.add_edge(g.vertex_index[17], g.vertex_index[23])
    e1819 = g.add_edge(g.vertex_index[18], g.vertex_index[19])
    e1920 = g.add_edge(g.vertex_index[19], g.vertex_index[20])
    e2021 = g.add_edge(g.vertex_index[20], g.vertex_index[21])
    e2122 = g.add_edge(g.vertex_index[21], g.vertex_index[22])
    e2223 = g.add_edge(g.vertex_index[22], g.vertex_index[23])


    ## Generating the requests ##
    all_requests = []
    for request_count in range(number_requests):
        request = []
        temp_source = randint(0,23)
        request.append(temp_source)
        while(1):
            temp_target = randint(0, 23)
            if(not(temp_target == temp_source)):
                request.append(temp_target)
                all_requests.append(request)
                break
        #if not(request in all_requests):
        #    all_requests.append(request)

    print("Number of requests are " + str(len(all_requests)))

elif simulated_on_network == 2:
    ## Network is USIP Backbone ##

    ## Creating the USIP Backbone ##
    g = Graph(directed=False)
    vertices_set = g.add_vertex(15)
    e01 = g.add_edge(g.vertex_index[0], g.vertex_index[1])
    e09 = g.add_edge(g.vertex_index[0], g.vertex_index[9])
    e010 = g.add_edge(g.vertex_index[0], g.vertex_index[1])
    e12 = g.add_edge(g.vertex_index[1], g.vertex_index[2])
    e111 = g.add_edge(g.vertex_index[1], g.vertex_index[11])
    e23 = g.add_edge(g.vertex_index[2], g.vertex_index[3])
    e211 = g.add_edge(g.vertex_index[2], g.vertex_index[11])
    e312 = g.add_edge(g.vertex_index[3], g.vertex_index[12])
    e34 = g.add_edge(g.vertex_index[3], g.vertex_index[4])
    e910 = g.add_edge(g.vertex_index[9], g.vertex_index[10])
    e98 = g.add_edge(g.vertex_index[9], g.vertex_index[8])
    e1011 = g.add_edge(g.vertex_index[10], g.vertex_index[11])
    e1112 = g.add_edge(g.vertex_index[11], g.vertex_index[12])
    e1114 = g.add_edge(g.vertex_index[11], g.vertex_index[14])
    e1214 = g.add_edge(g.vertex_index[12], g.vertex_index[14])
    e124 = g.add_edge(g.vertex_index[12], g.vertex_index[4])
    e413 = g.add_edge(g.vertex_index[4], g.vertex_index[13])
    e1314 = g.add_edge(g.vertex_index[13], g.vertex_index[14])
    e45 = g.add_edge(g.vertex_index[4], g.vertex_index[5])
    e135 = g.add_edge(g.vertex_index[13], g.vertex_index[5])
    e136 = g.add_edge(g.vertex_index[13], g.vertex_index[6])
    e65 = g.add_edge(g.vertex_index[6], g.vertex_index[5])
    e146 = g.add_edge(g.vertex_index[14], g.vertex_index[6])
    e714 = g.add_edge(g.vertex_index[7], g.vertex_index[14])
    e76 = g.add_edge(g.vertex_index[7], g.vertex_index[6])
    e87 = g.add_edge(g.vertex_index[8], g.vertex_index[7])

    ## Generating the requests ##
    all_requests = []
    for request_count in range(number_requests):
        request = []
        temp_source = randint(0,14)
        request.append(temp_source)
        while(1):
            temp_target = randint(0, 14)
            if(not(temp_target == temp_source)):
                request.append(temp_target)
                break
        if not(request in all_requests):
            all_requests.append(request)

    #print("Number of requests are " + str(len(all_requests)))

elif simulated_on_network == 3:

    ## Network is having 19 nodes ##

    ## Creating the 19 Node network ##
    g = Graph(directed=False)
    vertices_set = g.add_vertex(19)

    e01 = g.add_edge(g.vertex_index[0], g.vertex_index[1])
    e02 = g.add_edge(g.vertex_index[0], g.vertex_index[2])
    e05 = g.add_edge(g.vertex_index[0], g.vertex_index[5])
    e12 = g.add_edge(g.vertex_index[1], g.vertex_index[2])
    e13 = g.add_edge(g.vertex_index[1], g.vertex_index[3])
    e16 = g.add_edge(g.vertex_index[1], g.vertex_index[6])
    e54 = g.add_edge(g.vertex_index[5], g.vertex_index[4])
    e56 = g.add_edge(g.vertex_index[5], g.vertex_index[6])
    e27 = g.add_edge(g.vertex_index[2], g.vertex_index[7])
    e63 = g.add_edge(g.vertex_index[6], g.vertex_index[3])
    e67 = g.add_edge(g.vertex_index[6], g.vertex_index[7])
    e57 = g.add_edge(g.vertex_index[5], g.vertex_index[7])
    e512 = g.add_edge(g.vertex_index[5], g.vertex_index[12])
    e912 = g.add_edge(g.vertex_index[9], g.vertex_index[12])
    e97 = g.add_edge(g.vertex_index[9], g.vertex_index[7])
    e910 = g.add_edge(g.vertex_index[9], g.vertex_index[10])
    e514 = g.add_edge(g.vertex_index[5], g.vertex_index[14])
    e412 = g.add_edge(g.vertex_index[4], g.vertex_index[12])
    e68 = g.add_edge(g.vertex_index[6], g.vertex_index[8])
    e611 = g.add_edge(g.vertex_index[6], g.vertex_index[11])
    e710 = g.add_edge(g.vertex_index[7], g.vertex_index[10])
    e711 = g.add_edge(g.vertex_index[7], g.vertex_index[11])
    e616 = g.add_edge(g.vertex_index[6], g.vertex_index[16])
    e1011 = g.add_edge(g.vertex_index[10], g.vertex_index[11])
    e817 = g.add_edge(g.vertex_index[8], g.vertex_index[17])
    e1617 = g.add_edge(g.vertex_index[16], g.vertex_index[17])
    e916 = g.add_edge(g.vertex_index[9], g.vertex_index[16])
    e1718 = g.add_edge(g.vertex_index[17], g.vertex_index[18])
    e1618 = g.add_edge(g.vertex_index[16], g.vertex_index[18])
    e1215 = g.add_edge(g.vertex_index[12], g.vertex_index[15])
    e1116 = g.add_edge(g.vertex_index[11], g.vertex_index[16])
    e1016 = g.add_edge(g.vertex_index[10], g.vertex_index[16])

    ## Generating the requests ##
    all_requests = []
    for request_count in range(number_requests):
        request = []
        temp_source = randint(0,18)
        request.append(temp_source)
        while(1):
            temp_target = randint(0, 18)
            if(not(temp_target == temp_source)):
                request.append(temp_target)
                break
        if not(request in all_requests):
            all_requests.append(request)

    #print("Number of requests are " + str(len(all_requests)))

elif simulated_on_network == 4:

    ## Network is having 10 nodes ##

    ## Creating the 10 Node network ##
    g = Graph(directed=False)
    vertices_set = g.add_vertex(10)

    e01 = g.add_edge(g.vertex_index[0], g.vertex_index[1])
    e02 = g.add_edge(g.vertex_index[0], g.vertex_index[2])
    e03 = g.add_edge(g.vertex_index[0], g.vertex_index[3])
    e14 = g.add_edge(g.vertex_index[1], g.vertex_index[4])
    e13 = g.add_edge(g.vertex_index[1], g.vertex_index[3])
    e15 = g.add_edge(g.vertex_index[1], g.vertex_index[5])
    e23 = g.add_edge(g.vertex_index[2], g.vertex_index[3])
    e26 = g.add_edge(g.vertex_index[2], g.vertex_index[6])
    e28 = g.add_edge(g.vertex_index[2], g.vertex_index[8])
    e36 = g.add_edge(g.vertex_index[3], g.vertex_index[6])
    e37 = g.add_edge(g.vertex_index[3], g.vertex_index[7])
    e34 = g.add_edge(g.vertex_index[3], g.vertex_index[4])
    e47 = g.add_edge(g.vertex_index[4], g.vertex_index[7])
    e45 = g.add_edge(g.vertex_index[4], g.vertex_index[5])
    e57 = g.add_edge(g.vertex_index[5], g.vertex_index[7])
    e59 = g.add_edge(g.vertex_index[5], g.vertex_index[9])
    e67 = g.add_edge(g.vertex_index[6], g.vertex_index[7])
    e46 = g.add_edge(g.vertex_index[4], g.vertex_index[6])
    e68 = g.add_edge(g.vertex_index[6], g.vertex_index[8])
    e78 = g.add_edge(g.vertex_index[7], g.vertex_index[8])
    e79 = g.add_edge(g.vertex_index[7], g.vertex_index[9])
    e89 = g.add_edge(g.vertex_index[8], g.vertex_index[9])

    ## Generating the requests ##
    all_requests = []
    for request_count in range(number_requests):
        request = []
        temp_source = randint(0,9)
        request.append(temp_source)
        while(1):
            temp_target = randint(0, 9)
            if(not(temp_target == temp_source)):
                request.append(temp_target)
                break
        if not(request in all_requests):
            all_requests.append(request)

    #print("Number of requests are " + str(len(all_requests)))

elif simulated_on_network == 5:

    ## Network is having 14 nodes ##

    ## Creating the 14 Node network ##
    g = Graph(directed=False)
    vertices_set = g.add_vertex(14)

    e01 = g.add_edge(g.vertex_index[0], g.vertex_index[1])
    e03 = g.add_edge(g.vertex_index[0], g.vertex_index[3])
    e02 = g.add_edge(g.vertex_index[0], g.vertex_index[2])
    e17 = g.add_edge(g.vertex_index[1], g.vertex_index[7])
    e12 = g.add_edge(g.vertex_index[1], g.vertex_index[2])
    e25 = g.add_edge(g.vertex_index[2], g.vertex_index[5])
    e34 = g.add_edge(g.vertex_index[3], g.vertex_index[4])
    e45 = g.add_edge(g.vertex_index[4], g.vertex_index[5])
    e46 = g.add_edge(g.vertex_index[4], g.vertex_index[6])
    e67 = g.add_edge(g.vertex_index[6], g.vertex_index[7])
    e710 = g.add_edge(g.vertex_index[7], g.vertex_index[10])
    e78 = g.add_edge(g.vertex_index[7], g.vertex_index[8])
    e1011 = g.add_edge(g.vertex_index[10], g.vertex_index[11])
    e1013 = g.add_edge(g.vertex_index[10], g.vertex_index[13])
    e811 = g.add_edge(g.vertex_index[8], g.vertex_index[11])
    e59 = g.add_edge(g.vertex_index[5], g.vertex_index[9])
    e512 = g.add_edge(g.vertex_index[5], g.vertex_index[12])
    e89 = g.add_edge(g.vertex_index[8], g.vertex_index[9])
    e1112 = g.add_edge(g.vertex_index[11], g.vertex_index[12])
    e1113 = g.add_edge(g.vertex_index[11], g.vertex_index[13])
    e1213 = g.add_edge(g.vertex_index[12], g.vertex_index[13])

    ## Generating the requests ##
    all_requests = []
    for request_count in range(number_requests):
        request = []
        temp_source = randint(0,13)
        request.append(temp_source)
        while(1):
            temp_target = randint(0, 13)
            if(not(temp_target == temp_source)):
                request.append(temp_target)
                break
        if not(request in all_requests):
            all_requests.append(request)

    #print("Number of requests are " + str(len(all_requests)))

## Defining the graph properties ##
graph_weight = g.new_edge_property("float")
g.ep.weight = graph_weight

graph_pred_tree = g.new_vertex_property("int")
pred_tree = graph_pred_tree

edges_logger = {}

for e in g.edges():
    flags_of_edges = []
    # Temporary flag to ensure that alternative path is not on the primary path itself
    flags_of_edges.append(1)
    # Flags to see which channels are currently in use
    for i in range(number_frequency_bands):
        flags_of_edges.append(1)
    # Flags to keep record of the extent of the usage of a particular channel in a link
    for i in range(number_frequency_bands):
        flags_of_edges.append(0)
    # Flags to fulfil the single point failure protection between those who share their primary paths
    for i in range(number_frequency_bands):
        flags_of_edges.append(1)
    edges_logger[str(e.source()) + " --> " + str(e.target())] = flags_of_edges
    edges_logger[str(e.target()) + " --> " + str(e.source())] = flags_of_edges
    g.ep.weight[e] = 0

gt.graph_draw(g, vertex_text=g.vertex_index, vertex_font_size=12, vertex_shape="double_circle",vertex_fill_color="#729fcf", vertex_pen_width=3,edge_pen_width=1, output="USIP_Dijkstra.pdf")
time = g.new_vertex_property("int")

#file to write the path from dijkastra
file = open("All_Paths_From_RWA_DIJKASTRA.txt", "w+")

for request in all_requests:

    can_go_to_find_backup = 0

    for e in g.edges():
        edges_logger[str(e.source()) + " --> " + str(e.target())][0] = 1
        edges_logger[str(e.target()) + " --> " + str(e.source())][0] = 1

    request_key = str(request[0]) + " --> " + str(request[1])

    print("Request is " + request_key)

    #file.write("Requested source and destination" + str(request_key)+ "\n")

    rev_path = []
    src = g.vertex(request[0])
    tgt = g.vertex(request[1])
    tracer = request[1]
    dist, pred = gt.dijkstra_search(g, src, g.ep.weight)
    g.vp.pred_tree = pred
    ##print pred.a
    ##print g.vp.pred_tree.a

    while g.vertex(tracer) != src:
        rev_path.append(tracer)
        ##print(tracer)
        temp = tracer
        tracer = g.vp.pred_tree[g.vertex(tracer)]
        if temp == tracer:
            rev_path = []
            break

    if len(rev_path) == 0:

        print("F1")

        all_requests_with_primary_paths[request_key] = "Blocked"
        all_requests_with_alternative_paths[request_key] = "Blocked"
        all_requests_with_primary_frequency_channels[request_key] = -1
        all_requests_with_alternative_frequency_channels[request_key] = -1

    else:

        print("F2")
        
        disjointer_via_weight = 0 

        primary_path = []
        primary_path.append(request[0])
        for i in range(len(rev_path) - 1, -1, -1):
            primary_path.append(rev_path[i])

        print "Candidate primary path " + str(primary_path)

        channel_availability = []
        for i in range(number_frequency_bands):
            channel_availability.append(1)

        for i in range(len(primary_path) - 1):
            for j in range(number_frequency_bands):
                channel_availability[j] = channel_availability[j] & edges_logger[str(primary_path[i]) + " --> " + str(primary_path[i + 1])][j + 1]

        for i in range(number_frequency_bands):
            if channel_availability[i] == 1:
                can_go_to_find_backup = 1
                primary_channel = i
                for j in range(len(primary_path) - 1):
                    
                    if len(primary_path) > 6:
                        disjointer_via_weight = 50 - len(primary_path)
                    else:
                        disjointer_via_weight = 1
                    
                    ### If at a later stage in this iteration, the primary path has to be discarded, then the following step has to be reverted as well ###

                    # The primary weights have been increased, though they are not been assigned yet, as we want the backup path to be different from the primary path
                    g.ep.weight[primary_path[j], primary_path[j + 1]] += disjointer_via_weight

                    # Reset the temporary flag
                    edges_logger[str(primary_path[j]) + " --> " + str(primary_path[j + 1])][0] = 0
                    edges_logger[str(primary_path[j + 1]) + " --> " + str(primary_path[j])][0] = 0

                break

        if can_go_to_find_backup == 1:

            print "Candidate primary channel " + str(primary_channel)

            # Set all the non-disjoint flagsoo
            for e in g.edges():
                for j in range(number_frequency_bands):
                    edges_logger[str(e.source()) + " --> " + str(e.target())][j + 1 + (2 * number_frequency_bands)] = 1
                    edges_logger[str(e.target()) + " --> " + str(e.source())][j + 1 + (2 * number_frequency_bands)] = 1

            print("F3")

            non_disjoint = []

            for key in all_requests_with_primary_paths.keys():
                break_flag = 0
                temp_path = all_requests_with_primary_paths[key]
                for i in range(len(primary_path) - 1):
                    for j in range(len(temp_path) - 1):
                        if primary_path[i] == temp_path[j] and primary_path[i + 1] == temp_path[j + 1]:
                            non_disjoint.append(key)
                            break_flag = 1
                            break
                    if break_flag == 1:
                        break

            ##print request_key + "\n" + str(non_disjoint) + "\n"

            for i in range(len(non_disjoint)):
                temp_path = all_requests_with_alternative_paths[non_disjoint[i]]
                temp_channel = all_requests_with_alternative_frequency_channels[non_disjoint[i]]
                for j in range(len(temp_path) - 1):
                    edges_logger[str(temp_path[j]) + " --> " + str(temp_path[j + 1])][temp_channel + 1 + (2 * number_frequency_bands)] = 0
                    edges_logger[str(temp_path[j + 1]) + " --> " + str(temp_path[j])][temp_channel + 1 + (2 * number_frequency_bands)] = 0

            secondary_path = []
            rev_path = []
            tracer = request[1]
            dist, pred = gt.dijkstra_search(g, src, g.ep.weight)
            g.vp.pred_tree = pred

            while g.vertex(tracer) != src:
                rev_path.append(tracer)
                temp = tracer
                tracer = g.vp.pred_tree[g.vertex(tracer)]
                if temp == tracer:
                    rev_path = []
                    break

            if len(rev_path) == 0:

                print("F4")


                all_requests_with_primary_paths[request_key] = "Blocked"
                all_requests_with_alternative_paths[request_key] = "Blocked"
                all_requests_with_alternative_frequency_channels[request_key] = -1
                all_requests_with_primary_frequency_channels[request_key] = -1

                g.ep.weight[primary_path[j], primary_path[j + 1]] -= disjointer_via_weight

            else:

                print("F5")

                secondary_path = []
                secondary_path.append(request[0])
                for i in range(len(rev_path) - 1, -1, -1):
                    secondary_path.append(rev_path[i])

                print "Candidate secondary path " + str(secondary_path)

                for j in range(len(primary_path) - 1):
                    g.ep.weight[primary_path[j], primary_path[j + 1]] -= disjointer_via_weight

                channel_availability = []
                for i in range(number_frequency_bands):
                    channel_availability.append(1)

                #print channel_availability

                for i in range(len(secondary_path) - 1):
                    for j in range(number_frequency_bands):
                        #print str(channel_availability[j]) + str(edges_logger[str(secondary_path[i]) + " --> " + str(secondary_path[i + 1])][j + 1 + (2 * number_frequency_bands)]) + str(edges_logger[str(secondary_path[i]) + " --> " + str(secondary_path[i + 1])][0])
                        channel_availability[j] = channel_availability[j] & edges_logger[str(secondary_path[i]) + " --> " + str(secondary_path[i + 1])][j + 1 + (2 * number_frequency_bands)] & edges_logger[str(secondary_path[i]) + " --> " + str(secondary_path[i + 1])][0]

                #print channel_availability

                number_of_available_channels_for_backup = 0
                for i in range(number_frequency_bands):
                    if channel_availability[i] == 1:
                        number_of_available_channels_for_backup += 1
                        max_utilization_channel = i

                if number_of_available_channels_for_backup == 0:

                    print("F6")

                    all_requests_with_primary_paths[request_key] = "Blocked"
                    all_requests_with_alternative_paths[request_key] = "Blocked"
                    all_requests_with_alternative_frequency_channels[request_key] = -1
                    all_requests_with_primary_frequency_channels[request_key] = -1

                elif number_of_available_channels_for_backup == 1:

                    print("F7")

                    for i in range(len(primary_path) - 1):
                        edges_logger[str(primary_path[i]) + " --> " + str(primary_path[i + 1])][primary_channel + 1] = 0
                        edges_logger[str(primary_path[i + 1]) + " --> " + str(primary_path[i])][primary_channel + 1] = 0
                        g.ep.weight[primary_path[i], primary_path[i + 1]] += 1

                    for i in range(len(secondary_path) - 1):
                        edges_logger[str(secondary_path[i]) + " --> " + str(secondary_path[i + 1])][1 + number_frequency_bands + max_utilization_channel] += 1
                        edges_logger[str(secondary_path[i + 1]) + " --> " + str(secondary_path[i])][1 + number_frequency_bands + max_utilization_channel] += 1
                        edges_logger[str(secondary_path[i]) + " --> " + str(secondary_path[i + 1])][max_utilization_channel + 1] = 0
                        edges_logger[str(secondary_path[i + 1]) + " --> " + str(secondary_path[i])][max_utilization_channel + 1] = 0


                    all_requests_with_alternative_paths[request_key] = secondary_path
                    all_requests_with_primary_paths[request_key] = primary_path
                    all_requests_with_primary_frequency_channels[request_key] = primary_channel
                    all_requests_with_alternative_frequency_channels[request_key] = max_utilization_channel

                    print "Candidate secondary channel " + str(max_utilization_channel)

                    print "Allocated the resources finally"
                    print primary_path
                    print primary_channel
                    print secondary_path
                    print max_utilization_channel

                else:

                    print("F8")

                    sharing_index = -1
                    for j in range(number_frequency_bands):
                        temp_sharing_index = -1
                        for i in range(len(secondary_path) - 1):
                            if edges_logger[str(secondary_path[i]) + " --> " + str(secondary_path[i + 1])][j + number_frequency_bands + 1] > 0:
                                temp_sharing_index += 1
                        if temp_sharing_index > sharing_index:
                            max_utilization_channel = j
                            sharing_index = temp_sharing_index

                    for i in range(len(primary_path) - 1):
                        edges_logger[str(primary_path[i]) + " --> " + str(primary_path[i + 1])][primary_channel + 1] = 0
                        edges_logger[str(primary_path[i + 1]) + " --> " + str(primary_path[i])][primary_channel + 1] = 0
                        g.ep.weight[primary_path[i], primary_path[i + 1]] += 1

                    for i in range(len(secondary_path) - 1):
                        edges_logger[str(secondary_path[i]) + " --> " + str(secondary_path[i + 1])][1 + number_frequency_bands + max_utilization_channel] += 1
                        edges_logger[str(secondary_path[i + 1]) + " --> " + str(secondary_path[i])][1 + number_frequency_bands + max_utilization_channel] += 1
                        edges_logger[str(secondary_path[i]) + " --> " + str(secondary_path[i + 1])][max_utilization_channel + 1] = 0
                        edges_logger[str(secondary_path[i + 1]) + " --> " + str(secondary_path[i])][max_utilization_channel + 1] = 0

                    all_requests_with_alternative_paths[request_key] = secondary_path
                    all_requests_with_primary_paths[request_key] = primary_path
                    all_requests_with_primary_frequency_channels[request_key] = primary_channel
                    all_requests_with_alternative_frequency_channels[request_key] = max_utilization_channel

                    print "Candidate secondary channel " + str(max_utilization_channel)

                    print "Allocated the resources finally"
                    print primary_path
                    print primary_channel
                    print secondary_path
                    print max_utilization_channel


        else:

            print("F9")

            all_requests_with_primary_paths[request_key] = "Blocked"
            all_requests_with_alternative_paths[request_key] = "Blocked"
            all_requests_with_alternative_frequency_channels[request_key] = -1
            all_requests_with_primary_frequency_channels[request_key] = -1

        #print(primary_path)

        '''
        file.write("\n")
        for all_elements in range(len(primary_path)-1):
            file.write(str(primary_path[all_elements]))
            file.write(" --> ")
        file.write(str(primary_path[len(primary_path)-1]) + "\n")
        '''

resources_used_as_primary = 0
for key in all_requests_with_primary_paths.keys():
    temp_pp =  all_requests_with_primary_paths[key]
    if not temp_pp == "Blocked":
        resources_used_as_primary += (len(temp_pp) - 1)

number_blocked_requests = 0
for key in all_requests_with_alternative_paths.keys():
    if all_requests_with_primary_paths[key] == "Blocked" or all_requests_with_alternative_paths[key] == "Blocked":
        number_blocked_requests += 1

total_resources = 0
total_used_resources = 0
total_resources_shared = 0

for e in g.edges():
    for channel_iterator in range(number_frequency_bands):
        total_resources += 1
        if edges_logger[str(e.source()) + " --> " + str(e.target())][1 + number_frequency_bands + channel_iterator] > 0:
            total_used_resources += 1
            total_resources_shared += edges_logger[str(e.source()) + " --> " + str(e.target())][1 + number_frequency_bands + channel_iterator]

output.write(str(number_requests) + "\n" + str((number_blocked_requests * number_requests)/len(all_requests_with_primary_paths)) + "\n" + str(total_resources) + "\n" + str(total_used_resources) + "\n" + str(total_resources_shared) + "\n" + str(resources_used_as_primary) + "\n")

output.close()
#print("Number of blocked requests " + str(number_blocked_requests))
#print("All primary paths are " + str(len(all_requests_with_primary_paths)) + str(all_requests_with_primary_paths))
#print("All primary channels are " + str(len(all_requests_with_primary_frequency_channels)) + str(all_requests_with_primary_frequency_channels))
#print("All alternative paths are " + str(len(all_requests_with_alternative_paths))+ str(all_requests_with_alternative_paths))
#print("All alternative channels are " + str(len(all_requests_with_alternative_frequency_channels))+ str(all_requests_with_alternative_frequency_channels))

for key in all_requests_with_primary_paths.keys():
    all_paths = all_requests_with_primary_paths[key]
    file.write("Request source and destination pair "+ key+ "\n")
    file.write("Path given to the request: \t")
    if all_paths == "Blocked":
        file.write("Blocked \n")
    else :
        for each_path in range(len(all_paths)-1):
            file.write(str(all_paths[each_path]))
            file.write(str(" --> "))
        file.write(str(all_paths[len(all_paths) - 1]) + "\n")
    file.write("Channel allocated to the request: \t" + str(all_requests_with_primary_frequency_channels[key])  + "\n")


    all_paths = all_requests_with_alternative_paths[key]
    file.write("Alternative path given to the request: \t")
    if all_paths == "Blocked":
        file.write("Blocked \n")
    else :
        for each_path in range(len(all_paths)-1):
            file.write(str(all_paths[each_path]))
            file.write(str(" --> "))
        file.write(str(all_paths[len(all_paths) - 1]) + "\n")
    file.write("Channel allocated to the alternative path : \t" + str(all_requests_with_alternative_frequency_channels[key])  + "\n\n")
file.write("\n")



file.close()