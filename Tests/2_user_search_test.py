import requests
import json
import jsonpath

baseUrl = "https://petstore.swagger.io/v2"


def test_user_search():
    path = "/user"

    # Retrieve User data for search and assertion
    file = open('TestData/sample-user.json', "r")
    fileData = json.loads(file.read())
    email = fileData["email"]
    firstName = fileData["firstName"]
    lastName = fileData["lastName"]
    password = fileData["password"]
    phone = fileData["phone"]
    username = fileData["username"]
    userStatus = fileData["userStatus"]

    file = open('TestData/successful_user_registration.json', "r")
    fileData = json.loads(file.read())
    id = fileData["message"]

    # Send GET Request with username
    response = requests.get(url=baseUrl+path+"/"+str(username))
    responseJson = json.loads(response.text)


    # Print new user data in Test report
    print(responseJson)

    # Assertion Starts with status 200
    assert response.status_code == 200, "Status should be 200"

    # Validate User search data is matching with the successful user registration response 
    assert jsonpath.jsonpath(responseJson, '$.id')[
        0] == int(id), \
        "ID didn't Match with user registration Data"
    assert jsonpath.jsonpath(responseJson, '$.firstName')[
        0] == firstName, \
        "FirstName didn't Match with user registration Data"
    assert jsonpath.jsonpath(responseJson, '$.lastName')[
        0] == lastName, \
        "LastName didn't Match with user registration Data"
    assert jsonpath.jsonpath(responseJson, '$.email')[
        0] == email, \
        "Email didn't Match with user registration Data"
    assert jsonpath.jsonpath(responseJson, '$.password')[
        0] == password, \
        "Password didn't Match with user registration Data"
    assert jsonpath.jsonpath(responseJson, '$.phone')[
        0] == phone, \
        "Phone didn't Match with user registration Data"
    assert jsonpath.jsonpath(responseJson, '$.userStatus')[
        0] == userStatus, \
        "UserStatus didn't Match with user registration Data"
