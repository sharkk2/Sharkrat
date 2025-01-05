import ctypes

def notify(data):
    ctypes.windll.user32.MessageBoxW(0, data['body'], data['title'], 0)


