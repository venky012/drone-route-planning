#importing required libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.path


polygon = [(-5,0), ( -4,3),(-1,1), (0,-5), (-4,-3),(-5,0)]

x,y = np.meshgrid(np.arange(-6,6,1),np.arange(-6,6,1))  # Creating grid in the given polygon
points = list(zip(x.flatten(),y.flatten()))

path2 = matplotlib.path.Path(polygon[::-1])
inside2 = path2.contains_points(points,radius=1e-9)

fig,(ax2)=plt.subplots(ncols=1, figsize=(6,3))
patch2 = plt.Polygon(polygon[::-1], zorder=0, fill=False, lw=2)
ax2.add_patch(patch2)
ax2.scatter(x.flatten(),y.flatten(), c=inside2.astype(float),cmap="RdYlGn", vmin=-.1,vmax=1.2)
#Final
xnew = []
ynew = []
ax2.set_title("cw path")
plt.show()
new = np.array(inside2)
newin = np.array([points[i] for i in range(new.shape[0]) if new[i]])
plt.plot(newin[:,0],newin[:,1],'ro')

from sklearn.cluster import KMeans

plt.scatter(newin[:,0],newin[:,1])
plt.title('True Position')


kmeans = KMeans(n_clusters=3)
kmeans.fit(newin)

plt.scatter(newin[:,0],newin[:,1], c=kmeans.labels_, cmap='rainbow')
plt.scatter(kmeans.cluster_centers_[:,0] ,kmeans.cluster_centers_[:,1], color='black')

import tsp_ga as ga
for i in range(0,3):
    print("Cluster",i+1,"optimal path")
    ga.geneticAlgorithm([ga.City(j[0],j[1]) for j in newin[(kmeans.labels_==i)]],100,20,0.01,50)
