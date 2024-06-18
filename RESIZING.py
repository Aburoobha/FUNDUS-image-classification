#!/usr/bin/env python
# coding: utf-8


from PIL import Image
import os

def resize(input_dir, output_dir, target_size):
    os.makedirs(output_dir, exist_ok=True) #directory of output exists?
    for root, _, files in os.walk(input_dir): #through every folder in 1000images file
        for filename in files:
            if filename.lower().endswith(('.jpg', '.jpeg', '.png')): #ext check
                img_path = os.path.join(root, filename)
                relative_path = os.path.relpath(root, input_dir)
                output_subdir = os.path.join(output_dir, relative_path)
                os.makedirs(output_subdir, exist_ok=True)
                
                try:
                    img = Image.open(img_path)
                    img_resized = img.resize(target_size, Image.ANTIALIAS)
                    # Save resized image
                    output_path = os.path.join(output_subdir, filename)
                    img_resized.save(output_path)
                    print(f'Successfully resized and saved {output_path}')
                except Exception as e:
                    print(f'Failed to process {img_path}: {e}')


input_dir = 'C:\\Users\\aburo\\OneDrive\\Desktop\\INTERN TASKS\\1000images'
output_dir = 'C:\\Users\\aburo\\OneDrive\\Desktop\\INTERN TASKS\\resized'
target_size = (224, 224)
resize(input_dir, output_dir, target_size)


# In[ ]:




