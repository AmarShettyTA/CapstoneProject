import time
from selenium.webdriver.common.by import By


class OpportunitiesPage:

    def __init__(self, driver):
        self.driver = driver
        self.opportunity_dropdown = "//a[@title='Leads']/following::a[@role='button'][4]"
        self.new_opportunity = "//span[text()='New Opportunity']"
        self.opportunity_name = "//input[@name='Name']"
        self.opportunity_account_search = "//input[@placeholder='Search Accounts...']"
        self.opportunity_first_account = "//li[@class='slds-listbox__item'][1]"
        self.opportunity_close_date = "//input[@name='CloseDate']"
        self.opportunity_stage_dropdown = "(//button[@aria-haspopup='listbox'])[1]"
        self.opportunity_stage_options = "//div[@aria-label='Stage']/lightning-base-combobox-item"
        self.opportunity_forecast_category = "//button[@aria-label='Forecast Category']"
        self.opportunity_forecast_options = "//div[@aria-label='Forecast Category']/lightning-base-combobox-item"
        self.opportunity_save = "//button[@name='SaveEdit']"
        self.opportunity_final_name = "(//slot[@name='primaryField']/lightning-formatted-text)"

    def click_opportunity_dropdown(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.opportunity_dropdown).click()

    def click_new_opportunity(self):
        element = self.driver.find_element(By.XPATH, self.new_opportunity)
        self.driver.execute_script("arguments[0].click();", element)

    def enter_opportunity_name(self, opportunity_name):
        self.driver.find_element(By.XPATH, self.opportunity_name).send_keys(opportunity_name)

    def enter_opportunity_account_name(self, acc_name):
        self.driver.find_element(By.XPATH, self.opportunity_account_search).clear()
        self.driver.find_element(By.XPATH, self.opportunity_account_search).send_keys(acc_name)

    def select_opportunity_account_name(self):
        self.driver.find_element(By.XPATH, self.opportunity_first_account).click()

    def enter_close_date(self, date):
        self.driver.find_element(By.XPATH, self.opportunity_close_date).send_keys(date)

    def select_opportunity_stage(self, opportunity_stage):
        element = self.driver.find_element(By.XPATH, self.opportunity_stage_dropdown)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        elements = self.driver.find_elements(By.XPATH, self.opportunity_stage_options)
        for options in elements:
            if options.text == opportunity_stage:
                options.click()
                break

    def select_opportunity_forecast(self, opportunity__forecast):
        element = self.driver.find_element(By.XPATH, self.opportunity_forecast_category)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        elements = self.driver.find_elements(By.XPATH, self.opportunity_forecast_options)
        for options in elements:
            if options.text == opportunity__forecast:
                options.click()
                break

    def click_save_opportunity(self):
        self.driver.find_element(By.XPATH, self.opportunity_save).click()
        time.sleep(2)

    def verify_created_opportunity_name(self):
        self.driver.refresh()
        time.sleep(2)
        return self.driver.find_element(By.XPATH, self.opportunity_final_name).text
