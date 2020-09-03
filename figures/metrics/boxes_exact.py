

import numpy as np
import matplotlib.pylab as plt
import pandas as pd
import sys
import statistics as stat

cont_side = 5000;
cont_area = cont_side * cont_side;
squ_side = 640.077;
d_gap_2 = 80.0975;
num_sq = 36;

h_gap = 0.01;
r_vals = np.arange(0, d_gap_2, h_gap);


scp_vals = [];
for offset_val in r_vals:
    #print offset_val;
    c_side = cont_side - offset_val;
    s_side = squ_side + offset_val;
    c_area = c_side * c_side;
    s_area = s_side * s_side * num_sq;
    scp_vals.append( (c_area - s_area) / cont_area );


plt.clf()
plt.plot(r_vals, scp_vals, 'b', linewidth=1);
plt.show();
    

