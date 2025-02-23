import logging

from pytest_bdd import scenarios, given, when, then, parsers

# Load the feature file
scenarios("../features/create_lead.feature")


# Step Definitions
@given("User logs in to salesforce")
def step_impl(login_page):
    login_page.open_login_page("https://login.salesforce.com")


@when(parsers.parse(u'User enters "{username}" and "{password}"'))
def step_impl(login_page, username, password):
    login_page.enter_username(username)
    login_page.enter_password(password)


@then("User clicks on login")
def step_impl(login_page):
    login_page.click_login()


@then("User is on dashboard page")
def step_impl(login_page):
    assert login_page.is_dashboard_displayed()


@then("User is on Home Page")
def step_impl():
    pass


@then('User clicks on Accounts dropdown and new account')
def step_impl(account_page):
    account_page.click_account_dropdown()
    account_page.click_new_account()


@then(parsers.parse(u'User enters "{account_name}"'))
def step_impl(account_page, account_name):
    account_page.enter_account_name(account_name)


@then('User clicks on Save account button')
def step_impl(account_page):
    account_page.click_save_account()


@then(parsers.parse(u'Verify Account is Created by the "{account_name}"'))
def step_impl(account_page, account_name):
    assert account_page.verify_created_account_name() == account_name


@when("User clicks on Lead dropdown and clicks New Lead")
def step_impl(lead_page):
    lead_page.click_leads_drop_down()
    lead_page.click_new_lead()


@then(parsers.parse(u'User enters "{last_name}" and "{company}"'))
def step_impl(lead_page, last_name, company):
    lead_page.enter_the_details(last_name, company)


@then('Click on Save button')
def step_impl(lead_page):
    lead_page.click_save_lead()


@then(parsers.parse(u'Verify Lead is Created using "{last_name}"'))
def step_impl(lead_page, last_name):
    assert lead_page.verify_created_lead_name() == last_name
    logging.info("Lead created successfully")


@when('User clicks on convert')
def step_impl(lead_page):
    lead_page.click_lead_convert()


@then(parsers.parse('User choses account type: "{account type}" and account name: "{account namr}"'))
def step_impl(lead_page, account_type, account_name):
    lead_page.new_or_existing_account(account_type, account_name)


@then('User clicks on Convert button')
def step_impl(lead_page):
    lead_page.click_convert_button()


@then('Close Lead Popup screen')
def step_impl(lead_page):
    lead_page.close_lead_pop_up()
