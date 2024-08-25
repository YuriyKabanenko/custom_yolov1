import utils as ut
import cell


class Grid:
    def __init__(self, image, size):
        self.size = size
        self.grid = self.__fill_grid(image)
        
    def __fill_grid(self, image):
        cells = []
        
        for i in range(len(image)):
            part_array = []
            one_channel_arr = image[i]
            length = int(len(one_channel_arr) / self.size)
            for j in range(0, len(one_channel_arr), length):
                for k in range(0, len(one_channel_arr), length):
                    part = one_channel_arr[j:j+length, k:k+length]
                    part_array.append(cell.Cell(part))
                    
            cells.append(part_array)        
             
            
        return cells
    
    def set_label(self, label):
        for i in range(len(label.obj_class)):
            cell_row, cell_col = ut.get_object_cell_indexes(label.x_coor[i], label.y_coor[i])
            self.grid[0][(cell_row * self.size) + cell_col].set_label(label, label.x_coor[i] * ut.IMAGE_SIZE, label.y_coor[i] * ut.IMAGE_SIZE)
            self.grid[1][(cell_row * self.size) + cell_col].set_label(label, label.x_coor[i] * ut.IMAGE_SIZE, label.y_coor[i] * ut.IMAGE_SIZE)
            self.grid[2][(cell_row * self.size) + cell_col].set_label(label, label.x_coor[i] * ut.IMAGE_SIZE, label.y_coor[i] * ut.IMAGE_SIZE)
            
            



        
        