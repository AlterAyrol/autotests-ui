import allure
from playwright.sync_api import Playwright, Page


def initialize_playwright_page(
        playwright: Playwright,
        test_name: str,
        storage_state: str | None = None
) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state=storage_state, record_video_dir='./videos')   # Создаем контекст для новой сессии браузера и указываем директорию для сохранения видеозаписей
    context.tracing.start(screenshots=True, snapshots=True, sources=True)   # Включаем трейсинг
    # Перенесли инициализацию страницы в отдельную переменную
    page = context.new_page()

    yield page

    # В данном случае request.node.name содержит название текущего автотеста
    context.tracing.stop(path=f'./tracing/{test_name}.zip')  # Сохраняем трейсинг в файл
    browser.close()
    # Прикрепляем файл с трейсингом к Allure отчету
    allure.attach.file(f'./tracing/{test_name}.zip', name='trace', extension='zip')
    # Прикрепляем видео автотеста к Allure отчету
    allure.attach.file(page.video.path(), name='video', attachment_type=allure.attachment_type.WEBM)
