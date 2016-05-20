# -*- coding: utf-8 -*-
"""
Created on Fri May 20 13:29:07 2016

@author: mikebaldwin
"""

import tensorflow as tf
from PIL import Image, ImageFilter
import numpy

#define a function to prepare an image for learning
def prepare_image(image_file):
    from tensorflow.examples.tutorials.mnist import input_data
    mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

    #initilization of the regression
    x = tf.placeholder(tf.float32, [None, 784])
    #weights
    W = tf.Variable(tf.zeros([784, 10]))
    #bias'
    b = tf.Variable(tf.zeros([10]))
    
    #implement the softmax regression model 
    y = tf.nn.softmax(tf.matmul(x, W) + b)
    
    #training section
    #implement cross-entropy (our cost function).  This defines how the model should be trained
    y_ = tf.placeholder(tf.float32, [None, 10])
    cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))
    #train the model
    train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
    #save the model
    saver = tf.train.Saver()
    #initilize the variables
    init = tf.initialize_all_variables()
    
    #launch the model
    sess = tf.Session()
    sess.run(init)

    #train 1000 times
    for i in range(1000):
        batch_xs, batch_ys = mnist.train.next_batch(100)
        sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
        
    #now that we have confirmed the model is functioning correctly, lets save it to a file
    save_path = saver.save(sess, "model.ckpt")
    print ("Model saved in file: ", save_path)
    
    #make the image black and white
    bw_image = Image.open(image_file).convert('L')
    #get width and height of the image
    width = float(bw_image.size[0])
    height = float(bw_image.size[1])
    
    #create a new black and white image that is the same size as the dataset
    set_image = Image.new('L', (28, 28), (255))
        
    if width > height: #check which dimension is bigger
        #Width is bigger. Width becomes 20 pixels.
        new_height = int(round((20.0/width*height),0)) #resize height according to ratio width
        if (new_height == 0): #rare case but minimum is 1 pixel
            new_height = 1  
        # resize and sharpen
        img = bw_image.resize((20,new_height), Image.ANTIALIAS).filter(ImageFilter.SHARPEN)
        wtop = int(round(((28 - new_height)/2),0)) #caculate horizontal pozition
        set_image.paste(img, (4, wtop)) #paste resized image on white canvas
    else:
        #Width is bigger. Width becomes 20 pixels.
        new_width = int(round((20.0/height*width),0)) #resize width according to ratio height
        if (new_width == 0): #rare case but minimum is 1 pixel
            new_width = 1  
        # resize and sharpen
        img = bw_image.resize((20,new_width), Image.ANTIALIAS).filter(ImageFilter.SHARPEN)
        wtop = int(round(((28 - new_width)/2),0)) #caculate horizontal pozition
        set_image.paste(img, (4, wtop)) #paste resized image on white canvas
    
    pixel_values = list(set_image.getData())

    
    #make the pixels either black or white, not inbetween
    real_pixels = [ (255-x)*1.0/255.0 for x in pixel_values] 
    return real_pixels
    
def predict_int(pixels):
    with tf.Session() as sess:
        sess.run(init_op)
        saver.restore(sess, "model.ckpt")
        print ("Model restored.")

        prediction=tf.argmax(y,1)
        return prediction.eval(feed_dict={x: [pixels]}, session=sess)
    
    
pixels = prepare_image("UTH4666.jpg")
print(predict_int(pixels))
        
        




