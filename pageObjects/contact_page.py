import time
from selenium.webdriver.common.by import By


class ContactPage:

    def __init__(self, driver):
        self.driver = driver
        self.contact_dropdown = "//a[@title='Leads']/following::a[@role='button'][2]"
        self.new_contact = "//span[text()='New Contact']"
        self.contact_last_name = "//input[@name='lastName']"
        self.contact_account_search = "//input[@placeholder='Search Accounts...']"
        self.first_contact = "//li[@class='slds-listbox__item'][1]"
        self.contact_save = "//button[@name='SaveEdit']"
        self.contact_final_name = "//slot[@name='primaryField']/lightning-formatted-name"

    def click_contact_dropdown(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.contact_dropdown).click()

    def click_new_contact(self):
        element = self.driver.find_element(By.XPATH, self.new_contact)
        self.driver.execute_script("arguments[0].click();", element)

    def enter_contact_last_name(self, last_name):
        self.driver.find_element(By.XPATH, self.contact_last_name).send_keys(last_name)

    def enter_contact_account_name(self, acc_name):
        self.driver.find_element(By.XPATH, self.contact_account_search).clear()
        self.driver.find_element(By.XPATH, self.contact_account_search).send_keys(acc_name)

    def select_contact_account_name(self):
        self.driver.find_element(By.XPATH, self.first_contact).click()

    def click_save_contact(self):
        self.driver.find_element(By.XPATH, self.contact_save).click()
        time.sleep(2)

    def verify_created_contact_name(self):
        self.driver.refresh()
        time.sleep(3)
        return self.driver.find_element(By.XPATH, self.contact_final_name).text
