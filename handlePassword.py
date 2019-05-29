import pyperclip
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from db_func import get_xpath,add_xpath


def try_auto_enter_password(url, password):
    xpath = get_xpath(url)
    if xpath is not None:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome("chromedriver", options=chrome_options)
        driver.get(url)

        element = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_xpath(xpath[0][0]))
        element.send_keys(password)
        return 0
    else:
        return 1

def auto_enter_password(url, password, xpath):
    x = get_xpath(url)
    if x is None:
        try:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_experimental_option("detach", True)
            driver = webdriver.Chrome("chromedriver", options = chrome_options)
            driver.get(url)

            element = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_xpath(xpath))
            element.send_keys(password)
            add_xpath(url,xpath)
            return 0
        except:
            return 1
    else:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome("chromedriver", options=chrome_options)
        driver.get(url)

        element = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_xpath(x[0][0]))
        element.send_keys(password)
        return 0

def copy_to_clipboard(x):
    print("copied to clipboard")
    pyperclip.copy(x)

#try_auto_enter_password("https://www.facebook.com/","123")
#auto_enter_password("https://www.facebook.com/","123","//input[@type='password']")