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
#ENDREGION VARIABLES

def scan_timeline():
	print("Scanning " + str(len(timeline)) + " clustering spaces")
	all_overlaps = []
	
	for i in range(len(timeline) - 1):
		print("Comparing clustering " + str(i) + " and clustering " + str(i+1))
		all_overlaps.append(get_matches(timeline[i], timeline[i + 1]))

	return all_overlaps

def save(filename, element):
	pickle.dump(element, open(filename, "wb"))

def load(filename):
	return pickle.load(open(filename, "rb"))

#Given two sets of clusterings, prints the matches between a pair A,B
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

def min_bound_circle(cluster, labels, target):
	xpos = [cluster[j].position[0] for j in range(len(labels)) if labels[j] == target]
	ypos = [cluster[j].position[1] for j in range(len(labels)) if labels[j] == target]

	xavg = np.mean(xpos)
	yavg = np.mean(ypos)

	radius = np.max([np.linalg.norm(np.array([xavg, yavg])-np.array([xpos[i], ypos[i]])) for i in range(len(xpos))])
	return [[xavg, yavg], radius]

#REGION: OVERLAPS

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