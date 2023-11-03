from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
# from twilio.rest import Client
import time
import random
import os 


class Bot:
    def __init__(self, festival_url, browser):
        from selenium.webdriver.firefox.service import Service
        current_dir_path = os.path.dirname(__file__)
        driver_path = os.path.join(current_dir_path, 'geckodriver')
        service = Service(executable_path=driver_path)
        my_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
        profile = FirefoxProfile()
        profile.set_preference("general.useragent.override", my_user_agent)
        profile.set_preference("dom.webdriver.enabled", False)
        profile.set_preference('useAutomationExtension', False)
        firefox_options = Options()
        firefox_options.profile = profile
        self.webdriver = webdriver.Firefox(service=service, options=firefox_options)
        self.webdriver.get(festival_url)    

    def quit(self):
        self.webdriver.quit()

    def go_to_ticket_page(self, otherCategory, ticketName):
        time.sleep(1)
        item = self.select_item_by_tag_name('li')
        a = item.find_element('xpath', 'a')
        print(a.href)
        a.click()

    def find_available(self):
        try:
            self.webdriver.find_element('xpath', '//*[text()="No tickets available at the moment."]')
        except NoSuchElementException:
            return True
        return False

    def refresher(self):
        random_decimal = random.randint(40000, 80000) / 10000
        time.sleep(random_decimal)
        self.webdriver.refresh()

    def reserve_ticket(self):
        try:
            ticket = self.webdriver.find_element('xpath', '/html/body/div[1]/div[2]/div/div[4]/div[1]/div[2]/a')
        except NoSuchElementException:
            ticket = self.webdriver.find_element('xpath', '/html/body/div[1]/div[2]/div/div[4]/div[1]/div[2]/a[1]')
        ticket.click()
        time.sleep(0.355)
        self.webdriver.find_element('xpath', '//*[text()="Buy ticket"]').click()
