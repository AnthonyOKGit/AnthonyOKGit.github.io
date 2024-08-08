import os
import json

images_dir = 'images'

supported_extensions = ('.png', '.jpg', '.jpeg', '.gif')

image_files = [f for f in os.listdir(images_dir) if f.lower().endswith(supported_extensions)]

with open('images.json', 'w') as json_file:
    json.dump(image_files, json_file, indent=4)

print('images.json populated')
