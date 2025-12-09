# main.py

# Import modules from the 'scripts' directory
# This action triggers the creation of the __pycache__ folder and .pyc files.
from scripts.data_processing import load_and_clean_data
from scripts.model import train_models

print("Modules imported successfully.")
print("The __pycache__ folder should now be created inside the 'scripts' directory.")

# Note: You do not need to call the functions, just importing them is enough.