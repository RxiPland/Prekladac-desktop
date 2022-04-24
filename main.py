# Vytvořil RxiPland
# 2022

# python 3.9.9

from time import sleep
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication
from hlavni_menu import Ui_MainWindow_hlavni_menu
from os.path import exists
import os
from googletrans import Translator
import threading
from hashlib import md5
import pyperclip
from urllib.parse import quote
import urllib.request
from shutil import move, rmtree
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer


class hlavni_menu0(QMainWindow, Ui_MainWindow_hlavni_menu):


    def __init__(self, *args, **kwargs):

        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)


    def ulozene_jazyky(self):

        # tato funkce uchovává zkratky jazyků pro tento program

        ulozene_jazyky = {"Čeština": "cs", "Angličtina": "en", "Němčina": "de", "Slovenština": "sk", "Ukrajinština": "uk", "Španělština": "es", "Francouzština": "fr", "Italština": "it", "Ruština": "ru",  "Polština": "pl"}

        # https://cloud.google.com/translate/docs/languages

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

        # ukončí přehrávání zvuku a smaže temp složku

        try:
        
            mixer.music.stop()
            mixer.music.unload()

        except:

            pass

        cesta_program = os.getcwd()
        cesta_temp_slozka = cesta_program + "\\temp"

        try:

            rmtree(cesta_temp_slozka)

        except:

            pass


    def reset_tlacitko(self):

        # tlačítko reset - vymaže textové buňky a vrátí výběr jazyků do původního stavu

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
            msgBox.setText("Výběr jazyků byl úspěšně uložen")
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

        self.pushButton.setEnabled(False)


        for i in reversed(range(0, POCET_SEKUND)):

            sleep(1)

            odpocitavani_casu = i

            self.pushButton.setText(f"Dostupné za {str(odpocitavani_casu)}s")

        self.pushButton.setText("Přeložit")
        self.pushButton.setEnabled(True)

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

                    if (odpocitavani_casu == 0 and md5_hash_prekladu != md5_hash_predchoziho_prekladu) or self.plainTextEdit_2.toPlainText() == "":

                        prelozeny_text = str(translator.translate(text_k_prelozeni, dest=jazyk_2, src=jazyk_1).text)

                        md5_hash_prekladu = str(md5((text_k_prelozeni + jazyk_1 + jazyk_2).encode()).hexdigest())

                        self.plainTextEdit_2.setPlainText(prelozeny_text.replace(".", ". "))

                        thread.start()

                        if self.checkBox.isChecked():

                            self.poslechnout_prelozeny()


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

        # tato funkce zkopíruje obsah pole do schránky uživatele

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

        # tato funkce vloží aktuální obsah schránky do textového pole

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

    def pustit_zvuk(self, cesta: str):

        # spustí zvuk
        # tato funkce se spouští v threadu

        mixer.init()

        mixer.music.load(cesta)
        mixer.music.play(loops=0)

        while mixer.music.get_busy():

            pass
        
        mixer.music.unload()
        self.pushButton_2.setChecked(False)
        self.pushButton_3.setChecked(False)

    def poslechnout_neprelozeny(self):

        # poslechne nepřeložený text

        neprelozeny_text = str(self.plainTextEdit.toPlainText())

        if neprelozeny_text.strip() == "":

            # zkontroluje zda je textové pole prázdné

            self.pushButton_2.setChecked(False)

            return

        elif self.pushButton_2.isChecked():

            cesta_program = os.getcwd()
            cesta_temp_slozka = cesta_program + "\\temp"

            ulozene_jazyky_dict = self.ulozene_jazyky()

            jazyk_1 = str(self.comboBox.currentText())

            md5hash_neprelozeny = str(md5((neprelozeny_text).encode()).hexdigest())

            cesta_mp3_temp = str(cesta_temp_slozka + "\\" + ulozene_jazyky_dict[jazyk_1] + "_" + md5hash_neprelozeny + ".mp3")

            if exists(cesta_mp3_temp):

                # pokud již mp3 soubor existuje

                try:

                    thread = threading.Thread(target=self.pustit_zvuk, args=(cesta_mp3_temp,))
                    thread.start()

                except:

                    msgBox = QMessageBox()
                    msgBox.setIcon(QMessageBox.Warning)
                    msgBox.setWindowTitle("Problém")
                    msgBox.setText("MP3 soubor nelze přehrát!")
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec()

                    self.pushButton_2.setChecked(False)
                    self.pushButton_3.setChecked(False)

                    return

            else:

                # stáhnout

                if not exists(cesta_temp_slozka):

                    os.mkdir(cesta_temp_slozka)

                zvuk_ke_stazeni_url = quote(neprelozeny_text, safe='/:?&')

                url_zvuku = "https://translate.google.com/translate_tts?ie=UTF-8&tl=" + ulozene_jazyky_dict[jazyk_1] + "&client=tw-ob&q=" + zvuk_ke_stazeni_url

                try:

                    response = urllib.request.urlretrieve(url_zvuku)

                    cesta_mp3 = str(response[0])
                    cesta_mp3 = cesta_mp3.replace("//", "/")

                    try:

                        if not exists(cesta_mp3_temp):

                            move(cesta_mp3, cesta_mp3_temp)

                        try:

                            thread = threading.Thread(target=self.pustit_zvuk, args=(cesta_mp3_temp,))
                            thread.start()

                        except:

                            msgBox = QMessageBox()
                            msgBox.setIcon(QMessageBox.Warning)
                            msgBox.setWindowTitle("Problém")
                            msgBox.setText("Nelze spustit mp3 soubor!")
                            msgBox.setStandardButtons(QMessageBox.Ok)
                            msgBox.exec()

                            self.pushButton_2.setChecked(False)
                            self.pushButton_3.setChecked(False)

                            return

                    except:

                        msgBox = QMessageBox()
                        msgBox.setIcon(QMessageBox.Warning)
                        msgBox.setWindowTitle("Problém")
                        msgBox.setText("Nastala chyba při přesouvání mp3 souboru do temp složky!")
                        msgBox.setStandardButtons(QMessageBox.Ok)
                        msgBox.exec()

                        return

                except urllib.error.HTTPError:

                    msgBox = QMessageBox()
                    msgBox.setIcon(QMessageBox.Warning)
                    msgBox.setWindowTitle("Problém")
                    msgBox.setText("Text je moc dlouhý, aby se mohl zvukově přehrát!")
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec()

                    self.pushButton_2.setChecked(False)
                    self.pushButton_3.setChecked(False)

                    return

                except urllib.error.URLError:

                    msgBox = QMessageBox()
                    msgBox.setIcon(QMessageBox.Warning)
                    msgBox.setWindowTitle("Problém")
                    msgBox.setText("Nefunguje připojení k internetu!")
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec()

                    self.pushButton_2.setChecked(False)
                    self.pushButton_3.setChecked(False)

                    return

        else:

            try:

                mixer.music.stop()

            except:

                return


    def poslechnout_prelozeny(self):

        # poslechne přeložený text

        prelozeny_text = str(self.plainTextEdit_2.toPlainText())

        if prelozeny_text.strip() == "":

            # zkontroluje zda je textové pole prázdné, pokud ano, nebude se pokračovat dál

            self.pushButton_3.setChecked(False)

            return

        elif self.pushButton_3.isChecked() or self.checkBox.isChecked():

            # pokud bude tlačítko poslechnout u přeloženého textu, nebo zaškrtávácí políčko zmáčknuto, spustí se zvuk

            cesta_program = os.getcwd()
            cesta_temp_slozka = cesta_program + "\\temp"

            ulozene_jazyky_dict = self.ulozene_jazyky()

            jazyk_2 = str(self.comboBox_2.currentText())

            md5hash_prelozeny = str(md5((prelozeny_text).encode()).hexdigest())

            cesta_mp3_temp = str(cesta_temp_slozka + "\\" + ulozene_jazyky_dict[jazyk_2] + "_" + md5hash_prelozeny + ".mp3")

            if exists(cesta_mp3_temp):

                # pokud již mp3 soubor existuje

                try:

                    thread = threading.Thread(target=self.pustit_zvuk, args=(cesta_mp3_temp,))
                    thread.start()

                except:

                    msgBox = QMessageBox()
                    msgBox.setIcon(QMessageBox.Warning)
                    msgBox.setWindowTitle("Problém")
                    msgBox.setText("MP3 soubor nelze přehrát!\n\nZkuste zavřít a znovu otevřít program.")
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec()

                    self.pushButton_2.setChecked(False)
                    self.pushButton_3.setChecked(False)

                    return

            else:

                # stáhnout

                if not exists(cesta_temp_slozka):

                    os.mkdir(cesta_temp_slozka)

                zvuk_ke_stazeni_url = quote(prelozeny_text, safe='/:?&')

                url_zvuku = "https://translate.google.com/translate_tts?ie=UTF-8&tl=" + ulozene_jazyky_dict[jazyk_2] + "&client=tw-ob&q=" + zvuk_ke_stazeni_url

                try:

                    response = urllib.request.urlretrieve(url_zvuku)

                    cesta_mp3 = str(response[0])
                    cesta_mp3 = cesta_mp3.replace("//", "/")

                    try:

                        if not exists(cesta_mp3_temp):

                            move(cesta_mp3, cesta_mp3_temp)

                        try:

                            thread = threading.Thread(target=self.pustit_zvuk, args=(cesta_mp3_temp,))
                            thread.start()

                        except:

                            msgBox = QMessageBox()
                            msgBox.setIcon(QMessageBox.Warning)
                            msgBox.setWindowTitle("Problém")
                            msgBox.setText("Nelze spustit mp3 soubor!")
                            msgBox.setStandardButtons(QMessageBox.Ok)
                            msgBox.exec()

                            return

                    except:

                        msgBox = QMessageBox()
                        msgBox.setIcon(QMessageBox.Warning)
                        msgBox.setWindowTitle("Problém")
                        msgBox.setText("Nastala chyba při přesouvání mp3 souboru do temp složky!")
                        msgBox.setStandardButtons(QMessageBox.Ok)
                        msgBox.exec()

                        return

                except urllib.error.HTTPError:

                    msgBox = QMessageBox()
                    msgBox.setIcon(QMessageBox.Warning)
                    msgBox.setWindowTitle("Problém")
                    msgBox.setText("Text je moc dlouhý, aby se mohl zvukově přehrát!")
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec()

                    self.pushButton_2.setChecked(False)
                    self.pushButton_3.setChecked(False)

                    return

                except urllib.error.URLError:

                    msgBox = QMessageBox()
                    msgBox.setIcon(QMessageBox.Warning)
                    msgBox.setWindowTitle("Problém")
                    msgBox.setText("Nefunguje připojení k internetu!")
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec()

                    self.pushButton_2.setChecked(False)
                    self.pushButton_3.setChecked(False)

                    return

        else:

            try:

                mixer.music.stop()

            except:

                return

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
    hlavni_menu1.pushButton_2.clicked.connect(hlavni_menu1.poslechnout_neprelozeny)
    hlavni_menu1.pushButton_3.clicked.connect(hlavni_menu1.poslechnout_prelozeny)
    hlavni_menu1.pushButton_4.clicked.connect(hlavni_menu1.reset_tlacitko)
    hlavni_menu1.pushButton_5.clicked.connect(hlavni_menu1.ulozit_nastaveni)
    hlavni_menu1.pushButton_6.clicked.connect(hlavni_menu1.kopirovat_do_schranky)
    hlavni_menu1.pushButton_7.clicked.connect(hlavni_menu1.vlozit_ze_schranky)

    app.aboutToQuit.connect(hlavni_menu1.ukoncit)
    sys.exit(app.exec_())