import numpy as np
import os
from PIL import Image
import grid
import label as lb
import back_bone as bb
import utils as ut

root_images_folder = 'dataset/images/training/'
root_label_folder = 'dataset/labels/training/'


def get_channels_array(img_array):
    red_channel = img_array[:, :, 0]
    green_channel = img_array[:, :, 1]
    blue_channel = img_array[:, :, 2]
    return np.stack([red_channel, green_channel, blue_channel])

img_array = []
label_array = []

for subdir_name in os.listdir(root_images_folder):
    file_path = os.path.join(root_images_folder, subdir_name)
    file_path = file_path.replace('\\', '/')
    image = Image.open(file_path)
    img_array.append(get_channels_array(np.array(image)))

for subdir_name in os.listdir(root_label_folder):
    file_path = os.path.join(root_label_folder, subdir_name)
    file_path = file_path.replace('\\', '/')
    
    obj_classes = []
    x_coors = []
    y_coors = []
    widths = []
    heights = []

    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split()
            if len(parts) == 5:
                obj_class = int(parts[0]) + 1
                x_coor = float(parts[1])            
                y_coor = float(parts[2])            
                width = float(parts[3])
                height = float(parts[4])
                
                obj_classes.append(obj_class)
                x_coors.append(x_coor)
                y_coors.append(y_coor)
                widths.append(width)
                heights.append(height)

    label = lb.Label(obj_classes, x_coors, y_coors, widths, heights)
    label_array.append(label)

grid_array = []

for i in range(len(img_array)):
    grid_array.append(grid.Grid(img_array[i], 7))


for i in range(len(label_array)):
    grid_array[i].set_label(label_array[i])

backbone = bb.BackBone()

# img_names = ut.get_filenames_in_folder(root_images_folder)
# maps = []

# for i in range(len(img_names)):
#     maps.append(backbone.get_feature_maps(root_images_folder + img_names[i]))
#     ut.plot_feature_maps(maps[i])  
    
# ut.save_feature_maps(maps)    
    
loaded_feature_maps = ut.load_feature_maps()    

prediction_vectors = []

for i in range(len(grid_array)):
    img_vector = []
    for j in range(49):
        img_vector.append(grid_array[i].grid[0][j].get_prediction_vector())
    prediction_vectors.append(img_vector)




