# Importing json class library
import json

# create data object
data = {

    'name': 'John Doe',
    'age': 30,
    'city': 'New York, NY',
    'interests': ['Golf', 'Running', 'Football', 'Traveling'],
    'is_student': False   
}

# with statement to write to data.json file
with open('data.json','w') as json_file:

# formats the python data to a .json
    json.dump(data,json_file,indent=4)

# prints to console if data written
print("Data has been written to data.json.")


# with statement to read from the .json file
with open('data.json','r') as json_file:
   
    # create loaded_data object
    loaded_data = json.load(json_file)

# prints to console if successful
print("Successfully able to read data.json.")
print(loaded_data)

#
loaded_data['age'] = 34
loaded_data['interests'].append('History')
loaded_data['interests'].append('Gaming')
loaded_data['interests'].remove('Football')

# writes new list changes to data.json file
with open('data.json','w') as json_file:

    json.dump(loaded_data,json_file,indent=4)

print("Data has been re-written to data.json.")