import kagglehub
import shutil
import os

# Download to cache
path = kagglehub.dataset_download("alitaqishah/blood-cell-anomaly-detection-2025")

# Target directory (inside your data folder)
target_dir = os.path.join(os.path.dirname(__file__), "dataset")

# Move dataset into ./data/dataset
if not os.path.exists(target_dir):
    shutil.move(path, target_dir)
else:
    print("Dataset already exists in data/dataset")

print("Dataset ready at:", target_dir)