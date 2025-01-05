def is_screenshot(data):
    # Check for PNG header (magic number)
    png_header = b'\x89PNG\r\n\x1a\n'
    return data[:8] == png_header 
