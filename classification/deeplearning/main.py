from logistic_reg_with_multi_layers import train, predict
import numpy as np
import json

freq = {
  'a': 0.08857938718662953,
  'b': 0.017270194986072424,
  'c': 0.04011142061281337,
  'd': 0.030083565459610027,
  'e': 0.10250696378830083,
  'f': 0.01838440111420613,
  'g': 0.02841225626740947,
  'h': 0.03899721448467967,
  'i': 0.05682451253481894,
  'j': 0.0022284122562674096,
  'k': 0.019498607242339833,
  'l': 0.06239554317548746,
  'm': 0.03064066852367688,
  'n': 0.04902506963788301,
  'o': 0.07409470752089137,
  'p': 0.03565459610027855,
  'q': 0.002785515320334262,
  'r': 0.07409470752089137,
  's': 0.04902506963788301,
  't': 0.07242339832869081,
  'u': 0.03565459610027855,
  'v': 0.013927576601671309,
  'w': 0.016713091922005572,
  'x': 0.0038997214484679664,
  'y': 0.033983286908077996,
  'z': 0.002785515320334262
}

## load data
with open('./freq.json', 'r', encoding = 'utf-8') as fp:
  freq_data = json.load(fp)

data = []

file = open("cluster.txt", 'r')
try:
  while True:
    line = file.readline()
    if line:
      dict = {}
      dict["word"] = line.strip()
      dict["id"] = int(file.readline())
      dict["diff"] = int(file.readline())
      dict["freq"] = freq_data[dict["word"]]
      dict["a"] = 0.0
      dict["b"] = 0.0
      for i in range(5):
        if dict["word"][i] in {'a', 'e', 'i', 'o', 'u'}:
          dict["a"] += 0.2
        else:
          dict["b"] += 0.2
      dict["1"] = int(file.readline())
      dict["2"] = int(file.readline())
      dict["3"] = int(file.readline())
      dict["4"] = int(file.readline())
      dict["5"] = int(file.readline())
      dict["6"] = int(file.readline())
      dict["X"] = int(file.readline())
      file.readline() # empty line
      data.append(dict)
    else:
      break
finally:
  file.close()

m = len(data)
dim = 21
classes = 15

x = np.zeros((m, dim))
y = np.zeros((m, 15))
for i in range(m):
  dict = data[i]
  x[i][17] = dict["a"]
  x[i][18] = dict["b"]
  x[i][19] = dict["diff"] / 5
  x[i][20] = dict["freq"]
  for j in range(5):
    foo = dict["word"][j]
    x[i][j] = ((ord(foo) - ord('a')) / 26)
    x[i][5 + j] = freq[dict["word"][j]]
    if j < 4:
      bar = dict["word"][j + 1]
      x[i][10 + j] = ((ord(foo) - ord('a')) * 26 + (ord(bar) - ord('a'))) / (26 * 26)
    if j < 3:
      bar = dict["word"][j + 1]
      mls = dict["word"][j + 2]
      x[i][10 + j] = ((ord(foo) - ord('a')) * 26 * 26 + (ord(bar) - ord('a')) * 26 + (ord(mls) - ord('a'))) / (26 * 26 * 26)
  y[i][dict["id"]] = 1.0

print(x)
print(y)

### train
x = x.T
y = y.T

layer_nodes = [dim, 20, 15]
parameters = train(x, y, 0.05, layer_nodes, 1000000, True, 10000)

input_params = {}
for i in range(1, len(layer_nodes)):
  input_params["w" + str(i)] = parameters["w" + str(i)].tolist()
  input_params["b" + str(i)] = parameters["b" + str(i)].tolist()

### mark down parameters
with open("./params.json", "w") as input_json:
  json.dump(input_params, input_json, indent = 4, ensure_ascii = False)

### predict
print(predict(np.array([
  4/26, 4/26, 17/26, 8/26, 4/26,
  freq['e'], freq['e'], freq['r'], freq['i'], freq['e'],
  4/26 + 4/676, 4/26 + 17/676, 17/26 + 8/676, 8/26 + 4/676,
  4/26 + 4/676 + 17/17576, 4/26 + 17/676 + 8/17576, 17/26 + 8/676 + 4/17576,
  0.8,
  0.2,
  3/5,
  freq_data["eerie"]
]).reshape((dim, 1)), parameters, 15))
