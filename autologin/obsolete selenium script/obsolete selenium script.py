from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

# to make sure driver doesn't wait for webpage to load unnecessary elements before executing the script:
caps = DesiredCapabilities().CHROME
caps['pageLoadStrategy'] = "none"

website_link = 'https://campnet.bits-goa.ac.in:8090/'

# todo: write code to do good stuff with the password (done)

#login info: (could've used secure database but who cares)
username = 'f20190896'
password = 'fd531372'

# find corresponding elements in the webpage by html name/id:
element_for_username = 'username'  # name
element_for_password = 'password'  # name
element_for_submit = 'loginbutton'  # id

# open broswer:
driver = webdriver.Chrome("chromedriver.exe")
driver.get(website_link)

# wait for one second so that required elements load completely:
time.sleep(1)

# real action
try:
    username_element = driver.find_element_by_name(element_for_username)
    username_element.send_keys(username)

except Exception as e:
    print("something wrong with username")
    print(e)

try:
    password_element = driver.find_element_by_name(element_for_password)
    password_element.send_keys(password)
except Exception as e:
    print("something wrong with pw")
    print(e)

try:
    login_button = driver.find_element_by_id(element_for_submit)
    login_button.click()
except Exception as e:
    print("something wrong with login button")
    print(e)

# wait for 4 seconds before quitting browser window
time.sleep(4)
driver.quit()