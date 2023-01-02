import datetime
import time
from selenium import webdriver

#driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.maximize_window()

#taking inputs from user
username=""
password=""
name = ""#username of the reciever 
message= ""

# Open the instagram website
driver.get("https://www.instagram.com/")
time.sleep(5)

#login process
driver.find_element(by='xpath',value='/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input').send_keys(username)
driver.find_element(by='xpath',value='/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input').send_keys(password)
driver.find_element(by='xpath',value='/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]').click()
time.sleep(10)
driver.find_element(by='xpath',value='/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button').click()
time.sleep(5)
driver.find_element(by='xpath',value='/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
time.sleep(5)

#getting to the chat
#message icon
driver.find_element(by='xpath',value='/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[5]').click()
time.sleep(5)
#send message button
driver.find_element(by='xpath',value='/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div/div[3]/div/button').click()
#enter the name in the search box
driver.find_element(by='name',value='queryBox').send_keys(name)
time.sleep(5)
driver.find_element(by='xpath',value='/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div[1]/span/img').click()
driver.find_element(by='xpath',value='/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[3]/div/button/div').click()
time.sleep(3)

#sending the message
driver.find_element(by='xpath',value='/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(message)
time.sleep(2)
driver.find_element(by='xpath',value='/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
time.sleep(5)

#logging out
driver.find_element(by='xpath',value='/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[1]/div/div/div/div/div[3]/div').click()
time.sleep(5)
driver.find_element(by='xpath',value='/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[1]/div/div/div/div/div[3]/div/div/div[1]/div/div[1]/div[6]/div').click()
print("message sent successfully")

#we quit
time.sleep(10)
driver.quit()

# Created in 01-01-2023(Happy New Year lol)