from pprint import pprint
from random import randint
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test_form():

    driver_serves = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_serves)
    driver.maximize_window()

    driver.get('https://demoqa.com/automation-practice-form')

    driver.execute_script("document.getElementsByTagName('footer')[0].remove();")

    firstname = driver.find_element(By.XPATH, '//*[@id="firstName"]')
    firstname.send_keys('Hello')

    lastname = driver.find_element(By.CSS_SELECTOR, '#lastName')
    lastname.send_keys('World')

    email = driver.find_element(By.CSS_SELECTOR, '#userEmail')
    email.send_keys('Hello@World.com')

    gender = driver.find_element(By.XPATH, f'//*[@id="genterWrapper"]/div[2]/div[{randint(1, 3)}]/label')
    gender.click()

    mobile = driver.find_element(By.CSS_SELECTOR, '#userNumber')
    mobile.send_keys('88005553555')

    subject = driver.find_element(By.CSS_SELECTOR, '#subjectsInput')
    subject.send_keys('English')
    subject.send_keys(Keys.RETURN)

    hobbies = driver.find_element(By.XPATH, f'//*[@id="hobbiesWrapper"]/div[2]/div[{randint(1, 3)}]/label')
    hobbies.click()

    file_input = driver.find_element(By.CSS_SELECTOR, '#uploadPicture')
    file_input.send_keys(r'S:\jetbrain\projects\selenium_academ_task\test')

    currect_address = driver.find_element(By.CSS_SELECTOR, '#currentAddress')
    currect_address.send_keys('uganda_be_like')

    state = driver.find_element(By.CSS_SELECTOR, '#react-select-3-input')
    state.send_keys('NCR')
    state.send_keys(Keys.RETURN)

    city = driver.find_element(By.CSS_SELECTOR, '#react-select-4-input')
    city.send_keys('Noida')
    city.send_keys(Keys.RETURN)

    submit = driver.find_element(By.CSS_SELECTOR, '#submit')
    submit.click()

    result_list = driver.find_elements(By.XPATH, '/html/body/div[4]/div/div/div[2]/div/table/tbody//td[2]')

    time.sleep(0.5)

    result_text = [i.text for i in result_list]
    assert 'Hello World' == result_text[0]
    assert 'Hello@World.com' == result_text[1]
    assert 'Male' or 'Female' or 'Other' == result_text[2]
    assert '8800555355' == result_text[3]
    assert 'English' == result_text[5]
    assert 'Music' or 'Sports' or 'Reading' == result_text[6]
    assert 'test' == result_text[7]
    assert 'uganda_be_like' == result_text[8]
    assert 'NCR Noida' == result_text[9]






