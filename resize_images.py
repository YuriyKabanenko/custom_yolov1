from PIL import Image
import os

def resize_images_in_folder(folder_path, target_size=(448, 448)):
    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tiff')):  # Add more formats if needed
            file_path = os.path.join(folder_path, filename)

            # Open and resize the image
            with Image.open(file_path) as img:
                resized_img = img.resize(target_size)
                
                # Overwrite the original image
                resized_img.save(file_path)

            print(f"Resized and saved: {filename}")

# Example usage
folder_path = 'dataset/images/val'
resize_images_in_folder(folder_path)
