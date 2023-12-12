import json

# Read data from data1.json and data2.json
with open('AllData.json', 'r') as file:
    mainfile = json.load(file)

with open('mendata.json', 'r') as file:
    mendata = json.load(file)

with open('womendata.json', 'r') as file:
    womendata = json.load(file)

with open('kiddata.json', 'r') as file:
    kiddata = json.load(file)

with open('home&living.json', 'r') as file:
    homeliving = json.load(file)






for item in mainfile:
    if(item['departmentType']=='men'):
        item['product_images']=mendata[item['product_title']]

    if(item['departmentType']=='women'):
        item['product_images'] = womendata[item['product_title']]

    if item['departmentType']=='kid':
        item['product_images'] = kiddata[item['product_title']]

    if item['departmentType'] == 'home & living':
        item['product_images'] = homeliving[item['product_title']]



print(mainfile)


file_path = 'updatedata1.json'  # Replace 'mendata.json' with your desired file name and path

# Write the dictionary content to a JSON file
with open(file_path, 'w') as json_file:
    json.dump(mainfile, json_file)

