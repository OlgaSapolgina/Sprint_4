import allure
import pytest
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.urls import DataUrls
from data.data import TextData, RentalData
from data.persons import Persons


@pytest.mark.usefixtures("driver", "get_phone_number", "get_date_today", "get_date_tomorrow")
class TestOrderButton:
    @allure.title('Оформление заказа по кнопке "Заказать" в шапке страницы')
    @allure.description('Корректное заполнение всех полей заказа,'
                        ' после подтверждения отображается {TextData.SUCCESSFUL_ORDER_TEXT}')
    def test_order_button_on_header(self, driver, get_phone_number, get_date_today):
        page = BasePage(driver)
        page.open_page(DataUrls.SCOOTER_URL)
        click_order_button = MainPage(driver)
        click_order_button.click_order_button_in_header()
        order = OrderPage(driver)
        order.filling_form(Persons.PERSON_1, get_phone_number)
        order.wait_for_rent_form()
        order.input_rental_information(get_date_today, RentalData.DATA_1)
        order.wait_for_confirm()
        order.click_confirmation_order()
        order_title = order.get_new_order_title()
        order.wait_for_order_completed()
        assert TextData.SUCCESSFUL_ORDER_TEXT in order_title

    @allure.title('Оформление заказа по кнопке "Заказать" на главной странице')
    @allure.description('Корректное заполнение всех полей заказа,'
                        ' после подтверждения отображается {TextData.SUCCESSFUL_ORDER_TEXT}')
    def test_order_button_main_page_current_date_user_flow_positive(self, driver, get_phone_number, get_date_tomorrow):
        page = BasePage(driver)
        page.open_page(DataUrls.SCOOTER_URL)
        click_order_button = MainPage(driver)
        click_order_button.scroll_to_order_button()
        click_order_button.click_order_button()
        order = OrderPage(driver)
        order.filling_form(Persons.PERSON_2, get_phone_number)
        order.wait_for_rent_form()
        order.input_rental_information(get_date_tomorrow, RentalData.DATA_2)
        order.wait_for_confirm()
        order.click_confirmation_order()
        order_title = order.get_new_order_title()
        order.wait_for_order_completed()
        assert TextData.SUCCESSFUL_ORDER_TEXT in order_title
