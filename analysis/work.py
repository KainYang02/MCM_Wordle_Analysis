import matplotlib.pyplot as plt
import numpy as np
import json

### load frequency table
with open('./freq.json', 'r', encoding = 'utf-8') as fp:
  freq_data = json.load(fp)

data = []

for word in freq_data:
  freq_data[word][0] += np.exp(-20)
  freq_data[word][0] = np.log(freq_data[word][0]) + 20
  data.append((freq_data[word][0], freq_data[word][1] + 3.5))

data.sort()

n = len(data)

data_x = np.arange(0, n)
data_y_0 = np.zeros(n)
data_y_1 = np.zeros(n)

for i in range(n):
  data_y_0[i] = data[i][0]
  data_y_1[i] = data[i][1]

fig, ax = plt.subplots(1, 1)
plt.xticks(fontproperties = 'Times New Roman')
plt.yticks(fontproperties = 'Times New Roman')
ax.plot(data_x, data_y_0, label = '$y_1$')
ax.plot(data_x, data_y_1, label = '$y_2$')
ax.legend(loc = "upper left")
ax.grid(True)
ax.set_xlabel('Word No.', fontdict = {'family' : 'Times New Roman'})
# ax.set_ylabel('Number of reported results')
# ax.set_xlim([50, 400])
# ax.set_ylim([0, 2.7e5])
plt.savefig('fig4')
plt.show()
