import graph_tool.all as gt
from graph_tool import Graph
from header import *
from math import *
from decimal import *

def onegrade_output(op,number_requests,number_blocked_requests,number_low,number_high,primary_paths_high_all,primary_paths_low_all,backup_paths_all,established_low,established_high):
	print("\n"+str(number_requests) + " Requests")
	op.write(str(number_requests) + " Requests")
	print("Number of high priority requests: " + str(number_high) + " Number of low priority requests: " + str(number_low))
	op.write("\nNumber of high priority requests: " + str(number_high) + " Number of low priority requests: " + str(number_low))
	print("Number of high priority LightPaths Established: " + str(established_high) + " Number of low priority LightPaths Established: " + str(established_low))
	op.write("\nNumber of high priority LightPaths Established: " + str(established_high) + " Number of low priority LightPaths Established: " + str(established_low)) 
	print("Number of LightPaths Established (NLE): " + str(number_requests - number_blocked_requests))
	op.write("\nNumber of LightPaths Established (NLE): " + str(number_requests - number_blocked_requests))
	print("Blocking probability: " + str(Decimal(number_blocked_requests)/Decimal(number_requests)) + "\n")
	op.write("\nBlocking probability: " + str(Decimal(number_blocked_requests)/Decimal(number_requests)) + "\n")
	print("All high priority primary paths are " + str(primary_paths_high_all))
	print("All alternative paths are " + str(backup_paths_all))
	print("All low priority primary paths are " + str(primary_paths_low_all))

def twograde_output(op,number_requests,number_blocked_requests,number_low,number_high,primary_paths_high_all,primary_paths_low_all,backup_paths_all,established_low,established_high):

	print(str(number_requests) + " Requests")
	op.write(str(number_requests) + " Requests")
	print("Number of high priority requests: " + str(number_high) + " Number of low priority requests: " + str(number_low))
	op.write("\nNumber of high priority requests: " + str(number_high) + " Number of low priority requests: " + str(number_low))
	print("Number of high priority LightPaths Established: " + str(established_high) + " Number of low priority LightPaths Established: " + str(established_low))
	op.write("\nNumber of high priority LightPaths Established: " + str(established_high) + " Number of low priority LightPaths Established: " + str(established_low)) 
	print("Number of LightPaths Established (NLE): " + str(number_requests - number_blocked_requests))
	op.write("\nNumber of LightPaths Established (NLE): " + str(number_requests - number_blocked_requests))
	print("Blocking probability: " + str(Decimal(number_blocked_requests)/Decimal(number_requests)) + "\n")
	op.write("\nBlocking probability: " + str(Decimal(number_blocked_requests)/Decimal(number_requests)) + "\n")
	print("All high priority primary paths are " + str(primary_paths_high_all))
	print("All low priority primary paths are " + str(primary_paths_low_all))
	print("All alternative paths are " + str(backup_paths_all))

def threegrade_output(op,number_requests,number_blocked_requests,number_low,number_high,number_med,primary_paths_high_all,primary_paths_med_all,primary_paths_low_all,backup_paths_all,established_low,established_high,established_med):

	print(str(number_requests) + " Requests")
	op.write(str(number_requests) + " Requests")
	print("Number of high priority requests: " + str(number_high) + " Number of low priority requests: " + str(number_low) + " Number of medium priority request: " +str(number_med))
	op.write("\nNumber of high priority requests: " + str(number_high) + " Number of low priority requests: " + str(number_low) + " Number of medium priority request: " +str(number_med))
	print("Number of high priority LightPaths Established: " + str(established_high) + " Number of low priority LightPaths Established: " + str(established_low)+ " Number of medium priority LightPaths Established: " +str(established_med))
	op.write("\nNumber of high priority LightPaths Established: " + str(established_high) + " Number of low priority LightPaths Established: " + str(established_low) + " Number of medium priority LightPaths Established: " +str(established_med))
	print("Number of LightPaths Established (NLE): " + str(number_requests - number_blocked_requests))
	op.write("\nNumber of LightPaths Established (NLE): " + str(number_requests - number_blocked_requests))
	print("Blocking probability: " + str(Decimal(number_blocked_requests)/Decimal(number_requests)) + "\n")
	op.write("\nBlocking probability: " + str(Decimal(number_blocked_requests)/Decimal(number_requests)) + "\n")
	print("All high priority primary paths are " + str(primary_paths_high_all))
	print("All alternative paths are " + str(backup_paths_all))
	print("All mmedium priority primary paths are " + str(primary_paths_med_all))
	print("All low priority primary paths are " + str(primary_paths_low_all))
