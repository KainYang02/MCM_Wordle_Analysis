import re
import json
import math
import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

CLUSRER_NUMBER = 15

class Daily_Data :
	def __init__(self, date : str, id : int, word : str, easy : int, hard : int):
		self.date = date
		self.id = id
		self.word = word
		self.easy = easy
		self.hard = hard
		self.percent = np.zeros(7, dtype = int) # percent[i] : step i + 1 to correct
		self.entro = 0.0
		self.diff = 0
		self.cluster_id = 0
		self.frequency = 0

	def set_percent(self, index : int, value : int):
		assert 0 <= index
		assert index < 7
		self.percent[index] = value

	def print(self):
		print('{')
		print(str(self.id) + ' ' + self.date + ' ' + self.word)
		print(str(self.easy) + ' ' + str(self.hard))
		print(
			str(self.percent[0]) + ' ' + 
			str(self.percent[1]) + ' ' + 
			str(self.percent[2]) + ' ' + 
			str(self.percent[3]) + ' ' + 
			str(self.percent[4]) + ' ' + 
			str(self.percent[5]) + ' ' + 
			str(self.percent[6])
		)
		print('}')

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

	def calc_weight_3(self):
		return self.diff

	def calc_different_letter(self):
		return len(set(self.word))


def __init__(daily_data_list):
	ave_percent = np.zeros(7, dtype = float)
	for data in daily_data_list:
		for i in range(7):
			ave_percent[i] += data.percent[i]
	ave_percent /= len(daily_data_list)
	return ave_percent

def __main__():
	daily_data_list = []
	load_standard(daily_data_list)
	load_diff(daily_data_list)
	load_entro(daily_data_list)
	load_frequency(daily_data_list)
	ave_percent = __init__(daily_data_list)
	ave_percent = np.ones(7)

	# letter_frequency = calc_letter_frequency(daily_data_list)

	# data_viewer_letter(daily_data_list)
	# data_viewer_double_letter(daily_data_list)
	# data_viewer_diff_and_percent(daily_data_list)
	calc_k_means_cluster(daily_data_list, ave_percent)
	# data_viewer_cluster_all(daily_data_list)

	for i in range(CLUSRER_NUMBER):
		data_viewer_cluster(daily_data_list, i)

# ---- k-means cluster ----

def calc_distance(a : Daily_Data, b : Daily_Data, ave_percent):
	sum = 0
	for i in range(7):
		sum += ((a.percent[i] - b.percent[i])**2) / ave_percent[i]
	return math.sqrt(sum)

def calc_sumdis(a, b, daily_data_list, ave_percent):
	sum = 0
	for c in b:
		sum += calc_distance(daily_data_list[a], daily_data_list[c], ave_percent)
	return sum

def calc_k_means_cluster(daily_data_list, ave_percent, cluster_number = CLUSRER_NUMBER, cluster_round = 100, if_print : bool = True):
	n = len(daily_data_list)
	center_list = [random.randint(0, len(daily_data_list))]
	prob = np.zeros(len(daily_data_list), dtype = float)
	for _i in range(1, cluster_number):
		sumprob = 0
		for i in range(0, len(daily_data_list)):
			prob[i] = np.array([calc_distance(daily_data_list[i], daily_data_list[center_list[j]], ave_percent) for j in range(_i)]).min()
			sumprob += prob[i]
		for i in range(0, len(daily_data_list)):
			prob[i] /= 1.0 * sumprob
		prob_c = random.random()
		for i in range(0, len(daily_data_list)):
			if prob[i] > prob_c:
				center_list.append(i)
				break
			else:
				prob_c -= prob[i]
	# print(center_list)
	# return

	while cluster_round > 0:
		# print(cluster_round, "++++++++++++++")
		cluster_round -= 1
		
		for data in daily_data_list:
			data.cluster_id = -1

		for cluster_id in range(cluster_number):
			daily_data_list[center_list[cluster_id]].cluster_id = cluster_id
		
		for data in daily_data_list:
			if data.cluster_id != -1:
				# print(data.word, data.cluster_id)
				continue
			best_data_cluster_id = 0
			dis = calc_distance(data, daily_data_list[center_list[0]], ave_percent)
			for cluster_id in range(1, cluster_number):
				dis_new = calc_distance(data, daily_data_list[center_list[cluster_id]], ave_percent)
				if dis_new < dis:
					dis = dis_new
					best_data_cluster_id = cluster_id
			data.cluster_id = best_data_cluster_id

