import pytest
from playwright.sync_api import Page, expect
import allure

from tests.data_tests.tests_data import url, promo, ids, test_card, res


@pytest.fixture(autouse=True)
def setup(page: Page):
    page.set_viewport_size({"width": 1200, "height": 720})
    page.goto(url)
    expect(page).to_have_url(url)


@pytest.mark.elem
def test_subscription_elements(page: Page):

    expect(page).to_have_title("Task Management Board")

    expect(page.locator("h1")).to_be_visible()
    expect(
        page.locator('[class="subscription-title"]').filter(
            has_text="Подключение подписки StreamVibe"
        )
    ).to_be_visible()
    expect(page.locator('[class="period-switcher"]')).to_be_visible()
    expect(page.locator('[class="tariffs-section"]')).to_be_visible()
    expect(page.locator('[class="promo-section"]')).to_be_visible()
    expect(page.get_by_role("button", name="Применить")).to_be_visible()
    expect(page.locator('[class="payment-card-visual"]')).to_be_visible()
    expect(page.locator('[class="summary-section"]')).to_be_visible()


@allure.title("Проверка валидного промокода ALWAYS")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.prc
def test_promo_code_ALWAYS(page: Page):

    with allure.step("choose period"):
        page.get_by_test_id("period-12").click()
        expect(page.locator('[class="period-btn active"]')).to_be_visible()

    with allure.step("verify promo section is visible"):
        expect(page.locator('[class="promo-section"]')).to_be_visible()
        expect(page.get_by_role("button", name="Применить")).to_be_disabled()
        expect(page.get_by_placeholder("Введите промокод")).to_be_visible()

    with allure.step("enter promo code ALWAYS"):
        page.get_by_placeholder("Введите промокод").fill("ALWAYS")
        expect(page.get_by_role("button", name="Применить")).to_be_enabled()

    with allure.step("click the button"):
        page.get_by_role("button", name="Применить").click()

    with allure.step("verify promo code result"):
        expect(page.locator('[class="promo-message success"]')).to_have_text(
            "Промокод применён: Скидка 15% для для всех тарифов"
        )
        test_screen = page.screenshot()
        allure.attach(
            test_screen, name="result", attachment_type=allure.attachment_type.PNG
        )


@pytest.mark.prc
def test_promo_code_BASIC199(page: Page):

    page.get_by_test_id("period-1").click()
    expect(page.locator('[class="period-btn active"]')).to_be_visible()

    expect(page.locator('[class="tariffs-section"]')).to_be_visible()
    page.locator('[data-testid="tariff-basic"]').click()
    expect(page.get_by_test_id("tariff-basic")).to_have_class("tariff-card  selected")

    expect(page.locator('[class="promo-section"]')).to_be_visible()
    expect(page.get_by_role("button", name="Применить")).to_be_disabled()
    expect(page.get_by_placeholder("Введите промокод")).to_be_visible()

    page.get_by_placeholder("Введите промокод").fill("BASIC199")
    expect(page.get_by_role("button", name="Применить")).to_be_enabled()
    page.get_by_role("button", name="Применить").click()
    expect(page.locator('[class="promo-message success"]')).to_have_text(
        "Промокод применён: Специальная цена 199₷/мес на Базовый тариф"
    )


@pytest.mark.promo_code
@pytest.mark.parametrize("promo, expected_text", promo, ids=ids)
def test_credit_card_payment(page: Page, promo, expected_text):
    expect(page.locator('[class="promo-section"]')).to_be_visible()
    expect(page.get_by_role("button", name="Применить")).to_be_disabled()

    page.get_by_placeholder("Введите промокод").fill(promo)
    expect(page.get_by_role("button", name="Применить")).to_be_enabled()
    page.get_by_role("button", name="Применить").click()

    expect(page.get_by_test_id("promo-message")).to_have_text(expected_text)


@pytest.mark.payment
@pytest.mark.parametrize(
    "test_card, m_y, cv, class_model, expected_text", test_card, ids=res
)
def test_invalid_credit_card(
    page: Page, test_card, m_y, cv, class_model, expected_text
):
    expect(page.locator('[class="payment-section"]')).to_be_visible()
    page.get_by_placeholder("0000 0000 0000 0000").fill(test_card)
    page.get_by_placeholder("MM/YY").fill(m_y)
    page.get_by_placeholder("•••").fill(cv)

    expect(page.locator('[data-testid="summary-section"]')).to_be_visible()
    page.get_by_role("button", name="Подключить за ").click()

    if class_model == '[class="success-title"]':
        expect(page.locator(class_model)).to_have_text(expected_text)
        page.get_by_role("button", name="Отлично!").click()
    else:
        expect(page.get_by_test_id(class_model)).to_have_text(expected_text)
