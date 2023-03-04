from PIL import Image

import pytesseract

def functie_de_convertire_img_to_string(image_path):
    pytesseract.pytesseract.tesseract_cmd = "B:/All_Software/Tesseract/tesseract.exe"



    pdf_path = 'C:/Users/const/Downloads/scansmpl.pdf'
    # Simple image to string
    img_binary = Image.open(image_path)
    text_extras = pytesseract.image_to_string(img_binary)

    return text_extras

if __name__ == '__main__':
    img_path = 'C:/Users/const/OneDrive/Desktop/Screenshot_10.png'
    print(functie_de_convertire_img_to_string(img_path))
