import tensorflow as tf
import numpy as np
import pandas as pd
# Used to predict onset of diabetes

x = pd.read_csv('x.csv')
x_data = x.values.astype(np.float32)

y = pd.read_csv('y.csv')
y_data = y.values.astype(np.float32)

# Some Constants I Guess

input_size = 8
h1_size = 400
h2_size = 100
output_size = 2

# End of the Constants Hopefully

xs = tf.placeholder(tf.float32)
ys = tf.placeholder(tf.float32)

hidden_layer_1 = { 'weight': tf.Variable(tf.random_normal([input_size,h1_size])), 'bias': tf.Variable(tf.random_normal([1,h1_size])) }
hidden_layer_2 = { 'weight': tf.Variable(tf.random_normal([h1_size,h2_size])), 'bias': tf.Variable(tf.random_normal([1,h2_size])) }
output_layer = { 'weight': tf.Variable(tf.random_normal([h2_size,output_size])), 'bias': tf.Variable(tf.random_normal([1,output_size])) }

def neural_networking(input):
   h1 = tf.matmul(input, hidden_layer_1['weight']) + hidden_layer_1['bias']
   h1 = tf.sigmoid(h1)
   h2 = tf.matmul(h1, hidden_layer_2['weight']) + hidden_layer_2['bias']
   h2 = tf.sigmoid(h2)
   output = tf.matmul(h2, output_layer['weight']) + output_layer['bias']

   return output

net = neural_networking(xs)

delta = tf.square(net - ys)
cost = tf.reduce_mean(delta, 0)

optimizer = tf.train.GradientDescentOptimizer(0.01)
preditor = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.initialize_all_variables())

for i in range(5000):
   if i%250 == 0:
       print "Step: ", i
   sess.run(preditor, {xs:x_data, ys:y_data})

op = sess.run(net, {xs:x_data})

c = 0
for i in range(765):
   print np.argmax(y_data[i]), np.argmax(op[i])
   if(np.argmax(y_data[i]) == np.argmax(op[i])):
       c = c + 1
print 'Accuracy is :', (c * 100) / 766
