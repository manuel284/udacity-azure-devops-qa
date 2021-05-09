# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
# from selenium.common.exceptions import NoSuchElementException 
import datetime

def dateTimeNow():
    return datetime.datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)")

# Start the browser and login with standard_user
def login (user, password):
    print ('Starting the browser...')
    options = ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    # options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    print ('Browser started successfully. Navigating to the demo page to login.')
    driver.get('https://www.saucedemo.com/')
    driver.find_element_by_css_selector("input[id='user-name']").send_keys(user)
    driver.find_element_by_css_selector("input[id='password']").send_keys(password)
    driver.find_element_by_id("login-button").click()

    title = driver.find_element_by_css_selector("div[class='header_secondary_container'] > span[class='title']").text
    assert "PRODUCTS" in title
    print('{:s}: Successfully logged in with username \'{:s}\' and password \'{:s}\'.'.format(dateTimeNow(), user, password))

    return driver

# add items to cart
def add_items_to_cart(driver, item_count):
    items = driver.find_elements_by_css_selector("div[class='inventory_item']")
    for item in items:
        item_name = item.find_element_by_css_selector("div[class='inventory_item_description'] > div[class='inventory_item_label'] > a > div[class='inventory_item_name']").text
        button = item.find_element_by_css_selector("button[class='btn btn_primary btn_small btn_inventory']")
        button.click()
        print('{:s}: Successfully added \'{:s}\' to the cart.'.format(dateTimeNow(), item_name))

# remove items from cart
def remove_items_from_cart(driver, item_count):
    items = driver.find_elements_by_css_selector("div[class='inventory_item']")
    for item in items:
        item_name = item.find_element_by_css_selector("div[class='inventory_item_description'] > div[class='inventory_item_label'] > a > div[class='inventory_item_name']").text
        button = item.find_element_by_css_selector("button[class='btn btn_secondary btn_small btn_inventory']")
        button.click()
        print('{:s}: Successfully removed \'{:s}\' from the cart.'.format(dateTimeNow(), item_name))


print('{:s}: Start selenium tests.'.format(dateTimeNow()))
driver = login('standard_user', 'secret_sauce')
add_items_to_cart(driver, 6)
remove_items_from_cart(driver,6)
driver.close()
driver.quit()
print('{:s}: Selenium tests completed successfully.'.format(dateTimeNow()))