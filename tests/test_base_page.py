import allure
import pytest
from pages.base_page import BasePage
from pages.order_page import OrderPage


@pytest.mark.usefixtures("driver")
class TestLogo:
    @allure.title('Открытие сайта Самоката по логотипу "Самокат"')
    @allure.description('На странице заказа нажать на логотип "Самокат", выполнен переход на главную страницу Самоката')
    def test_main_page_open_by_scooter_logo(self, driver):
        open_order_page = OrderPage(driver)
        open_order_page.order_page()
        open_by_scooter_logo = BasePage(driver)
        open_by_scooter_logo.click_scooter_logo()
        open_by_scooter_logo.wait_for_main_page()
        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

    @allure.title('Открытие сайта Дзен по логотипу "Яндекс"')
    @allure.description('На странице заказа нажать на логотип "Яндекс", выполнен переход на страницу Дзен')
    def test_dzen_page_open_by_yandex_logo(self, driver):
        open_order_page = OrderPage(driver)
        open_order_page.order_page()
        open_by_yandex_logo = BasePage(driver)
        open_by_yandex_logo.click_yandex_logo()
        open_by_yandex_logo.wait_for_new_tab()
        driver.switch_to.window(driver.window_handles[1])
        open_by_yandex_logo.wait_for_page_load()
        assert driver.current_url == 'https://dzen.ru/?yredirect=true'
