import allure
import pytest

from locators.main_page_locators import FAQLocators
from pages.base_page import BasePage
from pages.main_page import YaMainPage
from helpers import answer_block

class TestAnswerText:
    @allure.feature('Проверка текста в блоке FAQ')
    @pytest.mark.parametrize("expected_text, question, answer", answer_block())
    def test_faq_answer(self, driver, expected_text, question, answer):
        ya_main_page = YaMainPage(driver)
        question_element = BasePage(driver)
        ya_main_page.go_to_site(YaMainPage.URL_MAIN)
        question_element.scroll_and_click(question)
        text_answer = ya_main_page.text_from_element(answer)
        assert text_answer == expected_text