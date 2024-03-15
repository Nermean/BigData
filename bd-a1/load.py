import sys
import pandas as pd

# Check if the dataset path is provided as an argument
if len(sys.argv) != 2:
    print("Please provide the dataset path as an argument: python load.py dataset_path")
    sys.exit(1)
# Get the dataset path from command-line arguments
dataset_path = sys.argv[1]

# Load the dataset
try:
    dataset = pd.read_csv(dataset_path)
    dataset.head()
except FileNotFoundError:
    print("File not found!")
except:
    print("Errorrrrrrrrr")

# run the next file:
import dpre
dpre.run_file(dataset_path)