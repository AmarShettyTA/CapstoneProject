from selenium import webdriver


def get_driver():
    options = webdriver.EdgeOptions()
    options.add_argument("inPrivate")
    driver = webdriver.Edge(options=options)
    driver.maximize_window()
    driver.implicitly_wait(15)
    return driver
