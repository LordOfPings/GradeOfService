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

primary_paths_all = {}
backup_paths_all = {}
op = open("twograde", "a")

if number_wavelengths > 1: #for simulation
    ## Network is USIP ##

    ## Creating the USIP network ##
    g = Graph(directed=False)
    topology.creation(g,16)
    
    ## Generating the requests ##
    request,all_requests = generate()
	#print request

## Defining the graph properties ##
available_wavelengths_alt,available_wavelengths,edge_flags,g.ep.weight_high,g.ep.weight_low,g.ep.counter_high,g.ep.counter_alt,channels_high,channels_low = twograde_property(g)
#print("counter"+str(g.ep.counter_low[e]))

gt.graph_draw(g, vertex_text=g.vertex_index, vertex_font_size=12, vertex_shape="double_circle",vertex_fill_color="#55cc22", vertex_pen_width=3,edge_pen_width=1, output="topology.pdf")
time = g.new_vertex_property("int")
#print("Edge logger"+str(edge_flags))
#refresh_counter = 0  

#Backup Path

def BackupPath(src,tgt,primary_path,request):        
	
	#print("source"+ str(src) + "dest "+str(tgt)+" path: "+str(primary_path)+ " request"+str(request) )
	graph_weight = g.new_edge_property("float") #graph tool property for edges
	g.ep.weight_alt = graph_weight  			#adding a temporary weight
	for e in g.edges():
		g.ep.weight_alt[e] = 1
	for i in range(len(primary_path)-1):
		g.ep.weight_alt[primary_path[i],primary_path[i+1]] = 9999
 	#tmp=1
 	#print("pred"+str(i))
 	path_count=0
 	while True:
 		path_count += 1
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
				#break

		tmp=1
		temp_value=1
		if len(rev_path) == 0:
			backup_paths_all[request_key] = "Blocked"
		else:
			path = []
	        path.append(request[0])
	        for i in range(len(rev_path) - 1, -1, -1):
	        	path.append(rev_path[i])
	        print("backup path searched: " +str(path) +"cost of path found is : "  +str(dist[tgt]) )
	        #temp_value = 0
	        channel_available = []
	        for i in range (int(number_wavelengths)):
	        	channel_available.append(1)
	        if dist[tgt] < 9999: 	
		        for i in range(len(path) - 1):
		        	#print("counter alt: "+str(g.ep.counter_alt[path[i],path[i+1]]))
		        	if g.ep.counter_alt[path[i],path[i+1]] > 0:
		        		print("traversing edge: " + str(path[i]) + " --> " + str(path[i + 1]))
		        		for j in range(int(channels_high),number_wavelengths):
		        			print("Channel " + str(j) + "\t" + str(edge_flags[str(path[i]) + " --> " + str(path[i + 1])][j + number_wavelengths]))
		        			available_wavelengths_alt[str(path[i]) + " --> " + str(path[i + 1])][j] = available_wavelengths_alt[str(path[i]) + " --> " + str(path[i + 1])][j] & edge_flags[str(path[i]) + " --> " + str(path[i + 1])][j + number_wavelengths]
		        			channel_available[j] = channel_available[j] & available_wavelengths_alt[str(path[i]) + " --> " + str(path[i + 1])][j]
			       	else:
			       		print("traversing edge: " + str(path[i]) + " --> " + str(path[i + 1]))
			       		print("no channel available ")
			       		temp_value = 0
			       		g.ep.weight_alt[path[i],path[i+1]] = 9999
			       		#print "weight alt " +str(g.ep.weight_alt[path[i],path[i+1]])
			       		break #find another backup path
			if temp_value == 1:
				for j in range (int(channels_high),number_wavelengths):
					if channel_available[j] == 1:
						print("backup path allocated : "+str(path))
						tmp = 0
						for i in range(len(path)-1):
							edge_flags[str(path[i]) + " --> " + str(path[i + 1])][j + number_wavelengths] = 0
							g.ep.counter_alt[path[i],path[i+1]] -= 1
							available_wavelengths_alt[str(path[i]) + " --> " + str(path[i + 1])][j] = 0
							print("Channel "+str(j)+" allocated for backup; " + " for edge: " + str(path[i]) + " --> " + str(path[i+1]))
							#op.write(str(j) + " is the backup channel allocated\n")
						break
				if tmp == 0:
					backup_paths_all[request_key] = path
					return 1
				else:
					print("no backup path found cost of path found is : " +str(dist[tgt]))
					return 0
			else:
				if dist[tgt] < 9999 and path_count <= 30:
					continue
                else:
                	print("no backup path found cost of path found is : " +str(dist[tgt]))
                	#backup_paths_all[request_key] = "Blocked"
                	return 0

