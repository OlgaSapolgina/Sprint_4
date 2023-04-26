import allure
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def click_cookie_button(self):
        self.driver.find_element(*MainPageLocators.COOKIE_BUTTON).click()

    @allure.step('Пролистать до раздела "Вопросы о важном"')
    def scroll_to_questions(self):
        faq = self.driver.find_element(*MainPageLocators.FAQ)
        self.driver.execute_script("arguments[0].scrollIntoView();", faq)
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(MainPageLocators.FAQ))

    def get_questions(self):
        return self.driver.find_elements(*MainPageLocators.QUESTIONS)

    @allure.step('Нажать на вопрос')
    def click_on_question(self, index):
        questions = self.get_questions()
        questions[index - 1].click()

    @allure.step('Получить текст ответа')
    def get_answer_text(self):
        return self.driver.find_element(*MainPageLocators.ANSWER).text

    def wait_for_get_answer(self):
        WebDriverWait(self.driver, 25).until(ec.visibility_of_element_located(MainPageLocators.ANSWER))

    @allure.step('Пролистать до кнопки "Заказать" на странице')
    def scroll_to_order_button(self):
        button = self.driver.find_element(*MainPageLocators.ORDER_BUTTON_MAIN_PAGE)
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(MainPageLocators.ORDER_BUTTON_MAIN_PAGE))

    @allure.step('Клик по кнопке "Заказать" на странице')
    def click_order_button(self):
        self.driver.find_element(*MainPageLocators.ORDER_BUTTON_MAIN_PAGE).click()

    @allure.step('Клик по кнопке "Заказать" в шапке')
    def click_order_button_in_header(self):
        self.driver.find_element(*MainPageLocators.ORDER_BUTTON_IN_HEADER).click()

    @allure.step('Получить текст заголовка главной страницы')
    def get_main_header_text(self):
        return self.driver.find_element(*MainPageLocators.HEADER_TEXT).text
