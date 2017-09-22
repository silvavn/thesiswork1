#!/usr/bin/env python	
'''
List of regions in this file:
	VARIABLES
	OVERLAPS
	SHAPES
'''
import numpy as np
import pickle

#REGION VARIABLES
#colors
WHITE = '#fff'
BLACK = '#000'

RED = '#f00'
GREEN = '#0f0'
BLUE = '#00f'

YELLOW = '#ff0'
CYAN = '#0ff'
MAGENTA = '#f0f'

GRAY = '#aaa'

datapoint_radius = 3

#canvas declaration
canvas_width = 800
canvas_height = 800

#stores a timeline of clustering spaces
timeline = []

#array of datapoints
datapoints = []

#dictionary of ids
ids = {}

#ENDREGION VARIABLES

#Gets -
#Return an array of overlaps
def scan_timeline():
	print("Scanning " + str(len(timeline)) + " clustering spaces")
	all_overlaps = []
	
	for i in range(len(timeline) - 1):
		print("Comparing clustering " + str(i) + " and clustering " + str(i+1))
		all_overlaps.append(get_matches(timeline[i], timeline[i + 1]))

	return all_overlaps


def gen_clusterid(t, cid):
	#print(type(t).__name__, t, type(cid).__name__, cid)
	if "int" in type(cid).__name__: return chr(cid + 65)+ str(t)
	else:
		name = lambda t, c: str(chr(c + 65)) + str(t)
		res = []
		for i in cid: 
			#print(name(t, i)
			res.append(name(t, i))
		return res


#Gets a filename and an array
#Saves the given array to a file using pickle in binary.
def save(filename, element):
	pickle.dump(element, open(filename, "wb"))


#Gets a filename
#Loads the given file to memory. The file must be binary.
def load(filename):
	return pickle.load(open(filename, "rb"))

#Receives a set of points, a set of labels and a target label
#Returns a tuple of arrays that contain the x, y positions of points that have the target label
def get_target_cluster(cluster, labels, target):
	xpos = [cluster[j].position[0] for j in range(len(labels)) if labels[j] == target]
	ypos = [cluster[j].position[1] for j in range(len(labels)) if labels[j] == target]
	return xpos, ypos


#REGION TRANSITIONS
def det(comparisons, timestep, tmatch, tsplit):
	X = [i[0] for i in comparisons]
	Y = [i[1] for i in comparisons]
	M = {}

	for c in comparisons:
		M[c[0], c[1]] = c[2]
	
	deadlist = []
	split_list = []

	for x in X:
		split_candidates = []
		absorb_survivals
		
		survival_cluster = None
		survival_score = -1
		for y in Y:
			m_cell = M[x, y]
			if m_cell >= tmatch:
				if m_cell > survival_score:
					survival_cluster = y
			elif m_cell >= tsplit:
				split_candidates.extend(y)
				split_union.extend(y)
		
		if survival_cluster == None or len(split_candidates) < 1:
			deadlist.extend(x)
		elif split_candidates > 1:
			for i in split_candidates:
				if M[x, i] >= tmatch:
					split_list.extend(i)
		else:
			absorb_survivals.append(x)
			absorb_survivals.append(survival_cluster)

	for y in Y:
		pass



def detect_external_transitions2(comparisons, timestep, tmatch, tsplit):
	match_pairs = {}
	match_splits = {}
	match_merge = {}
	
	new_timelines = []
	ceased_timelines = []

	X = np.unique([i[0] for i in comparisons])
	Y = np.unique([i[1] for i in comparisons])
	M = {}

	for c in comparisons:
		M[c[0], c[1]] = c[2]

	if timestep == 0: print("\n{} compose the initial clustering space.".format(gen_clusterid(timestep, X)))
	print("\nAt timestep {} to {}".format(timestep, timestep + 1))
	
	for x in X:
		survival_cluster = None
		survival_score = -1
		split_sum = 0

		for y in Y:
			if M [x,y] >= tmatch:
				try:
					match_merge[y].append(x)
				except:
					match_merge[y] = [x]

				if M[x,y] > survival_score:
					survival_cluster = y
			elif M[x,y] >= tsplit:
				try:
					match_splits[x].append(y)
				except:
					match_splits[x] = [y]
				split_sum += M[x,y]

		if survival_cluster == None and len(match_splits) == 0:
			#pass
			ceased_timelines.append(x)
		elif split_sum < tmatch and len(match_splits) > 0:
			ceased_timelines.append(x)

		
		for key, value in match_splits.items():
			if len(value) > 1:
				print("Cluster {} splits into clusters {}".format(gen_clusterid(timestep, key), gen_clusterid(timestep + 1, value)))
				ceased_timelines.append(key)
				new_timelines.extend(value)
	
	for y in Y:
		if y in match_merge.keys():
			if len(match_merge[y]) > 1:
				print("Clusters {} are absorbed by cluster {}".format(gen_clusterid(timestep, match_merge[y]), gen_clusterid(timestep+1, y)))
				new_timelines.append(y)
				ceased_timelines.extend(match_merge[y])
	for y in Y:
		if y in match_merge.keys():
			if len(match_merge[y]) == 1 and match_merge[y][0] not in ceased_timelines:
				print("Cluster {} survives as cluster {}".format(gen_clusterid(timestep, match_merge[y]), gen_clusterid(timestep + 1, y)))

		if y not in match_pairs and y not in match_splits and y not in match_merge:
			new_timelines.append(y)

	if len(new_timelines) > 0: print("New timelines: {}".format(gen_clusterid(timestep + 1, np.unique(new_timelines))))
	if len(ceased_timelines) > 0: print("Ceased timelines: {}".format(gen_clusterid(timestep, np.unique(ceased_timelines))))

	if timestep == len(timeline) - 2:
		print("\nThe end! All timelines ceased")