#rechecking for primary paths

def PrimaryPath(src,tgt,primary_path,request):        
	
	#for i in range(len(primary_path)-1):
		#g.ep.weight_temp[primary_path[i],primary_path[i+1]] = 9999
	graph_weight2 = g.new_edge_property("float") #graph tool property for edges
	g.ep.weight_temp = graph_weight2  			#adding a temporary weight
	for e in g.edges():
		g.ep.weight_temp[e] = 1
	for i in range(len(primary_path)-1):
		g.ep.weight_temp[primary_path[i],primary_path[i+1]] = 9999
 	
 	#print("pred"+str(i))
 	while True:
		rev_path = []
		destination_node = request[1]
		dist, pred = gt.dijkstra_search(g, src, g.ep.weight_temp)
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
	 			#break
	 	tmp=1
	 	temp_value=1
	 	if len(rev_path) == 0:
	 		backup_paths_all[request_key] = "Blocked"
	 	else:
			path = []
	        path.append(request[0])
	        for i in range(len(rev_path) - 1, -1, -1):
	        	path.append(rev_path[i])
	        print("new primary path searched: "+str(path))
	        channel_available = []
	        for i in range (int(number_wavelengths)):
	        	channel_available.append(1)
	        if dist[tgt] < 9999: 	
		        for i in range(len(path) - 1):
		        	#print("counter alt: "+str(g.ep.counter_alt[path[i],path[i+1]]))
		        	if g.ep.counter_high[path[i],path[i+1]] > 0:
		        		print("traversing edge: " + str(path[i]) + " --> " + str(path[i + 1]))
		        		for j in range(int(channels_high)):
		        			print("Channel " + str(j) + "\t" + str(edge_flags[str(path[i]) + " --> " + str(path[i + 1])][j]))
		        			available_wavelengths[str(path[i]) + " --> " + str(path[i + 1])][j] = available_wavelengths[str(path[i]) + " --> " + str(path[i + 1])][j] & edge_flags[str(path[i]) + " --> " + str(path[i + 1])][j]
		        			channel_available[j] = channel_available[j] & available_wavelengths[str(path[i]) + " --> " + str(path[i + 1])][j]
			       	else:
			       		temp_value = 0
			       		g.ep.weight_temp[path[i],path[i+1]] = 9999
			       		#print "weight alt " +str(g.ep.weight_alt[path[i],path[i+1]])
			       		break #find another backup path
			if temp_value == 1:
				for j in range (int(channels_high)):
					if channel_available[j] == 1:
						temp_value=1
			if temp_value == 1:
				return (path,channel_available)
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
				#return path
			else:
				path = []
				print("no primary path found; request blocked")
				primary_paths_all[request_key] = "Blocked"
				return (path,channel_available)

