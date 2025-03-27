from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_site(self, url):
        self.driver.get(url)

    def find_element_located_click(self, locator, time=10):
        element = WebDriverWait(self.driver, time).until(
             EC.presence_of_element_located(locator),
             message=f'Element not found in {locator}')
        element.click()

    def find_element_scroll(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def find_element_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'Element not found in {locator}')

    def find_window(self, time=10):
        return WebDriverWait(self.driver, time).until(EC.number_of_windows_to_be(2))

    def scroll_and_click(self, locator, time=10):
        element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                         message=f'Element no found in {locator}')
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)

    def click_to_element(self, locator):
        """Кликает по элементу с ожиданием его кликабельности"""
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def switch_window(self, window_index=-1):
        """Переключается на новое окно (по умолчанию последнее)"""
        WebDriverWait(self.driver, 10).until(
            lambda d: len(d.window_handles) > 1
        )
        self.driver.switch_to.window(self.driver.window_handles[window_index])