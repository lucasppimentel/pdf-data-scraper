from pdfminer.high_level import extract_pages
from matplotlib import pyplot as plt
from pdf2image import convert_from_path

pdf = 'E:/projs/webscrapper/Alpha/apresentação.pdf'

def mostrar_pagina(arquivo, numero_pagina):
    poppler = "C:/Program Files/poppler-22.01.0/Library/bin"
    image = convert_from_path(arquivo, poppler_path=poppler)
    pagina = image[numero_pagina]

    pages = extract_pages(pdf, page_numbers=[5])

    page_layouts = []
    for page_layout in pages:
        page_layouts.append(page_layout)
    
    x1 = page_layouts[numero_pagina-1].x1
    y1 = page_layouts[numero_pagina-1].y1

    ax.imshow(image[0], extent=[0, maior_x1, 0, maior_y1])
    plt.show()