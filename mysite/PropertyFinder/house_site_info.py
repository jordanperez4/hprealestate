from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re

def get_zillow_info(driver, search_text):
    driver.get("https://www.zillow.com/")
    zillow_search_input = driver.find_element_by_id("citystatezip")
    zillow_search_input.send_keys(search_text)
    zillow_search_input.submit()
    zillow_info = {}
    delay = 6
    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'estimates')))
        print("Page is ready!")
        est_text = driver.find_elements_by_class_name("estimates")[0].text
        price_items = re.findall(r'\$(?:\d+\.)?\d+.\d+', est_text)
        zillow_info["Zillow House Estimate"] = price_items[0]
        zillow_info["Zillow Rent Estimate"] = price_items[1]
    except TimeoutException:
        print("Loading took too much time!")
    est_text = driver.find_elements_by_class_name("estimates")[0].text
    price_items = re.findall(r'\$(?:\d+\.)?\d+.\d+', est_text)
    zillow_info = {}
    zillow_info["Zillow House Estimate"] = price_items[0]
    zillow_info["Zillow Rent Estimate"] = price_items[1]
    return zillow_info


