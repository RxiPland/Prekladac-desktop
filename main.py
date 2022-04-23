# Vytvořil RxiPland
# 2022

from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication, QFileDialog, QDialog
from hlavni_menu import Ui_MainWindow_hlavni_menu
from os.path import exists
import os
import requests 


class hlavni_menu0(QMainWindow, Ui_MainWindow_hlavni_menu):


    def __init__(self, *args, **kwargs):

        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)


    def ulozene_jazyky(self):

        # tato funkce uchovává všechny dostupné jazyky pro tento program

        ulozene_jazyky = {"Čeština": "cs", "Angličtina": "en", "Němčina": "de", "Slovenština": "sk", "Ukrajinština": "uk", "Španělština": "es", "Francouzština": "fr", "Italština": "it", "Ruština": "ru",  "Polština": "pl"}

        #Čeština
        #Angličtina
        #Němčina
        #Slovenština
        #Ukrajinština
        #Španělština
        #Francouzština
        #Italština
        #Ruština
        #Polština

        return ulozene_jazyky


    def najit_ulozene_nastaveni(self):

        # načte uložené nastavení z textového souboru pokud existuje

        cesta_k_programu = os.getcwd()
        cesta_k_nastaveni = cesta_k_programu + "\\nastaveni.txt"

        if exists(cesta_k_nastaveni):

            f = open(cesta_k_nastaveni, "rb")
            nacteny_obsah = f.readlines()
            f.close()

            if nacteny_obsah == []:

                return "ZADNE_NENI"

            else:

                return str(nacteny_obsah[0].decode("UTF-8"))

        else:

            return "ZADNE_NENI"

    def ukoncit(self):

        # dodělat smazání dočasné složky se zvuky

        pass

    def reset_tlacitko(self):

        self.plainTextEdit.clear()
        self.plainTextEdit_2.clear()

        self.checkBox.setChecked(False)

        ulozene_nastaveni = self.najit_ulozene_nastaveni()

        if ulozene_nastaveni != "ZADNE_NENI":

            ulozene_nastaveni_tuple = tuple(ulozene_nastaveni.split(";"))

            self.comboBox.setCurrentText(ulozene_nastaveni_tuple[0])
            self.comboBox_2.setCurrentText(ulozene_nastaveni_tuple[1])

        else:

            self.comboBox.setCurrentIndex(0)
            self.comboBox_2.setCurrentIndex(0)

    def ulozit_nastaveni(self):

        # uloží nastavení jazyků do textového souboru

        try:

            jazyk_1 = str(self.comboBox.currentText())
            jazyk_2 = str(self.comboBox_2.currentText())

            cesta_k_programu = os.getcwd()
            cesta_k_nastaveni = cesta_k_programu + "\\nastaveni.txt"

            f = open(cesta_k_nastaveni, "wb")
            f.write((jazyk_1 + ";" + jazyk_2).encode())
            f.close()

            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Question)
            msgBox.setWindowTitle("Oznámení")
            msgBox.setText("Rozložení jazyků bylo úspěšně uloženo")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()

        except:

            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setWindowTitle("Problém")
            msgBox.setText("Nastavení se nepodařilo uložit do textového souboru!")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()

    def prelozit(self):

        # funkce, která přeloží text

        try:

            ulozene_jazyky_dict = self.ulozene_jazyky()

            jazyk_1 = str(self.comboBox.currentText())
            jazyk_1 = ulozene_jazyky_dict[jazyk_1]


            jazyk_2 = str(self.comboBox_2.currentText())
            jazyk_2 = ulozene_jazyky_dict[jazyk_2]

            text_k_prelozeni = str(self.plainTextEdit.toPlainText())

            if text_k_prelozeni == "":
                
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Warning)
                msgBox.setWindowTitle("Chyba")
                msgBox.setText("Pole pro text nemůže být prázdné!")
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec()

                return

            else:

                url_prekladace = f"https://translate.google.com/?sl={jazyk_1}&tl={jazyk_2}&text={text_k_prelozeni}"

                try:

                    response = requests.get(url_prekladace)

                    print(response.text)

                except:

                    msgBox = QMessageBox()
                    msgBox.setIcon(QMessageBox.Warning)
                    msgBox.setWindowTitle("Problém")
                    msgBox.setText("Nelze se připojit k internetu!")
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec()

        except:

            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setWindowTitle("Problém")
            msgBox.setText("Někde se vyskytla chyba!")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()



if __name__ == "__main__":

    import sys
    app = QApplication(sys.argv)

    hlavni_menu1 = hlavni_menu0()

    hlavni_menu1.reset_tlacitko()
    hlavni_menu1.show()

    hlavni_menu1.pushButton.clicked.connect(hlavni_menu1.prelozit)
    hlavni_menu1.pushButton_4.clicked.connect(hlavni_menu1.reset_tlacitko)
    hlavni_menu1.pushButton_5.clicked.connect(hlavni_menu1.ulozit_nastaveni)

    app.aboutToQuit.connect(hlavni_menu1.ukoncit)
    sys.exit(app.exec_())