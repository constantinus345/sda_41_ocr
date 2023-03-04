from PIL import Image

import pytesseract

def functie_de_convertire_img_to_string(image_path, lang = "eng"):
    # https://tesseract-ocr.github.io/tessdoc/Data-Files-in-different-versions.html
    pytesseract.pytesseract.tesseract_cmd = "B:/All_Software/Tesseract/tesseract.exe"
    img_binary = Image.open(image_path)
    text_extras = pytesseract.image_to_string(img_binary, lang)
    return text_extras

if __name__ == '__main__':
    img_path = 'C:/Users/const/OneDrive/Desktop/Screenshot_10.png'
    print(functie_de_convertire_img_to_string(img_path))
