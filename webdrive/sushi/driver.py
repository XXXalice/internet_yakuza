import os
import yaml
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

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
    def get_app(self, cname='#canvas', loading_time=5):
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


    def driving_webgl(self):

        def __start(webgl_app, driver):
            app_locate = webgl_app.location
            start_button = {'x':app_locate['x'] + int(250),
                            'y':app_locate['y'] + int(150)
                            }
            click_action = ActionChains(driver)
            click_action.move_to_element_with_offset(to_element=webgl_app, xoffset=250, yoffset=-260)

            try:
                click_action.click()
                click_action.perform()
            except:
                Alert.danger_alert('Cant click.')
            else:
                Alert.safe_alert('Success click.')

        self.stay(time=5)
        __start(webgl_app=self.items['sushida_webgl'], driver=self.driver)
