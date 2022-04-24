# Vytvořil RxiPland
# 2022

# python 3.9.9

from time import sleep
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication, QFileDialog, QDialog
from hlavni_menu import Ui_MainWindow_hlavni_menu
from os.path import exists
import os
from googletrans import Translator
import threading
from hashlib import md5
import pyperclip


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

    def prodleva_mezi_preklady(self):

        # vyčká se POCET_SEKUND po přeložení textu, aby se předešlo zablokování ip adresy

        global odpocitavani_casu, POCET_SEKUND


        for i in reversed(range(0, POCET_SEKUND)):

            sleep(1)

            odpocitavani_casu = i

            self.pushButton.setText(f"Dostupné za {str(odpocitavani_casu)}s")

        self.pushButton.setText("Přeložit")

    def prelozit(self):

        # funkce, která přeloží text

        global md5_hash_prekladu

        try:

            ulozene_jazyky_dict = self.ulozene_jazyky()

            jazyk_1 = str(self.comboBox.currentText())
            jazyk_1 = ulozene_jazyky_dict[jazyk_1]


            jazyk_2 = str(self.comboBox_2.currentText())
            jazyk_2 = ulozene_jazyky_dict[jazyk_2]

            text_k_prelozeni = str(self.plainTextEdit.toPlainText())

            md5_hash_predchoziho_prekladu = str(md5((self.plainTextEdit.toPlainText() + jazyk_1 + jazyk_2).encode()).hexdigest())

            if text_k_prelozeni == "":
                
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Warning)
                msgBox.setWindowTitle("Chyba")
                msgBox.setText("Pole pro text nemůže být prázdné!")
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec()

                return

            else:

                translator = Translator(service_urls=['translate.google.com'])
                thread = threading.Thread(target=self.prodleva_mezi_preklady)

                try:

                    if odpocitavani_casu == 0 and md5_hash_prekladu != md5_hash_predchoziho_prekladu:

                        prelozeny_text = str(translator.translate(text_k_prelozeni, dest=jazyk_2, src=jazyk_1).text)

                        md5_hash_prekladu = str(md5((text_k_prelozeni + jazyk_1 + jazyk_2).encode()).hexdigest())

                        self.plainTextEdit_2.setPlainText(prelozeny_text)

                        thread.start()

                    else:

                        pass


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

    def kopirovat_do_schranky(self):

        try:

            prelozeny_text = str(self.plainTextEdit_2.toPlainText())

            pyperclip.copy(prelozeny_text)

            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Question)
            msgBox.setWindowTitle("Oznámení")
            msgBox.setText("Překlad byl úspěšně zkopírován")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()

        except:

            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setWindowTitle("Problém")
            msgBox.setText("Překlad se nepodařilo zkopírovat!")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()

    def vlozit_ze_schranky(self):

        try:

            text_ze_schranky = str(pyperclip.paste())

            self.plainTextEdit.setPlainText(text_ze_schranky)

        except:

            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setWindowTitle("Problém")
            msgBox.setText("Nepodařilo se vložit text ze schránky!")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()



if __name__ == "__main__":


    import sys
    app = QApplication(sys.argv)

    odpocitavani_casu = 0
    POCET_SEKUND = 5
    md5_hash_prekladu = ""

    hlavni_menu1 = hlavni_menu0()

    hlavni_menu1.reset_tlacitko()
    hlavni_menu1.show()

    hlavni_menu1.pushButton.clicked.connect(hlavni_menu1.prelozit)
    hlavni_menu1.pushButton_4.clicked.connect(hlavni_menu1.reset_tlacitko)
    hlavni_menu1.pushButton_5.clicked.connect(hlavni_menu1.ulozit_nastaveni)
    hlavni_menu1.pushButton_6.clicked.connect(hlavni_menu1.kopirovat_do_schranky)
    hlavni_menu1.pushButton_7.clicked.connect(hlavni_menu1.vlozit_ze_schranky)

    app.aboutToQuit.connect(hlavni_menu1.ukoncit)
    sys.exit(app.exec_())
