import cloudinary
import cloudinary.uploader
import cloudinary.api
import json

cloudinary.config(
  cloud_name = "dwirc57cl",
  api_key = "486897895613536",
  api_secret = "-yR19mx5ZuAZJvCylDBBjQlWVHo"
)

dict={}




def get_all_folders():
  result = cloudinary.api.subfolders('UrbanIndie')
  folders = result.get('folders', [])
  folder_names = [folder['name'] for folder in folders]

  for i in folder_names:
    subresult = cloudinary.api.subfolders('UrbanIndie/'+i)
    # print("subrult",subresult)
    subfolder = subresult.get('folders', [])
    sub_folder_names = [folder['name'] for folder in subfolder]

    for j in sub_folder_names:
      subsubresult = cloudinary.api.subfolders('UrbanIndie/' + i+'/'+j)
      # print('subsubresult',subsubresult)
      subsubfolder = subsubresult.get('folders', [])
      subsub_folder_names = [folder for folder in subsubfolder]
      image_list=[]
      for k in subsub_folder_names:
        subsubsubresult = cloudinary.api.resources_by_asset_folder(k['path'])
        subsubsubfolder = subsubsubresult.get('resources', [])
        imagelist=[image['url'] for image in subsubsubfolder]
        image_list=imagelist

        dict[k['name']]=imagelist

        print(k['name'],imagelist)

        # image_list.append(sub)

      # break
    # break



def save_json(data: dict, file_path: str):
    """
    Saves data to a JSON file.

    :param data: The data to save.
    :param file_path: The path to the JSON file.
    """
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)



get_all_folders()

savejson_path = 'UrbanIndie_Images.json'  # JSON containing titles and images arrays
save_json(dict, savejson_path)








# print(dict)


# print(folder_names)

#
# def fetch_images_from_folder(folder_path):
#   try:
#     # Fetch images from the specified folder
#     response = cloudinary.api.resources(
#       type='upload',
#       prefix=folder_path,
#       max_results=30  # Specify the number of results to fetch
#     )
#
#     print("resp",response)
#
#     # Extract URLs of the images
#     images = [resource['url'] for resource in response.get('resources', [])]
#
#     # Go
#
#
#
#
#     return images
#   except cloudinary.exceptions.Error as e:
#     print(f"Error fetching images: {e}")
#     return []
#
#
#
#
# # Example usage
# folder_path = 'UrbanIndie'  # Replace with your folder path in Cloudinary
# images = fetch_images_from_folder(folder_path)
# print(images)
