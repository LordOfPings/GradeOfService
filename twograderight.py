import graph_tool.all as gt
from graph_tool import Graph
from random import randint

from math import *
from decimal import *
from header import *
import topology
from genrequests import generate
from graphproperty import twograde_property
from outputs import twograde_output

primary_paths_high_all = {}
primary_channels_high_all = {}
backup_paths_all = {}
backup_channels_all = {}
primary_paths_low_all = {}
primary_channels_low_all = {}
channels_all = {}
keylist_temp = []
# channel_key = []
op = open("twograde", "a")

if number_wavelengths > 1:  # for simulation
    ## Network is USIP ##

    ## Creating the USIP network ##
    g = Graph(directed=False)
    topology.creation(g, 21)

    ## Generating the requests ##
    request, all_requests = generate()
# print request

## Defining the graph properties ##
available_wavelengths_alt, available_wavelengths, edge_flags, g.ep.weight_high, g.ep.weight_low, g.ep.counter_high, g.ep.counter_alt, channels_high, channels_low = twograde_property(
    g)
# print("counter"+str(g.ep.counter_low[e]))

gt.graph_draw(g, vertex_text=g.vertex_index, vertex_font_size=12, vertex_shape="double_circle",
              vertex_fill_color="#55cc22", vertex_pen_width=3, edge_pen_width=1, output="topology.pdf")
time = g.new_vertex_property("int")
# print("Edge logger"+str(edge_flags))
# refresh_counter = 0

# Backup Path

def simulate(type):
    count1 = 0
    iter = 0
    if type == 50:
        keylist = []
        global keylist_temp
        pathlist = []
        templist = []
        for key in primary_paths_high_all.keys():
            #print "in (1)"
            templist.append(primary_paths_high_all[key])
            #print iter
            #print templist[iter]
            if templist[iter] != "Blocked":
                keylist.append(key)
                keylist_temp.append(key)
                pathlist.append(primary_paths_high_all[key])
                count1 +=1
                if(count1 == 5):
                    print("count is(1): " +str(count1))
                    break
            iter += 1
        iter += 1
        for key in primary_paths_low_all.keys():
            #print "in (2)"
            templist.append(primary_paths_low_all[key])
            #print iter
            #print templist[iter]
            if templist[iter] != "Blocked":
                keylist.append(key)
                pathlist.append(primary_paths_low_all[key])
                count1 +=1
                if(count1 == 10):
                    print("count is(2): " + str(count1))
                    break
            iter += 1
        #print "debug"
        print keylist
        print pathlist
        for i in range (10):
            if i<5:
                count_intrrupted = 0
                iter = 0
                requestlist = []
                requestdict = {}
                backup_path = backup_paths_all[keylist[i]]
                print("high priority backup path is : " +str(backup_path))
                backup_channel = backup_paths_all[keylist[i]][-1]
                print("high priority backup channel is : " +str(backup_channel))
                for j in range (len(backup_path)-2):
                    channel_key = str(backup_path[j]) + " --> " + str(backup_path[j+1]) + " " +str(backup_channel)
                    print channel_key
                    #print channels_all.get(channel_key,"none")
                    requestlist.append(channels_all.get(channel_key,"none"))
                    print requestlist
                    if requestlist[iter] != "none":
                        requestdict[requestlist[iter]] = "present"
                    iter += 1
                print requestdict
                for key in requestdict.values():
                    if key == "present":
                        count_intrrupted += 1
                print "intrrupted light paths count : "
                print count_intrrupted

            if i>= 5:
                path = primary_paths_low_all[keylist[i]]
                print("low priority primary path is :" +str(path))
                primary_channel = primary_paths_low_all[keylist[i]][-1]
                print("low priority primary channel(to be freed) is : " +str(primary_channel))
                for j in range (len(path)-2):
                    edge_flags[str(path[j]) + " --> " + str(path[j + 1])][primary_channel] = 1
                    #print edge_flags[str(path[j]) + " --> " + str(path[j + 1])]
                    g.ep.counter_low[path[j], path[j + 1]] += 1
    if type == 80:
        print keylist_temp
        for i in range(5):
            path = primary_paths_high_all[keylist_temp[i]]
            print("high pririty failed path is :" +str(path))
            primary_channel = primary_paths_high_all[keylist_temp[i]][-1]
            print("high priority failed primary channel(to be freed) is : " +str(primary_channel))
            backup_path = backup_paths_all[keylist_temp[i]]
            print("high priority backup_path is : " +str(backup_path))
            backup_channel = backup_paths_all[keylist_temp[i]][-1]
            print("high priority backup_channel(to be freed) is : " +str(backup_channel))
            for j in range (len(path)-2):
                edge_flags[str(path[j]) + " --> " + str(path[j + 1])][primary_channel] = 1
                #print edge_flags[str(path[j]) + " --> " + str(path[j + 1])]
                g.ep.counter_high[path[j], path[j + 1]] += 1
            #print "backup"

            for j in range(len(backup_path)-2):
                edge_flags[str(backup_path[j]) + " --> " + str(backup_path[j + 1])][backup_channel + number_wavelengths] = 1
                #print edge_flags[str(backup_path[j]) + " --> " + str(backup_path[j + 1])]
                g.ep.counter_alt[backup_path[j], backup_path[j + 1]] += 1
        #keylist_temp = []