number_high = 0
number_low = 0
established_high = 0
established_low = 0
for request in all_requests:


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
            dist, pred = gt.dijkstra_search(g, src, g.ep.weight_high)
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
            #rev_path.append(request[0])
            temp = 0
            tmp = 1
            if len(rev_path) == 0:
              	primary_paths_all[request_key] = "Blocked"
        		#print("***blocked")
            else:
                path = []
                path.append(request[0])
                for i in range(len(rev_path) - 1, -1, -1):
                   path.append(rev_path[i])
                #path = list(reversed(rev_path)) #get back normal path
                print ("high priority primary path searched: "+str(path))
                
                channel_available = []
                for i in range (int(number_wavelengths)):
                	channel_available.append(1)
                for i in range(len(path) - 1):
                    #print("counter high"+str(g.ep.counter_high[path[i],path[i+1]]))
                    if g.ep.counter_high[path[i],path[i+1]] > 0:
                        print("traversing edge: " + str(path[i]) + " --> " + str(path[i + 1]))
                        for j in range(int(channels_high)):
                            print("Channel " + str(j) + "\t" + str(edge_flags[str(path[i]) + " --> " + str(path[i + 1])][j]))
                            available_wavelengths[str(path[i]) + " --> " + str(path[i + 1])][j] = available_wavelengths[str(path[i]) + " --> " + str(path[i + 1])][j] & edge_flags[str(path[i]) + " --> " + str(path[i + 1])][j]
                            channel_available[j] = channel_available[j] & available_wavelengths[str(path[i]) + " --> " + str(path[i + 1])][j]
                    else:
                        tmp = 0
                        print("traversing edge: " + str(path[i]) + " --> " + str(path[i + 1]))
                        print(" no channel available ")
                        g.ep.weight_high[path[i],path[i+1]] = 9999 #because counter is full/exhausted mo more free channles so this edge can't  be used in any other paths
                        #g.ep.weight_temp[path[i],path[i+1]] = 9999
                        break  #find another path
    		        
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
                print("print tmp value and temp value --- "+str(tmp) +str(temp))
                if tmp == 1:
                	print("in the loop ")
	                for j in range (int(channels_high)):
	                	if channel_available[j] == 1:
	                		temp=1
                if temp == 1 and int(dist[tgt]) < 9999:
                	print("high priority primary path found in temp==1; searching for backup path")
                	temp2 = BackupPath(src,tgt,path,request)
                	#print("temp2: "+str(temp2))
                	if temp2 == 1:
                		print ("high prioirty primary path allocated: "+str(path))
            			for j in range (int(channels_high)):
            				if channel_available[j] == 1:
            					for i in range(len(path)-1):
	            					edge_flags[str(path[i]) + " --> " + str(path[i + 1])][j] = 0
	            					g.ep.counter_high[path[i],path[i+1]] -= 1
	            					available_wavelengths[str(path[i]) + " --> " + str(path[i + 1])][j] = 0
	            					print("Channel " + str(j) + " allocated for high priority primary: " + " for edge: " + str(path[i]) + " --> " + str(path[i+1]))
	            					#op.write(str(j) + " is the channel allocated\n")
            					break
	                else:
	                	#path = []
	                	channel_available_new = []
	                	path,channel_available_new = PrimaryPath(src,tgt,path,request)
	                	if len(path) > 0:
	                		temp2 = BackupPath(src,tgt,path,request)
		                	if temp2 == 1:
		                		print ("high prioirty primary path allocated: "+str(path))
	                			for j in range (int(channels_high)):
	                				if channel_available_new[j] == 1:
	                					for i in range(len(path)-1):
		                					edge_flags[str(path[i]) + " --> " + str(path[i + 1])][j] = 0
		                					g.ep.counter_high[path[i],path[i+1]] -= 1
		                					available_wavelengths[str(path[i]) + " --> " + str(path[i + 1])][j] = 0
		                					print("Channel " + str(j) + " allocated for high priority primary: " + " for edge: " + str(path[i]) + " --> " + str(path[i+1]))
		                					#op.write(str(j) + " is the channel allocated\n")
	                					break
		                	else:
		                		print("primary path was found but no backup path found; request blocked")
		                		primary_paths_all[request_key] = "Blocked"
		                else:
		                	temp = 0
		                	print("primary path was not found; request blocked")
		                	primary_paths_all[request_key] = "Blocked"

                else:
                    if dist[tgt] < 9999 and tmp == 0:
                        continue
                    else:
                    	print("no primary path found; request blocked . cost of path found is : " +str(dist[tgt]))
                        primary_paths_all[request_key] = "Blocked"
                        break



            if temp == 1 and temp2 == 1:
            	established_high += 1
                primary_paths_all[request_key] = path
                #for j in range(len(path) - 1):
                #g.ep.weight_low[path[j], path[j + 1]] += 1
                #print "high priority primary path is :" + str(path) + "\n"
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
            dist, pred = gt.dijkstra_search(g, src, g.ep.weight_low)
            g.vp.pred_tree = pred
            #print pred.a
            #print g.vp.pred_tree.a
            while g.vertex(destination_node) != src:
                rev_path.append(destination_node)
                #print(destination_node)
                temp = destination_node
                destination_node = g.vp.pred_tree[g.vertex(destination_node)]
                #print("destination: "+destination_node)
                if temp == destination_node:
                    rev_path = []
                    break
            if len(rev_path) == 0:
                primary_paths_all[request_key] = "Blocked"
                #continue # if no path is foound in the first place so request is blockes
            else:
                path = []
                path.append(request[0])
                for i in range(len(rev_path) - 1, -1, -1):
                    path.append(rev_path[i])
                print ("low priority primary path searched: "+str(path))
                temp=1
                tmp=1
                channel_available = []
                for i in range (int(number_wavelengths)):
                	channel_available.append(1)
                for i in range(len(path) - 1):
                    #print("counter low "+str(g.ep.counter_low[path[i],path[i+1]]))
                    if g.ep.counter_low[path[i],path[i+1]] > 0:
                        print("traversing edge: " + str(path[i]) + " --> " + str(path[i + 1]))
                        for j in range(int(channels_high),number_wavelengths):
                            print("Channel " + str(j) + "\t" + str(edge_flags[str(path[i]) + " --> " + str(path[i + 1])][j]))
                            available_wavelengths[str(path[i]) + " --> " + str(path[i + 1])][j] = available_wavelengths[str(path[i]) + " --> " + str(path[i + 1])][j] & edge_flags[str(path[i]) + " --> " + str(path[i + 1])][j]
                            channel_available[j] = channel_available[j] & available_wavelengths[str(path[i]) + " --> " + str(path[i + 1])][j]
                        #print str(channel_available)
                    else:
                        temp=0
                        print("traversing edge: " + str(path[i]) + " --> " + str(path[i + 1]))
                        print(" no channel available ")
                        #print("no left")
                        g.ep.weight_low[path[i],path[i+1]] = 9999 #because counter is full/exhausted mo more free channles so this edge can't  be used in any other paths
                        break  #find another path

                if temp == 1:
            		for j in range (int(channels_high),number_wavelengths):
            			if channel_available[j] == 1 and int(dist[tgt]) < 9999:
            				print ("low priority primary path allocated: "+str(path))
            				tmp = 0
            				for i in range(len(path)-1):
	            				edge_flags[str(path[i]) + " --> " + str(path[i + 1])][j] = 0
	            				g.ep.counter_low[path[i],path[i+1]] -= 1
	            				available_wavelengths[str(path[i]) + " --> " + str(path[i + 1])][j] = 0
	            				print("Channel " + str(j) + " allocated for low priority primary: " + " for edge: " + str(path[i]) + " --> " + str(path[i+1]))
	            				#op.write(str(j) + " is the channel allocated\n")
            				break
            		if tmp == 1:
            			print("no primary was path found; request blocked")
                        primary_paths_all[request_key] = "Blocked"
                        #break
                else:
                    if dist[tgt] < 9999:
                        continue
                    else:
                    	print("no primary was path found; request blocked")
                        primary_paths_all[request_key] = "Blocked"
                        break

            if tmp == 0 :
            	established_low += 1
                primary_paths_all[request_key] = path
                #for j in range(len(path) - 1):
                #g.ep.weight_low[path[j], path[j + 1]] += 1
                #print "low prioriy primary path is :" + str(path) + "\n"
                print "Cost of path allocated is " + str(dist[tgt]) + "\n"
            break




number_blocked_requests = 0
for key in primary_paths_all.values():
	if key == "Blocked":
		number_blocked_requests += 1
getcontext().prec = 6
twograde_output(op,number_requests,number_blocked_requests,number_low,number_high,primary_paths_all,backup_paths_all,established_low,established_high)