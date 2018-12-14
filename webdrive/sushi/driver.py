import os
import yaml
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from alert import Alert

class Browser(Alert):

    def __init__(self):
        with open('param.yml', 'r') as param:
            self.param_dict = yaml.load(param)
        try:
            self.driver = webdriver.Chrome()
        except:
            Alert.danger_alert('Cant booting browser.')
            raise ValueError()
        else:
            Alert.safe_alert('driver startup.')
            self.items = {}


    def redirect_url(self, unique=None):
        if not unique:
            self.driver.get(self.param_dict['sushi']['url'])
            self.driver.set_page_load_timeout(5)
        else:
            self.driver.get(unique)


    #if you want to get new app(webGL ver), execute this func at 0 argument.
    #else, u wanto get old one, plz pass argument {cname}.
    def get_app(self, cname='#canvas', loading_time=7):
        try:
            self.stay(loading_time)
            self.items['sushida_webgl'] = self.driver.find_element_by_id(cname)
        except:
            Alert.danger_alert('Cant find app.')
        else:
            Alert.safe_alert('Success find app.')


    def stay(self, time):
        Alert.safe_alert('staying in time.sleep() {}sec'.format(str(time)))
        sleep(time)