def BackupPath(src, tgt, primary_path, request, request_key):
    # print("source"+ str(src) + "dest "+str(tgt)+" path: "+str(primary_path)+ " request"+str(request) )
    graph_weight = g.new_edge_property("float")  # graph tool property for edges
    g.ep.weight_alt = graph_weight  # adding a temporary weight
    for e in g.edges():
        g.ep.weight_alt[e] = 1
    for i in range(len(primary_path) - 1):
        g.ep.weight_alt[primary_path[i], primary_path[i + 1]] = 9999
    # tmp=1
    # print("pred"+str(i))
    path_count = 0
    while True:
        path_count += 1
        rev_path = []
        destination_node = request[1]
        dist, pred = gt.dijkstra_search(g, src, g.ep.weight_alt)
        g.vp.pred_tree = pred
        while g.vertex(destination_node) != src:
            # print(destination_node)
            rev_path.append(destination_node)
            temp = destination_node
            destination_node = g.vp.pred_tree[g.vertex(destination_node)]
            # print("dest:"+str(destination_node))
            # print("temp:"+str(temp))
            if temp == destination_node:
                rev_path = []
            # break

        tmp = 1
        temp_value = 1
        if len(rev_path) == 0:
            backup_paths_all[request_key] = "Blocked"
        else:
            path = []
        path.append(request[0])
        for i in range(len(rev_path) - 1, -1, -1):
            path.append(rev_path[i])
        print("backup path searched: " + str(path) + "cost of path found is : " + str(dist[tgt]))
        # temp_value = 0
        channel_available = []
        for i in range(int(number_wavelengths)):
            channel_available.append(1)
        if dist[tgt] < 9999:
            for i in range(len(path) - 1):
                # print("counter alt: "+str(g.ep.counter_alt[path[i],path[i+1]]))
                if g.ep.counter_alt[path[i], path[i + 1]] > 0:
                    print("traversing edge: " + str(path[i]) + " --> " + str(path[i + 1]))
                    for j in range(int(channels_high), number_wavelengths):
                        #print("Channel " + str(j) + "\t" + str(edge_flags[str(path[i]) + " --> " + str(path[i + 1])][j + number_wavelengths]))
                        available_wavelengths_alt[str(path[i]) + " --> " + str(path[i + 1])][j] = \
                        available_wavelengths_alt[str(path[i]) + " --> " + str(path[i + 1])][j] & \
                        edge_flags[str(path[i]) + " --> " + str(path[i + 1])][j + number_wavelengths]
                        channel_available[j] = channel_available[j] & \
                                               available_wavelengths_alt[str(path[i]) + " --> " + str(path[i + 1])][j]
                else:
                    print("traversing edge: " + str(path[i]) + " --> " + str(path[i + 1]))
                    print("no channel available ")
                    temp_value = 0
                    g.ep.weight_alt[path[i], path[i + 1]] = 9999
                    # print "weight alt " +str(g.ep.weight_alt[path[i],path[i+1]])
                    break  # find another backup path
            if temp_value == 1:
                for j in range(int(channels_high), number_wavelengths):
                    if channel_available[j] == 1:
                        print("backup path allocated : " + str(path))
                        tmp = 0
                        for i in range(len(path) - 1):
                            edge_flags[str(path[i]) + " --> " + str(path[i + 1])][j + number_wavelengths] = 0
                            g.ep.counter_alt[path[i], path[i + 1]] -= 1
                            available_wavelengths_alt[str(path[i]) + " --> " + str(path[i + 1])][j] = 0
                            #print("Channel " + str(j) + " allocated for backup; " + " for edge: " + str(path[i]) + " --> " + str(path[i + 1]))
                            channel_key = str(path[i]) + " --> " + str(path[i + 1]) + " " + str(j)
                            backup_channels_all[channel_key] = request_key
                        backup_paths_all[request_key] = path
                        backup_paths_all[request_key].append(j)  # op.write(str(j) + " is the backup channel allocated\n")
                        break
                if tmp == 0:
                    return 1
                else:
                    print("no backup path found cost of path found is : " + str(dist[tgt]))
                    return 0
            else:
                if dist[tgt] < 9999:
                    continue
        else:
            print("no backup path found cost of path found is : " + str(dist[tgt]))
            # backup_paths_all[request_key] = "Blocked"
            return 0


