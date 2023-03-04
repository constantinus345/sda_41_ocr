import pdf2image
from img_to_text import functie_de_convertire_img_to_string



def convert_pdf_to_text_dict(pdf_path, Folder):
    poppler_bin = "B:/prog/poppler-23.01.0/Library/bin"
    # Store Pdf with convert_from_path function
    images = pdf2image.convert_from_path(pdf_path, poppler_path = poppler_bin)
    dict_text = {}

    for i in range(len(images)):
        #iterare pe fiecare pagina a pdf-ului
        # Save pages as images in the pdf
        path_to_image = f"{Folder}/img_{str(i+1)}.jpg"
        images[i].save(path_to_image,"JPEG")
        dict_text[f"page_{str(i+1)}"] = functie_de_convertire_img_to_string(path_to_image)

    return  dict_text

if __name__ == "__main__":
    pdf_path = 'C:/Users/const/Downloads/scansmpl.pdf'
    Folder = 'C:/Users/const/OneDrive/Desktop'
    dictx = convert_pdf_to_text_dict(pdf_path, Folder)
    print(dictx["page_1"])
