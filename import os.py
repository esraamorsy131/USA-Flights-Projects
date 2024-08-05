

import os
import kaggle

# Ensure the Kaggle API is authenticated
os.environ['KAGGLE_USERNAME'] = '"esraamorsyelsayed"'
os.environ['KAGGLE_KEY'] = '3592d039bb56af2edb65fc990ed71ae5'

# Define the dataset you want to download
dataset = 'usdot/flight-delays'  # Replace with your dataset

# Define the path where the dataset will be downloaded
download_path = 'E:\POwer BI\D06\Dataset'

# Create the directory if it does not exist
if not os.path.exists(download_path):
    os.makedirs(download_path)

# Download the dataset
kaggle.api.dataset_download_files(dataset, path=download_path,unzip=True)

print(f"Dataset '{dataset}' downloaded and extracted to '{download_path}'")