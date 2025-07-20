import pdb
from datetime import datetime
from pathlib import Path
import pytest
from utils.driver_factory import get_driver

# Global variable to access driver for screenshots
driver_instance = None


@pytest.fixture(scope="function")
def browser():
    global driver_instance
    driver_instance = get_driver()
    yield driver_instance
    driver_instance.quit()


def _capture_screenshot(name):
    if driver_instance:
        screenshot_path = get_path / name
        driver_instance.save_screenshot(str(screenshot_path))
        return screenshot_path
    return None


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Required for pytest-html
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extras", [])

    if report.when == "call" and report.failed:
        # Save screenshot
        file_name = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        screenshot_path = _capture_screenshot(file_name)
        relative_path = screenshot_path.relative_to(get_path)
        if screenshot_path:
            html = (
                f'<div><img src="{relative_path}" alt="screenshot" '
                f'style="width:304px;height:228px;" '
                f'onclick="window.open(this.src)" align="right"/></div>'
            )
            extra.append(pytest_html.extras.html(html))
    report.extras = extra


# Create HTML report in unique folder
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    global pytest_html, get_path
    pytest_html = config.pluginmanager.getplugin("html")
    now = datetime.now()
    report_dir = Path("Reports", "TMDB_"+now.strftime("%d%m%Y_%H%M%S"))
    report_dir.mkdir(parents=True, exist_ok=True)
    get_path=report_dir
    config.option.htmlpath = report_dir / "report.html"
    config.option.self_contained_html = True


def pytest_html_report_title(report):
    report.title = "TMDB Automation Report"

def test_extra(extras):
    extras.append(pytest_html.extras.text("some string"))


