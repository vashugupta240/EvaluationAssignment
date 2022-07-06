###PROJECT OVERVIEW
This project is for test automation for the evaluation
>This project is done by using Python Request’s library for testing various APIs

##Requirements
order to utilise this project you need to have the following installed locally:
* Python 
* pytest
* Request

## ABOUT
* This task contains four test Cases:
    * Create a organization
    * Update Organization
    * Get Organization
    * Delete Organization

##Usage
The project is broken into separate modules for testing. 

To run modules, navigate to test-automation directory and run:

``` commands
py.test
 ```
Or to run specific test file
 
 ``` commands
 py.test testFileName
 ```
To get more infomation during running the test you can type
 ``` commands
 py.test -v
 ```
Or some more commands
 ``` commands
 py.test -s -k -m
 ```

##REQUIREMENTS
* __LANGUAGE:__ Python 3
* __FRAMEWORK:__ RequestLibrary and Pytest

## TABLE OF CONTENT
>###TestCase
>>####test_Organization
> ###Utils
>>####Locators
>>####ReadData
>>####TestData

##Summary
This task contains Creating API test framework using Python Request’s library for testing various APIs of the Web App https://trello.com/ for which API Documentation are at https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/.
This framework holds creating a new Organization, updating them, extracting necessary value and deleting the created organization.