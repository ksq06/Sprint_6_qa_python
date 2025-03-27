import allure
from selenium.webdriver.support.wait import WebDriverWait
from locators.switch_page_locators import SwitchPageLocators
from pages.base_page import BasePage


class SwitchPage(BasePage):
    @allure.step('Переходим на главную страницу')
    def switch_to_scooter_page(self):
        self.click_to_element(SwitchPageLocators.scooter_logo)

    @allure.step('Переходим на страницу Дзена')
    def switch_to_dzen_page(self):
        main_window = self.driver.current_window_handle
        self.click_to_element(SwitchPageLocators.dzen_logo)

        WebDriverWait(self.driver, 10).until(
            lambda d: len(d.window_handles) > 1
        )

        for window_handle in self.driver.window_handles:
            if window_handle != main_window:
                self.driver.switch_to.window(window_handle)
                break

        WebDriverWait(self.driver, 15).until(
            lambda d: "dzen.ru" in d.current_url
        )

    @allure.step('Получаем текст заголовка главной страницы')
    def get_scooter_headline_text(self):
        return self.get_text_from_element(SwitchPageLocators.title_main_page)

    @allure.step('Находим логотип на странице Дзена')
    def check_dzen_button(self):
        return self.find_element_with_wait(SwitchPageLocators.logo_dzen_main_page)