# rechecking for primary paths

def PrimaryPath(src, tgt, primary_path, request):
    # for i in range(len(primary_path)-1):
    # g.ep.weight_temp[primary_path[i],primary_path[i+1]] = 9999
    graph_weight2 = g.new_edge_property("float")  # graph tool property for edges
    g.ep.weight_temp = graph_weight2  # adding a temporary weight
    for e in g.edges():
        g.ep.weight_temp[e] = 1
    for i in range(len(primary_path) - 1):
        g.ep.weight_temp[primary_path[i], primary_path[i + 1]] = 9999

    # print("pred"+str(i))
    while True:
        rev_path = []
        destination_node = request[1]
        dist, pred = gt.dijkstra_search(g, src, g.ep.weight_temp)
        g.vp.pred_tree = pred
        while g.vertex(destination_node) != src:
            # print(destination_node)
            rev_path.append(destination_node)
            temp = destination_node
            destination_node = g.vp.pred_tree[g.vertex(destination_node)]
            # print("dest:"+str(destination_node))
            # print("temp:"+str(temp))
            if temp == destination_node:
                rev_path = []
            # break
        tmp = 1
        temp_value = 0
        if len(rev_path) == 0:
            primary_paths_high_all[request_key] = "Blocked"
        else:
            path = []
        path.append(request[0])
        for i in range(len(rev_path) - 1, -1, -1):
            path.append(rev_path[i])
        print("new primary path searched: " + str(path))
        channel_available = []
        for i in range(int(number_wavelengths)):
            channel_available.append(1)
        if dist[tgt] < 9999:
            for i in range(len(path) - 1):
                # print("counter alt: "+str(g.ep.counter_alt[path[i],path[i+1]]))
                if g.ep.counter_high[path[i], path[i + 1]] > 0:
                    print("traversing edge: " + str(path[i]) + " --> " + str(path[i + 1]))
                    for j in range(int(channels_high)):
                        #print("Channel " + str(j) + "\t" + str(edge_flags[str(path[i]) + " --> " + str(path[i + 1])][j]))
                        available_wavelengths[str(path[i]) + " --> " + str(path[i + 1])][j] = available_wavelengths[str(path[i]) + " --> " + str(path[i + 1])][j] & edge_flags[str(path[i]) + " --> " + str(path[i + 1])][j]
                        channel_available[j] = channel_available[j] & available_wavelengths[str(path[i]) + " --> " + str(path[i + 1])][j]
                else:
                    tmp = 0
                    g.ep.weight_temp[path[i], path[i + 1]] = 9999
                    # print "weight alt " +str(g.ep.weight_alt[path[i],path[i+1]])
                    break  # find another backup path
            if tmp == 1:
                for j in range(int(channels_high)):
                    if channel_available[j] == 1:
                        temp_value = 1
            if temp_value == 1:
                return (path, channel_available)
                '''
				print("primary path allocated : "+str(path))
				for i in range(len(path)-1):
					for j in range (int(channels_high)):
						if available_wavelengths[str(path[i]) + " --> " + str(path[i + 1])][j] == 1:
							edge_flags[str(path[i]) + " --> " + str(path[i + 1])][j] = 0
							g.ep.counter_high[path[i],path[i+1]] -= 1
							available_wavelengths_alt[str(path[i]) + " --> " + str(path[i + 1])][j] = 0
							print("Channel "+str(j)+" allocated for backup; " + " for edge: " + str(path[i]) + " --> " + str(path[i+1]))
							op.write(str(j) + " is the backup channel allocated\n")
							break
				#all_requests_with_primary[request_key] = path
				'''
            # return path
            else:
                path = []
                # print("no primary path found; request blocked")
                # primary_paths_high_all[request_key] = "Blocked"
                return (path, channel_available)


