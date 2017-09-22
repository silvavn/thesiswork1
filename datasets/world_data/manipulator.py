import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df = pd.read_csv("age_specific_fertility_rates.csv")

df = df.sort_values(['year'], ascending=[True])

snap_headers = np.unique(df['year'])

features = [i for i in df if 'fertility' in i]

datapoints = [df[df['year'] == i] for i in snap_headers]

#print(snap_headers)



for d in datapoints[0:]:
	axes = plt.gca()
	axes.set_xlim([0,400])
	axes.set_ylim([0,400])
	#print (datapoints[1][features])
	X = d[features[1:3]]

	#plt.scatter(X[features[0]], X[features[1]])
	#plt.savefig("{}.png".format(str(np.unique(d['year']))))
	db = DBSCAN(eps=5, min_samples=3, metric='euclidean', algorithm='auto', leaf_size=30, p=None, n_jobs=-1).fit_predict(X)#KMeans(n_clusters=int(np.sqrt(len(d))), random_state=0).fit_predict(X)
	#DBSCAN(eps=5, min_samples=3, metric='euclidean', algorithm='auto', leaf_size=30, p=None, n_jobs=-1).fit_predict(X)

	plt.scatter(X[features[1]], X[features[2]], c=db, cmap='Vega20', alpha=1, s =10)
	plt.savefig("./results/{}.png".format(str(np.unique(d['year'])[0])))
	plt.clf()
	print(np.unique(d['year']), np.unique(db), len(d))
#print(df.head())