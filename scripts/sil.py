import numpy as np
from numpy import linalg as LA

#	Computes Sil Takes in 3 parameters
#	a numpy array of dimensions number_of_items x number_of_features
#	a numpy array which contains which cluster the nth item belongs too
#	a function which computes the distance between 2 items

def euclideanDistance(itm1 , itm2):
	return LA.norm( itm1- itm2 )

def computeSil( items , clusterNumber , distanceFunction = euclideanDistance):
	
	#Finds the max number of clusters and the needed space
	maxClusterNum = np.amax(clusterNumber) + 1
	tmpDistance = np.zeros(maxClusterNum)
	clusterCount = np.zeros(maxClusterNum)
	sil = np.empty(clusterNumber.size)
	
	i = 0
	
	for itm in items:
		post = clusterNumber[i]
		j = 0
		for jtm in items:
			if i != j:
			
				pos = clusterNumber[j]
				
				tmpDistance[pos] += distanceFunction(itm , jtm)
				clusterCount[pos] += 1
			j += 1
			
		a = tmpDistance[ post ] / clusterCount[post]
		
		#find the clusters closest to the one the item is currently in
		
		b = 1000
		for k in range (0 , maxClusterNum):
			tmp = tmpDistance[k] / clusterNumber[k]
			if tmp < b and k != post and tmpDistance[k] != 0:
				b = tmp
		#compute silhouette coefficient
		
		if a == b:
			sil[i] = 0.0
		else:
			sil[i] = (b - a) / max(a,b) 
		
		clusterCount.fill(0.0)
		tmpDistance.fill(0.0)
		i += 1
	return sil
	


