import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# set the path for the geckodriver executable
geckodriver_path = '/snap/bin/geckodriver'
# set the path for the urls file
urls_file_path = 'urls.txt'
# set the timeout for waiting for elements to load
timeout = 30

# create a Firefox webdriver instance
driver = webdriver.Firefox(executable_path=geckodriver_path)

# read the urls from the urls file
with open(urls_file_path) as f:
    urls = f.readlines()

# remove whitespace and newlines from the urls
urls = [url.strip() for url in urls]

# create the screenshot directory if it doesn't exist
if not os.path.exists('~/screenshots'):
    os.makedirs('~/screenshots')

# iterate over the urls and take screenshots
for url in urls:
    # get rid of any leading 'http://' or 'https://'
    url_name = url.replace('http://', '').replace('https://', '')
    # navigate to the url
    driver.get(url)
    try:
        # wait for the page to load by checking for the presence of the body element
        element_present = EC.presence_of_element_located((By.TAG_NAME, 'body'))
        WebDriverWait(driver, timeout).until(element_present)
        # take a screenshot and save it with the url name
        screenshot_path = f'~/screenshots/{url_name}.png'
        driver.save_screenshot(os.path.expanduser(screenshot_path))
        print(f'Screenshot saved for {url}')
    except:
        print(f'Timeout occurred while trying to load {url}')
        continue

# close the webdriver instance
driver.quit()