#		for i in range(n):
#			print(daily_data_list[i].cluster_id)

		for cluster_id in range(cluster_number):
			cur_list = []
			for i in range(n):
				if daily_data_list[i].cluster_id == cluster_id:
					cur_list.append(i)

			best_cluster_center_id = cur_list[0]
			best_cluster_center_sum = calc_sumdis(cur_list[0], cur_list, daily_data_list, ave_percent)
			for i in range(1, len(cur_list)):
				cur_sum = calc_sumdis(cur_list[i], cur_list, daily_data_list, ave_percent)
				if cur_sum < best_cluster_center_sum:
					best_cluster_center_sum = cur_sum
					best_cluster_center_id = cur_list[i]
			center_list[cluster_id] = best_cluster_center_id

			# print(cluster_id, best_cluster_center_id)

	plt.clf()
	ax = plt.subplot(projection = '3d')
	ax.set_xlabel("average")
	ax.set_ylabel("variance")
	ax.set_zlabel("3")

	if if_print:
		for cluster_id in range(cluster_number):
			x = []
			y = []
			z = []
			for data in daily_data_list:
				if data.cluster_id != cluster_id:
					continue
				x.append(data.calc_average())
				y.append(data.calc_variance())
				z.append(data.calc_weight_3())
				print(data.word, data.calc_weight_3(), data.diff)
			ax.scatter(x, y, z)

	plt.show()

	cluster_file = open("cluster.txt", "w")
	__data = sorted(daily_data_list, key = lambda t : t.cluster_id)

	for data in __data:
		cluster_file.write(data.word + '\n' + str(data.cluster_id) + '\n' + str(data.calc_different_letter()) + "\n")
		for i in range(7):
			cluster_file.write(str(data.percent[i]) + '\n')
		cluster_file.write('\n')

	cluster_information = open("cluster_information.txt", "w")
	for cluster_id in range(cluster_number):
		cluster_node = []
		for data in daily_data_list:
			if data.cluster_id != cluster_id:
				continue
			cluster_node.append(data.percent)
		cluster_min = np.zeros(7)
		cluster_max = np.zeros(7)
		cluster_information.write(str(cluster_id) + '\n')
		for i in range(7):
			cur_data = np.array([cluster_node[j][i] for j in range(len(cluster_node))])
			cluster_min[i] = cur_data.min()
			cluster_max[i] = cur_data.max()
			cluster_information.write(str(cluster_min[i]) + '\n' + str(cluster_max[i]) + '\n')


# ---- load datas ----

def load_frequency(daily_data_list):
	file = open("frequency.txt", "r")
	lines = file.readlines()
	datas = {}
	for line in lines:
		cur = re.split(' |\n', line)
		datas[cur[0]] = float(cur[1])
	for i in range(len(daily_data_list)):
		cur = datas[daily_data_list[i].word]
		daily_data_list[i].frequency = math.log(cur + 1e-25)

def load_standard(daily_data_list):
	plt.clf()
	data_file = open("standard_oneline.txt", "r")
	lines = data_file.readlines()
	for line in lines:
		cur_data = line.split(' ');
		cur_daily_data = Daily_Data(
			cur_data[0], 
			int(cur_data[1]),
			cur_data[2],
			int(cur_data[3]),
			int(cur_data[4])
		)
		for i in range(0, 7):
			cur_daily_data.set_percent(i, int(cur_data[5 + i]))
		daily_data_list.append(cur_daily_data)
		# cur_daily_data.print()

def load_diff(daily_data_list):
	plt.clf()
	diff_file = open("diff_sim_small3.txt", "r")
	lines = diff_file.readlines()
	diff_datas = {}
	for line in lines:
		cur_value = re.split(' |\n', line)
		diff_datas[cur_value[0]] = float(cur_value[1])
		# print(float(cur_value[1]))
	for i in range(len(daily_data_list)):
		cur_diff = diff_datas[daily_data_list[i].word]
		daily_data_list[i].diff = cur_diff


def load_entro(daily_data_list):
	entro_file = open("entro.txt", "r")
	lines = entro_file.readlines()
	entro_datas = {}
	for line in lines:
		cur_value = re.split(' |\n', line)
		entro_datas[cur_value[0]] = float(cur_value[1])
	for i in range(len(daily_data_list)):
		cur_entro = entro_datas[daily_data_list[i].word]
		daily_data_list[i].entro = cur_entro
		# print(cur_entro)


