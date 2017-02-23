from __future__ import print_function
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# Training Data
mnist = input_data.read_data_sets('/tmp/data', one_hot=True)

# Hyper Parameters
LEARNING_RATE = 0.001
TRAINING_ITERS = 200000
BATCH_SIZE = 128
DISPLAY_STEP = 10

# Network Parameters
# 28 x 28 image
N_INPUT = 784
N_CLASSES = 10

# Technique created by Jeffery Hinton, that prevents over fitting.
# It randomly turns off neurons so that data is forced to find new paths.
DROPOUT = 0.75

# X and Y
# None means there is no limit to the number of rows
x = tf.placeholder(tf.float32, [None, N_INPUT])
y = tf.placeholder(tf.float32, [None, N_CLASSES])
# This is used by dropout
keep_prob = tf.placeholder(tf.float32)

# Outline of Model
# Input -> Conv1 -> ReLU -> Pool -> Conv2 -> ReLU -> Pool -> FullyConnected -> Dropout -> Output

# 2D Convolutional Layer
# Convolutional === Transformation Layer (Like image transforms, or like a filter)
# RELU === Rectified Linear Unit (Activation Function, like sigmoid)

# The filter is applied to image patches of the same size as the filter and
# >strided< according to the strides argument.
# strides = [1, 1, 1, 1] applies the filter to a patch at every offset,
# strides = [1, 2, 2, 1] applies the filter to every other image patch in each dimension
def conv2d(x, W, b, strides=1):
    x = tf.nn.conv2d(x, W, strides=[1, strides, strides, 1], padding = 'SAME')
    x = tf.nn.bias_add(x, b)
    return tf.nn.relu(x)

# Max Pooling Layer
# Takes a pool of data (small rectangular boxes) form the convolutional layer
# And then subsamples them to produce a single output block
# Basically used to chuck out values that are insignificant to output, and
# retains only the ones that are necessary
# K is 2 so that a nice square is strided over

# 1 1 2 4               {max(1,1,5,6) => 6}
# 5 6 7 8 ====> 6 8     {max(5,6,7,8) => 8}
# 3 2 1 0 ====> 3 4     {max(3,2,1,0) => 3}
# 1 2 3 4               {max(1,2,3,4) => 4}

# Typical values are 2x2 or no max-pooling. Very large input images may warrant
# 4x4 pooling in the lower-layers. Keep in mind however, that this will reduce
# the dimension of the signal by a factor of 16, and may result in throwing away
# too much information.
def maxpool2d(x, k=2):
    return tf.nn.max_pool(x, ksize=[1, k, k, 1], strides=[1, k, k, 1],
                          padding = 'SAME')

def conv_net(x, weights, biases, dropout):
    # reshape input data
    x = tf.reshape(x, shape=[-1, 28, 28, 1])

    # Convolution Layer
    conv1 = conv2d(x, weights['wc1'], biases['bc1'])
    # Max Pooling (down-sampling)
    conv1 = maxpool2d(conv1, k=2)

    # Convolution Layer
    conv2 = conv2d(conv1, weights['wc2'], biases['bc2'])
    # Max Pooling (down-sampling)
    conv2 = maxpool2d(conv2, k=2)

    # Fully connected layer === does the actual classification
    # Reshape conv2 output to fit fully connected layer input
    fc1 = tf.reshape(conv2, [-1, weights['wd1'].get_shape().as_list()[0]])
    fc1 = tf.add(tf.matmul(fc1, weights['wd1']), biases['bd1'])
    fc1 = tf.nn.relu(fc1)

    # Apply Dropout
    fc1 = tf.nn.dropout(fc1, dropout)

    # Output, class prediction
    out = tf.add(tf.matmul(fc1, weights['out']), biases['out'])

    return out

# Store layers weight & bias
weights = {
    # 5x5 conv, 1 input, 32 outputs
    'wc1': tf.Variable(tf.random_normal([5, 5, 1, 32])),
    # 5x5 conv, 32 inputs, 64 outputs
    'wc2': tf.Variable(tf.random_normal([5, 5, 32, 64])),
    # fully connected, 7*7*64 inputs, 1024 outputs
    'wd1': tf.Variable(tf.random_normal([7*7*64, 1024])),
    # 1024 inputs, 10 outputs (class prediction)
    'out': tf.Variable(tf.random_normal([1024, N_CLASSES]))
}

biases = {
    'bc1': tf.Variable(tf.random_normal([32])),
    'bc2': tf.Variable(tf.random_normal([64])),
    'bd1': tf.Variable(tf.random_normal([1024])),
    'out': tf.Variable(tf.random_normal([N_CLASSES]))
}

# Construct model
pred = conv_net(x, weights, biases, keep_prob)

# Define cost and optimizer
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=pred, labels=y))
optimizer = tf.train.AdamOptimizer(learning_rate=LEARNING_RATE).minimize(cost)

# Evaluate model
correct_pred = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

# Initializing the variables
init = tf.global_variables_initializer()

# Launch the graph
with tf.Session() as sess:
    sess.run(init)
    step = 1
    # Keep training until reach max iterations
    while step * BATCH_SIZE < TRAINING_ITERS:
        batch_x, batch_y = mnist.train.next_batch(BATCH_SIZE)
        # Run optimization op (backprop)
        sess.run(optimizer, feed_dict={x: batch_x, y: batch_y,
                                       keep_prob: DROPOUT})
        if step % DISPLAY_STEP == 0:
            # Calculate batch loss and accuracy
            loss, acc = sess.run([cost, accuracy], feed_dict={x: batch_x,
                                                              y: batch_y,
                                                              keep_prob: 1.})
            print("Iter " + str(step*BATCH_SIZE) + ", Minibatch Loss= " + \
                  "{:.6f}".format(loss) + ", Training Accuracy= " + \
                  "{:.5f}".format(acc))
        step += 1
    print("Optimization Finished!")

    # Calculate accuracy for 256 mnist test images
    print("Testing Accuracy:", \
        sess.run(accuracy, feed_dict={x: mnist.test.images[:256],
                                      y: mnist.test.labels[:256],
                                      keep_prob: 1.}))
