

import time
from selenium import webdriver ##Imports the selenium web driver
driver = webdriver.Firefox() ##Create a Firefox Webdriver

lurl="https://account.xiaomi.com/pass/serviceLogin?callback=http%3A%2F%2Fbuy.mi.com%2Fin%2Flogin%2Fcallback%3Ffollowup%3Dhttp%253A%252F%252Fwww.mi.com%252Fin%252F%26sign%3DMDNmZGJhZTdkNmQ3YzQwNzZkODNkZTA2MTliYTQ5MjFhYWEwZDE2Zg%2C%2C&sid=mi_overseain&_locale=en_IN"

url="http://buy.mi.com/in/buy/product/mimax"

uname=''
pword=''

driver.get(lurl)
continue_link = driver.find_element_by_xpath("//input[@id='username']")
continue_link.clear()
continue_link.send_keys(uname)
continue_link = driver.find_element_by_xpath("//input[@id='pwd']")
continue_link.clear()
continue_link.send_keys(pword)


print "TRYING TO LOGIN"
driver.find_element_by_xpath("//input[@id='login-button']").click()
time.sleep(5)
print "HOPING LOGIN IS SUCCEESSFUL"

driver.get(url)

while True:
	#try:
	continue_link = driver.find_element_by_xpath("//input[@id='pincode-input']")
	continue_link.clear()
	continue_link.send_keys('560012')

	print "Choosing Memory built"
	print type(driver.find_element_by_xpath("//p[@class='name J_name']").click())
	print "Choosing Color "


	print (driver.find_element_by_xpath("//span[@class='color-icon']").click())
	driver.get(url) 

	curl=driver.current_url
	print curl
	if url!=curl:
		break	
	#except:
	
	
print  "Buying"
driver.find_element_by_xpath("//a[@id='J_nextBtn'][@data-stat-id='058e32756bc30ece']").click()
while True:
	print " I Hope you could buy it"
