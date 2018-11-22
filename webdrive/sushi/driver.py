import os
import yaml
from time import sleep
from selenium import webdriver

class Browser:

    def __init__(self):
        with open('param.yml', 'r') as param:
            self.param_dict = yaml.load(param)
        try:
            self.driver = webdriver.Chrome()
        except:
            raise ValueError('Cant booting browser.')
        else:
            print('driver startup.')


    def redirect_url(self, unique=None):
        if not unique:
            self.driver.get(self.param_dict['sushi']['url'])
        else:
            self.driver.get(unique)