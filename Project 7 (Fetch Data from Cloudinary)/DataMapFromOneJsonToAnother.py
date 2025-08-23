import json
import re

cleaned_data = {}

def remove_special_characters_from_keys(data):

    for key, value in data.items():
        # Remove special characters from the key
        cleaned_key = re.sub(r'[^A-Za-z0-9\s]', '', key).replace(' ', '').upper()
        # Add the cleaned key and its value to the new dictionary
        cleaned_data[cleaned_key] = value



def load_json(file_path: str):
    """
    Loads JSON data from a file.

    :param file_path: The path to the JSON file.
    :return: The JSON data loaded as a dictionary.
    """
    with open(file_path, 'r') as file:
        return json.load(file)

def remove_special_characters(input_string):
    # Use regex to keep only alphanumeric characters and spaces
    cleaned_string = re.sub(r'[^A-Za-z0-9\s]', '', input_string).replace(' ', '')
    return cleaned_string

def update_images(product,image):

    for item in product:

        product_key=remove_special_characters(item['product_title']).upper()


        print(product_key)
        print(image[product_key])


        # if()
        # print(item[product_key])
        # key=item['product_title']
        item['product_images']=image[product_key]
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
file1_path = 'UrbanIndie.json'  # JSON mapping folder names to image paths
file2_path = 'temp.json'  # JSON containing titles and images arrays





# Load JSON data from files
data1 = load_json(file1_path)
data2 = load_json(file2_path)

# Remove special charater from keys in Images Json
remove_special_characters_from_keys(data2)

# print(cleaned_data)

# Update images array in the second file based on the first file's data
updated_data2 = update_images(data1, cleaned_data)

# Save the updated data back to the second file
save_json(updated_data2, file2_path)

print(f'Successfully updated {file2_path} with images from {file1_path}')