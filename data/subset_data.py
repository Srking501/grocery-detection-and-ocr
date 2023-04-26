import os
import shutil
import pandas as pd
from tqdm import tqdm

# Set the directory path where the images are stored
directory_path = 'SKU110K_fixed/images/'

# Set the output directory where the extracted images will be saved
output_directory = 'SKU110K_fixed_small/images/'

# Get a list of all the files in the directory
all_files = os.listdir(directory_path)

# Filter the files to only include those that start with "train_" and end with ".jpeg"
train_files = [f for f in all_files if f.startswith('train_') and f.endswith('.jpg')]

# Sort the list of files alphabetically
train_files.sort()

# Extract the first 998 files
train_subset = train_files[:998]

# Create the output directory if it doesn't already exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Copy the selected files to the output directory with a progress bar
for file_name in tqdm(train_subset, desc='Copying files', unit='file'):
    source_path = os.path.join(directory_path, file_name)
    destination_path = os.path.join(output_directory, file_name)
    shutil.copyfile(source_path, destination_path)

# Load the annotations CSV file
annotations_file = 'SKU110K_fixed/annotations/annotations_train.csv'
annotations = pd.read_csv(annotations_file, names=["image_name", "x1", "y1", "x2", "y2",
                                                   "class", "image_width", "image_height"])

# Filter the annotations to only include rows for the selected image files
annotations_subset = annotations.loc[annotations['image_name'].isin(train_subset)]

# Save the filtered annotations to a new CSV file
annotations_output_file = 'SKU110K_fixed_small/annotations/annotations_train_small.csv'
annotations_subset.to_csv(annotations_output_file, index=False)
