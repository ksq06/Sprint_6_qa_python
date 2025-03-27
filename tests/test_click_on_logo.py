import allure
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators
from pages.main_page import YaMainPage
from pages.order_page import OrderScooterPage
from selenium.webdriver.common.by import By
from pages.switch_page import SwitchPage


class TestClickOnLogo:
    @allure.title('Проверка перехода на главную страницу по клику на лого Самоката')
    def test_click_on_logo_scooter(self, driver):
        logo_scooter = YaMainPage(driver)
        order_page = OrderScooterPage(driver)
        order_page.go_to_site(OrderScooterPage.URL_ORDER)
        logo_scooter.click_logo_scooter()
        assert YaMainPage.URL_MAIN == driver.current_url

    @allure.title('Проверка перехода на Дзен по клику на лого Дзена')
    def test_transition_from_order_page_to_dzen(self, driver):
        switch_page = SwitchPage(driver)
        main_page = YaMainPage(driver)
        driver.get(YaMainPage.URL_MAIN)
        switch_page.switch_to_dzen_page()
        WebDriverWait(driver, 15).until(
            lambda d: "dzen.ru" in d.current_url or "sso.passport.yandex.ru" in d.current_url)
        assert driver.current_url.startswith("https://dzen.ru") or "retpath=https%3A%2F%2Fdzen.ru" in driver.current_url
        allure.attach(driver.current_url, name="Текущий URL", attachment_type=allure.attachment_type.TEXT)