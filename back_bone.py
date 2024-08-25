from tensorflow.keras import layers, models
import tensorflow as tf
from tensorflow.keras.utils import load_img, img_to_array
import numpy as np

class BackBone:
    def __init__(self):
        model = models.Sequential()

        model.add(layers.Conv2D(filters=64, kernel_size=(7, 7), strides=(2, 2),
                                padding='valid', activation='relu',
                                input_shape=(448, 448, 3)))
        model.add(layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2), padding='valid'))


        # model.add(layers.Conv2D(256, (3, 3), strides=(1, 1), padding='same', activation='relu'))


        # model.add(layers.Conv2D(256, (1, 1), strides=(1, 1), padding='same', activation='relu'))

        # model.add(layers.Conv2D(512, (3, 3), strides=(1, 1), padding='same', activation='relu'))
        # model.add(layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2), padding='valid'))

 
        # for _ in range(4):
        #     model.add(layers.Conv2D(256, (1, 1), strides=(1, 1), padding='same', activation='relu'))
        #     model.add(layers.Conv2D(512, (3, 3), strides=(1, 1), padding='same', activation='relu'))

       
        # model.add(layers.Conv2D(512, (1, 1), strides=(1, 1), padding='same', activation='relu'))
        # model.add(layers.Conv2D(1024, (3, 3), strides=(1, 1), padding='same', activation='relu'))
        # model.add(layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2), padding='valid'))


        # for _ in range(2):
        #     model.add(layers.Conv2D(512, (1, 1), strides=(1, 1), padding='same', activation='relu'))
        #     model.add(layers.Conv2D(1024, (3, 3), strides=(1, 1), padding='same', activation='relu'))

  
        # model.add(layers.Conv2D(1024, (3, 3), strides=(1, 1), padding='same', activation='relu'))

        # model.add(layers.Conv2D(1024, (3, 3), strides=(2, 2), padding='valid', activation='relu'))


        # model.add(layers.Conv2D(1024, (3, 3), strides=(1, 1), padding='same', activation='relu'))


        # model.add(layers.Conv2D(1024, (3, 3), strides=(1, 1), padding='same', activation='relu'))
        
        self.model = model
        
        print(self.model.summary())
        
    def get_feature_maps(self, image_path):
        image = load_img(image_path)
        image = img_to_array(image)
        image = np.expand_dims(image, axis=0)
        maps = self.model.predict(image)
        return maps
        