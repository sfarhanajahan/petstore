import requests
import json
import jsonpath

baseUrl = "https://petstore.swagger.io/v2"


def test_user_delete():
    path = "/user"

    # Retrieve User data for Deletion
    file = open('TestData/sample-user.json', "r")
    fileData = json.loads(file.read())
    username = fileData["username"]

    # Send DELETE Request with username
    response = requests.delete(url=baseUrl+path+"/"+str(username))
    responseJson = json.loads(response.text)


    # Print new user data in Test report
    print(responseJson)

    # Assertion Starts with status 200
    assert response.status_code == 200, "Status should be 200"
    assert jsonpath.jsonpath(responseJson, '$.message')[
        0] == username, \
        "Username didn't Match with user registration Data"
