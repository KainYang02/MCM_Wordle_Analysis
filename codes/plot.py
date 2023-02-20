import matplotlib.pyplot as plt
import matplotlib as mpl

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
y1 = [4.42,4.53,4.89,4.75,4.62,5.12,5.35,4.62,4.32,4.81,4.41,4.64,4.44,4.83,5.18]
y2 = [4.322243908,4.485535433,4.980788539,4.790769557,4.59004243,5.153079435,5.753208606,4.675115169,4.08866181,4.887468064,4.278206682,4.550417164,4.406233003,4.879783792,5.38859081]
c = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
c2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(0, 15):
	y2[i] = y2[i] + 0.05

cmap = mpl.colormaps.get_cmap("gist_rainbow")

plt.xticks(fontproperties = 'Times New Roman', fontsize = 8)
plt.yticks(fontproperties = 'Times New Roman', fontsize = 8)
# plt.title("Cluster Difficulty Analysis", fontdict = {'family' : 'Times New Roman', 'size':15})
# plt.xlabel("average of percentages", fontdict = {'family' : 'Times New Roman', 'size':10})
# plt.ylabel("variance of percentages", fontdict = {'family' : 'Times New Roman', 'size':10})
plt.scatter(x, y1, c="r")
plt.scatter(x, y2, c="b")
plt.savefig('./ClusterDifficultyAnalysis.png', dpi = 300, bbox_inches = "tight")
plt.show()