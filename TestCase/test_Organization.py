import pytest
import requests
from Utils.Locators import baseUrl, path, key_token, headers
from Utils.ReadData import createData, updateData


# CREATING THE ORGANIZATION
def test_createOrg():
    global GettingId
    response = requests.post(baseUrl + path, json=createData, params=key_token, headers=headers)
    assert response.status_code == 200      # validate status code
    resp = response.json()
    GettingId = resp["id"]                  # EXTRACT ID FROM THE RESPONSE


# UPDATING THE ORGANIZATION
def test_updateOrg():
    response = requests.put(baseUrl + path + GettingId, json=updateData, params=key_token, headers=headers)
    resp = response.json()
    assert response.status_code == 200
    verifyId = resp["id"]                   # LATEST ID FROM RESPONSE
    assert verifyId in GettingId
    newData = resp["desc"]                  # EXTRACT UPDATED FROM RESPONSE
    assert newData in updateData['desc']    # VERIFYING UPDATED DETAILS
    print(resp)

# GET THE ORGANIZATION
def test_getOrg():
    response = requests.get(baseUrl + path + GettingId, params=key_token, headers=headers)
    resp = response.json()
    assert response.status_code == 200
    verifyId = resp["id"]
    assert verifyId in GettingId
    print(resp)

# DELETE THE ORGANIZATION
def test_deleteOrg():
    response = requests.delete(baseUrl + path + GettingId, params=key_token, headers=headers)
    assert response.status_code == 200

