import utils as ut

class Cell:
    def __init__(self, channel_arrays):
        self.channel_arrays = channel_arrays
        self.contains_obj = False
        self.class_mark = None
        self.confidence = None
        self.x_coor = None
        self.y_coor = None
        self.box_width = None
        self.box_height = None
        
        
    def set_label(self, label, x_coord_img, y_coord_img):
        self.contains_obj = True
        self.class_mark = label.obj_class
        self.confidence = 1
        x = x_coord_img % ut.CELL_SIZE
        y = y_coord_img % ut.CELL_SIZE
        self.x_coor = x / 100
        self.y_coor = y / 100
        self.box_width = label.width
        self.box_height = label.height
        
        