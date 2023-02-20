import matplotlib.pyplot as plt
import numpy as np
import json

plt.rc('font', family = 'Times New Roman')

### load frequency table
with open('./freq.json', 'r', encoding = 'utf-8') as fp:
  freq_data = json.load(fp)

for word in freq_data:
  freq_data[word] += np.exp(-50)
  freq_data[word] = np.log(freq_data[word]) + 50

# print(freq_data["abyss"])
# print(min(freq_data))

### load excel data
load_data = []

file = open("standard.txt", 'r')
try:
  while True:
    line = file.readline()
    if line:
      dict = {}
      dict["id"] = int(file.readline())
      dict["word"] = file.readline().strip()
      dict["freq"] = freq_data[dict["word"]]
      dict["result_number"] = int(file.readline())
      dict["hard_number"] = int(file.readline())
      dict["1"] = int(file.readline())
      dict["2"] = int(file.readline())
      dict["3"] = int(file.readline())
      dict["4"] = int(file.readline())
      dict["5"] = int(file.readline())
      dict["6"] = int(file.readline())
      dict["X"] = int(file.readline())
      total = dict["1"] + dict["2"] + dict["3"] + dict["4"] + dict["5"] + dict["6"]
      dict["avg"] = (1 * dict["1"] + 2 * dict["2"] + 3 * dict["3"] + 4 * dict["4"] + 5 * dict["5"] + 6 * dict["6"]) / total
      load_data.append(dict)
    else:
      break
finally:
  file.close()

load_data.reverse()

days = len(load_data)

### Draw image
keys = [
  "id",
  "word",
  "freq",
  "result_number",
  "hard_number",
  "1",
  "2",
  "3",
  "4",
  "5",
  "6",
  "X",
  "avg"
]

data = {}
for key in keys:
  vec = []
  for dict in load_data:
    vec.append(dict[key])
  data[key] = vec
# vec = []
# for dict in load_data:
#   vec.append(dict["hard_number"] / dict["result_number"])

### Regression calculation
def f(x):
  return 6.85125127e+06 / x + 3.08777521e+08 / x / x + -4.97008077e+08 / x / x / x

x = np.arange(1, 1 + days)
y = data["result_number"]
new_y = [0.0] * days
for i in range(0, days):
  new_y[i] = 1.0 * y[i] * x[i] * x[i] 

poly = np.polyfit(x, new_y, 2)
p1 = np.poly1d(poly)
# pred_y = p1(x)

# print(poly)
pred_y = f(x)
# print(f(419))
  
# pred_y = [0.0] * days
# for i in range(0, days):
  # print(pred_y[i])
  # print(x[i])
  # pred_y[i] = pred_y[i] / x[i] / x[i] / x[i]

max_diff = 0
for i in range(200, days):
  if abs(pred_y[i] - y[i]) > max_diff:
    max_diff = abs(pred_y[i] - y[i])
print("predict: %d(+/-%d)" % (f(419), max_diff))

# new_y = np.multiply(y, np.multiply(x, np.multiply(x, x)))
# arg = np.array([0, 24000, 70000.3, 0.033]) # randomly
# arg = np.array([1434775.2, -5444988.26347, 472083.01786]) # randomly
# x = np.arange(50, days)
# y = data["result_number"][50 : days]
# arg = np.array([29.9, 6981402.0])

# def learn(arg, times, alpha = [1e-5, 1e-4, 1e-13, 1e-5]):
#   for i in range(0, times):
#     partial = [0.0, 0.0, 0.0]
#     for j in range(0, days):
#       if arg[2] * x[j] < 100:
#         foobar = (arg[0] * x[j] + arg[1]) * np.exp(-arg[2] * x[j])
#         partial[0] += 2 * (foobar - y[j]) * (x[j] * np.exp(-arg[2] * x[j]))
#         partial[1] += 2 * (foobar - y[j]) * (np.exp(-arg[2] * x[j]))
#         partial[2] += 2 * (foobar - y[j]) * (-arg[2] * foobar)
#     for j in range(0, 3):
#       arg[j] -= alpha[j] * partial[j]
#     # print("===")
#     # print(partial)
#     # print(arg)
#   return arg

# def cost(arg):
#   return np.sum(np.multiply(arg[1] / (x - arg[0]) - y, arg[1] / (x - arg[0]) - y))

# def learn(arg, times, alpha = [1e-20, 1e-12]):
#   for i in range(0, times):
#     partial = [0.0, 0.0]
#     foobar = arg[1] / (x - arg[0])
#     partial[0] = 2 * np.sum(np.multiply(foobar - y, -np.divide(foobar, x - arg[0])))
#     partial[1] = 2 * np.sum(np.multiply(foobar - y, (1 / arg[1]) * foobar))
#     for j in range(0, 2):
#       arg[j] += alpha[j] * partial[j]
#     # print(partial)
#     # print(arg)
#     print(cost(arg))
#   return arg

# print(cost(arg))
# arg = learn(arg, 10000)

# print(arg)


'''
  calculate R^2
'''
foo = 0
bar = 0
avg = 0.0
for i in range(0, days):
  avg += y[i]
avg /= days
for i in range(0, days):
  foo += (pred_y[i] - y[i]) * (pred_y[i] - y[i])
  bar += (avg - y[i]) * (avg - y[i])
print(avg, foo, bar)
print(1.0 - foo / bar)

fig, ax = plt.subplots(1, 1)
# plt.xticks(fontproperties = 'Times New Roman')
# plt.yticks(fontproperties = 'Times New Roman')
# ax.set_xlim([300, 350])
# ax.plot(np.arange(start, start + days), data["avg"]) 
# x = np.arange(start, start + days)
# y = data["result_number"]
ax.plot(x, new_y)
# poly = np.polyfit(x, y, 3)
# pred = np.polyval(poly, x)
# pred = np.multiply(arg[0] * np.multiply(x, x) + arg[1] * x + arg[2], np.exp(-arg[3] * x))
# pred = np.divide(arg[0] * np.multiply(x, x) + arg[1] * x + arg[2], np.multiply(x, np.multiply(x, x)))
# pred = arg[0] * np.multiply(x, x) + arg[1] * x + arg[2] / 1
# print(arg[0] * np.multiply(x, x) + arg[1] * x + arg[2])
# print(arg[0] * x + arg[1])
# ax.plot(x, pred_y)
# ax.plot(x, arg[1] / (x - arg[0]))
# ax.plot(np.arange(start, start + days), data["1"])
# ax.plot(np.arange(start, start + days), data["2"])
# ax.plot(np.arange(start, start + days), data["3"])
# ax.plot(np.arange(start, start + days), data["4"])
# ax.plot(np.arange(start, start + days), data["5"])
# ax.plot(np.arange(start, start + days), data["6"])
# ax.plot(np.arange(start, start + days), data["X"])
ax.grid(True)
# ax.set_xlabel('t')
# ax.set_ylabel('Number of reported results')
# ax.set_xlim([50, 400])
# ax.set_ylim([0, 2.7e5])
plt.savefig('fig9')
plt.show()
# fig, ax = plt.subplots(1, 1)
# ax[0].plot(np.arange(0, days), )
# ax[0].plot(np.arange(0, days), )
# ax[0].grid(True)
# # for i in range(0, 2):
# #   ax[i].grid(True)
# #   ax[i].set_ylabel('(%)')
# #   ax[i].set_xlim([0, PITY])
# ax[0].set_ylim([0, 11])
# # ax[0].set_ylim([0, 102])
# # ax[1].set_xlabel('Pulls')
# plt.show()
