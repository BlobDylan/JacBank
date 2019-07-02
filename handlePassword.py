import pyperclip
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from db_func import get_xpath,add_xpath


def try_auto_enter_password(url, password):
    """try's to open chrome and auto enter the given password in a given url"""
    xpath = get_xpath(url)
    if xpath is not None and xpath is not 'a':
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
    """try's to open chrome and auto enter the given password in a given url and xpath.
    in case of a success it saves the xpath in the database with the url"""
    x = get_xpath(url)
    if x is None and x is not 'a':
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
    """copies a given text to the clipboard"""
    print("copied to clipboard")
    pyperclip.copy(x)

#try_auto_enter_password("https://www.facebook.com/","123")
#auto_enter_password("https://www.facebook.com/","123","//input[@type='password']")