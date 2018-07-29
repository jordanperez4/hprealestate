from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re


delay = 10
zillow_info = {}
trulia_info = {}

def get_zillow_info(driver, search_text):
    driver.get("https://www.zillow.com/")
    try:
        zillow_search_input = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'citystatezip')))
        print("Page is ready!")
        zillow_search_input.send_keys(search_text)
        zillow_search_input.submit()
    except TimeoutException:
        print("Loading took too much time!")
    try:
        est_text = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'estimates'))).text
        print("Page is ready!")
        price_items = re.findall(r'\$(?:\d+\.)?\d+.\d+', est_text)
        zillow_info["Zillow House Estimate"] = price_items[0]
        #zillow_info["Zillow Rent Estimate"] = price_items[1]
    except TimeoutException:
        print("Loading took too much time!")
    return zillow_info

def get_trulia_info(driver, search_text):
    driver.get("https://www.trulia.com/")
    try:
        trulia_search_input = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'searchBox')))
        print("Page is ready!")
        trulia_search_input.send_keys(search_text)
        driver.find_element_by_class_name('css-16gf7cf').click()
    except TimeoutException:
        print("Loading took too much time!")
    try:
        est_text = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//span[@data-role="price"]'))).text
        print("Page is ready!")
        price_items = re.findall(r'\$(?:\d+\.)?\d+.\d+', est_text)
        trulia_info["Trulia House Estimate"] = price_items[0]
    except TimeoutException:
        print("Loading took too much time!")
    return trulia_info


