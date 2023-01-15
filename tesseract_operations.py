import pytesseract
import os


def tesseract_it(path):
    # get image from path run tesseract on it and save the result in save_path as txt
    if os.path.exists(path):
        text = pytesseract.image_to_string(path)
        return text
    else:
        return False
