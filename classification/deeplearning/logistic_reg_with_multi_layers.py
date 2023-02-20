# l: layers of neural network
# A[i: 1...l-1] = g(w[i] * A[i-1] + b[i])
#  - g(z) = ReLU(z)
# A[l] = g(w[l] * A[l-1] + b[l])
#  - g(z) = sigmoid(z)

# Loss function L(a, y) = -(y log a + (1-y) * log(1-a))
# Cost function J = 1/m sum L(a, y)
import numpy as np
from dnn_utils import sigmoid, sigmoid_backward, relu, relu_backward

# layer_nodes[0] = #features
# ...
def initialize(layer_nodes):
  parameters = {}
  layers = len(layer_nodes) - 1

  for i in range(1, layers + 1):
    parameters["w" + str(i)] = np.random.randn(layer_nodes[i], layer_nodes[i - 1]) / np.sqrt(layer_nodes[i - 1] / 2) # ???
    parameters["b" + str(i)] = np.zeros((layer_nodes[i], 1))

  return parameters

def forward_single(pa, w, b, activation):
  z = np.dot(w, pa) + b
  a = relu(z)[0] if activation == "relu" else sigmoid(z)[0]
  cache = (pa, w, z)
  # if activation == "sigmoid":
  #   print(a)
  return a, cache

def forward(x, parameters):
  caches = []
  a = x
  layers = len(parameters) // 2

  for i in range(1, layers + 1):
    a, cache = forward_single(a, parameters["w" + str(i)], parameters["b" + str(i)], "sigmoid" if i == layers else "relu")
    # print("===%i===" % (i))
    # print(a)
    # print("========")
    caches.append(cache)

  return a, caches

def get_cost(a, y):
  m = y.shape[1]
  cost = -(1 / m) * np.sum(np.multiply(y, np.log(a)) + np.multiply(1 - y, np.log(1 - a)))
  cost = np.squeeze(cost)
  return cost

def backward_single(da, cache, activation):
  pa, w, z = cache
  dz = relu_backward(da, z) if activation == "relu" else sigmoid_backward(da, z)
  m = pa.shape[1]
  dw = (1 / m) * np.dot(dz, pa.T)
  db = (1 / m) * np.sum(dz, axis = 1, keepdims = True)
  dpa = np.dot(w.T, dz)
  return dw, db, dpa

def backward(a, y, caches):
  grads = {}
  layers = len(caches)
  da = -np.divide(y, a) + np.divide(1 - y, 1 - a)

  for i in range(layers, 0, -1):
    grads["dw" + str(i)], grads["db" + str(i)], da = backward_single(da, caches[i - 1], "sigmoid" if i == layers else "relu")

  return grads

def feedback(x, parameters, y):
  m = x.shape[1]
  k = y.shape[0]
  a = forward(x, parameters)[0]
  cost = get_cost(a, y)

  # a = a.round()
  success = 0
  for i in range(m):
    (foo, bar, ans) = (-1, -1.0, -1)
    for j in range(k):
      if a[j][i] > bar:
        foo = j
        bar = a[j][i]
      if y[j][i] == 1.0:
        ans = j
    success += (foo == ans)

  return success, m, cost

def train(x, y, alpha, layer_nodes, iteration_num, debug = False, debug_breakpoint = 1):
  layers = len(layer_nodes) - 1
  parameters = initialize(layer_nodes)

  for i in range(iteration_num):
    a, caches = forward(x, parameters)
    grads = backward(a, y, caches)
    for j in range(1, layers + 1):
      parameters["w" + str(j)] = parameters["w" + str(j)] - alpha * grads["dw" + str(j)]
      parameters["b" + str(j)] = parameters["b" + str(j)] - alpha * grads["db" + str(j)]
    if debug and (((i + 1) % debug_breakpoint == 0) or (i + 1 == iteration_num)):
      success, m, cost = feedback(x, parameters, y)
      print("Feedback accuracy: %.3f%%(%d/%d), cost: %.5lf, after %i iterations." %
        ((success / m) * 100, success, m, cost, i + 1))

  return parameters

def predict(x, parameters, k):
  a = forward(x, parameters)[0]
  (foo, bar) = (-1, -1.0)
  for i in range(k):
    if a[i][0] > bar:
      foo = i
      bar = a[i][0]
  
  return foo
