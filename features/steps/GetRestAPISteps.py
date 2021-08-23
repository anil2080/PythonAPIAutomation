from behave import *
import requests
from utilities.configurations import *
from utilities.resources import *


@given('A Get Request with some parameters')
def step_impl(context):
    context.URL = getConfig()['API']['HOST'] + APIResources.GETRESOURCE
    context.APIheaders = {"Content-Type": "application/json"}


@when('I call requests module Get method with Get URL')
def step_impl(context):
    context.response = requests.get(context.URL,
                                    params={'page': 2},
                                    headers=context.APIheaders)
    response_Json = context.response.json()
    print(response_Json)
    first_name = response_Json['data'][0]['first_name']
    print("The first Name is : " + first_name)


@then('I should be able to see the related data')
def step_impl(context):
    assert context.response.status_code == 200
    assert context.response.json()['data'][0]['first_name'] == 'Michael'