def detect_external_transitions(comparisons, timestep, tmatch, tsplit):
	match_pairs = {}
	match_splits = {}
	match_merge = {}
	match_disappears = []
	match_appears = []

	for c in comparisons:
		if c[2] >= tmatch: #c2 is the monic overlap
			try:
				match_pairs[c[0]].append(c[1])
			except:
				match_pairs[c[0]] = [c[1]]

		if c[2] >= tmatch:
			try:
				match_merge[c[1]].append(c[0])
			except:
				match_merge[c[1]] = [c[0]]

		if c[2] >= tsplit:
			try:
				match_splits[c[0]].append(c[1])
			except:
				match_splits[c[0]] = [c[1]]

	if timestep == 0:
		print("\n{} compose the initial clustering space.\n".format([i[0] for i in comparisons]))

	print("At timestep {} to {}".format(timestep, timestep + 1))
	
	new_timelines = []
	ceased_timelines = []

	#BUG!!!
	#absorbed is called twice
	for key, value in match_pairs.items():
		if len(value) == 1 and len(match_merge[value[0]]) == 1: 
			print("Cluster {} matches with clusters {}".format(gen_clusterid(timestep, key), gen_clusterid(timestep + 1, value)))
		
		elif len(match_merge[value[0]]) > 1: 
			print("Clusters {} are absorbed by cluster {}".format(gen_clusterid(timestep, match_merge[value[0]]), gen_clusterid(timestep+1, value)))
			new_timelines.extend(value)
			ceased_timelines.extend(match_merge[value[0]])
			break

	for key, value in match_splits.items():
		if len(value) > 1:
			print("Cluster {} splits into clusters {}".format(gen_clusterid(timestep, key), gen_clusterid(timestep + 1, value)))
			ceased_timelines.append(key)
			new_timelines.extend(value)

	for c in comparisons:
		#print(c[0])
		if c[1] not in match_appears and c[1] not in match_pairs and (c[1] not in match_splits):
			match_appears.append(c[1])

		if c[0] not in match_disappears and c[0] not in match_pairs and (c[0] not in match_splits or len(match_splits[c[0]]) < 2): # and c[0] not in match_merge:
			match_disappears.append(c[0])

	if len(match_disappears) > 0: 
		print("Clusters {} disappeared :(".format(gen_clusterid(timestep, match_disappears)))
		ceased_timelines.extend(match_disappears)
	
	if len(match_appears) > 0: 
		print("Clusters {} emerged :)".format(gen_clusterid(timestep + 1, match_disappears)))
		new_timelines.extend(match_appears)

	print("New timelines: {}".format(gen_clusterid(timestep + 1, new_timelines)))
	print("Ceased timelines: {}\n".format(gen_clusterid(timestep, ceased_timelines)))

#ENDREGION TRANSITIONS


#REGION SHAPES

#Gets a set of points, all labels and a target label
#Returns a circle structure in the form [[x,y] radius]
#this do NOT return the true minimum bouding circle, but a circle that has the center in the mean
#of the cluster and radius is equal to the distance between the farthest point and the center
def min_bound_circle(cluster, labels, target):
	xpos, ypos = get_target_cluster(cluster, labels, target)

	xavg = np.mean(xpos)
	yavg = np.mean(ypos)

	radius = max([np.linalg.norm(np.array([xavg, yavg])-np.array([xpos[i], ypos[i]])) for i in range(len(xpos))])
	return [[xavg, yavg], radius]


#Gets a set of points, all labels and a target label
#Returns a minimum bounding box for the points that have the target label
def min_bound_box(cluster, labels, target):
	xpos, ypos = get_target_cluster(cluster, labels, target)
	return [min(xpos), min(ypos), max(xpos), max(ypos)]


#Gets a set of points and a bounding box
#Returns True if any of the points collide with the bounding box
#Returns False otherwise
def cluster_collision(cluster, box):
	for p in cluster:
		if (p.position[0] >= box[0] and p.position[0] <= box[2]) and (p.position[1] >= box[1] and p.position[1] <= box[3]):
			return True
	return False


