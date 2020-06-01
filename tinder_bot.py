
""" Install Selenium and Chromedriver according to your chrome browser version 
  	To intall selenium,
		Simply use 
	  		'pip install selenium' for Python 2.7
	  		'pip3 install selenium' for Python 3.5

	To install chromedriver, 
		visit chromedriver.chromium.org

"""

from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver')
driver.get('https://tinder.com')
time.sleep(5)

accept_terms_btn = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
accept_terms_btn.click()



class tinder_bot():

	"""
	This class makes a Tinder bot for autoswiping
	simply, create a bot with 
		user id = "  "
		password = " "
		autoswiping = True/False

	"""

	def __init__(self, userid, password, bool_autoswipe = False):
		self.userid 	= userid
		self.password 	= password
		self.autoswipe = autoswipe


	def login(self):
		
		try:
			fb_btn = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
		except Exception:
			time.sleep(2)
			try:
				fb_btn = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
			except Exception as e:
				raise e
			raise e

		fb_btn.click()

		#Popup
		no_of_windows = len(driver.window_handles)

		if no_of_windows > 2:
		    base_window=driver.window_handles[1]
		    popup = driver.switch_to.window(driver.window_handles[2])
		else:
		    base_window=driver.window_handles[0]
		    popup = driver.switch_to.window(driver.window_handles[1])


		#User_ID
		fb_user_id = driver.find_element_by_xpath('//*[@id="email"]')
		fb_user_id.send_keys(self.userid)

		#Password


		pass_box = driver.find_element_by_xpath('//*[@id="pass"]')
		pass_box.send_keys(self.password)

		log_in_button = driver.find_element_by_xpath('//*[@id="u_0_0"]')
		log_in_button.click()

		driver.switch_to.window(base_window)


		try:
			time.sleep(5)
			location_allow_popup = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
			location_allow_popup.click()
		except Exception:
			try:
				time.sleep(5)
				location_allow_popup = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
				location_allow_popup.click()
			except Exception as e:
				raise e

		time.sleep(2)
		block_notification=driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]/span')
		block_notification.click()

	def like(self):
		swipe_right = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
		swipe_right.click()


	def dislike(self): # This button is Not working
		swipe_left = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/div[2]/button')
		swipe_left.click()

	def Auto_swipe(self):
		while(self.bool_autoswipe):
			try: 				#Try like button
				self.like()
				time.sleep(2)
			except Exception:
				try: 			#Try if it's a match
					after_match = driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
					after_match.click()
				except Exception:
					try: 		#Try if tinder is asking to add shortcut
						add_shortcut = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
						add_shortcut.click()
					except Exception:
						try: 	#Try if tinder is doing promotion
							superlike = driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
						except Exception as e:
							raise e