number_high = 0
number_low = 0
request_count = 0
request_served = 0
established_high = 0
established_low = 0
for request in all_requests:
    print "check"
    print request_served
    if request_served == 50:
        print "debugg"
        print request_count
        simulate(50)
        request_served = 0
    if request_count == 80:
        print "free"
        simulate(80)
        request_count = 0
        #simulate()
    if request[2] > 0.5 * number_wavelengths:
        request_key = str(request[0]) + " --> " + str(request[1]) + " " + str(randint(0, 10000))
        print("\nRequest is " + request_key)
        print("Request is high priority")
        number_high += 1
        while True:
            rev_path = []
            src = g.vertex(request[0])
            tgt = g.vertex(request[1])
            destination_node = request[1]
            dist, pred = gt.dijkstra_search(g, src, g.ep.weight_high)
            g.vp.pred_tree = pred  # previous vertex of graph taken
            while g.vertex(destination_node) != src:  # backtracing till destination is equal to source (reverse path used)
                rev_path.append(destination_node)  # destination node added to reverse path array
                temp = destination_node  # temp: nodes from destination to source
                destination_node = g.vp.pred_tree[g.vertex(destination_node)]  # destination_node gives parent nodes from destination to source
                if temp == destination_node:  # check for same source and destination since temp =last to source-1 and destination=dest-1 to source are going to be different
                    rev_path = []
                    break

            temp = 0
            tmp = 1
            if len(rev_path) == 0:
                primary_paths_high_all[request_key] = "Blocked"
            else:
                path = []
                path.append(request[0])
                for i in range(len(rev_path) - 1, -1, -1):
                    path.append(rev_path[i])
                print ("high priority primary path searched: " + str(path))
                channel_available = []
                for i in range(int(number_wavelengths)):
                    channel_available.append(1)
                for i in range(len(path) - 1):
                    if g.ep.counter_high[path[i], path[i + 1]] > 0:
                        print("traversing edge: " + str(path[i]) + " --> " + str(path[i + 1]))
                        for j in range(int(channels_high)):
                            #print("Channel " + str(j) + "\t" + str(edge_flags[str(path[i]) + " --> " + str(path[i + 1])][j]))
                            available_wavelengths[str(path[i]) + " --> " + str(path[i + 1])][j] = available_wavelengths[str(path[i]) + " --> " + str(path[i + 1])][j] & edge_flags[str(path[i]) + " --> " + str(path[i + 1])][j]
                            channel_available[j] = channel_available[j] & available_wavelengths[str(path[i]) + " --> " + str(path[i + 1])][j]
                    else:
                        tmp = 0
                        print("traversing edge: " + str(path[i]) + " --> " + str(path[i + 1]))
                        print(" no channel available ")
                        g.ep.weight_high[path[i], path[i + 1]] = 9999  # because counter is full/exhausted mo more free channles so this edge can't  be used in any other paths
                        break  # find another path

                '''
                for i in range(int(channels_high)):
                    if available_wavelengths[i] == 1:
                        temp = 1
                        print("Channel allocated is " + str(i))
                        op.write(str(i) + " is the channel allocated\n")
                        for j in range(len(path) - 1):
                            edge_flags[str(path[j]) + " --> " + str(path[j + 1])][i] = 0
                            g.ep.counter_high[path[j],path[j+1]] -= 1
                        break  #ye outer for loop k liye h so that once we get the available channle through out the entire pat we set counter and edge logger value
                '''
                print("print tmp value and temp value --- " + str(tmp) + str(temp))
                if tmp == 1:
                    #print("in the loop ")
                    for j in range(int(channels_high)):
                        if channel_available[j] == 1:
                            temp = 1
                if temp == 1 and int(dist[tgt]) < 9999:
                    print("high priority primary path found ; searching for backup path")
                    temp2 = BackupPath(src, tgt, path, request, request_key)
                    # print("temp2: "+str(temp2))
                    if temp2 == 1:
                        print ("high prioirty primary path allocated: " + str(path))
                        for j in range(int(channels_high)):
                            if channel_available[j] == 1:
                                for i in range(len(path) - 1):
                                    edge_flags[str(path[i]) + " --> " + str(path[i + 1])][j] = 0
                                    g.ep.counter_high[path[i], path[i + 1]] -= 1
                                    available_wavelengths[str(path[i]) + " --> " + str(path[i + 1])][j] = 0
                                    print("Channel " + str(j) + " allocated for high priority primary: " + " for edge: " + str(path[i]) + " --> " + str(path[i + 1]))
                                    channel_key = str(path[i]) + " --> " + str(path[i + 1]) + " " + str(j)
                                    channels_all[channel_key] = request_key
                                primary_paths_high_all[request_key] = path
                                primary_paths_high_all[request_key].append(j)
                                established_high += 1
                                request_served += 1
                                request_count += 1
                                break
                    else:
                        # path = []
                        channel_available_new = []
                        path, channel_available_new = PrimaryPath(src, tgt, path, request)
                        if len(path) > 0:
                            temp2 = BackupPath(src, tgt, path, request, request_key)
                            if temp2 == 1:
                                print ("high prioirty primary path allocated: " + str(path))
                                for j in range(int(channels_high)):
                                    if channel_available_new[j] == 1:
                                        for i in range(len(path) - 1):
                                            edge_flags[str(path[i]) + " --> " + str(path[i + 1])][j] = 0
                                            g.ep.counter_high[path[i], path[i + 1]] -= 1
                                            available_wavelengths[str(path[i]) + " --> " + str(path[i + 1])][j] = 0
                                            print("Channel " + str(j) + " allocated for high priority primary: " + " for edge: " + str(path[i]) + " --> " + str(path[i + 1]))
                                            channel_key = str(path[i]) + " --> " + str(path[i + 1]) + " " + str(j)
                                            channels_all[channel_key] = request_key
                                        primary_paths_high_all[request_key] = path
                                        primary_paths_high_all[request_key].append(j)
                                        established_high += 1
                                        request_served += 1
                                        request_count += 1
                                        break
                            else:
                                print("primary path was found but no backup path found; request blocked")
                                primary_paths_high_all[request_key] = "Blocked"
                                break
                        else:
                            temp = 0
                            print("primary path was not found; request blocked")
                            primary_paths_high_all[request_key] = "Blocked"
                            break

                else:
                    if dist[tgt] < 9999 and tmp == 0:
                        continue
                    else:
                        print("no primary path found; request blocked . cost of path found is : " + str(dist[tgt]))
                        primary_paths_high_all[request_key] = "Blocked"
                        break
            if temp == 1 and temp2 == 1:
                print "Cost of path allocated is " + str(dist[tgt]) + "\n"
            break
    else:
        request_key = str(request[0]) + " --> " + str(request[1]) + " " + str(randint(0, 10000))
        print("\nRequest is " + request_key)
        print("Request is low priority")
        number_low += 1
        while True:
            rev_path = []
            src = g.vertex(request[0])
            tgt = g.vertex(request[1])
            destination_node = request[1]
            dist, pred = gt.dijkstra_search(g, src, g.ep.weight_low)
            g.vp.pred_tree = pred
            while g.vertex(destination_node) != src:
                rev_path.append(destination_node)
                temp = destination_node
                destination_node = g.vp.pred_tree[g.vertex(destination_node)]
                if temp == destination_node:
                    rev_path = []
                    break
            if len(rev_path) == 0:
                primary_paths_low_all[request_key] = "Blocked"
            else:
                path = []
                path.append(request[0])
                for i in range(len(rev_path) - 1, -1, -1):
                    path.append(rev_path[i])
                print ("low priority primary path searched: " + str(path))
                temp = 1
                tmp = 1
                channel_available = []
                for i in range(int(number_wavelengths)):
                    channel_available.append(1)
                for i in range(len(path) - 1):
                    if g.ep.counter_low[path[i], path[i + 1]] > 0:
                        print("traversing edge: " + str(path[i]) + " --> " + str(path[i + 1]))
                        for j in range(int(channels_high), number_wavelengths):
                            #print("Channel " + str(j) + "\t" + str(edge_flags[str(path[i]) + " --> " + str(path[i + 1])][j]))
                            available_wavelengths[str(path[i]) + " --> " + str(path[i + 1])][j] = \
                            available_wavelengths[str(path[i]) + " --> " + str(path[i + 1])][j] & \
                            edge_flags[str(path[i]) + " --> " + str(path[i + 1])][j]
                            channel_available[j] = channel_available[j] & available_wavelengths[str(path[i]) + " --> " + str(path[i + 1])][j]
                    else:
                        temp = 0
                        print("traversing edge: " + str(path[i]) + " --> " + str(path[i + 1]))
                        print(" no channel available ")
                        g.ep.weight_low[path[i], path[i + 1]] = 9999  # because counter is full/exhausted mo more free channles so this edge can't  be used in any other paths
                        break  # find another path
                tmp = 1
                if temp == 1:
                    for j in range(int(channels_high), number_wavelengths):
                        if channel_available[j] == 1 and int(dist[tgt]) < 9999:
                            print ("low priority primary path allocated: " + str(path))
                            for i in range(len(path) - 1):
                                edge_flags[str(path[i]) + " --> " + str(path[i + 1])][j] = 0
                                g.ep.counter_low[path[i], path[i + 1]] -= 1
                                available_wavelengths[str(path[i]) + " --> " + str(path[i + 1])][j] = 0
                                print("Channel " + str(j) + " allocated for low priority primary: " + " for edge: " + str(path[i]) + " --> " + str(path[i + 1]))
                                channel_key = str(path[i]) + " --> " + str(path[i + 1]) + " " + str(j)
                                channels_all[channel_key] = request_key
                            # print("channel_key: " +str(channel_key) +"request_key: " +str(request_key))
                            primary_paths_low_all[request_key] = path
                            primary_paths_low_all[request_key].append(j)
                            established_low += 1
                            request_served += 1
                            request_count += 1
                            tmp = 0
                            break
                    if tmp == 1:
                        print("no1 primary was path found; request blocked")
                        primary_paths_low_all[request_key] = "Blocked"
                        break
                else:
                    if dist[tgt] < 9999:
                        continue
                    else:
                        print("no primary was path found; request blocked")
                        primary_paths_low_all[request_key] = "Blocked"
                        break
            if tmp == 0:
                print "Cost of path allocated is " + str(dist[tgt]) + "\n"
            break

number_blocked_requests = 0
for key in primary_paths_high_all.values():
    if key == "Blocked":
        number_blocked_requests += 1
for key in primary_paths_low_all.values():
    if key == "Blocked":
        number_blocked_requests += 1
print("request served " + str(request_served) + "request_count" + str(request_count))
getcontext().prec = 6
twograde_output(op, number_requests, number_blocked_requests, number_low, number_high, primary_paths_high_all,
                primary_paths_low_all, backup_paths_all, established_low, established_high)
print("all channels are ch " + str(channels_all))
