from selenium.webdriver.common.by import By


class BasePageLocators:
    YANDEX_LOGO = By.XPATH, "//*[@alt='Yandex']"  # Логотип "Яндекс"
    SCOOTER_LOGO = By.XPATH, "//*[@alt='Scooter']"  # Логотип "Самокат"
    ORDER_BUTTON_IN_HEADER = By.XPATH, "//*[contains(@class, 'Header_Nav')]/button[text()='Заказать']"  # Кнопка "Заказать"
