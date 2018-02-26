import graph_tool.all as gt
from graph_tool import Graph
from random import randint

from math import *
from decimal import *
from header import *
import topology
from genrequests import generate
from graphproperty import onegrade_property
from outputs import onegrade_output

primary_paths_high_all = {}
primary_paths_high_all_temp = {}
primary_paths_low_all = {}
primary_paths_low_all_temp = {}
backup_paths_all = {}
channels_all ={}
keylist_temp = []
op = open("onegrade", "a")

if  number_wavelengths > 0: 
    
    ## Network is USIP ##
    g = Graph(directed=False)
    topology.creation(g,21)
    
    ## Generating the requests ##
    request,all_requests = generate()
    #print request

## Defining the graph properties ##
available_wavelengths_low,available_wavelengths_alt,available_wavelengths_high,edge_flags,g.ep.weight_primary,g.ep.weight_high,g.ep.counter_channels = onegrade_property(g)
#print("counter"+str(g.ep.counter_channels[e]))

#drawing the graph
gt.graph_draw(g, vertex_text=g.vertex_index, vertex_font_size=12, vertex_shape="double_circle",vertex_fill_color="#55cc22", vertex_pen_width=3,edge_pen_width=1, output="topology.pdf")
time = g.new_vertex_property("int")

#refresh_counter = 0
def simulate(type):
    count1 = 0
    iter = 0
    if type == 30:
        keylist = []
        global keylist_temp
        pathlist = []
        templist = []
        for key in primary_paths_high_all_temp.keys():
            #print "in (1)"
            templist.append(primary_paths_high_all_temp[key])
            #print iter
            #print templist[iter]
            if templist[iter] != "Blocked":
                keylist.append(key)
                keylist_temp.append(key)
                pathlist.append(primary_paths_high_all_temp[key])
                count1 +=1
                if(count1 == 5):
                    print("count is(1): " +str(count1))
                    break
            iter += 1
        iter += 1
        for key in primary_paths_low_all_temp.keys():
            #print "in (2)"
            templist.append(primary_paths_low_all_temp[key])
            #print iter
            #print templist[iter]
            if templist[iter] != "Blocked":
                keylist.append(key)
                pathlist.append(primary_paths_low_all_temp[key])
                count1 +=1
                if(count1 == 10):
                    print("count is(2): " + str(count1))
                    break
            iter += 1
        #print "debug"
        print keylist
        print pathlist
        for i in range (10):
            count_intrrupted = 0
            if i<5:
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
                    #print("edge : " +str(path[j]) + "-->" + str(path[j+1])+"channel : " +str(primary_channel))
                    edge_flags[str(path[j]) + " --> " + str(path[j + 1])][primary_channel] = 1
                    print edge_flags[str(path[j]) + " --> " + str(path[j + 1])]
                    g.ep.counter_channels[path[j], path[j + 1]] += 1
                del primary_paths_low_all_temp[keylist[i]]
    if type == 50:
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
                g.ep.counter_channels[path[j], path[j + 1]] += 1

            for j in range(len(backup_path)-2):
                edge_flags[str(backup_path[j]) + " --> " + str(backup_path[j + 1])][backup_channel + number_wavelengths] = 1
            del primary_paths_high_all_temp[keylist_temp[i]]

        keylist_temp = []
                #print edge_flags[str(backup_path[j]) + " --> " + str(backup_path[j + 1])]
                #g.ep.counter_alt[backup_path[j], backup_path[j + 1]] += 1
