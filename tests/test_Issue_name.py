import allure
from allure_commons.types import Severity
from selene import browser, have
from models.models import Github

@allure.tag("web")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "nlevusenkov")
@allure.feature("Поиск названия issu")
@allure.story("Проверка названия issue без шагов аллюра")
@allure.link("https://github.com", name="Testing")
def test_issue_name_selene():
    browser.open("https://github.com")
    browser.element("[data-target='qbsearch-input.inputButton']").click()
    browser.element("#query-builder-test").type('nlevusenkov/qa_guru_homework5').press_enter()
    browser.element("[href='/nlevusenkov/qa_guru_homework5']").click()
    browser.element('#issues-tab').click()
    browser.element('[data-testid="issue-pr-title-link"]').should(have.text('test'))

@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "nlevusenkov")
@allure.feature("Поиск названия issu")
@allure.story("Проверка названия issue с шагами аллюра with")
@allure.link("https://github.com", name="Testing")
def test_issue_name_with_allure_step():
    github = Github()
    with allure.step('Открываем github'):
        github.open_github2()
    with allure.step('ищем свой репозиторий'):
        github.search_repository2()
    with allure.step('Переходим в свой репозиторий'):
        github.go_to_repository2()
    with allure.step('Переходим во вкладку issue'):
        github.open_issue2()
    with allure.step('Проверяем имя issue'):
        github.find_issue_name('test1')


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "nlevusenkov")
@allure.feature("Поиск названия issu")
@allure.story("Проверка названия issue с шагами аллюра step")
@allure.link("https://github.com", name="Testing")
def test_issue_name_allure_step():
    github = Github()
    github.open_github()
    github.search_repository()
    github.go_to_repository()
    github.open_issue()
    github.find_issue_name('test')