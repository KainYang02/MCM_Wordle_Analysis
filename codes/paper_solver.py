import math
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

COLOR_MAP_SET = ['Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds', 'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu', 'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']
COLOR_MAP_SET2 = ['binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink', 'spring', 'summer', 'autumn', 'winter', 'cool', 'Wistia', 'hot', 'afmhot', 'gist_heat', 'copper']

WORD_NUMBER = 359
CLUSTER_NUMBER = 15
SIGNLE_WORD_LINE = 11
PERCENT_NUMBER = 7

cmap = mpl.colormaps.get_cmap("gist_rainbow")
plt.rc('font', family = 'Times New Roman')

class Word:
	def __init__(self, word : str, cluster_id : int):
		self.word = word
		self.cluster_id = cluster_id
		self.percent = np.zeros(7, dtype = int) # percent[i] : step i + 1 to correct
		self.entro = 0.0
		self.diff = 0
		self.frequency = 0

	def set_percent(self, index : int, value : int):
		assert 0 <= index
		assert index < 7
		self.percent[index] = value

	def which_is_most(self):
		most_id = 0
		for i in range(1, 7):
			if self.percent[i] > self.percent[most_id]:
				most_id = i
		return most_id

	def calc_average(self):
		num = 0
		sum = 0.0
		for i in range(7):
			num += self.percent[i]
			sum += (i + 1) * self.percent[i]
		return sum / num

	def calc_variance(self):
		ave = self.calc_average()
		num = 0
		sig = 0.0
		for i in range(7):
			num += self.percent[i]
			sig += (i + 1 - ave) * (i + 1 - ave) * self.percent[i]
		sig /= num
		return math.sqrt(sig)

	def calc_different_letter(self):
		return len(set(self.word))

def __main__():
	data_file = open("cluster_final.txt", "r")

	word_list = [[] for cluster_id in range(CLUSTER_NUMBER)]
	for word_id in range(WORD_NUMBER):
		datas = []
		for line in range(SIGNLE_WORD_LINE):
			datas.append(data_file.readline())
		word = Word(datas[0].split('\n')[0], int(datas[1]))
		for perc_id in range(PERCENT_NUMBER):
			word.percent[perc_id] = int(datas[3 + perc_id])
		word_list[word.cluster_id].append(word)
		# print(word.word)

	word_result_cluster(word_list)

def word_result_cluster(word_list):
	plt.xticks(fontproperties = 'Times New Roman', fontsize=8)
	plt.yticks(fontproperties = 'Times New Roman', fontsize=8)
	# plt.title("Word Result Clusters", fontdict = {'family' : 'Times New Roman', 'size':15})
	plt.xlabel("Average of percentages", fontdict = {'family' : 'Times New Roman', 'size':10})
	plt.ylabel("Variance of percentages", fontdict = {'family' : 'Times New Roman', 'size':10})
	x = []
	y = []
	c = []
	for cluster_id in range(CLUSTER_NUMBER):
		for data in word_list[cluster_id]:
			x.append(data.calc_average())
			y.append(data.calc_variance())
			c.append(cluster_id)
	plt.scatter(x, y, s = 7, c = c, cmap = cmap)
	plt.savefig('./WordResultClusters.png', dpi = 300, bbox_inches = "tight")
	plt.show()

__main__()