#Backup Path
def BackupPath(src,tgt,primary_path,request,request_key):
    
    #print("source"+ str(src) + "dest "+str(tgt)+" path: "+str(primary_path)+ " request"+str(request) )
    graph_weight = g.new_edge_property("float") #graph tool property for edges
    g.ep.weight_alt = graph_weight              #adding a temporary weight
    for e in g.edges():
        g.ep.weight_alt[e] = 1
    for i in range(len(primary_path)-1):
        g.ep.weight_alt[primary_path[i],primary_path[i+1]] = 9999
    
    #print("pred"+str(i))
    while True:
        for e in g.edges():
            for j in range(number_wavelengths):
                edge_flags[str(e.source()) + " --> " + str(e.target())][j + (2 * number_wavelengths)] = 1
                edge_flags[str(e.target()) + " --> " + str(e.source())][j + (2 * number_wavelengths)] = 1
        non_disjointlist = []
        rev_path = []
        destination_node = request[1]
        dist, pred = gt.dijkstra_search(g, src, g.ep.weight_alt)
        g.vp.pred_tree = pred
        while g.vertex(destination_node) != src:
            #print(destination_node)
            rev_path.append(destination_node)
            temp = destination_node
            destination_node = g.vp.pred_tree[g.vertex(destination_node)]
            #print("dest:"+str(destination_node))
            #print("temp:"+str(temp))
            if temp == destination_node:
                rev_path = []
        tmp = 1
        temp_value = 1
        if len(rev_path) == 0:
            backup_paths_all[request_key] = "Blocked"
        else:
            path = []
            path.append(request[0])
            for i in range(len(rev_path) - 1, -1, -1):
                path.append(rev_path[i])
            for key in primary_paths_high_all_temp.keys():
                flag = 0
                temp_path = primary_paths_high_all_temp[key]
                # print("temp path cal is : " +str(temp_path))
                # print("primary path cal is : " + str(primary_path))
                for i in range(len(primary_path) - 1):
                    for j in range(len(temp_path) - 2):
                        if primary_path[i] == temp_path[j] and primary_path[i + 1] == temp_path[j + 1]:
                            non_disjointlist.append(key)
                            # print("non list : " +str(non_disjointlist))
                            flag = 1
                            break
                    if flag == 1:
                        break
            print("backup path searched: " + str(path) + "cost of path found is : " + str(dist[tgt]))
            print("non-disjoint list : " + str(non_disjointlist))
            for i in range(len(non_disjointlist)):
                temp_path = backup_paths_all[non_disjointlist[i]]
                print("temp path : " + str(temp_path))
                temp_channel = backup_paths_all[non_disjointlist[i]][-1]
                print("temp channel : " + str(temp_channel))
                for j in range(len(temp_path) - 2):
                    edge_flags[str(temp_path[j]) + " --> " + str(temp_path[j + 1])][temp_channel + (2 * number_wavelengths)] = 0
            channel_available = []
            for i in range (int(number_wavelengths)):
                channel_available.append(1)
            if dist[tgt] < 9999:    
                for i in range(len(path) - 1):
                    #print("counter alt: "+str(g.ep.counter_alt[path[i],path[i+1]]))
                    if g.ep.counter_channels[path[i],path[i+1]] > 0:
                        print("traversing edge: " + str(path[i]) + " --> " + str(path[i + 1]))
                        for j in range(int(number_wavelengths)):
                            print("Channel " + str(j) + "\t" + str(edge_flags[str(path[i]) + " --> " + str(path[i + 1])][j]) + "\t" + str(edge_flags[str(path[i]) + " --> " + str(path[i + 1])][j + 2 * number_wavelengths]))
                            #available_wavelengths_alt[str(path[i]) + " --> " + str(path[i + 1])][j] = available_wavelengths_alt[str(path[i]) + " --> " + str(path[i + 1])][j] & edge_flags[str(path[i]) + " --> " + str(path[i + 1])][j + int(number_wavelengths)] & edge_flags[str(path[i]) + " --> " + str(path[i + 1])][j]
                            #print("Channel " + str(j) + "\t" + str(available_wavelengths_alt[str(path[i]) + " --> " + str(path[i + 1])][j]))
                            channel_available[j] = channel_available[j] & edge_flags[str(path[i]) + " --> " + str(path[i + 1])][j] & edge_flags[str(path[i]) + " --> " + str(path[i + 1])][j + 2 * number_wavelengths]

                    else:
                        temp_value = 0
                        g.ep.weight_alt[path[i],path[i+1]] = 9999
                        #print "weight alt " +str(g.ep.weight_alt[path[i],path[i+1]])
                        break #find another backup path
            if temp_value == 1:
                for j in range (int(number_wavelengths)):
                    if channel_available[j] == 1:
                        print("backup path allocated : " + str(path))
                        tmp = 0
                        for i in range(len(path)-1):
                            edge_flags[str(path[i]) + " --> " + str(path[i + 1])][j + int(number_wavelengths)] = 0
                            #g.ep.counter_channels[path[i],path[i+1]] -= 1
                            #available_wavelengths_alt[str(path[i]) + " --> " + str(path[i + 1])][j] = 0
                            print("Channel "+str(j)+" allocated for backup; " + " for edge: " + str(path[i]) + " --> " + str(path[i+1]))
                            channel_key = str(path[i]) + " --> " + str(path[i + 1]) + " " + str(j)
                            channels_all[channel_key] = request_key
                        backup_paths_all[request_key] = path
                        backup_paths_all[request_key].append(j)
                        break
                if tmp == 0:
                    return 1
                else:
                    print("no backup path found cost of path found is : " + str(dist[tgt]))
                    return 0
            else:
                #return 0
                if dist[tgt] < 9999:
                    continue
                else:
                    print("no backup path found; request blocked")
                    #backup_paths_all[request_key] = "Blocked"
                    return 0

number_high = 0
number_low = 0
established_high = 0
established_low = 0
request_count = 0
request_served = 0
total_request = 0

