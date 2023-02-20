import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s: ')

package_name = "scania"

list_of_files = [
   ".github/workflows/main.yaml",
   f"{package_name}/__init__.py", 
   f"{package_name}/components/__init__.py", 
   f"{package_name}/pipeline/__init__.py", 
   f"{package_name}/entity/__init__.py", 
      f"{package_name}/utils.py", 
   f"{package_name}/connection.py",
   "requirements.txt", 
   "data_dump.py",
   "setup.py",
   "main.py",
   "init_setup.sh"
    
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")