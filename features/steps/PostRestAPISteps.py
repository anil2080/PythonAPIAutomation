from behave import *
import requests
from utilities.configurations import *
from utilities.resources import *
from utilities.post_payload import *


@given('A post Request with some parameters')
def step_impl(context):
    context.URL = getConfig()['API']['HOST'] + APIResources.POSTRESOURCE
    context.APIheaders = {"Content-Type": "application/json"}


@when('I call Requests post method with request payload to create user')
def step_impl(context):
    context.response = requests.post(context.URL, json=createUserPayload(), headers=context.APIheaders)
    response_Json = context.response.json()
    print(response_Json)
    name = response_Json['name']
    id = response_Json['id']
    print("The first Name is : " + name)
    print("The Id is : " + id)


@then('I should be able to create a user successfully')
def step_impl(context):
    assert context.response.status_code == 201
    assert context.response.json()['name'] == 'morpheus'