for request in all_requests:
    print "check"
    print request_served
    if request_served == 30:
        print "debugg"
        print total_request
        simulate(30)
        #request_served = 0
    if request_served == 50:
        print "debugg1"
        print total_request
        simulate(50)
        request_served = 0
    if request[2] > 0.5*number_wavelengths:
        request_key = str(request[0]) + " --> " + str(request[1]) + " " +str(randint(0,10000))
        print("\nRequest is " + request_key)
        print("Request is high priority")
        number_high += 1
        while True:
            rev_path = []
            src = g.vertex(request[0])
            tgt = g.vertex(request[1])
            destination_node = request[1]
            dist, pred = gt.dijkstra_search(g, src, g.ep.weight_primary)
            g.vp.pred_tree = pred #previous vertex of graph taken
            #print pred.a
            #print g.vp.pred_tree.a
            while g.vertex(destination_node) != src: #backtracing till destination is equal to source (reverse path used)
                rev_path.append(destination_node) #destination node added to reverse path array
                temp = destination_node #temp: nodes from destination to source
                destination_node = g.vp.pred_tree[g.vertex(destination_node)] #destination_node gives parent nodes from destination to source
                if temp == destination_node: #check for same source and destination since temp =last to source-1 and destination=dest-1 to source are going to be different
                    rev_path = []
                    break
            temp = 0
            tmp = 1
            if len(rev_path) == 0:
                primary_paths_high_all[request_key] = "Blocked"
                primary_paths_high_all_temp[request_key] = "Blocked"
                #print("***blocked")
            else:
                path = []
                path.append(request[0])
                for i in range(len(rev_path) - 1, -1, -1):
                   path.append(rev_path[i])
                #path = list(reversed(rev_path)) #get back normal path
                print ("high priority primary path searched: "+str(path)+ "cost is : " +str(dist[tgt]))
                channel_available = []
                for i in range (int(number_wavelengths)):
                    channel_available.append(1)
                for i in range(len(path) - 1):
                    if g.ep.counter_channels[path[i],path[i+1]] > 0:
                        print("traversing edge: " + str(path[i]) + " --> " + str(path[i + 1]))
                        for j in range(int(number_wavelengths)):
                            #print("Channel " + str(j) + "\t" + str(edge_flags[str(path[i]) + " --> " + str(path[i + 1])][j]))
                            available_wavelengths_high[str(path[i]) + " --> " + str(path[i + 1])][j] = available_wavelengths_high[str(path[i]) + " --> " + str(path[i + 1])][j] & edge_flags[str(path[i]) + " --> " + str(path[i + 1])][j] & edge_flags[str(path[i]) + " --> " + str(path[i + 1])][j+int(number_wavelengths)]
                            print("Channel " + str(j) + "\t" + str(available_wavelengths_high[str(path[i]) + " --> " + str(path[i + 1])][j]))
                            channel_available[j] = channel_available[j] & available_wavelengths_high[str(path[i]) + " --> " + str(path[i + 1])][j]

                    else:
                        tmp = 0
                        g.ep.weight_primary[path[i],path[i+1]] = 9999 #because counter is full/exhausted mo more free channles so this edge can't  be used in any other paths
                        break
                if tmp == 1:
                    for j in range(int(number_wavelengths)):
                        if channel_available[j] == 1:
                            temp = 1
                if temp == 1:
                    print("high priority primary path found; searching for backup path")
                    temp2 = BackupPath(src,tgt,path,request,request_key)
                    if temp2 == 1:
                        print ("high prioirty primary path allocated: "+str(path))
                        for j in range (int(number_wavelengths)):
                            if channel_available[j] == 1:
                                for i in range(len(path)-1):
                                    edge_flags[str(path[i]) + " --> " + str(path[i + 1])][j] = 0
                                    g.ep.counter_channels[path[i],path[i+1]] -= 1
                                    available_wavelengths_high[str(path[i]) + " --> " + str(path[i + 1])][j] = 0
                                    available_wavelengths_low[str(path[i]) + " --> " + str(path[i + 1])][j] = 0
                                    print("Channel " + str(j) + " allocated for high priority primary: " + " for edge: " + str(path[i]) + " --> " + str(path[i+1]))
                                    channel_key = str(path[i]) + " --> " + str(path[i + 1]) + " " + str(j)
                                    channels_all[channel_key] = request_key
                                primary_paths_high_all[request_key] = path
                                primary_paths_high_all[request_key].append(j)
                                primary_paths_high_all_temp[request_key] = path
                                #primary_paths_high_all_temp[request_key].append(j)
                                established_high += 1
                                request_served += 1
                                request_count += 1
                                total_request += 1
                                break
                    else:
                        print("primary path was found but no backup path found; request blocked")
                        primary_paths_high_all[request_key] = "Blocked"
                        primary_paths_high_all_temp[request_key] = "Blocked"
                        break
                else:
                    if dist[tgt] < 9999 and tmp == 0:
                        continue
                    else:
                        print("no primary path found; request blocked")
                        primary_paths_high_all[request_key] = "Blocked"
                        primary_paths_high_all_temp[request_key] = "Blocked"
                        break
            if temp == 1 & temp2 == 1:
                print "Cost of path allocated is " + str(dist[tgt]) + "\n"
                #op.write(str(path) + " is the path\n" + str(dist[tgt]) + " is cost\n")
            break
    
    else: #request is low priority section
        request_key = str(request[0]) + " --> " + str(request[1]) + " " + str(randint(0,10000))
        print("\nRequest is " + request_key)
        print("Request is low priority")
        number_low += 1
        while True:
            rev_path = []
            src = g.vertex(request[0])
            tgt = g.vertex(request[1])
            destination_node = request[1]
            dist, pred = gt.dijkstra_search(g, src, g.ep.weight_primary)
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
                primary_paths_low_all_temp[request_key] = "Blocked"
                #continue # if no path is foound in the first place so request is blockes
            else:
                path = []
                path.append(request[0])
                for i in range(len(rev_path) - 1, -1, -1):
                    path.append(rev_path[i])
                print ("low priority primary path searched: "+str(path))
                temp = 1
                tmp = 1
                channel_available = []
                for i in range (int(number_wavelengths)):
                    channel_available.append(1)
                for i in range(len(path) - 1):
                    #print("counter low "+str(g.ep.counter_channels[path[i],path[i+1]]))
                    if g.ep.counter_channels[path[i],path[i+1]] > 0:
                        print("traversing edge: " + str(path[i]) + " --> " + str(path[i + 1]))
                        for j in range(int(number_wavelengths)):
                            #print("Channel " + str(j) + "\t" + str(edge_flags[str(path[i]) + " --> " + str(path[i + 1])][j]))
                            available_wavelengths_low[str(path[i]) + " --> " + str(path[i + 1])][j] = available_wavelengths_low[str(path[i]) + " --> " + str(path[i + 1])][j] & edge_flags[str(path[i]) + " --> " + str(path[i + 1])][j]
                            print("Channel " + str(j) + "\t" + str(available_wavelengths_low[str(path[i]) + " --> " + str(path[i + 1])][j]))
                            channel_available[j] = channel_available[j] & available_wavelengths_low[str(path[i]) + " --> " + str(path[i + 1])][j]

                    else:
                        temp=0
                        print("traversing edge: " + str(path[i]) + " --> " + str(path[i + 1]) + "cost is : " + str(dist[tgt]))
                        print(" no channel available; weight of edge increased " + str(path[i]) + "--> " + str(path[i + 1]))
                        g.ep.weight_primary[path[i],path[i+1]] = 9999 #because counter is full/exhausted mo more free channles so this edge can't  be used in any other paths
                        break  #find another path

                if temp == 1:
                    print ("low priority primary path allocated: "+str(path))
                    for j in range (int(number_wavelengths)):
                        if channel_available[j] == 1:
                            for i in range(len(path)-1):
                                edge_flags[str(path[i]) + " --> " + str(path[i + 1])][j] = 0
                                g.ep.counter_channels[path[i],path[i+1]] -= 1
                                available_wavelengths_low[str(path[i]) + " --> " + str(path[i + 1])][j] = 0
                                available_wavelengths_high[str(path[i]) + " --> " + str(path[i + 1])][j] = 0
                                print("Channel " + str(j) + " allocated for low priority primary: " + " for edge: " + str(path[i]) + " --> " + str(path[i+1]))
                                channel_key = str(path[i]) + " --> " + str(path[i + 1]) + " " + str(j)
                                channels_all[channel_key] = request_key
                            primary_paths_low_all[request_key] = path
                            primary_paths_low_all[request_key].append(j)
                            primary_paths_low_all_temp[request_key] = path
                            #primary_paths_low_all_temp[request_key].append(j)
                            established_low += 1
                            request_served += 1
                            request_count += 1
                            total_request += 1
                            tmp = 0
                            break
                    if tmp == 1:
                        print("no1 primary was path found; request blocked")
                        primary_paths_low_all[request_key] = "Blocked"
                        primary_paths_low_all_temp[request_key] = "Blocked"
                        break
                else:
                    if dist[tgt] < 9999:
                        continue
                    else:
                        print("no primary was path found; request blocked")
                        primary_paths_low_all[request_key] = "Blocked"
                        primary_paths_low_all_temp[request_key] = "Blocked"
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
getcontext().prec = 6
onegrade_output(op,number_requests,number_blocked_requests,number_low,number_high,primary_paths_high_all,primary_paths_low_all,backup_paths_all,established_low,established_high)