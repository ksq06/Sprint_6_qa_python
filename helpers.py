from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators.main_page_locators import FAQLocators

def answer_block():
    return [
        (
            "Сутки — 400 рублей. Оплата курьеру — наличными или картой.",
            FAQLocators.FAQ_QUESTION_1,
            FAQLocators.FAQ_ANSWER_1
        ),

        (
            "Пока что у нас так: один заказ — один самокат. "
            "Если хотите покататься с друзьями, можете просто сделать несколько заказов "
            "— один за другим.",
            FAQLocators.FAQ_QUESTION_2,
            FAQLocators.FAQ_ANSWER_2
        ),

        (
            "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня."
            " Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру."
            " Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.",
            FAQLocators.FAQ_QUESTION_3,
            FAQLocators.FAQ_ANSWER_3
        ),

        (
            "Только начиная с завтрашнего дня. Но скоро станем расторопнее.",
            FAQLocators.FAQ_QUESTION_4,
            FAQLocators.FAQ_ANSWER_4
        ),

        (
            "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку "
            "по красивому номеру 1010.",
            FAQLocators.FAQ_QUESTION_5,
            FAQLocators.FAQ_ANSWER_5
        ),

        (
            "Самокат приезжает к вам с полной зарядкой. "
            "Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.",
            FAQLocators.FAQ_QUESTION_6,
            FAQLocators.FAQ_ANSWER_6
        ),

        (
            "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже "
            "не попросим. Все же свои.",
            FAQLocators.FAQ_QUESTION_7,
            FAQLocators.FAQ_ANSWER_7
        ),

        (
            "Да, обязательно. Всем самокатов! И Москве, и Московской области.",
            FAQLocators.FAQ_QUESTION_8,
            FAQLocators.FAQ_ANSWER_8
        ),
    ]

def questions_block():
    return [
        (
            "Сколько это стоит? И как оплатить?",
            FAQLocators.FAQ_QUESTION_1
        ),
        (
            "Хочу сразу несколько самокатов! Так можно?",
            FAQLocators.FAQ_QUESTION_2
        ),
        (
            "Как рассчитывается время аренды?",
            FAQLocators.FAQ_QUESTION_3
        ),
        (
            "Можно ли заказать самокат прямо на сегодня?",
            FAQLocators.FAQ_QUESTION_4
        ),
        (
            "Можно ли продлить заказ или вернуть самокат раньше?",
            FAQLocators.FAQ_QUESTION_5
        ),
        (
            "Вы привозите зарядку вместе с самокатом?",
            FAQLocators.FAQ_QUESTION_6
        ),
        (
            "Можно ли отменить заказ?",
            FAQLocators.FAQ_QUESTION_7
        ),
        (
            "Я жизу за МКАДом, привезёте?",
            FAQLocators.FAQ_QUESTION_8
        ),
    ]