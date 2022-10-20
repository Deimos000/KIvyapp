from logging import root
from tokenize import Name
from typing_extensions import Self
import kivy
from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window 
from kivy.uix.scrollview import ScrollView
from kivy.properties import ObjectProperty  
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
from kivy.lang import Builder
from kivy.properties import StringProperty 
import mplcyberpunk
from qbstyles import mpl_style
import pickle
from kivy.uix.spinner import Spinner
from kivy.base import runTouchApp
from kivy.clock import Clock
import numpy as np




                                                                        #At the bottom of the file is the Problem 



class MainWindow(Screen,object):


    def Allgemeinepunkte(self, *args):
        print("nice")
        self.manager.get_screen("main").ids.Graph.clear_widgets()
        global Alist 
        with open ('Allgemein.txt', 'r') as m:
            Alist = m.read().splitlines()

        Alist = [int(item) for item in Alist]


        AAnzahlNoten = []
        x = 0
        for i in Alist:
            
            AAnzahlNoten.append(x+1)
            x = x+1 

        plt.clf()
        plt.gcf() 
        plt.plot(AAnzahlNoten,Alist)
        plt.tight_layout() 
        self.manager.get_screen('main').ids.Graph.add_widget(FigureCanvasKivyAgg(plt.gcf()))


    def Durchschnitt(self):
        AlleNoten = 0
        x = 0
        for i in Alist:
            AlleNoten = AlleNoten + 1
            x = x + i



        Durchschnitt = x / AlleNoten
        durch = str(round(Durchschnitt, 2)) 
        self.manager.get_screen('main').ids.ds.text = "⌀" + durch  
  


    def btn(self):
        with open (Fach +'.txt', 'r') as m:
            list = m.read().splitlines()
            
        if not list == "":
            list = [int(item) for item in list]

            
            global AnzahlNoten
            AnzahlNoten = []
            x = 0

            for i in list:
                AnzahlNoten.append(x+1)
                x = x+1



            mpl_style()
            plt.clf()
            plt.gcf()
            plt.plot(AnzahlNoten,list, color="purple", marker= ".")
            self.manager.get_screen("mathe").ids.box.add_widget(FigureCanvasKivyAgg(plt.gcf()))



    def Fachdurchschnitt(self):
        with open (Fach + '.txt', 'r') as m:
            list = m.read().splitlines()

        list = [int(item) for item in list]

        Fachdu = list
        global strfachdu
        strfachdu = "" 
        NA = 0
        for i in Fachdu: 
                if NA < 10:
                    NA = NA + 1
                    strfachdu = strfachdu + str(i)+"\n     "

        x = SecondWindow.FachPunkte(self)



    def Mathe (self):
        global Fach 
        Fach = "mathe"

    def Physik (self):
        global Fach 
        Fach = "physik"



