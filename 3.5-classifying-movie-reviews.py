# import tensorflow in cell 1
import keras
import tensorflow as tf

#... prefix tf.keras in cell 13
model.compile(optimizer=tf.keras.optimizers.RMSprop(learning_rate=0.001),
              loss='binary_crossentropy',
              metrics=['accuracy'])

# change history keys in cell 21
acc = history.history['binary_accuracy']
val_acc = history.history['val_binary_accuracy']

# and in cell 24
acc_values = history_dict['binary_accuracy']
val_acc_values = history_dict['val_binary_accuracy']