import numpy as np

#TODO: MOVE OUT
#Gets two circles [[x,y], radius] and return the Jaccard index A^B/A
def jaccard_overlap(c1, c2):
	inter = intersection_area(c1, c2)
	return inter / ((c1[1] * c1[1] * np.pi) + (c2[1] * c2[1] * np.pi) - inter)

#TODO: MOVE OUT
#Gets two circles [[x,y], radius] and return the MONIC index: A^B/AUB
def monic_overlap(c1, c2):
	inter = intersection_area(c1, c2)
	return inter / (c1[1] * c1[1] * np.pi)

#TODO: MOVE OUT
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