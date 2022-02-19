from PyQt5 import QtCore, QtGui, QtWidgets
from pdf2image import convert_from_path
from io import BytesIO
import utils


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.B_avancar = QtWidgets.QPushButton(self.centralwidget)
        self.B_avancar.setGeometry(QtCore.QRect(110, 40, 71, 41))
        self.B_avancar.setObjectName("B_avancar")
        self.B_voltar = QtWidgets.QPushButton(self.centralwidget)
        self.B_voltar.setGeometry(QtCore.QRect(30, 40, 71, 41))
        self.B_voltar.setObjectName("B_voltar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 90, 450, 390))
        self.label.setObjectName("label")
        self.CB_file = QtWidgets.QComboBox(self.centralwidget)
        self.CB_file.setGeometry(QtCore.QRect(510, 80, 161, 21))
        self.CB_file.setObjectName("CB_file")

        self.pdfs = utils.apresentar_arquivos()
        for i in self.pdfs:
            self.CB_file.addItem("")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(510, 60, 141, 16))
        self.label_2.setObjectName("label_2")
        self.B_arquivo = QtWidgets.QPushButton(self.centralwidget)
        self.B_arquivo.setGeometry(QtCore.QRect(680, 80, 75, 23))
        self.B_arquivo.setObjectName("B_arquivo")
        self.B_pagina = QtWidgets.QPushButton(self.centralwidget)
        self.B_pagina.setGeometry(QtCore.QRect(200, 60, 75, 23))
        self.B_pagina.setObjectName("B_pagina")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 10, 241, 21))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.B_avancar.setText(_translate("MainWindow", "Avançar"))
        self.B_voltar.setText(_translate("MainWindow", "Voltar"))
        self.label.setText(_translate("MainWindow", "TextLabel"))

        self.has_file = False
        
        self.images = [] # Page photo
        self.page = 0 # Page on display

        self.poppler = "C:/Program Files/poppler-22.01.0/Library/bin"

        self.label_2.setText(_translate("MainWindow", "Selecione o arquivo PDF"))
        self.B_arquivo.setText(_translate("MainWindow", "Selecionar"))
        self.B_pagina.setText(_translate("MainWindow", "Selecionar"))
        self.label_3.setText(_translate("MainWindow", "Opções de páginas"))

        for i, pdf in enumerate(self.pdfs):
            self.CB_file.setItemText(i, _translate("MainWindow", pdf))

        self.B_voltar.clicked.connect(self.previousPage)
        self.B_avancar.clicked.connect(self.nextPage)
        self.B_pagina.clicked.connect(self.selectPage)
        self.B_arquivo.clicked.connect(self.selectFile)
    
    def loadppm(self, image, PixMap):
        img_byte_arr = BytesIO()
        image.save(img_byte_arr, format='ppm')
        img_byte_arr = img_byte_arr.getvalue()
        PixMap.loadFromData(img_byte_arr)

    def nextPage(self):
        # true = next; false = previous
        if (self.page == (len(self.images) - 1)) or (self.has_file == False):
            pass
        else:
            self.page += 1
            self.loadppm(self.images[self.page], self.page_pixmap)
            self.label.setPixmap(self.page_pixmap)

    def previousPage(self):
        # true = next; false = previous
        if (self.page == 0) or (self.has_file == False):
            pass
        else:
            self.page -= 1
            self.loadppm(self.images[self.page], self.page_pixmap)
            self.label.setPixmap(self.page_pixmap)
    
    def selectPage(self):
        #global a
        #global coords
        #a = 0
        #coords = 0
        utils.mostrar_pagina(self.arquivo, self.page)
    
    def selectFile(self):
        self.has_file = True

        self.arquivo = f"Examples/{self.CB_file.currentText()}"
        self.images = convert_from_path(self.arquivo, poppler_path=self.poppler, fmt="ppm", size=(450, None))
        self.page_pixmap = QtGui.QPixmap()
        self.loadppm(self.images[self.page], self.page_pixmap)

        self.label.setGeometry(QtCore.QRect(20, 90, 450, self.images[0].size[1]))
        self.label.setPixmap(self.page_pixmap)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
