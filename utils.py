from enum import Enum
import utils as ut
import math
import os
import matplotlib.pyplot as plt
import numpy as np

IMAGE_SIZE = 448
CELL_SIZE = 64

class ImageObject(Enum):
    CAR = 1
    WOMAN = 2
    MAN = 3
    MOBILE = 4
    WATCH = 5
    CAT = 6
    DOG = 7


def get_one_hot_encoded(obj):
    one_hot_vector = []
    
    for imgObject in ImageObject:
        if imgObject.value == obj:
            one_hot_vector.append(1)
        else:
            one_hot_vector.append(0)
            
    return one_hot_vector         
            

def save_feature_maps(feature_maps):
    np.save('feature_maps.npy', feature_maps)
        
def load_feature_maps():
    data = np.load('feature_maps.npy')
    return data
    
 
def plot_feature_maps(feature_maps, num_cols=16):
    num_feature_maps = feature_maps.shape[-1]
    num_rows = num_feature_maps // num_cols + (num_feature_maps % num_cols != 0)
    
    plt.figure(figsize=(num_cols * 2, num_rows * 2))
    for i in range(num_feature_maps):
        plt.subplot(num_rows, num_cols, i + 1)
        plt.imshow(feature_maps[0, :, :, i], cmap='viridis')
        plt.axis('off')
    plt.show()    
 
        
def get_filenames_in_folder(directory_path):
    file_names = []

    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_names.append(file)
            
    return file_names        
    
    
def get_object_cell_indexes(x_coor, y_coor):
    x_coordinate_in_pixels = x_coor * ut.IMAGE_SIZE
    y_coordinate_in_pixels = y_coor * ut.IMAGE_SIZE
    object_cell_column = math.floor(x_coordinate_in_pixels / ut.CELL_SIZE)
    object_cell_row = math.floor(y_coordinate_in_pixels / ut.CELL_SIZE)
    return object_cell_row, object_cell_column      
    