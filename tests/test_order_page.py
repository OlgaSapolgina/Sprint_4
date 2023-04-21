import allure
import pytest
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.order_page import OrderPage


@pytest.mark.usefixtures("driver", "get_phone_number", "get_date")
class TestOrderButton:
    @allure.title('Оформление заказа по кнопке "Заказать" в шапке страницы')
    @allure.description('Корректное заполнение всех полей заказа, после подтверждения отображается "Заказ оформлен"')
    def test_order_button_on_header(self, driver, get_phone_number, get_date):
        open_main_page = MainPage(driver)
        open_main_page.main_page()
        click_order_button = BasePage(driver)
        click_order_button.click_order_button_in_header()
        order = OrderPage(driver)
        order.filling_form('Алиса', 'Максимова', 'Ленина ул. 123', 'Люблино',get_phone_number)
        order.wait_for_rent_form()
        order.input_rental_information(get_date, 'one', 'black', 'Позвонить заранее')
        order.wait_for_confirm()
        order.click_confirmation_order()
        order_title = order.get_new_order_title()
        order.wait_for_order_completed()
        assert 'Заказ оформлен' in order_title

    @allure.title('Оформление заказа по кнопке "Заказать" на главной странице')
    @allure.description('Корректное заполнение всех полей заказа, после подтверждения отображается "Заказ оформлен"')
    def test_order_button_main_page_current_date_user_flow_positive(self, driver, get_phone_number):
        click_order_button = MainPage(driver)
        click_order_button.main_page()
        click_order_button.scroll_to_order_button()
        click_order_button.click_order_button()
        order = OrderPage(driver)
        order.filling_form('Егор', 'Лапшин', 'Попова ул. 99', 'Аэропорт', get_phone_number)
        order.wait_for_rent_form()
        order.input_rental_information("09.09.2023", 'two', 'grey', 'no call')
        order.wait_for_confirm()
        order.click_confirmation_order()
        order_title = order.get_new_order_title()
        order.wait_for_order_completed()
        assert 'Заказ оформлен' in order_title
