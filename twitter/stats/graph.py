import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from scipy.interpolate import spline
import datetime
import string
import numpy as np

data ={
				'11/01/2017': {'neg': 8, 'pos': 1},
				'12/01/2017': {'neg': 10, 'pos': 9},
				'13/01/2017': {'neg': 9, 'pos': 5},
				'14/01/2017': {'neg': 14, 'pos': 27},
				'15/01/2017': {'neg': 16, 'pos': 16},
				'16/01/2017': {'neg': 6, 'pos': 9},
				'17/01/2017': {'neg': 14, 'pos': 11},
				'18/01/2017': {'neg': 74, 'pos': 39},
				'19/01/2017': {'neg': 198, 'pos': 92},
				'20/01/2017': {'neg': 378, 'pos': 1196},
				'21/01/2017': {'neg': 75, 'pos': 227}
			}

import matplotlib.pyplot as plt
xdate = []
neg = []
pos = []

for key in sorted(data):
		xdate.append(key)
		tneg = data[key]['neg']
		tpos = data[key]['pos']
		if tneg < 150 and tpos < 150:
			tneg = tneg*10
			tpos = tpos*10
			print key

		neg.append(tneg)
		pos.append(tpos)

x = np.arange(len(xdate))
plt.axis([0,2.5, -100.0,1500.0])
plt.xticks(x,xdate,rotation=45)
xnew = np.linspace(x.min(),x.max(),150)
pos_smooth = spline(x,pos,xnew)
neg_smooth = spline(x,neg,xnew)
posline = plt.plot(xnew,pos_smooth,'b',linewidth=2, label='Positive tweets')
negline = plt.plot(xnew,neg_smooth,'r', linewidth=2, label='Negative tweets')
plt.legend(loc=2)
#red_patch = mpatches.Patch(color='red', label='The red data')
plt.ylabel('No. of tweets')



plt.show()
