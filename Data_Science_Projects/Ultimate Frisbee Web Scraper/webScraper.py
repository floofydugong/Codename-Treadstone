from selenium import webdriver

path_to_chromedriver = '/Users/Hayw1re/Downloads/chromedriver' # change path as needed
browser = webdriver.Chrome(executable_path = path_to_chromedriver)

url = 'http://play.usaultimate.org/teams/events/rankings/'
browser.get(url)





