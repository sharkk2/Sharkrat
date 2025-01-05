import pyautogui
from io import BytesIO


def screenshot():
    screenshot_buffer = BytesIO()
    screenshot = pyautogui.screenshot()
    screenshot.save(screenshot_buffer, format="PNG")
    screenshot_data = screenshot_buffer.getvalue()
    return screenshot_data
