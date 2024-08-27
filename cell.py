import utils as ut

class Cell:
    def __init__(self, channel_arrays):
        self.channel_arrays = channel_arrays
        self.contains_obj = False
        self.class_mark = 0
        self.confidence = 0
        self.x_coor = 0
        self.y_coor = 0
        self.box_width = 0
        self.box_height = 0
        
        
    def set_label(self, label, x_coord_img, y_coord_img):
        self.contains_obj = True
        self.class_mark = label.obj_class[0]
        self.confidence = 1
        x = x_coord_img % ut.CELL_SIZE
        y = y_coord_img % ut.CELL_SIZE
        self.x_coor = x / 100
        self.y_coor = y / 100
        self.box_width = label.width[0]
        self.box_height = label.height[0]
    
    def get_prediction_vector(self):
        prediction_vector = [self.confidence, self.x_coor, self.y_coor, self.box_width, self.box_height]
        prediction_vector.extend(ut.get_one_hot_encoded(self.class_mark))
        return prediction_vector
        