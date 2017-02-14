# {
    #     'banjallikattu': {'neg': 608, 'pos': 327},
    #     'banpeta': {'neg': 194, 'pos': 1306}
    # }

import matplotlib.pyplot as plt


# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Positive', 'Negative'
sizes = [32700/(608+327),60800/(608+327)]
#explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
plt.title('Tweets on #BanJallikattu')
plt.pie(sizes, labels=labels, autopct='%1.1f%%',
        startangle=90, colors = ['#FFB543','#26CEFF'])
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
