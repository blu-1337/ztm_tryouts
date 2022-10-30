from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys  # return keys and so on
from selenium.webdriver.chrome.options import Options  # disable notifications
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import undetected_chromedriver as uc
from time import sleep


# accept_all_button = chrome_browser.find_element(By.XPATH, '//*[@id="ez-accept-all"]')

# assert 'http' in chrome_browser.title
# accept_all_button.click()
# print(accept_all_button.get_attribute('innerHTML'))


# assert 'Continue with Recommended Cookies' in chrome_browser.page_source  # checks if the button is on the page,
# page source is the complete page source html code

#
# input_field_01 = chrome_browser.find_element(By.XPATH, '//*[@id="post-body-3077692503353518311"]/div[1]/div/div/h2[2]/div[1]/div/div[2]/input')
# input_field_01.send_keys('I am Cristian Gilca')
#
# chrome_browser.execute_script("window.scrollTo(0, 100)")
#
# time.sleep(5.5)  # waiting for weitere info cookie shit
# ok_weiter_info = chrome_browser.find_element(By.XPATH, '//*[@id="cookieChoiceDismiss"]')
# ok_weiter_info.click()


# chrome_browser.close()
# chrome_browser.quit()
# you might have to close this twice


#####################
# YouTube Comment Bot
#####################

# Step 01: Chrome Driver Setup

service = ChromeService(executable_path=ChromeDriverManager().install())
option=webdriver.ChromeOptions()
option.add_argument("--disable-infobars")
option.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block


driver = uc.Chrome(use_subprocess=True, service=service, options=option)
driver.maximize_window()  # full screen
url = 'https://www.youtube.com/account'
driver.get(url)



wait = WebDriverWait(driver, 30)  # time in seconds to wait until timeout

# Step 02: Inputs Setup

username = 'penori.craiova@gmail.com'
password = 'Www.gmail.com8'
backup_code = '01153046'

search_phrase = 'rain sounds'  # what are we searching for?
comments = 5  # how many comments should this bot leave?
comment = 'beautiful, thanks for sharing I wish everyone a blessed evening <3 💜💜'  # maybe make this and array of comms

# Step 03: accept terms and rights
accept_all_conditions_01 = driver.find_element(By.XPATH,
                                               '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/form[2]/div/div/button')
if accept_all_conditions_01:
    accept_all_conditions_01.click()

# accept_all_conditions_02 = driver.find_element(By.XPATH, '//*[@id="button"]')
# if accept_all_conditions_02:
#     accept_all_conditions_02.click()

# Step 04: Sign in
sign_in_input_form = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
sign_in_input_form.send_keys(username)

next_button_01 = driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button')
next_button_01.click()

password_input_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input')))
password_input_field.send_keys(password)

#passwordNext > div > button

next_button_02 = driver.find_element(By.CSS_SELECTOR, '#passwordNext > div > button')
next_button_02.click()

enter_backup_code_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#view_container > div > div > div.pwWryf.bxPAYd > div > div.WEQkZc > div > form > span > section > div > div > div.pQ0lne > ul > li:nth-child(5)')))
enter_backup_code_button.click()

backup_code_input_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#backupCodePin')))
backup_code_input_field.send_keys(backup_code)
backup_code_input_field.send_keys(Keys.RETURN)

# Step 05: Search
# wait for search button to appear, you need to tap yes on phone before this...
search_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#search')))
search_field.send_keys(search_phrase).send_keys(Keys.RETURN)


sleep(999999)

