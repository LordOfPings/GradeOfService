import graph_tool.all as gt
from graph_tool import Graph
from random import randint
from header import *

def generate():
	## Generating the requests ##
    all_requests = []   #2D array storing all requests in the end
    for request_count in range(number_requests): #number of requests loop
        request = []    
        temp_source = randint(0,15) #generating random source
        request.append(temp_source) #added source in request array
        while(1):
            temp_target = randint(0,15) #generating random destination node
            if(not(temp_target == temp_source)):#checking that source and target dont match
                temp_id = randint(0,40)#generating random id for priority
                request.append(temp_target)#destination added to request array
                request.append(temp_id)#prioirity id added to request array
                break
        #if not(request in all_requests): #check that requests are not duplicate and not in all_request array
        all_requests.append(request) #then added to all request array
    return (request,all_requests)
    #print request