class SecondWindow(Screen,object):
    durchschnittfach = ObjectProperty(None)
    global Fach
    global Punkte
    global list
    global AnzahlNoten
    global ArtTest
    global ArtenDictionary
    ArtenDictionary = { "mathe":{}, "physik":{} }                               # Brauche dringend eine Lösung muss jedes Fach per Hand Eintragen
    global ArtenList
    ArtenList = []
    global TeilerDictionary
    TeilerDictionary = {}
    


    def mathe(self):
        global Punkte
        global Zahl
        Punkte = None
        Zahl = self.durchschnittfach.text   

        if  Zahl == "15" or Zahl == "15" or Zahl == "14" or Zahl == "13" or Zahl == "12" or Zahl == "11" or Zahl == "10" or Zahl == "9" or Zahl == "8" or Zahl == "7" or Zahl == "6" or Zahl == "5" or Zahl == "4" or Zahl == "3" or Zahl == "2" or Zahl == "1":

            Punkte = int(Zahl)
            self.durchschnittfach.text = ""


            ArtNote = self.auswahlNote.text
            with open( Fach + '.txt','a') as m:
                m.write(''.join([str(Punkte)]))
                m.write('\n')
        

            with open (Fach + '.txt', 'r') as m:
                list = m.read().splitlines()
            list = [int(item) for item in list]
            


            AnzahlNoten = []
            x = 0
            for i in list:
                AnzahlNoten.append(x+1)
                x = x+1 



            with open( Fach + ArtNote +'.txt','a') as m:
                m.write("".join([str(Punkte)]))
                m.write('\n')



            Test = 20 
            Klassenarbeit = 90                                              #Vorrübergehende lösung speichert die Prozente zu welchen gezählt wird wird zusammengefasst in TeilerDictionary



            with open (Fach + ArtNote + '.txt', 'r') as m:
                listn = m.read().splitlines()
            listn = [int(item) for item in listn]



            NotenDerArt = 0
            AnzahlNotenDerArt = 0
            for i in listn:
                AnzahlNotenDerArt = AnzahlNotenDerArt + 1
                NotenDerArt = NotenDerArt + i
            
            ArtDurchschnitt = ( NotenDerArt / AnzahlNotenDerArt ) * eval(ArtNote)


            with open( Fach + ArtNote + 'Du.txt','a') as m:
                m.write(str(ArtDurchschnitt))

            open (Fach + "Arten.txt","a")
            
            with open (Fach + "Arten.txt","r") as m:
                ArtenList = m.read().splitlines()
                print(ArtenList)




            if not ArtNote in ArtenList:
                ArtenList.append(ArtNote)
                with open(Fach + "Arten.txt","a") as m:
                    m.write(ArtNote + "\n")
            print(ArtenList)

            open (Fach + "ArtenDictionary.pkl", "a")


            try:
                with open(Fach + "ArtenDictionary.pkl", 'rb') as f:             # Brauche eine Überprüfung ob leer weil sonst crasht er einfach
                    ArtenDictionary = pickle.load(f)
                    print(ArtenDictionary)
            except EOFError:
                ArtenDictionary = { "mathe":{}, "physik":{} }                   #Eher Ungünstig aber sollte über eval(Fächer) Gehen......Hoffentlich   
    


            for Art in ArtenList:
                TeilerDictionary[Art] = eval(Art)
            Stringdenichbrauche = str(ArtNote)              
            ArtenDictionary[Fach][Stringdenichbrauche] = ArtDurchschnitt 
            print(ArtenDictionary)



            with open(Fach + "ArtenDictionary.pkl", 'wb') as f:
                pickle.dump(ArtenDictionary, f)
                print(ArtenDictionary)



            x = 0
            Endteiler = 0
            if ArtNote in ArtenList:             #Artenlist speichern ist die liste mit den arten der noten
                for i in ArtenList:
                    x =  TeilerDictionary[i]     #Teilerdictionyry speichert die werte der einzelnen arten wäre sinnvoll es zu speichern
                    Endteiler = Endteiler + x    #Endteiler speichern




            GesamtdurchTeiler = 0
            for Art in ArtenList: 
                GesamtdurchTeiler = GesamtdurchTeiler + ArtenDictionary[Fach][Art]
            DerFinaleFachDurchschnitt = GesamtdurchTeiler / Endteiler


            print(Endteiler,GesamtdurchTeiler,DerFinaleFachDurchschnitt) # Das Finale Ergebnis (Durchschnitt aller Noten mit richtiger Gewichtung als Durchschnitt)


            with open(Fach + "ArtVerlauf.txt", "a") as m: 
                m.write("".join(ArtNote + "\n"))


        else:
            print("du bist dumm")
            self.durchschnittfach.text = ""







    def Allgemein(self):
         
        if  Zahl == "15" or Zahl == "15" or Zahl == "14" or Zahl == "13" or Zahl == "12" or Zahl == "11" or Zahl == "10" or Zahl == "9" or Zahl == "8" or Zahl == "7" or Zahl == "6" or Zahl == "5" or Zahl == "4" or Zahl == "3" or Zahl == "2" or Zahl == "1":
            with open('Allgemein.txt','a') as m:
                m.write(''.join([str(Punkte)]))
                m.write('\n')
            
        else:
            print("du bist behindert")





    def delete(self):
        with open (Fach + '.txt', 'r') as m:
            AlleFachNoten = m.read().splitlines()     
        with open (Fach + 'ArtVerlauf.txt', 'r') as m:
            ArtVerlauf = m.read().splitlines()



        if not ArtVerlauf == []:
            DArt = ArtVerlauf.pop()

            with open (Fach + 'ArtVerlauf.txt', 'w') as m:
                for i in ArtVerlauf:
                    m.write(str(i) + "\n")

            with open (Fach + DArt + '.txt', 'r') as m:
                RichtigeArtNotenListe = m.read().splitlines()
                if not RichtigeArtNotenListe == []:
                    Deleted = RichtigeArtNotenListe.pop()

                with open (Fach + DArt + '.txt', 'w') as m:    
                        for i in RichtigeArtNotenListe:
                            m.write(i + "\n")


                with open(Fach + ".txt", "r") as m:
                    AlleNoten = m.read().splitlines()
                    EineNoteWeg = AlleNoten.pop()

                with open(Fach + ".txt", "w") as m:
                    for i in AlleNoten:
                        m.write(str(i) + "\n")


        else:
            print("stupid")

        z = SecondWindow.clear(self)
        x = MainWindow.Fachdurchschnitt(self)
        y = MainWindow.btn(self)
        






    def FachPunkte(self):
        self.manager.get_screen("mathe").ids.fachverlauf.text = "Verlauf: \n     " + strfachdu


    def ArtNoten(self):
        global ArtNoten
        ArtNote = self.auswahlNote.text



    def clear(self):
        self.manager.get_screen('mathe').ids.box.clear_widgets()

    def call(self):
        x = MainWindow.btn(self)

    def createmaingraph(self):
        x = MainWindow.Allgemeinepunkte(self)
    
    def calldurchschnitt(self):
        x = MainWindow.Durchschnitt(self)
    
    def callFachdurchschnitt(self):
        X = MainWindow.Fachdurchschnitt(self)
    

class WindowManager(ScreenManager):
    pass


class MyMainApp(App):
    def build(self):
        Window.clearcolor = (0.08,0.12,0.17,1)
        kv = Builder.load_file("my.kv")
        return kv

    def on_start(self, **kwargs):
        mw = MainWindow()
        #mw.Allgemeinepunkte()     Uncomment this line if you want to test whats wrong!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


if __name__ == "__main__":
    app = MyMainApp()
    app.run()   

