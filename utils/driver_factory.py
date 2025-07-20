from selenium import webdriver
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

browser = config['default']['browser']

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    return webdriver.Chrome(options=options)