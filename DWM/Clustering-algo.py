def InitializeMeans(items, k, cMin, cMax):

	# Initialize means to random numbers between
	# the min and max of each column/feature	
	f = len(items[0]); # number of features
	means = [[0 for i in range(f)] for j in range(k)];
	
	for mean in means:
		for i in range(len(mean)):

			# Set value to a random float
			# (adding +-1 to avoid a wide placement of a mean)
			mean[i] = uniform(cMin[i]+1, cMax[i]-1);

	return means;
