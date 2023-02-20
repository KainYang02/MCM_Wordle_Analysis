import matplotlib.pyplot as plt
import matplotlib as mpl

x = [1, 2, 3, 4, 5, 6, 7]
y1 = [0, 6, 152, 185, 16, 0, 0]

cmap = mpl.colormaps.get_cmap("gist_rainbow")

plt.xticks(fontproperties = 'Times New Roman', fontsize = 8)
plt.yticks(fontproperties = 'Times New Roman', fontsize = 8)
# plt.title("Cluster Difficulty Analysis", fontdict = {'family' : 'Times New Roman', 'size':15})
plt.xlabel("guess time", fontdict = {'family' : 'Times New Roman', 'size':10})
plt.ylabel("word count", fontdict = {'family' : 'Times New Roman', 'size':10})
plt.bar(x, y1, width=0.6)
plt.savefig('./GuessTimeDistribution.png', dpi = 300, bbox_inches = "tight")
plt.show()