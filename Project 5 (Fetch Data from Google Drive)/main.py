from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import json

# Provide your credentials (client ID, client secret, etc.) here
credentials = Credentials(
    token="",
    refresh_token="",
    token_uri="",
    client_id="",
    client_secret="",
)

# Build the Drive API service
service = build('drive', 'v3', credentials=credentials)

# ID of the folder you want to access (replace with your folder ID)
folder_id = '19-nJUHhZiQAzAvl4T9D9l3doqQbGSIRC'
# Call the Drive v3 API
results = service.files().list(q=f"'{folder_id}' in parents",pageSize=50).execute()
# get the results
items = results.get('files', [])

url="https://drive.google.com/uc?export=view&id="

dict={}
list=[]
for i1 in items:
    r1 = service.files().list(q=f"'{i1['id']}' in parents", pageSize=18).execute()
    # print(i1)

    # <img src="https://drive.google.com/uc?export=view&id=1N-msX_JEDVI6d2zTJLROCFxXtHn270m4">
    name=i1['name'].split('.')[0]
    url="<img src='https://drive.google.com/uc?export=view&id="+i1['id']+"'>"
    print(url+" "+name)
    dict[int(name)]=url
    list.append(url)

    # for i2 in r1.get('files',[]):

        # print(i1['name']+" "+i2['name'])
        #
        # r2 = service.files().list(q=f"'{i2['id']}' in parents", pageSize=18).execute()
        #
        # list=[]
        #
        # for i3 in r2.get('files',[]):
        #     final_url=url+i3['id']
        #     list.append(final_url)
        #     print(final_url)
        #
        # dict[i2['name']]=list

    # print()


print(dict)
print(list.reverse())
list.reverse()
file_path = 'home&living.json'  # Replace 'mendata.json' with your desired file name and path

# Write the dictionary content to a JSON file
with open(file_path, 'w') as file:
    for i in range(1,30,1):
        print(i)
        str=dict[i]
        file.write('\n'+str)



