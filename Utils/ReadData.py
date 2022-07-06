import json

from Utils import Locators

#HANDING JSON FILE
with open(Locators.File_Path, 'r+') as json_file:
    file_load = json.load(json_file)
    createData = file_load['DATA']              #EXTRACT 'DATA' VALUE
    updateData = file_load['UPDATE_DATA']       #EXTRACT 'UPDATE_DATA' VALUE
