from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
import csv
import re

# Windows users need to specify the path to chrome driver you just downloaded.
# You need to unzip the zipfile first and move the .exe file to any folder you want.
# driver = webdriver.Chrome(r'path\to\where\you\download\the\chromedriver.exe')
driver = webdriver.Chrome()

driver.get("https://seekingalpha.com/stock-ideas/long-ideas?page=220")

# Windows users need to open the file using 'wb'
# csv_file = open('reviews.csv', 'wb')
csv_file = open('long30.csv', 'w')
writer = csv.writer(csv_file)
# Page index used to keep track of where we are.
index = 1
#pageCount = 10
#button = driver.find_element_by_xpath('//li[@class="next"]')

while index<=1:

	#time.sleep(random.uniform(2, 5))

	try:
		index = index + 1
		# Find all the reviews on the page
		#wait_review = WebDriverWait(driver, 10)
		calls = driver.find_elements_by_xpath('//li[@class="article media"]')
		print(len(calls))
		print('='*50)

		for call in calls:
			# Initialize an empty dictionary for each review
			call_dict = {}
			# Use relative xpath to locate the title, content, username, date.
			# Once you locate the element, you can use 'element.text' to return its string.
			# To get the attribute instead of the text of each element, use 'element.get_attribute()'
			article_title = call.find_element_by_xpath('.//a[@class="a-title"]').text
			article_link = call.find_element_by_xpath('.//a[@class="a-title"]').get_attribute('href')
			# There might be multiple paragraphs, so you use find elements instead of find element.
			ticker = call.find_element_by_xpath('.//div[@class="a-info"]/span/a').text
			company = call.find_element_by_xpath('.//div[@class="a-info"]/span/a').get_attribute('title')
			date_time = call.find_element_by_xpath('.//div[@class="a-info"]/span[4]').text
			issuer = call.find_element_by_xpath('.//div[@class="a-info"]/a').text


			call_dict['article_title'] = article_title
			call_dict['article_link'] = article_link
			call_dict['ticker'] = ticker
			call_dict['company'] = company
			call_dict['date_time'] = date_time
			call_dict['issuer'] = issuer

			writer.writerow(call_dict.values())

		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			#button = driver.find_element_by_xpath('//li[@class="next"]')
			#button.click()
			#time.sleep(5)


	except Exception as e:
		print(e)
		csv_file.close()
		driver.close()
		break
