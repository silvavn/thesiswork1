#!/usr/bin/env python	  
import tkinter as tk
from tkinter.simpledialog import *

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

	def close_windows(self):
		self.master.destroy()

#numpy.random.normal(loc=0.0, scale=1.0, size=None)
class DistributionScreen(tk.Frame):
	def __init__(self, master):
		tk.Frame.__init__(self, master)
		self.grid()
		master.title("Distribution Config")

		tk.Label(self, text="Scale in Std. Dev.:").grid(row=0)
		tk.Label(self, text="Size (Num. of points):").grid(row=1)
		
		self.scale = StringVar(self)
		self.scale_entry = tk.Entry(self, textvariable=self.scale)
		self.scale_entry.insert(0, "30")
		self.scale_entry.grid(row=0,column=1)

		self.size = StringVar(self)
		self.size_entry = tk.Entry(self, textvariable=self.size)
		self.size_entry.insert(0, "150")
		self.size_entry.grid(row=1,column=1)

	def close_windows(self):
		self.master.destroy()

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
		
		self.eps = StringVar(self)
		self.eps_entry = tk.Entry(self, textvariable=self.eps)
		self.eps_entry.insert(0, "0.5")
		self.eps_entry.grid(row=1,column=1)

		self.min_samples = StringVar(self)
		self.min_samples_entry = tk.Entry(self, textvariable=self.min_samples)
		self.min_samples_entry.insert(0, "5")
		self.min_samples_entry.grid(row=1,column=1)

		self.n_jobs = StringVar(self)
		self.n_jobs_entry = tk.Entry(self, textvariable=self.n_jobs)
		self.n_jobs_entry.insert(0, "1")
		self.n_jobs_entry.grid(row=1,column=1)

	def close_windows(self):
		self.master.destroy()
