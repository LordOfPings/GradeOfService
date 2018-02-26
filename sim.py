if(request_served == 50):
		count1 = 0
		keylist = []
		pathlist = []
		for key in primary_paths_high_all.keys():
			keylist.append(key)
			pathlist.append(primary_paths_high_all[key])
			count1 +=1
			if(count1 == 5):
				break
		for key in primary_paths_low_all.keys():
			keylist.append(key)
			pathlist.append(primary_paths_low_all[key])
			count1 +=1
			if(count1 == 10):
				break
		print keylist
		print pathlist
	if(request_served == 100):
		request_served = 0