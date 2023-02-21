from selenium import webdriver



options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\download\python")

browser = webdriver.Chrome(chrome_options=options)

