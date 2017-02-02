import matplotlib.pyplot as plt 
import numpy as np 

# X = ['NB Classifier','B','C','D','E','F']
# Y = [1,2,3,4,5,6]
# #plt.figure(figsize=(20,12))

# plt.xticks(range(len(X)),X,rotation=50)
# Bar = plt.bar(range(len(X)),Y,align='center',color=['#FF4081', '#64B5F6', '#4DD0E1', '#FFA000', '#90A4AE'],width=0.5,edgecolor= None)

# plt.show()

# #WFMFS

SVM_algorithm_accuracy = (97, 82)
DecisionTree_algorithm_accuracy = (94, 77)
Naive_algorithm_accuracy = (97,78)


ind = np.arange(2)
width = 0.18       # the width of the bars

fig,ax = plt.subplots()
fig.subplots_adjust(left=0.1, right=0.9)
plt.axis([-0.15,2.5, 0,100.0])
ax.set_autoscale_on(False)
rects1 = ax.bar(ind, SVM_algorithm_accuracy, width, color='#56E39F',)
rects2 = ax.bar(ind+width, DecisionTree_algorithm_accuracy, width, color='#59C9A5',)
rects3 = ax.bar(ind+2*width, Naive_algorithm_accuracy, width, color='#5B6C5D',)

#rects2 = ax.bar(ind + width, DecisionTree_algorithm_accuracy, width, color='y', )

# add some text for labels, title and axes ticks
ax.set_ylabel('Accuracy')
#ax.set_title('Scores by group and gender')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('WFMFS', 'BIGRAM'),rotation=45)
ax.legend((rects1[0], rects2[0],rects3[0]), ('SVM Algorithm', 'Decision Tree Algorithm', 'Naive Bayes Algorithm'))


plt.show()