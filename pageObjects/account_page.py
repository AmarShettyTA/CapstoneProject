import time
from selenium.webdriver.common.by import By


class AccountPage:

    def __init__(self, driver):
        self.driver = driver
        self.account_dropdown = "//a[@title='Leads']/following::a[@role='button'][3]"
        self.new_account = "//span[text()='New Account']"
        self.account_name = "//input[@name='Name']"
        self.account_save = "//button[@name='SaveEdit']"
        self.account_final_name = "(//slot[@name='primaryField']/lightning-formatted-text)"

    def click_account_dropdown(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.account_dropdown).click()

    def click_new_account(self):
        element = self.driver.find_element(By.XPATH, self.new_account)
        self.driver.execute_script("arguments[0].click();", element)

    def enter_account_name(self, acc_name):
        self.driver.find_element(By.XPATH, self.account_name).send_keys(acc_name)

    def click_save_account(self):
        self.driver.find_element(By.XPATH, self.account_save).click()
        time.sleep(2)

    def verify_created_account_name(self):
        self.driver.refresh()
        time.sleep(2)
        return self.driver.find_element(By.XPATH, self.account_final_name).text
