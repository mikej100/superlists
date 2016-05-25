from behave import given, when, then
from selenium import webdriver

@when(u'I visit the list home page')
def step(context):
    context.browser = webdriver.Firefox()

    context.browser.get('http://localhost:8000')

@then(u'The page title should include {text}')
def step(context, text):
    assert text in context.browser.title
