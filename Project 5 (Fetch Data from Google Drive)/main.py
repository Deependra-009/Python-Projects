import json
from pathlib import Path


def load_json(file_path: str):
    """
    Loads JSON data from a file.

    :param file_path: The path to the JSON file.
    :return: The JSON data loaded as a dictionary.
    """
    with open(file_path, 'r') as file:
        return json.load(file)


def update_images(image,product):

    for item in product:
        print(item['product_title'])
        key=item['product_title']
        item['product_images']=image[key]
    # allProduct=product

    return product;


def save_json(data: dict, file_path: str):
    """
    Saves data to a JSON file.

    :param data: The data to save.
    :param file_path: The path to the JSON file.
    """
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


# Define file paths
file1_path = 'image_folders_map.json'  # JSON mapping folder names to image paths
file2_path = 'home&living.json'  # JSON containing titles and images arrays

# Load JSON data from files
data1 = load_json(file1_path)
data2 = load_json(file2_path)

# Update images array in the second file based on the first file's data
updated_data2 = update_images(data1, data2)

# Save the updated data back to the second file
save_json(updated_data2, file2_path)

print(f'Successfully updated {file2_path} with images from {file1_path}')

# ------------------------------------------------------------------------------------------------

# from pathlib import Path
# import json
#
#
# def find_images(base_dir: Path, image_extensions: set):
#     """
#     Recursively finds all image files in the given directory and its subdirectories.
#
#     :param base_dir: The root directory to start searching from.
#     :param image_extensions: A set of image file extensions to search for.
#     :return: A list of paths to the image files.
#     """
#     image_paths = []
#     for file in base_dir.rglob('*'):
#         if file.suffix.lower() in image_extensions:
#             image_paths.append(file)
#     return image_paths
#
#
# def create_folder_image_map(base_dir: Path, image_paths: list):
#     """
#     Creates a dictionary mapping folder names to the relative paths of images within them.
#
#     :param base_dir: The base directory to calculate relative paths from.
#     :param image_paths: A list of image file paths.
#     :return: A dictionary with folder names as keys and relative paths as values.
#     """
#     folder_image_map = {}
#     for image_path in image_paths:
#         relative_path = image_path.relative_to(base_dir)
#         # Extract folder name and image path
#         parts = relative_path.parts
#         folder_name = parts[-2] if len(parts) >= 2 else parts[0]
#         if folder_name not in folder_image_map:
#             folder_image_map[folder_name] = []
#         folder_image_map[folder_name].append(str(relative_path).replace('\\', '/'))
#     return folder_image_map
#
#
# def save_to_json(data: dict, output_file: str):
#     """
#     Saves the given dictionary to a JSON file.
#
#     :param data: The dictionary to save.
#     :param output_file: The path to the output JSON file.
#     """
#     with open(output_file, 'w') as f:
#         json.dump(data, f, indent=4)
#
#
# # Define the base directory where the images are stored
# base_dir = Path('UrbanIndie')
#
# # Define the set of image file extensions to look for
# image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'}
#
# # Find all image files
# image_paths = find_images(base_dir, image_extensions)
#
# # Create folder to image path map
# folder_image_map = create_folder_image_map(base_dir, image_paths)
#
# # Save the map to a JSON file
# output_file = 'image_folders_map.json'
# save_to_json(folder_image_map, output_file)
#
# print(f'Successfully saved the image folder map to {output_file}')

#     ------------------------------------------------------------------------------------------------

# from googleapiclient.discovery import build
# from google.oauth2.credentials import Credentials
# import json
#
# # Provide your credentials (client ID, client secret, etc.) here
# credentials = Credentials(
#     token="",
#     refresh_token="",
#     token_uri="",
#     client_id="",
#     client_secret="",
# )
#
# # Build the Drive API service
# service = build('drive', 'v3', credentials=credentials)
#
# # ID of the folder you want to access (replace with your folder ID)
# folder_id = '19-nJUHhZiQAzAvl4T9D9l3doqQbGSIRC'
# # Call the Drive v3 API
# results = service.files().list(q=f"'{folder_id}' in parents",pageSize=50).execute()
# # get the results
# items = results.get('files', [])
#
# url="https://drive.google.com/uc?export=view&id="
#
# dict={}
# list=[]
# for i1 in items:
#     r1 = service.files().list(q=f"'{i1['id']}' in parents", pageSize=18).execute()
#     # print(i1)
#
#     # <img src="https://drive.google.com/uc?export=view&id=1N-msX_JEDVI6d2zTJLROCFxXtHn270m4">
#     name=i1['name'].split('.')[0]
#     url="<img src='https://drive.google.com/uc?export=view&id="+i1['id']+"'>"
#     print(url+" "+name)
#     dict[int(name)]=url
#     list.append(url)
#
#     # for i2 in r1.get('files',[]):
#
#         # print(i1['name']+" "+i2['name'])
#         #
#         # r2 = service.files().list(q=f"'{i2['id']}' in parents", pageSize=18).execute()
#         #
#         # list=[]
#         #
#         # for i3 in r2.get('files',[]):
#         #     final_url=url+i3['id']
#         #     list.append(final_url)
#         #     print(final_url)
#         #
#         # dict[i2['name']]=list
#
#     # print()
#
#
# print(dict)
# print(list.reverse())
# list.reverse()
# file_path = 'UrbanIndie.json'  # Replace 'mendata.json' with your desired file name and path
#
# # Write the dictionary content to a JSON file
# with open(file_path, 'w') as file:
#     for i in range(1,30,1):
#         print(i)
#         str=dict[i]
#         file.write('\n'+str)
#
#
#
