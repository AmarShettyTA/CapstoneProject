from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username = "username"
        self.password = "password"
        self.login_button = "Login"
        self.sales_dashboard = "//span[@title='Sales']"

    def open_login_page(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.username).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, self.login_button).click()

    def is_dashboard_displayed(self):
        return self.driver.find_element(By.XPATH, self.sales_dashboard).is_displayed()
