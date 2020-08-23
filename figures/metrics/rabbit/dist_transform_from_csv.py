# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 11:44:22 2020

@author: azer
"""

import numpy as np
import matplotlib.pylab as plt
import pandas as pd



# C:\Users\azer\OneDrive\Images\PhysicsPak_Snapshots_01

csv_data=pd.read_csv('C://Users//azer//workspace//uw_thesis//figures//metrics//rabbit//dist_all.csv', sep=',',header=None);

dist_data  = csv_data.values[:,0];

ncol = int(np.sqrt(len(dist_data)));

dist_img = np.reshape(dist_data, (-1, ncol))

#hist, bin_edges = np.histogram(dist_data);
#fig, ax = plt.subplots()
#ax.plot(hist[:-1], bin_edges)
#max_val = max(dist_data);
#dist_norm = [float(i)/max_val for i in dist_data]
#green_array = [x for x in dist_norm if x >= 1e-5];


plt.clf()
green_array = [x for x in dist_data if x >= 1e-5];
plt.hist(green_array, density=True, bins=30)
plt.show();

#plt.imshow(dist_img);
#plt.show();