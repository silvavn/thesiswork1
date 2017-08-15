#!/usr/bin/env python	  
import tkinter as tk
from tkinter.simpledialog import *


#Screen that controls the Click on distribution
#numpy.random.normal(loc=0.0, scale=1.0, size=None)
class DistributionScreen(tk.Frame):
	def __init__(self, master):
		tk.Frame.__init__(self, master)
		self.grid()
		master.title("Distribution Config")

		tk.Label(self, text="Scale in Std. Dev.:").grid(row=0)
		tk.Label(self, text="Size (Num. of points):").grid(row=1)
		tk.Label(self, text="Cluster Label:").grid(row=2)
		
		self.scale = StringVar(self)
		self.scale_entry = tk.Entry(self, textvariable=self.scale)
		self.scale_entry.insert(0, "30")
		self.scale_entry.grid(row=0,column=1)

		self.size = StringVar(self)
		self.size_entry = tk.Entry(self, textvariable=self.size)
		self.size_entry.insert(0, "150")
		self.size_entry.grid(row=1,column=1)

		self.label = StringVar(self)
		self.label_entry = tk.Entry(self, textvariable=self.label)
		self.label_entry.insert(0, "None")
		self.label_entry.grid(row=2,column=1)

	def close_windows(self):
		self.master.destroy()


#Screen that controls the MONIC Framework
#Currently Implements:
#@Tau Match, @Tau Split, @Cluster Shape, @Quadtree Depth, @GridX Resolution, @GridY Resolution
class MONICScreen(tk.Frame):
	def __init__(self, master):
		tk.Frame.__init__(self, master)
		self.grid()
		master.title("MONIC Config")

		tk.Label(self, text="tau match:").grid(row=0)
		tk.Label(self, text="tau split:").grid(row=1)
		tk.Label(self, text="Cluster Shape:").grid(row=2)
		tk.Label(self, text="Quadtree Depth:").grid(row=3)
		tk.Label(self, text="Grid X Resolution:").grid(row=4)
		tk.Label(self, text="Grid Y Resolution:").grid(row=5)

		self.match = StringVar(self)
		self.match_entry = tk.Entry(self, textvariable=self.match)
		self.match_entry.insert(0, "0.5")
		self.match_entry.grid(row=0,column=1)

		self.split = StringVar(self)
		self.split_entry = tk.Entry(self, textvariable=self.split)
		self.split_entry.insert(0, "0.1")
		self.split_entry.grid(row=1,column=1)

		self.shape_state = StringVar(self)
		self.shape_state.set("Circle")
		self.shapemenu = OptionMenu(self, self.shape_state, "Circle", "Box", "Grid", "Quadtree")#, command=self.clustering_controller)
		self.shapemenu.grid(row=2, column=1)

		self.qt_depth = StringVar(self)
		self.qt_depth_entry = tk.Entry(self, textvariable=self.qt_depth)
		self.qt_depth_entry.insert(0, "5")
		self.qt_depth_entry.grid(row=3,column=1)

		self.grid_res_x = StringVar(self)
		self.grid_res_x_entry = tk.Entry(self, textvariable=self.grid_res_x)
		self.grid_res_x_entry.insert(0, "5")
		self.grid_res_x_entry.grid(row=4,column=1)

		self.grid_res_y = StringVar(self)
		self.grid_res_y_entry = tk.Entry(self, textvariable=self.grid_res_y)
		self.grid_res_y_entry.insert(0, "5")
		self.grid_res_y_entry.grid(row=5,column=1)

	def close_windows(self):
		self.master.destroy()


#Screen that controls the DBSCAN Algorithm
#TODO
#Implement metric, algorithm, leaf_size, p
#class sklearn.cluster.DBSCAN(eps=0.5, min_samples=5, metric='euclidean', algorithm='auto', leaf_size=30, p=None, n_jobs=1)
class DBSCANScreen(tk.Frame):
	def __init__(self, master):
		tk.Frame.__init__(self, master)
		self.grid()
		master.title("DBSCAN Config")

		tk.Label(self, text="eps (datapoints max distance):").grid(row=0)
		tk.Label(self, text="minsamples:").grid(row=1)
		tk.Label(self, text="Num Jobs:").grid(row=2)
		
		self.eps = StringVar(self)
		self.eps_entry = tk.Entry(self, textvariable=self.eps)
		self.eps_entry.insert(0, "50.0")
		self.eps_entry.grid(row=0,column=1)

		self.min_samples = StringVar(self)
		self.min_samples_entry = tk.Entry(self, textvariable=self.min_samples)
		self.min_samples_entry.insert(0, "5")
		self.min_samples_entry.grid(row=1,column=1)

		self.n_jobs = StringVar(self)
		self.n_jobs_entry = tk.Entry(self, textvariable=self.n_jobs)
		self.n_jobs_entry.insert(0, "1")
		self.n_jobs_entry.grid(row=2,column=1)

	def close_windows(self):
		self.master.destroy()


#Screen that controls the Kmeans Algorithm
class KmeansScreen(tk.Frame):
	def __init__(self, master):
		tk.Frame.__init__(self, master)
		self.grid()
		master.title("Kmeans Config")


		tk.Label(self, text="Number of Clusters:").grid(row=0)
		tk.Label(self, text="Number of Jobs:").grid(row=1)

		self.num_jobs = StringVar(self)
		self.n_jobs_entry = tk.Entry(self, textvariable=self.num_jobs)
		self.n_jobs_entry.insert(0, "1")
		self.n_jobs_entry.grid(row=1,column=1)
		
		self.num_clusters = StringVar(self)
		self.n_clusters_entry = tk.Entry(self, textvariable=self.num_clusters)
		self.n_clusters_entry.insert(0, "1")
		self.n_clusters_entry.grid(row=0,column=1)

		tk.Button(self, text='Quit', command=self.close_windows).grid(columnspan=2)

		#master.geometry('%dx%d+%d+%d' % (self.winfo_width(), self.winfo_height(), 50, 50))

	def close_windows(self):
		self.master.destroy()
