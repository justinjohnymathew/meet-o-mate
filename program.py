from dotenv import load_dotenv
load_dotenv()
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3803.0 Safari/537.36'
meet_id ="oad-prha-jqs"
url="https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmeet.google.com%2F" + meet_id
email=os.environ.get("email")
password=os.environ.get("password")
options = Options()
capabilities = DesiredCapabilities.FIREFOX.copy()
options.headless= True
options.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 2,
    "profile.default_content_setting_values.media_stream_camera": 2,
     "profile.default_content_setting_values.notifications": 2
  })
options.add_argument("window-size=800,600")
options.add_argument(f'user-agent={user_agent}')
capabilities['acceptSslCerts'] = True 
capabilities['acceptInsecureCerts'] = True
driver = webdriver.Chrome(executable_path='./chromedriver',options=options,desired_capabilities=capabilities)
time.sleep(10)
driver.get(url)
print("1.URL")
username_input= driver.find_element_by_xpath("//input[@class='whsOnd zHQkBf']")
username_input.send_keys(email)
next_key=driver.find_element_by_xpath("//span[@class='RveJvd snByac']")
next_key.click()
print("2.Email")
time.sleep(4)
password_input= driver.find_element_by_xpath("//input[@class='whsOnd zHQkBf']")
password_input.send_keys(password)
time.sleep(4)
password_key=driver.find_element_by_id("passwordNext")
password_key.click()
print("3.Password")
time.sleep(15)
driver.find_element_by_xpath("//span[@class='NPEfkd RveJvd snByac' and contains(text(), 'Join now')]").click()
print("4.WHoah!!!")
time.sleep(10)
count=driver.find_element_by_xpath("//span[@class='wnPUne N0PJ8e']").get_attribute("innerHTML")
for i in range(1,5):
  print(count)
  if count == 5:
    driver.quit()
  time.sleep(5)
  count = driver.find_element_by_xpath("//span[@class='wnPUne N0PJ8e']").get_attribute("innerHTML")
driver.quit()
