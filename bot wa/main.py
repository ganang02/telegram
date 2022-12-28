from selenium import webdriver
from selenium.webdriver.common.keys import Keys

phone_number = "6289661945278"
password = "020908"

recipient_name = "nyimpen"
message = "Test"

driver = webdriver.Chrome()

driver.get ("https://web.whatsapp.com/")

input("Press Enter afer scanning the qrcode")

search_box = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/input')
search_box.send_keys(recipient_name)
search_box.send_keys(Keys.RETURN)

chat_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
chat_box.send_keys(message)

send_button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
send_button.click()

driver.close()