import allure
import pytest

from locators.main_page_locators import FAQLocators
from pages.main_page import YaMainPage
from helpers import questions_block


class TestTextQuestion:
    @allure.feature('Проверка текста вопросов в блоке FAQ')
    @pytest.mark.parametrize("expected_text, locator", questions_block())
    def test_faq_question(self, driver, expected_text, locator):
        ya_main_page = YaMainPage(driver)
        ya_main_page.go_to_site(YaMainPage.URL_MAIN)
        ya_main_page.scroll_to_question()
        text_answer = ya_main_page.text_from_element(locator)
        assert text_answer == expected_text