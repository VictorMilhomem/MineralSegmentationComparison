import os
import shutil
from config import *
from math import floor
import cv2
import numpy as np

def rename_files_in_directory(directory_path: str, key: str, save_path: str, is_mask=False):
    files = os.listdir(directory_path)
    
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    
    for file_name in files:
        if os.path.isfile(os.path.join(directory_path, file_name)):
            # Create the save directory if it doesn't exist
            if not os.path.exists(save_path):
                os.makedirs(save_path)
            
            # Copy the file to the save directory
            source_file_path = os.path.join(directory_path, file_name)
            save_file_path = os.path.join(save_path, file_name)
            shutil.copy2(source_file_path, save_file_path)
            
            # Rename the copied file
            file_base, file_ext = os.path.splitext(file_name)
            def remove_chars(string, chars_to_remove):
                if chars_to_remove in string:
                    index = string.find(chars_to_remove)
                    string = string[:index] + string[index+len(chars_to_remove):]
                return string
            
            if key == "Fe19" and is_mask:
                file_base = remove_chars(file_base, "_NewRef")
                file_base = f"{key}_{file_base}"
            elif key == "Fe19" and (is_mask == False):
                file_base = remove_chars(file_base, "_MLR")
                file_base = f"{key}_{file_base}"
            elif key == "FeM" or key == "Cu":
                file_base = remove_chars(file_base, "_Ref") if is_mask else remove_chars(file_base, "_RLM")         

            #new_file_name = f"{file_base}_{key}{file_ext}" if is_mask else f"{file_base}{file_ext}"
            new_file_name = f"{file_base}{file_ext}"
            new_file_path = os.path.join(save_path, new_file_name)
            os.rename(save_file_path, new_file_path)


def split_train_test(path: str, n_images: float, is_mask=False):
    files = os.listdir(path)
    n = len(files)
    train_folder_name = "train_mask" if is_mask else "train_rlm"
    test_folder_name = "test_mask" if is_mask else "test_rlm"
    train_path = os.path.join(path, train_folder_name)
    test_path = os.path.join(path, test_folder_name)

    if not os.path.exists(train_path):
        os.makedirs(train_path)
    if not os.path.exists(test_path):
        os.makedirs(test_path)
    if n_images > n: 
        raise ValueError("n_images should be a number bellow the size of your dataset")
    
    test_files = files[:n_images]
    train_files = files[n_images:]
    for file_name in test_files:
        source = os.path.join(path, file_name)
        destination = os.path.join(test_path, file_name)
        shutil.move(source, destination)
    for file_name in train_files:
        source = os.path.join(path, file_name)
        destination = os.path.join(train_path, file_name)
        shutil.move(source, destination) 


"""
import tifffile
def convert_to_ome_tiff(img_path: str):
    train_path = os.path.join(img_path, "train_mask")
    test_path = os.path.join(img_path, "test_mask")
    train_files = os.listdir(train_path)
    test_files = os.listdir(test_path)
    def convert(files, path):
        for file in files:
            file_base, ext = os.path.splitext(file)
            file_name = os.path.join(path, f"{file_base}.ome.tiff")
            if ext.lower() == ".tif" or ext.lower() == ".tiff":
                tif_image = tifffile.imread(os.path.join(path, file))
                tifffile.imwrite(file_name, tif_image, imagej=True)
                print(f"Converted {file} to OME-TIFF.")
            else:
                print(f"Skipping {file}: Not a TIFF file.")
    convert(train_files, train_path)
    convert(test_files, test_path)"""



def convert_background(img_path: str):
    train_path = os.path.join(img_path, "train_mask")
    test_path = os.path.join(img_path, "test_mask")
    
    for path in [train_path, test_path]:
        if not os.path.isdir(path):
            print(f"Directory {path} does not exist.")
            return

        files = os.listdir(path)
        for file in files:
            file_base, ext = os.path.splitext(file)
            file_name = os.path.join(path, file_base)
            if ext.lower() in [".tif", ".tiff"]:
                image = cv2.imread(os.path.join(path, file))
                if image is None:
                    print(f"Error reading {file_name}. Skipping...")
                    continue

                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                result = cv2.bitwise_not(gray)  # Invert the grayscale image
                output_file = os.path.join(file_name  + f"_inverted{ext}")
                cv2.imwrite(output_file, result)

                os.remove(f"{file_name}{ext}")
                os.rename(output_file, f"{file_name}{ext}")

                result = np.ones_like(image) * 0
                output_path = os.path.join(path, "background")
                if not os.path.exists(output_path):
                    os.makedirs(output_path)
                output_file = os.path.join(output_path, file_base  + f"_background{ext}")
                cv2.imwrite(output_file, result)   # Save with a different name to avoid overwriting
                
                
                print(f"Converted {file} background. Saved as {output_file}")
            else:
                print(f"Skipping {file}: Not a TIFF file.")



def process_folders(path_to_folder: dict):
    for ore, t in path_to_folder.items():
        for k, path in t.items():
            save_to = os.path.join(PROCESSED_FOLDER, "apeers", ore, os.path.basename(path))
            print(f"Processing {path} . Saved as {save_to}")
            if k == "RLM":
                rename_files_in_directory(path, ore, save_to)
                split_train_test(save_to, 4, is_mask=False)
            else:
                rename_files_in_directory(path, ore, save_to, is_mask=True)
                split_train_test(save_to, 4, is_mask=True)
                convert_background(save_to)

            

        

if __name__ == "__main__":
   process_folders(PATH_TO_FOLDER)