#Gets a set of points, a set of labels, a target label and a resolution array [x,y]
#Returns a grid shape where the shape represent the cluster given a resolution
def grid_shape(cluster, labels, target, resolution=[5,5]):
	bb = min_bound_box(cluster, labels, target)
	x_side = (bb[2] - bb[0]) / resolution[0]
	y_side = (bb[3] - bb[1]) / resolution[1]
	
	cells = []

	for y in range(resolution[1]):
		for x in range(resolution[0]):
			x_min = x * x_side + bb[0]
			x_max = x_min + x_side
			y_min = y * y_side + bb[1]
			y_max = y_min + y_side
			box = [x_min, y_min, x_max, y_max]
			if cluster_collision(cluster, box):
				cells.append(box)
	return cells


#Gets a set of points, a bounding box arra [x0, y0, x1, y1] and a recursion depth
#returns a shape given by a quadtree
def quadtree(cluster, bb, depth=5):
	if(depth == 0): return []
	boxes = [bb]
	
	halfx = (bb[0]+bb[2])/2
	halfy = (bb[1]+bb[3])/2
	bb0 = [bb[0], bb[1], halfx, halfy]
	bb1 = [halfx, bb[1], bb[2], halfy]
	bb2 = [halfx, halfy, bb[2], bb[3]]
	bb3 = [bb[0], halfy, halfx, bb[3]]
	candidates = [bb0,bb1,bb2,bb3]
	child = []

	for i in candidates: 
		if cluster_collision(cluster, i):
			child.append(i)
			boxes.append(i)

	for i in child:
		boxes.extend (quadtree(cluster, i, depth - 1))
	return boxes

#ENDREGION SHAPES

#REGION OVERLAPS

#Given two clustering spaces, return the overlap table bertween the clusters in the given spaces
#The overlap table is an array that contain the overlap for a pair of clusters
#The internal array is as follows [cluster1, cluster2, MONIC OVERLAP, JACCARD OVERLAP]
def get_matches(set1, set2):
	'''pos = [i.position for i in set1]
	print(np.mean([i[0] for i in pos]))
	print(np.mean([i[1] for i in pos]))

	pos = [i.position for i in set2]
	print(np.mean([i[0] for i in pos]))
	print(np.mean([i[1] for i in pos]))'''

	labels_a = [i.label for i in set1]
	labels_b = [i.label for i in set2]

	get_clusters = lambda x, y: [[min_bound_circle(x, y, i), i] for i in np.unique(y)]
	clusters_a = get_clusters(set1, labels_a)
	clusters_b = get_clusters(set2, labels_b)
	overlap_table = []
	for i in clusters_a:
		for j in clusters_b:
			overlap_table.append([i[1], j[1], monic_overlap(i[0],j[0]), jaccard_overlap(i[0], j[0])])
	return overlap_table


#Gets two circles [[x,y], radius] and return the Jaccard index A^B/A
def jaccard_overlap(c1, c2):
	inter = intersection_area(c1, c2)
	return inter / ((c1[1] * c1[1] * np.pi) + (c2[1] * c2[1] * np.pi) - inter)


#Gets two circles [[x,y], radius] and return the MONIC index: A^B/AUB
def monic_overlap(c1, c2):
	inter = intersection_area(c1, c2)
	return inter / (c1[1] * c1[1] * np.pi)


#Based on this: https://stackoverflow.com/questions/4247889/area-of-intersection-between-two-circles
#and this: http://mathworld.wolfram.com/Circle-CircleIntersection.html
#this just calculates between circles!
def intersection_area(c0, c1):
	x0, y0, r0 = c0[0][0], c0[0][1], c0[1]
	x1, y1, r1 = c1[0][0], c1[0][1], c1[1]

	rr0 = r0 * r0
	rr1 = r1 * r1
	d = np.linalg.norm(np.array([x0,y0]) - np.array([x1,y1]))
	#np.sqrt((x1 - x0) * (x1 - x0) + (y1 - y0) * (y1 - y0))
	#print(r0, np.pi * rr0, r1, np.pi * rr1)

	#Circles do not overlap
	if d > r1 + r0: return 0
	#Circle1 is completely inside circle0
	elif d <= np.absolute(r0 - r1) and r0 >= r1: 
		#print('r0')
		return np.pi * rr1 #/ (np.pi * rr0)
	#Circle0 is completely inside circle1
	elif d <= np.absolute(r0 - r1) and r0 < r1: 
		#print('r1')
		return np.pi * rr0 #/ (np.pi * rr1)
	else:
		#print('else')
		phi = (np.arccos((rr0 + (d * d) - rr1) / (2 * r0 * d))) * 2
		theta = (np.arccos((rr1 + (d * d) - rr0) / (2 * r1 * d))) * 2
		area1 = 0.5 * theta * rr1 - 0.5 * rr1 * np.sin(theta)
		area2 = 0.5 * phi * rr0 - 0.5 * rr0 * np.sin(phi)
		overlap = area1 + area2
		total = (np.pi * rr0 + np.pi * rr1) - overlap
		return overlap #/total

#ENDREGION OVERLAPS