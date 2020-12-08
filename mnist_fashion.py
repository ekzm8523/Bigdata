# import tensorflow as tf
# import matplotlib.pyplot as plt
# import numpy as np
# (train_images, train_labels),(test_images,test_labels)=tf.keras.datasets.fashion_mnist.load_data()
#
#
# class_names=['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Angle boot']
# train_images = train_images/255.0
# test_images = test_images/255.0
#
# np.round(train_images[0],2)
# model = tf.keras.Sequential([
#                               tf.keras.layers.Flatten(input_shape=(28,28)),
#                               tf.keras.layers.Dense(128, activation='relu'),
#                              tf.keras.layers.Dense(10,activation='softmax')
# ])
# model.compile(optimizer='adam',
#               loss = 'sparse_categorical_crossentropy',
#               metrics=['accuracy'])
#
# model.fit(train_images,train_labels, epochs=10)
# #
# # test_loss, test_acc = model.evaluate(test_images, test_labels)
#
#
#
