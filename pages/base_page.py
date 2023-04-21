import allure
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Клик по логотипу "Яндекс"')
    def click_yandex_logo(self):
        self.driver.find_element(*BasePageLocators.YANDEX_LOGO).click()

    def wait_for_new_tab(self):
        WebDriverWait(self.driver, 10).until(ec.number_of_windows_to_be(2))

    def wait_for_page_load(self):
        WebDriverWait(self.driver, 10).until(ec.url_to_be('https://dzen.ru/?yredirect=true'))

    @allure.step('Клик по кнопке "Заказать"')
    def click_order_button_in_header(self):
        self.driver.find_element(*BasePageLocators.ORDER_BUTTON_IN_HEADER).click()

    @allure.step('Клик по логотипу "Самокат"')
    def click_scooter_logo(self):
        self.driver.find_element(*BasePageLocators.SCOOTER_LOGO).click()

    def wait_for_main_page(self):
        WebDriverWait(self.driver, 10).until(ec.url_to_be('https://qa-scooter.praktikum-services.ru/'))
