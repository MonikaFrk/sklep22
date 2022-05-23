# Zautomatyzowane przypadki testowe funcjonalne strony internetowej typu e-commerce


from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s=Service("D:\chromedriver.exe")
driver = webdriver.Chrome(service=s)
from selenium.webdriver.common.keys import Keys

PATH = "D:\chromedriver.exe"
driver = webdriver.Chrome(PATH)
# Test funkcjonalny negatywny
driver.get("https://dlakrolika.pl/client-new.php?register")
input_firstname = driver.find_element_by_id("client_firstname")
input_firstname.send_keys('Monika')
input_firstname.submit()
lastname = driver.find_element_by_id("client_lastname")
lastname.send_keys("Frączek")
lastname.submit()
phone = driver.find_element_by_id("client_phone")
phone.send_keys("726655626")
phone.submit()
city = driver.find_element_by_id("client_city")
city.send_keys("Bydgoszcz")
city.submit()
street = driver.find_element_by_id("client_street")
street.send_keys("Władysława Bełzy")
street.submit()
localnumber = driver.find_element_by_xpath("//")
localnumber.submit()
input_zipcode = driver.find_element_by_xpath('//input[@id="zipcode_wrapper"]')
input_zipcode.send_keys("85-817")
input_zipcode.submit()
email = driver.find_element_by_xpath("//input[@id='client_email']")
email.send_keys("monika@gmail.com")
email.submit()
login = driver.find_element_by_id("client_login")
login.send_keys("monika2204")
login.submit()
password = driver.find_element_by_id("client_password")
password.send_keys("monika123")
password.submit()
termsagree = driver.find_element_by_id("terms_agree")
termsagree.click()



