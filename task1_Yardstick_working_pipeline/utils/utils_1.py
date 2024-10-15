import os 
from box.exceptions import BoxValueError
import yaml

import json


from box import ConfigBox
from pathlib import Path
from typing import Any
import base64



def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    reads yaml file and returns

    Args:
        path_to_yaml (str) : path like input

    Raises:
        Valueerror: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type

    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
# Function to save text to a file
def save_to_file(filename, text):
    try:
        # Open the file in write mode ('w') - it will create the file if it doesn't exist
        with open(filename, 'w') as file:
            file.write(text)
        print(f"Text successfully saved to {filename}")
    except Exception as e:
        print(f"Error saving file: {e}")

# Function to read text from a file
def read_from_file(filename):
    try:
        # Open the file in read mode ('r')
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    except Exception as e:
        print(f"Error reading file: {e}")


# # Example usage
# filename = "output.txt"
# text = "This is a sample text that will be saved to a file."

# # Call the function to save the text
# save_to_file(filename, text)
    
# @ensure_annotations
# def create_directories(path_to_directories: list, verbose=True):
#     """"
#     creates list of directories

#     Args:
#         path_to_directories(list): list of path of directoreies
#         ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to True
#     """
#     for path in path_to_directories:
#         os.makedirs(path, exist_ok=True)
#         if verbose:
#             logger.info(f"created directory at: {path}")

# @ensure_annotations
# def save_json(path: Path, data: dict):
#     """
#     save json data
#     Args:
#         path (Path): path to json file
#         data (dict): data to be saved in json file
#     """

#     with open(path, 'w') as f:
#         json.dump(data, f, indent=4)
#     logger.info(f"json file saved at: {path}")

# @ensure_annotations
# def load_json(path: Path) -> ConfigBox:
#     """
#     load json files data
#     Args:
#         path (Path): path to json file

#     Returns:
#         ConfigBox: data as class attributes instead of dict
#     """
#     with open(path)  as f:
#         content = json.load(f)
#     logger.info(f"json file loaded successfully from: {path}")
#     return ConfigBox(content)

# @ensure_annotations
# def save_bin(data: Any, path: Path):
#     """
#     save binary file
#     Args:
#         data (Any): data to be saved as binary
#         path (Path): path to binary file
#     """
#     joblib.dump(value=data, filename=path)
#     logger.info(f"binary file saved at: {path}")

# @ensure_annotations
# def load_bin(path: Path)-> Any:
#     """
#     load binary data
#     Args:
#         path (Path):path to binary file
#     Returns: 
#         Any : object stored in the file
#     """
#     data = joblib.load(path)
#     logger.info(f"binary file loaded from: {path}")
#     return data

# @ensure_annotations
# def get_size(path: Path)->str:
#     """
#     get size in KB
#     Args:
#         path (Path): path of the file
#     Returns:
#         str: size in KB
#     """
#     size_in_kb = round(os.path.getsize(path)/1024)
#     return f"~ {size_in_kb} KB"

# def decodeImage(imgstring, filenamne):
#     imgdata = base64.b64decode(imgstring)
#     with open(filenamne,'wb') as f:
#         f.write(imgdata)
#         f.close()

# def encodedImageIntoBase64(croppedImagePath):
#     with open(croppedImagePath, "rb") as f:
#         return base64.b64encode(f.read())