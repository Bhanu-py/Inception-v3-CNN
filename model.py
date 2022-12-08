import tensorflow as tf
from keras.applications.inception_v3 import InceptionV3
from keras import Sequential, Model
from keras.activations import softmax
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Dense, Activation, Flatten, Dropout, MaxPool2D


def add_new_last_layer(n_classes, fc_layer_size):
    """Add last layer to the convnet

    Args:
        base_model: keras model excluding top
        nb_classes: # of classes

    Returns:
        new keras model with last layer
    """
    base_model = InceptionV3(input_shape=(224, 224, 3), weights='imagenet', include_top=False)
    base_model_output = base_model.output
    # x = MaxPooling2D()(base_model_output)
    x = Dropout(0.4)(base_model_output)
    model_flat = Flatten()(base_model_output)
    predictions = Dense(n_classes, activation='softmax', name='predictions')(model_flat)
    model = Model(inputs=base_model.input, outputs=predictions)
    for i in model.layers:
        i.trainable = False
    return model


if __name__ == '__main__':
    # model.summary()
    model = add_new_last_layer(n_classes=9, fc_layer_size=(224, 224, 3))
    print(model.summary())