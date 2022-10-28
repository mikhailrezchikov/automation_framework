import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_page import Cart_page
from pages.client_information_page import Client_information_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.payment_page import Payment_page

@allure.description("Test link about")
def test_link_about(set_up):
    driver = webdriver.Chrome(executable_path='/Users/mikhailrezchikov/PycharmProjects/resource/chromedriver')

    print("Start Test")

    login = Login_page(driver)
    login.autorization()

    mp = Main_page(driver)
    mp.select_menu_about()

    print("Finish test")
    time.sleep(5)
    driver.quit()
