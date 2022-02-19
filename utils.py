from pdfminer.high_level import extract_pages
from matplotlib import pyplot as plt
from pdf2image import convert_from_path
from os import listdir
import camelot


def mostrar_pagina(arquivo, numero_pagina):
    # Variáveis importantes para a função mouse_click()
    global a
    global coords
    coords = ''
    a = 0

    def mouse_click(event):
        x, y = event.xdata, event.ydata
        
        global a
        global coords
        if a==0:
            coords = coords + f'{x},{y}'
            a += 1
        else:
            coords = coords + f',{x},{y}'
            a += 1
        
        print(coords)
        
        if a==2:
            table = camelot.read_pdf(arquivo, pages=str(numero_pagina+1), flavor='stream', 
                                    table_areas=[coords], flag_size=False)
            print("Total tables extracted:", table.n)
            df = table[0].df
            print(df)
            print("Tabela enviada para Excel")
            df.to_excel("Teste.xlsx")

    # Poppler e foto da página
    poppler = "C:/Program Files/poppler-22.01.0/Library/bin"
    image = convert_from_path(arquivo, poppler_path=poppler, first_page=numero_pagina+1, last_page=numero_pagina+1)

    # Layout da página (dimensões e elementos)
    pages = extract_pages(arquivo, page_numbers=[numero_pagina+1])

    page_layouts = []
    for page_layout in pages:
        page_layouts.append(page_layout)
    
    # Plotar a figura com as dimensões corretas
    x1 = page_layouts[0].x1
    y1 = page_layouts[0].y1

    fig, ax = plt.subplots()
    ax.imshow(image[0], extent=[0, x1, 0, y1])

    plt.connect('button_press_event', mouse_click)
    plt.show()


def apresentar_arquivos():
    # Lista todos os pdfs na pasta
    files = list()
    lista = listdir("Examples")
    for file in lista:
        if '.pdf' in file:
            files.append(file)
        else:
            pass

    return files