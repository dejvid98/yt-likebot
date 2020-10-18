from selenium import webdriver
import random
import time
import math
PATH = '/Users/david/Desktop/chromedriver'
SIGN_IN_XPATH = '//*[@id="gb_70"]'
CREATE_ACCOUNT_XPATH = '//*[@id="ow312"]/span/span'
FOR_MYSELF_XPATH = '//*[@id="initialView"]/div[2]/div[2]/div/div/span[1]/div[2]/div'
FIRST_NAME_XPATH = '//*[@id="firstName"]'
LAST_NAME_XPATH = '//*[@id="lastName"]'
USERNAME_XPATH = '//*[@id="username"]'
PASSWORD_XPATH = '//*[@id="passwd"]/div[1]/div/div[1]/input'
CONFIRM_PASSWORD_XPATH = '//*[@id="confirm-passwd"]/div[1]/div/div[1]/input'
NEXT_XPATH = '//*[@id="accountDetailsNext"]/span/span'
SECOND_NEXT_XPATH = '//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button'
PHONE_NUMBER_XPATH = '//*[@id="phoneNumberId"]'
VERIFY_BUTTON_XPATH = '//*[@id="view_container"]/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/button'
MONTH_XPATH = '//*[@id="month"]/option[2]'
DAY_XPATH = '//*[@id="day"]'
YEAR_XPATH = '//*[@id="year"]'
GENDER_XPATH = '//*[@id="gender"]/option[3]'
THIRD_NEXT_XPATH = '//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button'
SKIP_BUTTON_XPATH = '//*[@id="view_container"]/div/div/div[2]/div/div[2]/div[2]/div[2]/div/div/button'
AGREE_XPATH = '//*[@id="termsofserviceNext"]'
SEARCHBAR_XPATH = '//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input'
SEARCH_BUTTON_XPATH = '//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]'
YT_LINK_XPATH = '//*[@id="rso"]/div[1]/div/div/div[1]/a'
YT_SEARCH_INPUT = '/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input'
YT_SEARCH_BUTTON_XPATH = '//*[@id="search-icon-legacy"]'
YT_SIGNIN_BUTTON_XPATH = '/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-button-renderer/a'
YT_LIKE_BUTTON_XPATH = '//*[@id="top-level-buttons"]/ytd-toggle-button-renderer[1]/a'
YT_SUBSRIBE_BUTTON_XPATH = '//*[@id="subscribe-button"]/ytd-button-renderer/a'
MATEMATIKA_XPATH = '/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a'

def createFirstName():
    length = random.randint(4,13)
    name = ''
    for i in range(length):
        name+= chr(random.randint(66,90))
    return name

def createUserName():
    return firstName+lastName+str(random.randint(100,999))

def createPassword():
    return firstName+lastName+str(random.randint(1000,9999))+'!'

firstName = createFirstName()
lastName = firstName[::1]
userName = createUserName()
password = createPassword()
phoneNumber = '0600286191'
videoName = 'Matematika 1 prva nedelja'

driver = webdriver.Chrome(PATH)

driver.get("https://www.google.com/")

# Click on the sign in button
driver.find_element_by_xpath(SIGN_IN_XPATH).click()

# Click on the create an account button
driver.find_element_by_xpath(CREATE_ACCOUNT_XPATH).click()

time.sleep(1)

# Click on the for myself button
driver.find_element_by_xpath(FOR_MYSELF_XPATH).click()

time.sleep(2)

# Enter firstname
driver.find_element_by_xpath(FIRST_NAME_XPATH).send_keys(firstName)

# Enter lastname
driver.find_element_by_xpath(LAST_NAME_XPATH).send_keys(lastName)

# Enter username
driver.find_element_by_xpath(USERNAME_XPATH).send_keys(userName)

# Enter password
driver.find_element_by_xpath(PASSWORD_XPATH).send_keys(password)

# Confirm password
driver.find_element_by_xpath(CONFIRM_PASSWORD_XPATH).send_keys(password)

time.sleep(1)

# Continiue
driver.find_element_by_xpath(NEXT_XPATH).click()

time.sleep(2)

# Enter phone number
driver.find_element_by_xpath(PHONE_NUMBER_XPATH).send_keys(phoneNumber)

time.sleep(2)

# Continiue
driver.find_element_by_xpath(SECOND_NEXT_XPATH).click()

time.sleep(20)

driver.find_element_by_xpath(VERIFY_BUTTON_XPATH).click()

time.sleep(2)

driver.find_element_by_xpath(MONTH_XPATH).click()

driver.find_element_by_xpath(DAY_XPATH).send_keys('22')

driver.find_element_by_xpath(YEAR_XPATH).send_keys('1998')

driver.find_element_by_xpath(GENDER_XPATH).click()

time.sleep(1)

driver.find_element_by_xpath(THIRD_NEXT_XPATH).click()

time.sleep(2)

driver.find_element_by_xpath(SKIP_BUTTON_XPATH).click()

time.sleep(2)

driver.find_element_by_xpath(AGREE_XPATH).click()

time.sleep(2)

driver.find_element_by_xpath(SEARCHBAR_XPATH).send_keys('youtube')

driver.find_element_by_xpath(SEARCH_BUTTON_XPATH).click()

time.sleep(1)

driver.find_element_by_xpath(YT_LINK_XPATH).click()

time.sleep(4)

driver.find_element_by_xpath(YT_SIGNIN_BUTTON_XPATH).click()

time.sleep(2)

driver.find_element_by_xpath(YT_SEARCH_INPUT).send_keys(videoName)

time.sleep(1)

driver.find_element_by_xpath(YT_SEARCH_BUTTON_XPATH).click()

time.sleep(1)

driver.find_element_by_xpath(MATEMATIKA_XPATH).click()

time.sleep(2)

driver.find_element_by_xpath(YT_LIKE_BUTTON_XPATH).click()

time.sleep(1)

driver.find_element_by_xpath(YT_SUBSRIBE_BUTTON_XPATH).click()
