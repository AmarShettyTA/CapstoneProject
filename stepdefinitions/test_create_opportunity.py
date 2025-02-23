from pytest_bdd import scenarios, given, when, then, parsers

# Load the feature file
scenarios("../features/create_opportunity.feature")


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


@then('User clicks on contact dropdown and clicks new contact')
def step_impl(contact_page):
    contact_page.click_contact_dropdown()
    contact_page.click_new_contact()


@then(parsers.parse(u'User enters "{last name}" and selects the "{account name}"'))
def step_impl(contact_page, last_name, account_name):
    contact_page.enter_contact_last_name(last_name)
    contact_page.enter_contact_account_name(account_name)
    contact_page.select_contact_account_name()


@then('User clicks on save contact button')
def step_impl(contact_page):
    contact_page.click_save_contact()


@then(parsers.parse(u'Verify contact is created by the "{last name}"'))
def step_impl(contact_page, last_name):
    assert contact_page.verify_created_contact_name() == last_name


@then('User clicks on opportunity dropdown and clicks new opportunity')
def step_impl(opportunity_page):
    opportunity_page.click_opportunity_dropdown()
    opportunity_page.click_new_opportunity()


@then(parsers.parse(u'User enters "{opportunity name}" and Select the "{account name}"'))
def step_impl(opportunity_page, opportunity_name, account_name):
    opportunity_page.enter_opportunity_name(opportunity_name)
    opportunity_page.enter_opportunity_account_name(account_name)
    opportunity_page.select_opportunity_account_name()


@then(parsers.parse(u'User enters opportunity close date: "{close_date}"'))
def step_impl(opportunity_page, close_date):
    opportunity_page.enter_close_date(close_date)


@then('User selects opportunity stage: "{opportunity stage}"')
def step_impl(opportunity_page, opportunity_stage):
    opportunity_page.select_opportunity_stage(opportunity_stage)


@then(parsers.parse(u'User selects opportunity forecast: "{opportunity_forecast}"'))
def step_impl(opportunity_page, opportunity_forecast):
    opportunity_page.select_opportunity_forecast(opportunity_forecast)


@then(parsers.parse(u'User clicks on save button contact button'))
def step_impl(opportunity_page):
    opportunity_page.click_save_opportunity()


@then(parsers.parse(u'Verify opportunity is created by the "{opportunity name}"'))
def step_impl(opportunity_page, opportunity_name):
    assert opportunity_page.verifyCreatedopportunityName() == opportunity_name
