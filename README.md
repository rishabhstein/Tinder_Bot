# Tinder_Bot

This bot is based on Chromedriver library to control chrome using python shell.
To run this script first follow the steps:


## Install Selenium and Chromedriver according to your chrome browser version 

###	To intall selenium
Simply use 
	'pip install selenium' for Python 2.7
	'pip3 install selenium' for Python 3.5

### To install chromedriver, 
Visit chromedriver.chromium.org and download Chromedriver according to your chrome browser version 
and install it to default location of windows or linux.


### Now run it:

create a bot:	bot = tinder_bot('facebook_user_id', 'facebook_password', autoswipe = True/False)

Log id	    :	bot.login()

one like    : 	bot.like()

autoswipe   :	bot.Auto_Swipe()


If it throughs error simply close the chrome and stop the script and re run it.
If still it throughs error (it might be because of slow loading of page) just increase 
the "time.sleep(time)" before the step at which the error comes.
