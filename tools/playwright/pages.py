import allure
from playwright.sync_api import Playwright, Page
from config import settings
from config import settings, Browser  # Импортируем enum Browser


def initialize_playwright_page(
        playwright: Playwright,
        test_name: str,
        browser_type: Browser,  # Передаем бразуер в качестве аргумента
        storage_state: str | None = None
) -> Page:
    # Используем settings.headless
    # Динамически получаем нужный браузер
    browser = playwright[browser_type].launch(headless=settings.headless)

    # Создаем контекст для новой сессии браузера и указываем директорию для сохранения видеозаписей
    # Используем settings.videos_dir
    context = browser.new_context(
        base_url=settings.get_base_url(),  # Необходимо добавить settings.get_base_url()
        storage_state=storage_state,
        record_video_dir=settings.videos_dir
    )

    context.tracing.start(screenshots=True, snapshots=True, sources=True)   # Включаем трейсинг
    # Перенесли инициализацию страницы в отдельную переменную
    page = context.new_page()

    yield page

    # В данном случае request.node.name содержит название текущего автотеста
    # Сохраняем трейсинг в файл
    # Используем settings.tracing_dir
    context.tracing.stop(path=settings.tracing_dir.joinpath(f'{test_name}.zip'))

    browser.close()
    # Прикрепляем файл с трейсингом к Allure отчету
    # Используем settings.tracing_dir
    allure.attach.file(settings.tracing_dir.joinpath(f'{test_name}.zip'), name='trace', extension='zip')

    # Прикрепляем видео автотеста к Allure отчету
    allure.attach.file(page.video.path(), name='video', attachment_type=allure.attachment_type.WEBM)
