from selenium import webdriver ##Imports the selenium web driver
driver = webdriver.Firefox() ##Create a Firefox Webdriver
driver.get("https://web.whatsapp.com") ##Tells the driver to go to facebook.com
import time
time.sleep(1) ##waits for 1 second

count =0
flag=0
time.sleep(20)

continue_link = driver.find_element_by_xpath("//span[@title='Rahul Kumar']")
continue_link.click()
flag=1
continue_link = driver.find_element_by_xpath("//div[@class='input'][@contenteditable='true']")	
while True:
		#continue_link.click()
		continue_link.clear()
		continue_link.send_keys("TEST")
		print driver.find_elements_by_css_selector(".send-container")[0].click()

