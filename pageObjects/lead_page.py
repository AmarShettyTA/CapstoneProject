import time
from selenium.webdriver.common.by import By


class LeadPage:

    def __init__(self, driver):
        self.driver = driver
        self.leads_dropdown = "//a[@title='Leads']/following::a[@role='button'][1]"
        self.new_lead = "//span[text()='New Lead']"
        self.lead_lastname = "//input[@name='lastName']"
        self.lead_company = "//input[@name='Company']"
        self.lead_save = "//button[@name='SaveEdit']"
        self.lead_final_name = "//*[@name='primaryField']/lightning-formatted-name"
        self.lead_convert = "//button[@name='Convert']"
        self.convert_lead_button = "(//button[text()='Convert'])[2]"
        self.converted_lead_text = "(//h2[text()='Your lead has been converted'])"
        self.close_lead_window = "//button[@title='Close this window']"
        self.close_go_to_lead = "//button[text()='Go to Leads']"
        self.existing_account = "//span[text()='Choose Existing Account']"
        self.existing_account_text_field = "//input[@title='Search for matching accounts']"
        self.account_list = "//div[@class='listContent']//li"
        self.list_first_account = "//div[@class='listContent']//li[1]"

    def click_leads_drop_down(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.leads_dropdown).click()

    def click_new_lead(self):
        element = self.driver.find_element(By.XPATH, self.new_lead)
        self.driver.execute_script("arguments[0].click();", element)

    def enter_the_details(self, lastname, company):
        self.driver.find_element(By.XPATH, self.lead_lastname).send_keys(lastname)
        self.driver.find_element(By.XPATH, self.lead_company).send_keys(company)

    def click_save_lead(self):
        self.driver.find_element(By.XPATH, self.lead_save).click()
        time.sleep(3)

    def verify_created_lead_name(self):
        self.driver.refresh()
        time.sleep(3)
        return self.driver.find_element(By.XPATH, self.lead_final_name).text

    def click_lead_convert(self):
        self.driver.find_element(By.XPATH, self.lead_convert).click()

    def click_convert_button(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.convert_lead_button).click()
        time.sleep(2)

    def verify_converted_or_not(self):
        return self.driver.find_element(By.XPATH, self.converted_lead_text).text

    def close_lead_pop_up(self):
        element = self.driver.find_element(By.XPATH, self.close_lead_window)
        self.driver.execute_script("arguments[0].click();", element)

    def is_user_on_lead_page(self):
        return self.driver.find_element(By.XPATH, self.lead_final_name).isDisplayed()

    def new_or_existing_account(self, account_type, account_name):
        if account_type == "New":
            pass
        elif account_type == "Existing":
            self.driver.find_element(By.XPATH, self.existing_account).click()
            self.driver.find_element(By.XPATH, self.existing_account_text_field).send_keys(account_name)
            time.sleep(3)
            self.driver.find_element(By.XPATH, self.list_first_account).click()
        else:
            print("Provide Either 'New' or 'Existing' value as Account type")
            raise NotImplementedError