# ---- data viewer ----

def data_viewer_cluster(daily_data_list, cluster_id):
	ax = plt.subplot()
	ax.set_xlabel("step")
	ax.set_ylabel("percent")
	x = np.arange(7)
	for data in daily_data_list:
		if data.cluster_id == cluster_id:
			ax.plot(x, data.percent)
	plt.show()

def data_viewer_cluster_all(daily_data_list):
	ax = plt.subplot()
	ax.set_xlabel("step")
	ax.set_ylabel("percent")
	x = np.arange(7)
	for data in daily_data_list:
		if data.cluster_id == 4:
			ax.plot(x, data.percent, c = plt.cm.Set3(0))
	for data in daily_data_list:
		if data.cluster_id == 5:
			ax.plot(x, data.percent, c = plt.cm.Set3(2))
	for data in daily_data_list:
		if data.cluster_id == 3:
			ax.plot(x, data.percent, c = plt.cm.Set3(4))
	plt.show()


def data_viewer_letter(daily_data_list):
	split_num = 10
	split_siz = 2.0 / split_num
	x = np.linspace(3, 5, split_num)
	y = [np.zeros(split_num, dtype = int) for i in range(5)]
	num = np.zeros(5)

	plt.clf()
	plt.title("If double letter exist.")
	plt.xlabel("Solve Step Average")
	plt.ylabel("Percent")
	for data in daily_data_list:
		ave = data.calc_average()
		
		if ave < 3 or ave > 5:
			continue
		
		for i in range(split_num):
			if i * split_siz + 3 <= ave and ave < (i + 1) * split_siz + 3:
				letter_number = data.calc_different_letter() - 1
				y[letter_number][i] += 1
				num[letter_number] += 1
	
	for i in range(5):
		plt.plot(x, y[i]/num[i], label = i)
	plt.show()

def data_viewer_diff_and_percent(daily_data_list):
	x = np.arange(1, 8)
	fig, plts = plt.subplots(1, 7, figsize = (20, 2.7), layout='constrained');
	for data in daily_data_list:
		# print(data.diff)
		plts[int(data.diff)].plot(x, data.percent)
	plt.show()


def data_viewer1(daily_data_list):
	split_num = 10
	split_siz = 6.0 / split_num
	x =	np.linspace(1, 7, split_num)
	y = [np.zeros(split_num, dtype = float) for i in range(9)]
	num = np.zeros(9, dtype = float)
	for data in daily_data_list:
		for i in range(split_num):
			ave = data.calc_average()
			if 1.0 + split_siz * i <= ave and ave < 1.0 + split_siz * (i + 1):
				y[int(round(data.entro / 0.5))][i] += 1
				num[int(round(data.entro / 0.5))] += 1
	for i in range(9):
		if num[i] == 0:
			continue
		for j in range(split_num):
			y[i][j] /= num[i]
		plt.plot(x, y[i])
	plt.show()
	return

def data_viewer2(daily_data_list):
	x = []
	y = []
	plt.xlabel("Average")
	plt.ylabel("Variance")
	for data in daily_data_list:
		# print(data.entro)
		plt.scatter([data.calc_average()], [data.calc_variance()], c = plt.cm.Set1(int(round(data.entro))))
	plt.scatter(x, y)
	plt.show()
	return

def data_viewer3(daily_data_list):
	x = np.arange(1, 8)
	fig, plts = plt.subplots(1, 7, figsize=(20, 2.7), layout='constrained');
	entro_num = np.zeros(7, dtype = int)
	entro_sum = np.zeros(7, dtype = float)
	for data in daily_data_list:
		cur_id = data.which_is_most()
		plts[cur_id].plot(x, data.percent)
		entro_num[cur_id] += 1
		entro_sum[cur_id] += data.entro
	plt.show()
	for i in range(7):
		print(entro_num[i], entro_sum[i] / entro_num[i])

# ---- calc letter frequency

def calc_letter_frequency(daily_data_list, if_print : bool = False):
	letter_number = np.zeros(26, dtype = float)
	sum = 0
	for data in daily_data_list:
		for ch in data.word:
			sum += 1
			letter_number[ord(ch) - ord("a")] += 1
	for i in range(0, 26):
		letter_number[i] /= 1.0 * sum
		if (if_print):
			print(chr(ord("a") + i) + ' ' + str(letter_number[i]))

	return letter_number

__main__()