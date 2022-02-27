from ast import Index, excepthandler
from logging import root
from sys import path
from tkinter import Image
from data import *

import datetime
import time
from pathlib import Path
import os
import webbrowser

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from kivy.uix.modalview import ModalView
from KivyCalendar import CalendarWidget
from KivyCalendar import DatePicker
from kivy.uix.button import Button
from kivy.uix.behaviors.focus import FocusBehavior
from kivy.properties import BooleanProperty
from kivy.properties import NumericProperty
from kivy.clock import Clock
from kivy.factory import Factory

Builder.load_file('layout.kv')
Window.size = (1200, 900)
Window.minimum_width, Window.minimum_height = Window.size
Window.top = 100
Window.left = 400

# Class with content of main app (with themepark map)

class Mainscreen(Widget):

    day = StringProperty("")
    date = StringProperty("")
    clock_time = StringProperty("")
    openinghours = StringProperty("")
    Img_openinghours = StringProperty("")

    total_malfunction = ObjectProperty("")
    total_off = ObjectProperty("")
    total_morningcheck = ObjectProperty("")
    total_running = ObjectProperty("") 
    total_on_park = ObjectProperty("") 

    attr1_icon = ObjectProperty("")
    attr2_icon = ObjectProperty("")
    attr3_icon = ObjectProperty("")
    attr4_icon = ObjectProperty("")
    attr5_icon = ObjectProperty("")
    attr6_icon = ObjectProperty("")
    attr7_icon = ObjectProperty("")
    attr8_icon = ObjectProperty("")
    attr9_icon = ObjectProperty("")
    attr10_icon = ObjectProperty("")
    attr11_icon = ObjectProperty("")
    attr12_icon = ObjectProperty("")
    attr13_icon = ObjectProperty("")
    attr14_icon = ObjectProperty("")
    attr15_icon = ObjectProperty("")
    attr16_icon = ObjectProperty("")
    attr17_icon = ObjectProperty("")
    attr18_icon = ObjectProperty("")
    attr19_icon = ObjectProperty("")
    attr20_icon = ObjectProperty("")
    attr21_icon = ObjectProperty("")
    attr22_icon = ObjectProperty("")
    attr23_icon = ObjectProperty("")
    attr24_icon = ObjectProperty("")
    attr25_icon = ObjectProperty("")
    attr26_icon = ObjectProperty("")
    attr27_icon = ObjectProperty("")
    attr28_icon = ObjectProperty("")


    attr1_status = ObjectProperty("")
    attr2_status = ObjectProperty("")
    attr3_status = ObjectProperty("")
    attr4_status = ObjectProperty("")
    attr5_status = ObjectProperty("")
    attr6_status = ObjectProperty("")
    attr7_status = ObjectProperty("")
    attr8_status = ObjectProperty("")
    attr9_status = ObjectProperty("")
    attr10_status = ObjectProperty("")
    attr11_status = ObjectProperty("")
    attr12_status = ObjectProperty("")
    attr13_status = ObjectProperty("")
    attr14_status = ObjectProperty("")
    attr15_status = ObjectProperty("")
    attr16_status = ObjectProperty("")
    attr17_status = ObjectProperty("")
    attr18_status = ObjectProperty("")
    attr19_status = ObjectProperty("")
    attr20_status = ObjectProperty("")
    attr21_status = ObjectProperty("")
    attr22_status = ObjectProperty("")
    attr23_status = ObjectProperty("")
    attr24_status = ObjectProperty("")
    attr25_status = ObjectProperty("")
    attr26_status = ObjectProperty("")
    attr27_status = ObjectProperty("")
    attr28_status = ObjectProperty("")

    attr1_test1 = ObjectProperty("")
    attr2_test1 = ObjectProperty("")
    attr3_test1 = ObjectProperty("")
    attr4_test1 = ObjectProperty("")
    attr5_test1 = ObjectProperty("")
    attr6_test1 = ObjectProperty("")
    attr7_test1 = ObjectProperty("")
    attr8_test1 = ObjectProperty("")
    attr9_test1 = ObjectProperty("")
    attr10_test1 = ObjectProperty("")
    attr11_test1 = ObjectProperty("")
    attr12_test1 = ObjectProperty("")
    attr13_test1 = ObjectProperty("")
    attr14_test1 = ObjectProperty("")
    attr15_test1 = ObjectProperty("")
    attr16_test1 = ObjectProperty("")
    attr17_test1 = ObjectProperty("")
    attr18_test1 = ObjectProperty("")
    attr19_test1 = ObjectProperty("")
    attr20_test1 = ObjectProperty("")
    attr21_test1 = ObjectProperty("")
    attr22_test1 = ObjectProperty("")
    attr23_test1 = ObjectProperty("")
    attr24_test1 = ObjectProperty("")
    attr25_test1 = ObjectProperty("")
    attr26_test1 = ObjectProperty("")
    attr27_test1 = ObjectProperty("")
    attr28_test1 = ObjectProperty("")

    attr1_test2 = ObjectProperty("")
    attr2_test2 = ObjectProperty("")
    attr3_test2 = ObjectProperty("")
    attr4_test2 = ObjectProperty("")
    attr5_test2 = ObjectProperty("")
    attr6_test2 = ObjectProperty("")
    attr7_test2 = ObjectProperty("")
    attr8_test2 = ObjectProperty("")
    attr9_test2 = ObjectProperty("")
    attr10_test2 = ObjectProperty("")
    attr11_test2 = ObjectProperty("")
    attr12_test2 = ObjectProperty("")
    attr13_test2 = ObjectProperty("")
    attr14_test2 = ObjectProperty("")
    attr15_test2 = ObjectProperty("")
    attr16_test2 = ObjectProperty("")
    attr17_test2 = ObjectProperty("")
    attr18_test2 = ObjectProperty("")
    attr19_test2 = ObjectProperty("")
    attr20_test2 = ObjectProperty("")
    attr21_test2 = ObjectProperty("")
    attr22_test2 = ObjectProperty("")
    attr23_test2 = ObjectProperty("")
    attr24_test2 = ObjectProperty("")
    attr25_test2 = ObjectProperty("")
    attr26_test2 = ObjectProperty("")
    attr27_test2 = ObjectProperty("")
    attr28_test2 = ObjectProperty("")

    attr1_maintance1 = ObjectProperty("")
    attr2_maintance1 = ObjectProperty("")
    attr3_maintance1 = ObjectProperty("")
    attr4_maintance1 = ObjectProperty("")
    attr5_maintance1 = ObjectProperty("")
    attr6_maintance1 = ObjectProperty("")
    attr7_maintance1 = ObjectProperty("")
    attr8_maintance1 = ObjectProperty("")
    attr9_maintance1 = ObjectProperty("")
    attr10_maintance1 = ObjectProperty("")
    attr11_maintance1 = ObjectProperty("")
    attr12_maintance1 = ObjectProperty("")
    attr13_maintance1 = ObjectProperty("")
    attr14_maintance1 = ObjectProperty("")
    attr15_maintance1 = ObjectProperty("")
    attr16_maintance1 = ObjectProperty("")
    attr17_maintance1 = ObjectProperty("")
    attr18_maintance1 = ObjectProperty("")
    attr19_maintance1 = ObjectProperty("")
    attr20_maintance1 = ObjectProperty("")
    attr21_maintance1 = ObjectProperty("")
    attr22_maintance1 = ObjectProperty("")
    attr23_maintance1 = ObjectProperty("")
    attr24_maintance1 = ObjectProperty("")
    attr25_maintance1 = ObjectProperty("")
    attr26_maintance1 = ObjectProperty("")
    attr27_maintance1 = ObjectProperty("")
    attr28_maintance1 = ObjectProperty("")

    attr1_maintance2 = ObjectProperty("")
    attr2_maintance2 = ObjectProperty("")
    attr3_maintance2 = ObjectProperty("")
    attr4_maintance2 = ObjectProperty("")
    attr5_maintance2 = ObjectProperty("")
    attr6_maintance2 = ObjectProperty("")
    attr7_maintance2 = ObjectProperty("")
    attr8_maintance2 = ObjectProperty("")
    attr9_maintance2 = ObjectProperty("")
    attr10_maintance2 = ObjectProperty("")
    attr11_maintance2 = ObjectProperty("")
    attr12_maintance2 = ObjectProperty("")
    attr13_maintance2 = ObjectProperty("")
    attr14_maintance2 = ObjectProperty("")
    attr15_maintance2 = ObjectProperty("")
    attr16_maintance2 = ObjectProperty("")
    attr17_maintance2 = ObjectProperty("")
    attr18_maintance2 = ObjectProperty("")
    attr19_maintance2 = ObjectProperty("")
    attr20_maintance2 = ObjectProperty("")
    attr21_maintance2 = ObjectProperty("")
    attr22_maintance2 = ObjectProperty("")
    attr23_maintance2 = ObjectProperty("")
    attr24_maintance2 = ObjectProperty("")
    attr25_maintance2 = ObjectProperty("")
    attr26_maintance2 = ObjectProperty("")
    attr27_maintance2 = ObjectProperty("")
    attr28_maintance2 = ObjectProperty("")

    # Properties to determine hovercolor and -outline for attractionbuttons (in data.py)

    hover_color = StringProperty(hover_color)
    hover_outline = StringProperty(hover_outline)

    # Input attraction objects

    attraction1 = Carrousel("attraction1", "Adderrad", "Reuzenrad", 
                            "Photos/Adderrad_foto.jpg", "704765473", "2012", vekoma,
                            maintance_adm1, "2", "1", "15", "4", "16", "64", "590", 
                            "75 m", "1 km/u", "6:00 min", "24 m", "100 cm", "Ketting", 
                            "100 kW", "nee")

    attraction2 = Rollercoaster("attraction2", "Anaconda", "Grote Achtbaan", 
                                "Photos/Anaconda_foto.jpg", "884739546", "2018", vekoma, 
                                maintance_adm2, "2", "4", "60", "28", "2", "56", "950", 
                                "750 m", "85 km/u", "2:08 min", "29 m", "130 cm", 
                                "Schouderbeugel", "120 kW", "3,6 g", "4", "ja")
    
    attraction3 = Playground("attraction3", "Ballenzee", "Ballenbak", 
                             "Photos/Ballenzee_foto.jpg", "621476498", "2011", eliplay, 
                             maintance_adm3, "2", "1", "15", "30", "1", "30", "0m", 
                             "90 cm")
    
    attraction4 = SpinPuke("attraction4", "Basket Drop", "Vrije val Attractie", 
                           "Photos/Basket_Drop_foto.jpg", "802375843", "2014", 
                           hussparkattractions, maintance_adm4, "2", "2", "30", "3", 
                           "4", "12", "360", "40 m", "50 km/u", "0:50 min", "50 m", 
                           "120 cm", "Schouderbeugel", "160 kW", "nee")

    attraction5 = SpinPuke("attraction5", "Black Mamba", "Breakdance", 
                           "Photos/Black_Mamba_foto.jpg", "295746374", "1990", 
                           hussparkattractions, maintance_adm5, "2", "2", "30", "2", "16", 
                           "32", "548", "42 m", "30 km/u", "2:00 min", "0 m", "120 cm", 
                           "Heupbeugel", "120 kW", "nee")
    
    attraction6 = SpinPuke("attraction6", "Cobra", "Calypso", "Photos/Cobra_foto.jpg", 
                           "284573850", "1981", krekel, maintance_adm6, "2", "2", "30",
                           "2", "12", "24", "410", "48 m", "24 km/u", "2:30 min", "0 m", 
                           "120 cm", "Heupbeugel", "45 kW", "nee")
    
    attraction7 = Carrousel("attraction7", "Graaf Slis", "Draaimolen", 
                            "Photos/Graaf_Slis_foto.jpg", "372890462", "1994", wooddesign, 
                            maintance_adm7, "2", "1", "15", "divers", "20", "28", "480", 
                            "30 m", "8 km/u", "2:30 min", "0 m", "90 cm", "Geen", "12 kW", 
                            "nee")
    
    attraction8 = Carrousel("attraction8", "Happy Ajar", "Luchtballonnencarrousel", 
                            "Photos/Happy_Ajar_foto.jpg", "904637823", "2019", wooddesign, 
                            maintance_adm8, "2", "1", "15", "4", "8", "32", "548", 
                            "32 m", "6 km/u", "2:30 min", "8 m", "90 cm", "Ketting", 
                            "18 kW", "nee")
    
    attraction9 = Playground("attraction9", "Jumpy XL", "Trampolines", 
                             "Photos/Jumpy_XL_foto.jpg", "621856785", "2011", hajump, 
                             maintance_adm9, "2", "1", "15", "2", "12", "24", "1 m", 
                             "90 cm")

    attraction10 = WaterRide("attraction10", "Jungle Book", "Tow boat Ride", 
                             "Photos/Jungle_Book_foto.jpg", "795647329", "2014", mackrides, 
                             maintance_adm10, "2", "2", "30", "16", "14", "224", "1800", 
                             "285  m", "2 km/u", "8:00 min", "0 m", "120 cm", "120 kW", "nee")
    
    attraction11 = Transport("attraction11", "Kaa trein", "Locomotief", 
                             "Photos/Kaa-trein_foto.jpg", "629887436", "2011", vekoma, 
                             maintance_adm11, "2", "1", "15", "2", "36", "72", "480", 
                             "800 m", "6 km/u", "8:00 min", "0 m", "100 cm", "0 kW", "nee")
    
    attraction12 = Playground("attraction12", "Medusa", "Indoor Speeltuin", 
                             "Photos/Medusa_foto.jpg", "629984632", "2011", eliplay, 
                             maintance_adm12, "2", "1", "15", "40", "1", "40", "3 m", 
                             "90 cm")
    
    attraction13 = Playground("attraction13", "Niagara Roetsj", "Superglijbaan", 
                             "Photos/Niagara_Roetsj_foto.jpg", "627749328", "2011", vanegdom, 
                             maintance_adm13, "2", "1", "15", "1", "8", "8", "14 m", 
                             "90 cm")
    
    attraction14 = Carrousel("attraction14", "Paradijsslang", "Red Baron", 
                            "Photos/Paradijsslang_foto.jpg", "593743299", "1999", 
                            hussparkattractions, maintance_adm14, "2", "1", "15", "2",
                            "16", "32", "548", "42 m", "12 km/u", "2:30 min", "4 m", 
                            "90 cm", "Heupbeugel", "30 kW", "nee")

    attraction15 = SpinPuke("attraction15", "Pie Piraat", "Schommelschip", 
                            "Photos/Pie_Piraat_foto.jpg", "628465443", "2001", 
                            hussparkattractions, maintance_adm15, "2", "1", "15", "54", 
                            "1", "54", "1080", "36 m", "32 km/u", "2:30 min", "20 m", 
                            "120 cm", "Heupbeugel", "75 kW", "nee")
    
    attraction16 = SpinPuke("attraction16", "Pulpo", "Polyp", 
                            "Photos/Pulpo_foto.jpg", "327569214", "1992", 
                            schwarzkopf, maintance_adm16, "2", "2", "30", "2", "30", 
                            "60", "900", "60 m", "32 km/u", "3:00 min", "4 m", "120 cm", 
                            "Heupbeugel", "110 kW", "nee")
    
    attraction17 = Rollercoaster("attraction17", "Python", "Familie Achtbaan", 
                                "Photos/Python_foto.jpg", "628473674", "2011", gerstlauer, 
                                maintance_adm17, "2", "4", "60", "24", "3", "72", "1600", 
                                "643 m", "65 km/u", "1:31 min", "20 m", "120 cm", 
                                "Heupbeugel", "100 kW", "3,5 g", "0", "ja")
    
    attraction18 = Rollercoaster("attraction18", "Ratelslang", "Kinder Achtbaan", 
                                 "Photos/Ratelslang_foto.jpg", "728364758", "2012", zierer, 
                                 maintance_adm18, "2", "3", "45", "20", "2", "40", "1250", 
                                 "360 m", "36 km/u", "1:10 min", "8 m", "100 cm", 
                                 "Heupbeugel", "80 kW", "1,8 g", "0", "nee")
    
    attraction19 = Transport("attraction19", "Safari Jeeps", "Rondrit", 
                             "Photos/Safari_Jeeps_foto.jpg", "639841232", "2011", 
                             metallbauemmeln, maintance_adm19, "2", "1", "15", "2", "10", 
                             "20", "350", "300 m", "6 km/u", "3:00 min", "0 m", "100 cm", 
                             "60 kW", "nee")

    attraction20 = Carrousel("attraction20", "Sahara Swing", "Zweefmolen", 
                             "Photos/Sahara_Swing_foto.jpg", "492363741", "1998",
                             wooddesign, maintance_adm20, "2", "1", "15", "1", "48", 
                             "48", "800", "45 m", "16 km/u", "2:30 min", "6 m", "120 cm", 
                             "Ketting", "20 kW", "nee")
    
    attraction21 = Playground("attraction21", "De Slangenkuil", "Doolhof", 
                             "Photos/De_Slangenkuil_foto.jpg", "627483290", "2011", 
                             donkergroen, maintance_adm21, "2", "4", "15", "60", "1", "60",
                             "14 m", "90 cm")
    
    attraction22 = SpinPuke("attraction22", "Snakebite", "Frisbee", 
                            "Photos/Snakebite_foto.jpg", "846281291", "2018", kmg, 
                            maintance_adm22, "2", "2", "30", "40", "1", "40", "600", "62 m", 
                            "65 km/u", "3:00 min", "20 m", "140 cm", "Schouderbeugel", 
                            "180 kW", "nee")
    
    attraction23 = Carrousel("attraction23", "Snake Charmer", "Theekopjescarrousel", 
                             "Photos/Snake_Charmer_foto.jpg", "338562973", "1992",
                             mackrides, maintance_adm23, "2", "1", "15", "4", "12", "48", 
                             "820", "30 m", "15 km/u", "2:30 min", "0 m", "110 cm", 
                             "Heupbeugel", "10 kW", "nee")
    
    attraction24 = WaterRide("attraction24", "Snaky Rivers", "Wildwaterbaan", 
                             "Photos/Snaky_Rivers_foto.jpg", "714632734", "2012", reverchon, 
                             maintance_adm24, "2", "3", "45", "5", "14", "70", "1250", 
                             "524 m", "50 km/u", "3:30 min", "23 m", "120 cm", "160 kW", "ja")
    
    attraction25 = Transport("attraction25", "Spookhuis", "Dark Ride", 
                             "Photos/Spookhuis_foto.jpg", "719456435", "2012", kumbak, 
                             maintance_adm25, "2", "2", "30", "6", "10", "60", "560", "190 m", 
                             "3 km/u", "6:00 min", "0 m", "120 cm", "80 kW", "ja")
    
    attraction26 = WaterRide("attraction26", "Swamp Trouble", "Botsbootjes", 
                             "Photos/Swamp_Trouble_foto.jpg", "629583675", "2011", barcachoc, 
                             maintance_adm26, "2", "1", "15", "2", "16", "32", "480", "vrij", 
                             "6 km/u", "3:00 min", "0 m", "120 cm", "2 kW", "nee")
    
    attraction27 = WaterRide("attraction27", "The Amazone", "Rapid River", 
                             "Photos/The_Amazone_foto.jpg", "816483647", "2015", vekoma, 
                             maintance_adm27, "2", "4", "60", "4", "45", "180", "2000", "350 m", 
                             "20 km/u", "5:00 min", "3 m", "120 cm", "300 kW", "ja")
    
    attraction28 = SpinPuke("attraction28", "Vipers", "Botsauto's", "Photos/Vipers_foto.jpg", 
                            "602367543", "2005", bumpercars, maintance_adm28, "2", "1", "15", 
                            "2", "20", "40", "690", "vrij", "12 km/u", "3:00 min", "0 m", 
                            "140 cm", "Autogordel", "100 kW", "nee")
    
    # Function to resize screen by clicking to right aspect ratios (4:3)

    def on_touch_up(self, touch):

        Window.size = (Window.height/3 * 4, Window.height)

    # Function to show time

    def clock(self, *args):   

        date_now = datetime.datetime.now()

        self.day = datetime.datetime.now().strftime("%A")
        self.date = date_now.strftime("%d") + "/" + date_now.strftime("%m") + "/" + date_now.strftime("%Y")
        self.clock_time = date_now.strftime("%H") + ":" + date_now.strftime("%M") 
        
    # Function to show if themepark is open or not

    def closed_open(self, *args):

        hour = datetime.datetime.now().strftime("%H")
        hour = int(hour)

        weekdays = [Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday]
        day_index = int(datetime.datetime.now().strftime("%w"))
        day_now = weekdays[day_index]
        

        if  day_now.open == "closed" or hour < day_now.open or hour >= day_now.closed:

           self.openinghours = "Closed"
           self.Img_openinghours = 'Img/Red.jpg'
        
        else:
            self.openinghours = "Open"
            self.Img_openinghours = 'Img/Green.jpg'

    # Function to put a running attraction back on off when a new day occurs

    def check_newday(self):  

        date_now = datetime.datetime.now()
        date_now = date_now.strftime("%d") + "/" + date_now.strftime("%m") + "/" + date_now.strftime("%Y")

        folderpath = r'Database/Lists/Running'
        filepaths  = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]

        for path in filepaths:

            with open(path, 'r') as f:
                file = f.read().splitlines()
                date = file[1]
                name = file[0]
               
            if date != date_now:
                with open('Database/Lists/Off/' + name + '.txt' , 'w') as f:
                    f.write("")
                os.remove(path)
    
    # Function to update Malfunction info on unknown when there is no input given 
    # in case app closes with an error 

    def malfunction_unknown(self):

        folderpath = r'Database/Lists/Malfunction'
        filepaths  = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]

        for path in filepaths:

            f = open(path, 'r+')
            file = f.read().splitlines()
            
            try:
                info = file[2]

            except IndexError:
             
                f.write("Oorzaak Storing")
                f.write('\n')
                f.write('\n')
                f.write("Onbekend")
            
            f.close()

    # Function to update statuslight of an attraction

    def update_light(self, attraction, light):

        if Path('Database/Lists/Malfunction/' + attraction + '.txt').is_file():
            light.source = 'Img/status_red.jpg'
        
        elif Path('Database/Lists/Morningcheck/' + attraction + '.txt').is_file():
            light.source = 'Img/status_yellow.jpg'
        
        elif Path('Database/Lists/Running/' + attraction + '.txt').is_file():
            light.source = 'Img/status_green.jpg'
        
        else: 
            light.source = 'Img/status_orange.jpg'
    
    # Function to warn that maintance is upcoming with a yellow sign
    
    def signal_maintance_yellow(self, attraction, signal): 

        signal.source = 'Img/maintance_no.jpg'

        date_now = datetime.datetime.now()
        date_now = date_now.strftime("%d") + "/" + date_now.strftime("%m") + "/" + date_now.strftime("%Y")

        d6 = datetime.timedelta(days=0)
        d7 = datetime.timedelta(days= warn_maintance)

        try:

            with open(attraction.adm_maintance.maintance_1, "r") as f:
                file = f.read().splitlines()
                date1 = file[0]
                check1 = file[1]
             
            d1 = datetime.datetime.strptime(date_now, "%d/%m/%Y").date()
            d2 = datetime.datetime.strptime(date1, "%d/%m/%Y").date()
        
            if check1 == "Planned" and d2 - d1 > d6 and d2 - d1 < d7:
                signal.source = 'Img/maintance_yellow.jpg'
            
            else:
                pass


        except IndexError:
            
            pass
    
        try:

            with open(attraction.adm_maintance.maintance_2, "r") as f:
                file = f.read().splitlines()
                date2 = file[0]
                check2 = file[1]
                
             
            d1 = datetime.datetime.strptime(date_now, "%d/%m/%Y").date()
            d3 = datetime.datetime.strptime(date2, "%d/%m/%Y").date()
        
            if check2 == "Planned" and d3 - d1 > d6 and d3 - d1 < d7:
                signal.source = 'Img/maintance_yellow.jpg'
            
            else:
                pass

        except IndexError:
            
            pass
        
        try:

            with open(attraction.adm_maintance.maintance_3, "r") as f:
                file = f.read().splitlines()
                date3 = file[0]
                check3 = file[1]
                
             
            d1 = datetime.datetime.strptime(date_now, "%d/%m/%Y").date()
            d4 = datetime.datetime.strptime(date3, "%d/%m/%Y").date()
        
            if check3 == "Planned" and d4 - d1 > d6 and d4 - d1 < d7:
                signal.source = 'Img/maintance_yellow.jpg'
            
            else:
                pass

        except IndexError:
            
            pass
        
        try:

            with open(attraction.adm_maintance.maintance_4, "r") as f:
                file = f.read().splitlines()
                date4 = file[0]
                check4 = file[1]
                
             
            d1 = datetime.datetime.strptime(date_now, "%d/%m/%Y").date()
            d5 = datetime.datetime.strptime(date4, "%d/%m/%Y").date()
        
            if check4 == "Planned" and d5 - d1 > d6 and d5 - d1 < d7:
                signal.source = 'Img/maintance_yellow.jpg'
            
            else:
                pass

        except IndexError:
            
            pass
    
    # Function to warn that maintance is forgotten sign or that there's no input with a red sign
    # or update to a green light when maintance is in progress

    def signal_maintance_red(self, attraction, signal): 

        try:

            with open('Database/Lists/Malfunction/' + attraction.adm_maintance.attractionstring + '.txt', "r") as f:
                file = f.read().splitlines()
                info = file[2]

                if info == "Groot Onderhoud":
                    signal.source = 'Img/maintance_green.jpg'
                    
                else:
                
                    try:

                        with open(attraction.adm_maintance.maintance_1, "r") as f:
                            file = f.read().splitlines()
                            date1 = file[0]
                            check1 = file[1]
                        
                        with open(attraction.adm_maintance.maintance_2, "r") as f:
                            file = f.read().splitlines()
                            date2 = file[0]
                            check2 = file[1]
                        
                        with open(attraction.adm_maintance.maintance_3, "r") as f:
                            file = f.read().splitlines()
                            date3 = file[0]
                            check3 = file[1]
                        
                        with open(attraction.adm_maintance.maintance_4, "r") as f:
                            file = f.read().splitlines()
                            date4 = file[0]
                            check4 = file[1]
                    
                        date_now = datetime.datetime.now()
                        date_now = date_now.strftime("%d") + "/" + date_now.strftime("%m") + "/" + date_now.strftime("%Y")
                            
                        d1 = datetime.datetime.strptime(date_now, "%d/%m/%Y").date()
                        d2 = datetime.datetime.strptime(date1, "%d/%m/%Y").date()
                        d3 = datetime.datetime.strptime(date2, "%d/%m/%Y").date()
                        d4 = datetime.datetime.strptime(date3, "%d/%m/%Y").date()
                        d5 = datetime.datetime.strptime(date4, "%d/%m/%Y").date()
                
                        if check1 == "Planned" and d1 >= d2: 
                            
                            signal.source = 'Img/maintance_red.jpg'
                                        
                        elif check2 == "Planned" and d1 >= d3:

                            signal.source = 'Img/maintance_red.jpg'
                                
                        elif check3 == "Planned" and d1 >= d4:

                            signal.source = 'Img/maintance_red.jpg'
                                    
                        elif check4 == "Planned" and d1 >= d5:
                                        
                            signal.source = 'Img/maintance_red.jpg'
                                        
                        else:
                            signal.source = 'Img/maintance_no.jpg'
                    
                    except IndexError:
                    
                        signal.source = 'Img/maintance_red.jpg'
            
        except FileNotFoundError:

            try:

                with open(attraction.adm_maintance.maintance_1, "r") as f:
                    file = f.read().splitlines()
                    date1 = file[0]
                    check1 = file[1]
                
                with open(attraction.adm_maintance.maintance_2, "r") as f:
                    file = f.read().splitlines()
                    date2 = file[0]
                    check2 = file[1]
                
                with open(attraction.adm_maintance.maintance_3, "r") as f:
                    file = f.read().splitlines()
                    date3 = file[0]
                    check3 = file[1]
                
                with open(attraction.adm_maintance.maintance_4, "r") as f:
                    file = f.read().splitlines()
                    date4 = file[0]
                    check4 = file[1]
            
                date_now = datetime.datetime.now()
                date_now = date_now.strftime("%d") + "/" + date_now.strftime("%m") + "/" + date_now.strftime("%Y")
                    
                d1 = datetime.datetime.strptime(date_now, "%d/%m/%Y").date()
                d2 = datetime.datetime.strptime(date1, "%d/%m/%Y").date()
                d3 = datetime.datetime.strptime(date2, "%d/%m/%Y").date()
                d4 = datetime.datetime.strptime(date3, "%d/%m/%Y").date()
                d5 = datetime.datetime.strptime(date4, "%d/%m/%Y").date()
        
                if check1 == "Planned" and d1 >= d2: 
                    
                    signal.source = 'Img/maintance_red.jpg'
                                
                elif check2 == "Planned" and d1 >= d3:

                    signal.source = 'Img/maintance_red.jpg'
                        
                elif check3 == "Planned" and d1 >= d4:

                    signal.source = 'Img/maintance_red.jpg'
                            
                elif check4 == "Planned" and d1 >= d5:
                                
                    signal.source = 'Img/maintance_red.jpg'
                                
                else:
                    signal.source = 'Img/maintance_no.jpg'
            
            except IndexError:
                
                signal.source = 'Img/maintance_red.jpg'
    
    # Function to warn that a test is upcoming with a yellow sign
    
    def signal_test_yellow(self, attraction, signal):

        signal.source = 'Img/test_no.jpg'

        date_now = datetime.datetime.now()
        date_now = date_now.strftime("%d") + "/" + date_now.strftime("%m") + "/" + date_now.strftime("%Y")

        d6 = datetime.timedelta(days=0)
        d7 = datetime.timedelta(days= warn_test)

        try:

            with open(attraction.adm_maintance.next_inspection, "r") as f:
                file = f.read().splitlines()
                date1 = file[0]
             
            d1 = datetime.datetime.strptime(date_now, "%d/%m/%Y").date()
            d2 = datetime.datetime.strptime(date1, "%d/%m/%Y").date()
        
            if d2 - d1 > d6 and d2 - d1 < d7:
                signal.source = 'Img/test_yellow.jpg'
            
            else:
                pass


        except IndexError:
            
            pass
    
    # Function to warn that a test is forgotten sign or that there's no input with a red sign
    # or update to a green light when test is in progress
    
    def signal_test_red(self, attraction, signal): 

        try:

            with open('Database/Lists/Malfunction/' + attraction.adm_maintance.attractionstring + '.txt', "r") as f:
                file = f.read().splitlines()
                info = file[2]

                if info == "Keuring":
                    signal.source = 'Img/test_green.jpg'
                    
                else:
                
                    try:

                        with open(attraction.adm_maintance.last_inspection, "r") as f:
                            file = f.read().splitlines()
                            date_last = file[0]
                            
                        
                        with open(attraction.adm_maintance.next_inspection, "r") as f:
                            file = f.read().splitlines()
                            date_next = file[0]
                    
                        date_now = datetime.datetime.now()
                        date_now = date_now.strftime("%d") + "/" + date_now.strftime("%m") + "/" + date_now.strftime("%Y")
                        date_expire = ((datetime.datetime.strptime(date_last, "%d/%m/%Y").date()) + 
                        (datetime.timedelta(days=(int(attraction.validity_rapport) * 365)))).strftime("%d/%m/%Y")
                            
                        d1 = datetime.datetime.strptime(date_now, "%d/%m/%Y").date()
                        d2 = datetime.datetime.strptime(date_last, "%d/%m/%Y").date()
                        d3 = datetime.datetime.strptime(date_next, "%d/%m/%Y").date()
                        d4 = datetime.datetime.strptime(date_expire, "%d/%m/%Y").date()
                
                        if d1 < d2:

                            signal.source = 'Img/test_red.jpg'

                        elif d1 >= d3: 
                            
                            signal.source = 'Img/test_red.jpg'
                                        
                        elif d1 > d4:

                            signal.source = 'Img/test_red.jpg'
                                        
                        else:
                            signal.source = 'Img/test_no.jpg'
                    
                    except IndexError:
                    
                        signal.source = 'Img/test_red.jpg'
            
        except FileNotFoundError:

            try:

                with open(attraction.adm_maintance.last_inspection, "r") as f:
                    file = f.read().splitlines()
                    date_last = file[0]
                    
                
                with open(attraction.adm_maintance.next_inspection, "r") as f:
                    file = f.read().splitlines()
                    date_next = file[0]
            
                date_now = datetime.datetime.now()
                date_now = date_now.strftime("%d") + "/" + date_now.strftime("%m") + "/" + date_now.strftime("%Y")
                date_expire = ((datetime.datetime.strptime(date_last, "%d/%m/%Y").date()) + 
                (datetime.timedelta(days=(int(attraction.validity_rapport) * 365)))).strftime("%d/%m/%Y")
                    
                d1 = datetime.datetime.strptime(date_now, "%d/%m/%Y").date()
                d2 = datetime.datetime.strptime(date_last, "%d/%m/%Y").date()
                d3 = datetime.datetime.strptime(date_next, "%d/%m/%Y").date()
                d4 = datetime.datetime.strptime(date_expire, "%d/%m/%Y").date()
        
                if d1 < d2:

                    signal.source = 'Img/test_red.jpg'

                elif d1 >= d3: 
                    
                    signal.source = 'Img/test_red.jpg'
                                
                elif d1 > d4:

                    signal.source = 'Img/test_red.jpg'
                                
                else:
                    signal.source = 'Img/test_no.jpg'
            
            except IndexError:
            
                signal.source = 'Img/test_red.jpg'
 
    # Function to count statuses of attractions and show them in mainscreen with warning signs

    def update_statuses(self):

        number_on_malfunction = len(os.listdir('Database/Lists/Malfunction'))
        number_on_off = len(os.listdir('Database/Lists/Off'))
        number_on_morningcheck = len(os.listdir('Database/Lists/Morningcheck'))
        number_on_running = len(os.listdir('Database/Lists/Running')) 
        number_on_park = number_on_malfunction + number_on_off + number_on_morningcheck + number_on_running

        self.total_malfunction.text = str(number_on_malfunction)  
        self.total_off.text = str(number_on_off)
        self.total_morningcheck.text = str(number_on_morningcheck)
        self.total_running.text = str(number_on_running) 
        self.total_on_park.text = str(number_on_park)

        self.update_light(self.attraction1.string, self.attr1_status)
        self.update_light(self.attraction2.string, self.attr2_status)
        self.update_light(self.attraction3.string, self.attr3_status)
        self.update_light(self.attraction4.string, self.attr4_status)
        self.update_light(self.attraction5.string, self.attr5_status)
        self.update_light(self.attraction6.string, self.attr6_status)
        self.update_light(self.attraction7.string, self.attr7_status)
        self.update_light(self.attraction8.string, self.attr8_status)
        self.update_light(self.attraction9.string, self.attr9_status)
        self.update_light(self.attraction10.string, self.attr10_status)
        self.update_light(self.attraction11.string, self.attr11_status)
        self.update_light(self.attraction12.string, self.attr12_status)
        self.update_light(self.attraction13.string, self.attr13_status)
        self.update_light(self.attraction14.string, self.attr14_status)
        self.update_light(self.attraction15.string, self.attr15_status)
        self.update_light(self.attraction16.string, self.attr16_status)
        self.update_light(self.attraction17.string, self.attr17_status)
        self.update_light(self.attraction18.string, self.attr18_status)
        self.update_light(self.attraction19.string, self.attr19_status)
        self.update_light(self.attraction20.string, self.attr20_status)
        self.update_light(self.attraction21.string, self.attr21_status)
        self.update_light(self.attraction22.string, self.attr22_status)
        self.update_light(self.attraction23.string, self.attr23_status)
        self.update_light(self.attraction24.string, self.attr24_status)
        self.update_light(self.attraction25.string, self.attr25_status)
        self.update_light(self.attraction26.string, self.attr26_status)
        self.update_light(self.attraction27.string, self.attr27_status)
        self.update_light(self.attraction28.string, self.attr28_status)

        self.signal_maintance_yellow(self.attraction1, self.attr1_maintance1)
        self.signal_maintance_yellow(self.attraction2, self.attr2_maintance1)
        self.signal_maintance_yellow(self.attraction3, self.attr3_maintance1)
        self.signal_maintance_yellow(self.attraction4, self.attr4_maintance1)
        self.signal_maintance_yellow(self.attraction5, self.attr5_maintance1)
        self.signal_maintance_yellow(self.attraction6, self.attr6_maintance1)
        self.signal_maintance_yellow(self.attraction7, self.attr7_maintance1)
        self.signal_maintance_yellow(self.attraction8, self.attr8_maintance1)
        self.signal_maintance_yellow(self.attraction9, self.attr9_maintance1)
        self.signal_maintance_yellow(self.attraction10, self.attr10_maintance1)
        self.signal_maintance_yellow(self.attraction11, self.attr11_maintance1)
        self.signal_maintance_yellow(self.attraction12, self.attr12_maintance1)
        self.signal_maintance_yellow(self.attraction13, self.attr13_maintance1)
        self.signal_maintance_yellow(self.attraction14, self.attr14_maintance1)
        self.signal_maintance_yellow(self.attraction15, self.attr15_maintance1)
        self.signal_maintance_yellow(self.attraction16, self.attr16_maintance1)
        self.signal_maintance_yellow(self.attraction17, self.attr17_maintance1)
        self.signal_maintance_yellow(self.attraction18, self.attr18_maintance1)
        self.signal_maintance_yellow(self.attraction19, self.attr19_maintance1)
        self.signal_maintance_yellow(self.attraction20, self.attr20_maintance1)
        self.signal_maintance_yellow(self.attraction21, self.attr21_maintance1)
        self.signal_maintance_yellow(self.attraction22, self.attr22_maintance1)
        self.signal_maintance_yellow(self.attraction23, self.attr23_maintance1)
        self.signal_maintance_yellow(self.attraction24, self.attr24_maintance1)
        self.signal_maintance_yellow(self.attraction25, self.attr25_maintance1)
        self.signal_maintance_yellow(self.attraction26, self.attr26_maintance1)
        self.signal_maintance_yellow(self.attraction27, self.attr27_maintance1)
        self.signal_maintance_yellow(self.attraction28, self.attr28_maintance1)

        self.signal_maintance_red(self.attraction1, self.attr1_maintance2)
        self.signal_maintance_red(self.attraction2, self.attr2_maintance2)
        self.signal_maintance_red(self.attraction3, self.attr3_maintance2)
        self.signal_maintance_red(self.attraction4, self.attr4_maintance2)
        self.signal_maintance_red(self.attraction5, self.attr5_maintance2)
        self.signal_maintance_red(self.attraction6, self.attr6_maintance2)
        self.signal_maintance_red(self.attraction7, self.attr7_maintance2)
        self.signal_maintance_red(self.attraction8, self.attr8_maintance2)
        self.signal_maintance_red(self.attraction9, self.attr9_maintance2)
        self.signal_maintance_red(self.attraction10, self.attr10_maintance2)
        self.signal_maintance_red(self.attraction11, self.attr11_maintance2)
        self.signal_maintance_red(self.attraction12, self.attr12_maintance2)
        self.signal_maintance_red(self.attraction13, self.attr13_maintance2)
        self.signal_maintance_red(self.attraction14, self.attr14_maintance2)
        self.signal_maintance_red(self.attraction15, self.attr15_maintance2)
        self.signal_maintance_red(self.attraction16, self.attr16_maintance2)
        self.signal_maintance_red(self.attraction17, self.attr17_maintance2)
        self.signal_maintance_red(self.attraction18, self.attr18_maintance2)
        self.signal_maintance_red(self.attraction19, self.attr19_maintance2)
        self.signal_maintance_red(self.attraction20, self.attr20_maintance2)
        self.signal_maintance_red(self.attraction21, self.attr21_maintance2)
        self.signal_maintance_red(self.attraction22, self.attr22_maintance2)
        self.signal_maintance_red(self.attraction23, self.attr23_maintance2)
        self.signal_maintance_red(self.attraction24, self.attr24_maintance2)
        self.signal_maintance_red(self.attraction25, self.attr25_maintance2)
        self.signal_maintance_red(self.attraction26, self.attr26_maintance2)
        self.signal_maintance_red(self.attraction27, self.attr27_maintance2)
        self.signal_maintance_red(self.attraction28, self.attr28_maintance2)
        
        self.signal_test_yellow(self.attraction1, self.attr1_test1)
        self.signal_test_yellow(self.attraction2, self.attr2_test1)
        self.signal_test_yellow(self.attraction3, self.attr3_test1)
        self.signal_test_yellow(self.attraction4, self.attr4_test1)
        self.signal_test_yellow(self.attraction5, self.attr5_test1)
        self.signal_test_yellow(self.attraction6, self.attr6_test1)
        self.signal_test_yellow(self.attraction7, self.attr7_test1)
        self.signal_test_yellow(self.attraction8, self.attr8_test1)
        self.signal_test_yellow(self.attraction9, self.attr9_test1)
        self.signal_test_yellow(self.attraction10, self.attr10_test1)
        self.signal_test_yellow(self.attraction11, self.attr11_test1)
        self.signal_test_yellow(self.attraction12, self.attr12_test1)
        self.signal_test_yellow(self.attraction13, self.attr13_test1)
        self.signal_test_yellow(self.attraction14, self.attr14_test1)
        self.signal_test_yellow(self.attraction15, self.attr15_test1)
        self.signal_test_yellow(self.attraction16, self.attr16_test1)
        self.signal_test_yellow(self.attraction17, self.attr17_test1)
        self.signal_test_yellow(self.attraction18, self.attr18_test1)
        self.signal_test_yellow(self.attraction19, self.attr19_test1)
        self.signal_test_yellow(self.attraction20, self.attr20_test1)
        self.signal_test_yellow(self.attraction21, self.attr21_test1)
        self.signal_test_yellow(self.attraction22, self.attr22_test1)
        self.signal_test_yellow(self.attraction23, self.attr23_test1)
        self.signal_test_yellow(self.attraction24, self.attr24_test1)
        self.signal_test_yellow(self.attraction25, self.attr25_test1)
        self.signal_test_yellow(self.attraction26, self.attr26_test1)
        self.signal_test_yellow(self.attraction27, self.attr27_test1)
        self.signal_test_yellow(self.attraction28, self.attr28_test1)

        self.signal_test_red(self.attraction1, self.attr1_test2)
        self.signal_test_red(self.attraction2, self.attr2_test2)
        self.signal_test_red(self.attraction3, self.attr3_test2)
        self.signal_test_red(self.attraction4, self.attr4_test2)
        self.signal_test_red(self.attraction5, self.attr5_test2)
        self.signal_test_red(self.attraction6, self.attr6_test2)
        self.signal_test_red(self.attraction7, self.attr7_test2)
        self.signal_test_red(self.attraction8, self.attr8_test2)
        self.signal_test_red(self.attraction9, self.attr9_test2)
        self.signal_test_red(self.attraction10, self.attr10_test2)
        self.signal_test_red(self.attraction11, self.attr11_test2)
        self.signal_test_red(self.attraction12, self.attr12_test2)
        self.signal_test_red(self.attraction13, self.attr13_test2)
        self.signal_test_red(self.attraction14, self.attr14_test2)
        self.signal_test_red(self.attraction15, self.attr15_test2)
        self.signal_test_red(self.attraction16, self.attr16_test2)
        self.signal_test_red(self.attraction17, self.attr17_test2)
        self.signal_test_red(self.attraction18, self.attr18_test2)
        self.signal_test_red(self.attraction19, self.attr19_test2)
        self.signal_test_red(self.attraction20, self.attr20_test2)
        self.signal_test_red(self.attraction21, self.attr21_test2)
        self.signal_test_red(self.attraction22, self.attr22_test2)
        self.signal_test_red(self.attraction23, self.attr23_test2)
        self.signal_test_red(self.attraction24, self.attr24_test2)
        self.signal_test_red(self.attraction25, self.attr25_test2)
        self.signal_test_red(self.attraction26, self.attr26_test2)
        self.signal_test_red(self.attraction27, self.attr27_test2)
        self.signal_test_red(self.attraction28, self.attr28_test2)
    
    # Function to open and show attraction-popup

    def show_attraction(self, attraction):

        self.popup_attraction = PopupscreenAttraction(attraction)
        self.widget = (PopupAttractionContent(attraction))
        self.popup_attraction.content = self.widget
        self.popup_attraction.title = ""
        self.popup_attraction.separator_height = 0
        self.popup_attraction.size_hint = (0.9, 0.9)
        self.popup_attraction.background_color=(0, 0, 0, 0)
        self.popup_attraction.on_dismiss = self.popup_attraction.content.close_update
        self.popup_attraction.open()

# Class main popup Attraction

class PopupscreenAttraction(Popup):
    
    def __init__(self, attraction):
        super(PopupscreenAttraction, self).__init__()
        self.attraction = attraction

        # Create Popup for maintance input
        
        content_maintance = PopupscreenMaintance(self.attraction)
        self.popup_maintance = ModalView(size_hint= (0.4, 0.4))
        self.popup_maintance.add_widget(content_maintance)
        self.popup_maintance.auto_dismiss = False

        # Create Popup for inspection input

        content_inspection = PopupscreenInspection(self.attraction)
        self.popup_inspection = ModalView(size_hint= (0.4, 0.4))
        self.popup_inspection.add_widget(content_inspection)
        self.popup_inspection.auto_dismiss = False
    
    # Function to open maintance- and inspection popup with inlogscreen

    def show_inlogscreen(self, popup):

        content_inlog = PopupscreenInlog(self.attraction, popup)
        self.popup_inlog = ModalView(size_hint= (0.4, 0.4))
        self.popup_inlog.add_widget(content_inlog)
        self.popup_inlog.auto_dismiss = True
        self.popup_inlog.open()
    
    # Function to open passwordscreen if maintance needs to be ticked off

    def show_passwordscreen(self, date, path, button ):

        content_password = PopupscreenPassword(self.attraction, date, path, button)
        self.popup_password = ModalView(size_hint= (0.4, 0.4))
        self.popup_password.add_widget(content_password)
        self.popup_password.auto_dismiss = True
        self.popup_password.open()
    
# Class with content of main popup Attraction

class PopupAttractionContent(BoxLayout):

    attr_popup = ObjectProperty("None")

    # Static variables

    attr_name = StringProperty("None")
    attr_image = StringProperty("None")
    attr_type = StringProperty("None")
    attr_RAS_number = StringProperty("None")
    attr_date_of_construction = StringProperty("None")
    attr_manufacturer = StringProperty("None") 
    attr_tel = StringProperty("None")
    attr_email = StringProperty("None")
    attr_durance_maintance = StringProperty("None")
    attr_durance_morningcheck = StringProperty("None")

    attr_property_1 = StringProperty("None")
    attr_property_2 = StringProperty("None")
    attr_property_3 = StringProperty("None")
    attr_property_4 = StringProperty("None")
    attr_property_5 = StringProperty("None")
    attr_property_6 = StringProperty("None")
    attr_property_7 = StringProperty("None")
    attr_property_8 = StringProperty("None")
    attr_property_9 = StringProperty("None")
    attr_property_10 = StringProperty("None")
    attr_property_11 = StringProperty("None")
    attr_property_12 = StringProperty("None")
    attr_property_13 = StringProperty("None")
    attr_property_14 = StringProperty("None")
    
    attr_info_1 = StringProperty("None")
    attr_info_2 = StringProperty("None")
    attr_info_3 = StringProperty("None")
    attr_info_4 = StringProperty("None")
    attr_info_5 = StringProperty("None")
    attr_info_6 = StringProperty("None")
    attr_info_7 = StringProperty("None")
    attr_info_8 = StringProperty("None")
    attr_info_9 = StringProperty("None")
    attr_info_10 = StringProperty("None")
    attr_info_11 = StringProperty("None")
    attr_info_12 = StringProperty("None")
    attr_info_13 = StringProperty("None")
    attr_info_14 = StringProperty("None")

    # Variable variables or Button and panel variables

    attr_certification = ObjectProperty("None")
    attr_state = ObjectProperty("None")
    attr_rapport_expiredate = ObjectProperty("None")                                  
    attr_validity_rapport = ObjectProperty("None")
    attr_last_inspection_date = ObjectProperty("None")
    attr_next_inspection_date = ObjectProperty("None")
    
    attr_maintance_1 = StringProperty("None")
    attr_maintance_2 = StringProperty("None")
    attr_maintance_3 = StringProperty("None")
    attr_maintance_4 = StringProperty("None")
    attr_check1 = StringProperty("None")
    attr_check2 = StringProperty("None")
    attr_check3 = StringProperty("None")
    attr_check4 = StringProperty("None")

    btn_malfunction = ObjectProperty("None")
    btn_check = ObjectProperty("None")

    btn_maintance1 = ObjectProperty("None")
    btn_maintance2 = ObjectProperty("None")
    btn_maintance3 = ObjectProperty("None")
    btn_maintance4 = ObjectProperty("None")

    btn_rapport1 = ObjectProperty("None")
    btn_rapport2 = ObjectProperty("None")
    btn_rapport3 = ObjectProperty("None")
    btn_rapport4 = ObjectProperty("None")

    check_remaining = NumericProperty()
    check_time = StringProperty("None")
    attr_stopwatch = ObjectProperty("None")

    attr_infopanel = ObjectProperty("None")
    
    # Function to create main popup attraction content

    def __init__(self, attraction, **kwargs):
        
        super(PopupAttractionContent, self).__init__(**kwargs)

        # Get maintance dates

        with open(attraction.adm_maintance.maintance_1, "r") as a:
            try:
                maintance_date1 = a.read().splitlines()[0] 
            except IndexError:
                maintance_date1 = ""
        with open(attraction.adm_maintance.maintance_2, "r") as b:
            try:
                maintance_date2 = b.read().splitlines()[0] 
            except IndexError:
                maintance_date2 = ""
        with open(attraction.adm_maintance.maintance_3, "r") as c:
            try:
                maintance_date3 = c.read().splitlines()[0] 
            except IndexError:
                maintance_date3 = ""
        with open(attraction.adm_maintance.maintance_4, "r") as d:
            try:
                maintance_date4 = d.read().splitlines()[0] 
            except IndexError:
                maintance_date4 = ""
        
        # Check if maintance has been performed
        
        with open(attraction.adm_maintance.maintance_1, "r") as e:
            try:
                check_date1 = e.read().splitlines()[1] 
            except IndexError:
                check_date1 = ""
        with open(attraction.adm_maintance.maintance_2, "r") as f:
            try:
                check_date2 = f.read().splitlines()[1] 
            except IndexError:
                check_date2 = ""
        with open(attraction.adm_maintance.maintance_3, "r") as g:
            try:
                check_date3 = g.read().splitlines()[1] 
            except IndexError:
                check_date3 = ""
        with open(attraction.adm_maintance.maintance_4, "r") as h:
            try:
                check_date4 = h.read().splitlines()[1] 
            except IndexError:
                check_date4 = ""

        # Get inspection dates
        
        with open(attraction.adm_maintance.last_inspection, "r") as i:
            try:
                inspection_date1 = i.read().splitlines()[0] 

            except IndexError:
                inspection_date1 = ""

        with open(attraction.adm_maintance.next_inspection, "r") as j:
            try:
                inspection_date2 = j.read().splitlines()[0] 
                
            except IndexError:
                inspection_date2 = ""
        
        # Check if attraction is on malfunction

        try:
            with open('Database/Lists/Malfunction/' + attraction.string + '.txt', "r") as k:
                malfunction_info = k.read()

        except FileNotFoundError:
            pass

        self.attraction = attraction
        self.attr_name = attraction.name
        self.attr_image = attraction.image
        self.attr_type = attraction.type
        self.attr_RAS_number = attraction.RAS_number
        self.attr_date_of_construction = attraction.date_of_construction
        self.attr_manufacturer = attraction.manufacturer.name
        self.attr_tel = attraction.manufacturer.phonenumber
        self.attr_email = attraction.manufacturer.email
        self.attr_state.text = self.attraction_state()
        self.attr_validity_rapport.text = attraction.validity_rapport
        self.attr_rapport_expiredate.text = self.attraction_expire()
        self.attr_durance_maintance = attraction.durance_maintance
        self.attr_durance_morningcheck = attraction.durance_morningcheck

        self.attr_infopanel.text = "Ochtendcheck nodig"

        self.attr_check1 = check_date1
        self.attr_check2 = check_date2
        self.attr_check3 = check_date3
        self.attr_check4 = check_date4

        # Get text to be shown on maintance buttons for ticking off maintance

        if maintance_date1 == "":
            self.attr_maintance_1 = "Onbekend"
        else:
            self.attr_maintance_1 = maintance_date1

        if maintance_date2 == "":
            self.attr_maintance_2 = "Onbekend"
        else:
            self.attr_maintance_2 = maintance_date2

        if maintance_date3 == "":
            self.attr_maintance_3 = "Onbekend"
        else:
            self.attr_maintance_3 = maintance_date3
        
        if maintance_date4 == "":
            self.attr_maintance_4 = "Onbekend"
        else:
            self.attr_maintance_4 = maintance_date4
        
        if inspection_date1 == "":
            self.attr_last_inspection_date.text = "Onbekend"
        else:
            self.attr_last_inspection_date.text = inspection_date1
        
        if inspection_date2 == "":
            self.attr_next_inspection_date.text = "Onbekend"
        else:
            self.attr_next_inspection_date.text = inspection_date2

        # Specify layout for atraction classes

        if type(self.attraction) == Rollercoaster:

            self.attr_property_1 = "Capaciteit per trein:"
            self.attr_property_2 = "Totaal aantal treinen:"
            self.attr_property_3 = "Capaciteit totaal:"
            self.attr_property_4 = "Capaciteit per uur:"
            self.attr_property_5 = "Baanlengte:"
            self.attr_property_6 = "Maximale snelheid:"
            self.attr_property_7 = "Duur rit:"
            self.attr_property_8 = "Maximale hoogte:"
            self.attr_property_9 = "Minimale vereiste lengte:"
            self.attr_property_10 = "Veiligheidsvoorziening:" 
            self.attr_property_11 = "Aansluitwaarde:"
            self.attr_property_12 = "Maximale G-kracht:"
            self.attr_property_13 = "Inversies:"
            self.attr_property_14 = "On-ride-foto:"
            
            self.attr_info_1 = attraction.train_capacity
            self.attr_info_2 = attraction.number_of_trains
            self.attr_info_3= attraction.capacity_total
            self.attr_info_4 = attraction.capacity_hour
            self.attr_info_5 = attraction.track_length
            self.attr_info_6 = attraction.max_speed
            self.attr_info_7 = attraction.trip_duration
            self.attr_info_8 = attraction.max_height
            self.attr_info_9 = attraction.min_length
            self.attr_info_10 = attraction.safety_device
            self.attr_info_11 = attraction.powerconsumption
            self.attr_info_12 = attraction.max_gforce
            self.attr_info_13 = attraction.inversions
            self.attr_info_14 = attraction.onride_photo

        if type(self.attraction) == WaterRide:

            self.attr_property_1 = "Capaciteit per boot:"
            self.attr_property_2 = "Totaal aantal boten:"
            self.attr_property_3 = "Capaciteit totaal:"
            self.attr_property_4 = "Capaciteit per uur:"
            self.attr_property_5 = "Baanlengte:"
            self.attr_property_6 = "Maximale snelheid:"
            self.attr_property_7 = "Duur rit:"
            self.attr_property_8 = "Maximale hoogte:"
            self.attr_property_9 = "Minimale vereiste lengte:"
            self.attr_property_10 = "On-ride-foto:" 
            self.attr_property_11 = ""
            self.attr_property_12 = "Aansluitwaarde:"
            self.attr_property_13 = ""
            self.attr_property_14 = ""
            
            self.attr_info_1 = attraction.boat_capacity
            self.attr_info_2 = attraction.number_of_boats
            self.attr_info_3= attraction.capacity_total
            self.attr_info_4 = attraction.capacity_hour
            self.attr_info_5 = attraction.track_length
            self.attr_info_6 = attraction.max_speed
            self.attr_info_7 = attraction.trip_duration
            self.attr_info_8 = attraction.max_height
            self.attr_info_9 = attraction.min_length
            self.attr_info_10 = attraction.onride_photo
            self.attr_info_11 = ""
            self.attr_info_12 = attraction.powerconsumption
            self.attr_info_13 = ""
            self.attr_info_14 = ""   
        
        if type(self.attraction) == Transport:

            self.attr_property_1 = "Capaciteit per wagon:"
            self.attr_property_2 = "Totaal aantal wagons:"
            self.attr_property_3 = "Capaciteit totaal:"
            self.attr_property_4 = "Capaciteit per uur:"
            self.attr_property_5 = "Baanlengte:"
            self.attr_property_6 = "Maximale snelheid:"
            self.attr_property_7 = "Duur rit:"
            self.attr_property_8 = "Maximale hoogte:"
            self.attr_property_9 = "Minimale vereiste lengte:"
            self.attr_property_10 = "On-ride-foto:" 
            self.attr_property_11 = ""
            self.attr_property_12 = "Aansluitwaarde:"
            self.attr_property_13 = ""
            self.attr_property_14 = ""
            
            self.attr_info_1 = attraction.wagon_capacity
            self.attr_info_2 = attraction.number_of_wagons
            self.attr_info_3= attraction.capacity_total
            self.attr_info_4 = attraction.capacity_hour
            self.attr_info_5 = attraction.track_length
            self.attr_info_6 = attraction.max_speed
            self.attr_info_7 = attraction.trip_duration
            self.attr_info_8 = attraction.max_height
            self.attr_info_9 = attraction.min_length
            self.attr_info_10 = attraction.onride_photo
            self.attr_info_11 = ""
            self.attr_info_12 = attraction.powerconsumption
            self.attr_info_13 = ""
            self.attr_info_14 = ""
        
        if type(self.attraction) == Carrousel:
            
            self.attr_property_1 = "Capaciteit per cabine:"
            self.attr_property_2 = "Totaal aantal cabines:"
            self.attr_property_3 = "Capaciteit totaal:"
            self.attr_property_4 = "Capaciteit per uur:"
            self.attr_property_5 = "Baanlengte:"
            self.attr_property_6 = "Maximale snelheid:"
            self.attr_property_7 = "Duur rit:"
            self.attr_property_8 = "Maximale hoogte:"
            self.attr_property_9 = "Minimale vereiste lengte:"
            self.attr_property_10 = "Veiligheidsvoorziening:" 
            self.attr_property_11 = ""
            self.attr_property_12 = "Aansluitwaarde:"
            self.attr_property_13 = "On-ride-foto:"
            self.attr_property_14 = " "

            self.attr_info_1 = attraction.cabin_capacity
            self.attr_info_2 = attraction.number_of_cabins
            self.attr_info_3= attraction.capacity_total
            self.attr_info_4 = attraction.capacity_hour
            self.attr_info_5 = attraction.track_length
            self.attr_info_6 = attraction.max_speed
            self.attr_info_7 = attraction.trip_duration
            self.attr_info_8 = attraction.max_height
            self.attr_info_9 = attraction.min_length
            self.attr_info_10 = attraction.safety_device
            self.attr_info_11 = ""
            self.attr_info_12 = attraction.powerconsumption
            self.attr_info_13 = attraction.onride_photo
            self.attr_info_14 = ""
        
        if type(self.attraction) == SpinPuke:
            
            self.attr_property_1 = "Capaciteit per cabine:"
            self.attr_property_2 = "Totaal aantal cabines:"
            self.attr_property_3 = "Capaciteit totaal:"
            self.attr_property_4 = "Capaciteit per uur:"
            self.attr_property_5 = "Baanlengte:"
            self.attr_property_6 = "Maximale snelheid:"
            self.attr_property_7 = "Duur rit:"
            self.attr_property_8 = "Maximale hoogte:"
            self.attr_property_9 = "Minimale vereiste lengte:"
            self.attr_property_10 = "Veiligheidsvoorziening:" 
            self.attr_property_11 = ""
            self.attr_property_12 = "Aansluitwaarde:"
            self.attr_property_13 = "On-ride-foto:"
            self.attr_property_14 = " "

            self.attr_info_1 = attraction.cabin_capacity
            self.attr_info_2 = attraction.number_of_cabins
            self.attr_info_3= attraction.capacity_total
            self.attr_info_4 = attraction.capacity_hour
            self.attr_info_5 = attraction.track_length
            self.attr_info_6 = attraction.max_speed
            self.attr_info_7 = attraction.trip_duration
            self.attr_info_8 = attraction.max_height
            self.attr_info_9 = attraction.min_length
            self.attr_info_10 = attraction.safety_device
            self.attr_info_11 = ""
            self.attr_info_12 = attraction.powerconsumption
            self.attr_info_13 = attraction.onride_photo
            self.attr_info_14 = ""
        
        if type(self.attraction) == Playground:

            self.attr_property_1 = ""
            self.attr_property_2 = "Capaciteit per onderdeel:"
            self.attr_property_3 = "Totaal aantal onderdelen:"
            self.attr_property_4 = "Capaciteit totaal:"
            self.attr_property_5 = ""
            self.attr_property_6 = ""
            self.attr_property_7 = ""
            self.attr_property_8 = ""
            self.attr_property_9 = "Maximale hoogte:"
            self.attr_property_10 = "Minimale vereiste lengte:" 
            self.attr_property_11 = ""
            self.attr_property_12 = ""
            self.attr_property_13 = ""
            self.attr_property_14 = ""

            self.attr_info_1 = ""
            self.attr_info_2 = attraction.play_equipment_capacity
            self.attr_info_3 = attraction.number_of_play_equipment
            self.attr_info_4 = attraction.capacity_total
            self.attr_info_5 = ""
            self.attr_info_6 = ""
            self.attr_info_7 = ""
            self.attr_info_8 = ""
            self.attr_info_9 = attraction.max_height
            self.attr_info_10 = attraction.min_length
            self.attr_info_11 = ""
            self.attr_info_12 = ""
            self.attr_info_13 = ""
            self.attr_info_14 = ""

        # Get time required for morningcheck and make a string to use it in layout

        self.check_remaining = (int(attraction.durance_morningcheck) * 60) 
        self.check_time = str(datetime.timedelta(seconds=self.check_remaining))
        
        # Update layout main popup attraction to attraction status runnnig if attraction was in morningcheck 
        # at a previous visit (which was finished) 
        
        if Path('Database/Lists/Running/' + self.attraction.string + '.txt').is_file():
            self.attr_infopanel.text = "Attractie is gereed om te draaien"

            self.btn_check.state = 'down'
            self.btn_check.text = "Check Voltooid"        
            self.btn_check.background_color = (102/255, 204/255, 0/255, 150/255)
            self.btn_check.color = (233/255, 233/255, 251/255, 255/255)
            self.btn_check.outline_color = (32/255, 32/255, 32/255)
        
        # Update layout main popup attraction to attraction status malfunction if attraction was put on 
        # malfunction at a previous visit

        if Path('Database/Lists/Malfunction/' + self.attraction.string + '.txt').is_file():

            self.attr_infopanel.text = malfunction_info
            self.attr_popup.line_color = (255/255, 0/255, 0/255, 150/255)
            
            self.btn_malfunction.state = 'down'
            self.btn_malfunction.background_color = (255/255, 0/255, 0/255, 150/255)
            self.btn_malfunction.color = (169/255, 169/255, 169/255, 255/255)
            
            self.btn_check.state = "down"
            self.btn_check.text = "Storing" 
            self.btn_check.background_color = (102/255, 204/255, 0/255, 150/255)
            self.btn_check.color = (233/255, 233/255, 251/255, 255/255)
            self.btn_check.outline_color = (32/255, 32/255, 32/255)
        
        # Update maintance-date color to green when maintance has been performed and been 
        # checked

        if check_date1 == "Checked":
            self.btn_maintance1.background_color = (0/255, 255/255, 0/255, 255/255)
        
        if check_date2 == "Checked":
            self.btn_maintance2.background_color = (0/255, 255/255, 0/255, 255/255)
        
        if check_date3 == "Checked":
            self.btn_maintance3.background_color = (0/255, 255/255, 0/255, 255/255)
        
        if check_date4 == "Checked":
            self.btn_maintance4.background_color = (0/255, 255/255, 0/255, 255/255)
        
        # Create popup to put attraction on malfunction
        
        content_malfunction1 = PopupMalfunction1Content(self.attraction)
        self.popup_malfunction1 = PopupscreenMalfunction1(self.attraction)
        self.popup_malfunction1.content = content_malfunction1
        self.popup_malfunction1.auto_dismiss = True
        self.popup_malfunction1.size_hint = (0.45, 0.45)
        self.popup_malfunction1.title = ""
        self.popup_malfunction1.separator_height = 0
        self.popup_malfunction1.background_color=(0, 0, 0, 0)

        # Create popup to put attraction back on running after malfunction
        
        content_malfunction2 = PopupscreenMalfunction2(self.attraction)
        self.popup_malfunction2 = ModalView(size_hint= (0.4, 0.4))
        self.popup_malfunction2.add_widget(content_malfunction2)
        self.popup_malfunction2.auto_dismiss = False
 
    # Update rapport button to green when a rapport excists

        def check_rapport(directory, button):

            if len(os.listdir(directory)) == 1:

                button.color = (233/255, 233/255, 251/255, 255/255)
                button.outline_color = (32/255, 32/255, 32/255)
                button.outline_width = 1
                button.background_color = (0/255, 128/255, 255/255, 255/255)
                button.line_color = (32/255, 32/255, 32/255, 255/255)
            
            elif len(os.listdir(directory)) > 1:
                
                button.text = "Rapport error!"
                button.color = (255/255, 0/255, 0/255, 80/255)
                button.line_color = (255/255, 0/255, 0/255, 80/255)
                
            else:
                pass

        check_rapport(self.attraction.adm_maintance.rapport_1, self.btn_rapport1)
        check_rapport(self.attraction.adm_maintance.rapport_2, self.btn_rapport2)
        check_rapport(self.attraction.adm_maintance.rapport_3, self.btn_rapport3)
        check_rapport(self.attraction.adm_maintance.rapport_4, self.btn_rapport4)

    # Function to get rapport expiredate        
    
    def attraction_expire(self):

        with open(self.attraction.adm_maintance.last_inspection, "r") as i:
            inspection_date1 = i.read()
        
        if inspection_date1 == "":

            return "Onbekend"
        
        else:

            return ((datetime.datetime.strptime(inspection_date1, "%d/%m/%Y").date()) + 
                    (datetime.timedelta(days=(int(self.attraction.validity_rapport) * 365)))).strftime("%d/%m/%Y")

    # Function to check if validaty rapport has expired

    def attraction_state(self):

        with open(self.attraction.adm_maintance.last_inspection, "r") as i:
            inspection_date1 = i.read()
        
        if inspection_date1 == "":

            
            return "Afgekeurd"
        
        else:

            date_now = datetime.datetime.now()
            date_now = date_now.strftime("%d") + "/" + date_now.strftime("%m") + "/" + date_now.strftime("%Y")
            
            date_expire = ((datetime.datetime.strptime(inspection_date1, "%d/%m/%Y").date()) + 
                        (datetime.timedelta(days=(int(self.attraction.validity_rapport) * 365)))).strftime("%d/%m/%Y")

            d1 = datetime.datetime.strptime(date_now, "%d/%m/%Y").date()
            d2 = datetime.datetime.strptime(date_expire, "%d/%m/%Y").date()
            
            if d1 <= d2:

                self.attr_certification.source = 'Img/Goedgekeurd.jpg'
                return "Goedgekeurd"

            else:

                self.attr_certification.source = 'Img/Afgekeurd.jpg'
                return "Afgekeurd"

    # Function to put attraction on malfunction or back on running when attraction was 
    # on malfunction

    def malfunction_attraction(self):

        if self.btn_check.text == "Pauzeer Check":
            pass

        elif Path('Database/Lists/Malfunction/' + self.attraction.string + '.txt').is_file():
            self.attraction.transfer_list(Attraction.off)
            self.popup_malfunction2.open()
            self.update_content()

        else:
            self.popup_malfunction1.open()
            self.popup_malfunction1.content.attr_malfunction_info.text = ""     

    # Function to administrate the cause of the malfunction
    
    def register_malfunction(self):

        self.attraction.transfer_list(Attraction.malfunction)
        self.update_content()

        if self.popup_malfunction1.content.malfunction_choice1.active == True:

            self.attraction.adm_maintance.write_malfunction("Keuring")
            self.popup_malfunction1.dismiss()
        
        elif self.popup_malfunction1.content.malfunction_choice2.active == True:

            self.attraction.adm_maintance.write_malfunction("Groot Onderhoud")
            self.popup_malfunction1.dismiss()

        elif self.popup_malfunction1.content.malfunction_choice3.active == True:

            if self.popup_malfunction1.content.attr_malfunction_info.text == "":
                pass

            else:
                self.attraction.adm_maintance.write_malfunction(self.popup_malfunction1.content.attr_malfunction_info.text)
                self.popup_malfunction1.dismiss()
        
        else: 
            pass
    
    # Function to put attraction on status running after malfunction

    def undo_malfunction_yes(self):

        self.attraction.transfer_list(Attraction.running)
        self.popup_malfunction2.dismiss()
        self.check_remaining = 0
        self.check_time = str(datetime.timedelta(seconds=self.check_remaining))

    # Function to put attraction on status off after malfunction
        
    def undo_malfunction_no(self):

        self.popup_malfunction2.dismiss()
        self.btn_check.on_press = self.start_timer
        self.check_remaining = (int(self.attraction.durance_morningcheck) * 60)
        self.check_time = str(datetime.timedelta(seconds=self.check_remaining))

    # Function for attraction-morningcheck and update layout main popup attraction to
    # attraction status morningcheck
        
    def check_attraction(self, interval):

        self.check_remaining -= 1
        self.check_time = str(datetime.timedelta(seconds=self.check_remaining))

        if self.check_remaining > 0:
            self.btn_check.text = "Pauzeer Check"
            self.btn_check.on_press = self.pause_timer
        
        if self.check_remaining == 0:
            Clock.unschedule(self.check_attraction)
            self.btn_check.text = "Voltooi Check"
            self.btn_check.on_press = self.complete_check
            App.get_running_app().root.popup_attraction.auto_dismiss = False                                 
    
    # Function to start morningcheck-timer and update layout main popup attraction to
    # attraction status morningcheck 

    def start_timer(self):

        if Path('Database/Lists/Running/' + self.attraction.string + '.txt').is_file():
            pass
        
        elif Path('Database/Lists/Malfunction/' + self.attraction.string + '.txt').is_file():
            pass

        else:
            Clock.unschedule(self.check_attraction)
            self.attraction.transfer_list(Attraction.morningcheck)
            Clock.schedule_interval(self.check_attraction, 1)
            self.attr_infopanel.text = "Ochtendcheck bezig"
            App.get_running_app().root.popup_attraction.auto_dismiss = False
            App.get_running_app().root.update_statuses()

    # Function to pause morningcheck-timer

    def pause_timer(self):
        Clock.unschedule(self.check_attraction)
        self.btn_check.text = "Hervat Check"
        self.btn_check.on_press = self.start_timer
        self.attr_infopanel.text = "Ochtendcheck pauze"
        App.get_running_app().root.popup_attraction.auto_dismiss = True

    # Function to complete morningcheck and put attraction on status running

    def complete_check(self):

        if Path('Database/Lists/Running/' + self.attraction.string + '.txt').is_file():
            pass
        
        elif Path('Database/Lists/Malfunction/' + self.attraction.string + '.txt').is_file():
            pass

        else:

            Clock.unschedule(self.check_attraction)
            self.attraction.transfer_list(Attraction.running)
            self.update_content()
            App.get_running_app().root.popup_attraction.auto_dismiss = True
        
    # Function to disable button when attraction is on running or malfunction

    def maintain_buttonstate(self):

        if Path('Database/Lists/Running/' + self.attraction.string + '.txt').is_file():
            self.btn_check.state = 'down'
        
        elif Path('Database/Lists/Malfunction/' + self.attraction.string + '.txt').is_file():
            self.btn_check.state = 'down'
            
        else: 
            pass

    # Function to tick off maintance dates attraction. (red is planned, green is finished)

    def tickoff_maintance(self, date, path, button):

        try:

            date_now = datetime.datetime.now()
            date_now = date_now.strftime("%d") + "/" + date_now.strftime("%m") + "/" + date_now.strftime("%Y")
            
            d1 = datetime.datetime.strptime(date_now, "%d/%m/%Y").date()
            d2 = datetime.datetime.strptime(date, "%d/%m/%Y").date()
            d3 = datetime.timedelta(days=int(self.attraction.durance_maintance))
            d4 = d2 + d3

            if d1 > d4:
                button.background_color = (0/255, 255/255, 0/255, 255/255)
                self.attraction.adm_maintance.check_date(path , date)
                self.update_content()
            
            else: 
                pass
        
        except ValueError:
            pass

    # Function to open a rapport

    def open_rapport(self, rapport):

        try:

            f = os.listdir(rapport)   
            if len(f) == 1:
                webbrowser.open_new(rapport + '\\' + f[0])  

            else:
                pass
                
        except IndexError:

            pass

    # Function to update content main pop attaction after a performed action

    def update_content(self):

        # Get (new) maintance dates

        with open(self.attraction.adm_maintance.maintance_1, "r") as a:
            try:
                maintance_date1 = a.read().splitlines()[0] 
            except IndexError:
                maintance_date1 = ""
        with open(self.attraction.adm_maintance.maintance_2, "r") as b:
            try:
                maintance_date2 = b.read().splitlines()[0] 
            except IndexError:
                maintance_date2 = ""
        with open(self.attraction.adm_maintance.maintance_3, "r") as c:
            try:
                maintance_date3 = c.read().splitlines()[0] 
            except IndexError:
                maintance_date3 = ""
        with open(self.attraction.adm_maintance.maintance_4, "r") as d:
            try:
                maintance_date4 = d.read().splitlines()[0] 
            except IndexError:
                maintance_date4 = ""
        
        # Check if maintance has been ticked off

        with open(self.attraction.adm_maintance.maintance_1, "r") as e:
            try:
                check_date1 = e.read().splitlines()[1]
            except IndexError:
                check_date1 = ""
        with open(self.attraction.adm_maintance.maintance_2, "r") as f:
            try:
                check_date2 = f.read().splitlines()[1]
            except IndexError:
                check_date2 = ""
        with open(self.attraction.adm_maintance.maintance_3, "r") as g:
            try:
                check_date3 = g.read().splitlines()[1]
            except IndexError:
                check_date3 = ""
        with open(self.attraction.adm_maintance.maintance_4, "r") as h:
            try:
                check_date4 = h.read().splitlines()[1]
            except IndexError:
                check_date4 = ""

        # Get (new) inspection dates
        
        with open(self.attraction.adm_maintance.last_inspection, "r") as i:
            inspection_date1 = i.read()
        with open(self.attraction.adm_maintance.next_inspection, "r") as j:
            inspection_date2 = j.read()
        
        # Check if attraction has been put on malfunction

        try:
            with open('Database/Lists/Malfunction/' + self.attraction.string + '.txt', "r") as k:
                malfunction_info = k.read()

        except FileNotFoundError:
            pass

        # Get text to be shown on maintance buttons for ticking off maintance

        if maintance_date1 == "":
            self.attr_maintance_1 = "Onbekend"
        else:
            self.attr_maintance_1 = maintance_date1

        if maintance_date2 == "":
            self.attr_maintance_2 = "Onbekend"
        else:
            self.attr_maintance_2 = maintance_date2

        if maintance_date3 == "":
            self.attr_maintance_3 = "Onbekend"
        else:
            self.attr_maintance_3 = maintance_date3
        
        if maintance_date4 == "":
            self.attr_maintance_4 = "Onbekend"
        else:
            self.attr_maintance_4 = maintance_date4

        if inspection_date1 == "":
            self.attr_last_inspection_date.text = "Onbekend"
        else:
            self.attr_last_inspection_date.text = inspection_date1
        
        if inspection_date2 == "":
            self.attr_next_inspection_date.text = "Onbekend"
        else:
            self.attr_next_inspection_date.text = inspection_date2

        self.attr_check1 = check_date1     
        self.attr_check2 = check_date2
        self.attr_check3 = check_date3
        self.attr_check4 = check_date4                                        

        # Refresh rapport expire date 

        self.attr_rapport_expiredate.text = self.attraction_expire()
        
        # Update attraction state

        self.attr_state.text = self.attraction_state()
        
        # Update layout main popup attraction to attraction status off  

        if Path('Database/Lists/Off/' + self.attraction.string + '.txt').is_file():
            self.attr_infopanel.text = "Ochtendcheck nodig"
            self.attr_popup.line_color = (32/255, 32/255, 32/255, 100/255) 

            self.btn_check.state = 'normal'
            self.btn_check.text = "Start Check"     
            self.btn_check.background_color = (102/255, 204/255, 0/255, 255/255)
            self.btn_check.color = (32/255, 32/255, 32/255, 255/255)
            self.btn_check.outline_color= (233/255, 233/255, 251/255)

            self.btn_malfunction.background_color = (255/255, 0/255, 0/255, 255/255)
            self.btn_malfunction.color = (255/255, 255/255, 255/255, 255/255)
        
        # Update layout main popup attraction to attraction status running 
        
        if Path('Database/Lists/Running/' + self.attraction.string + '.txt').is_file():
            self.attr_infopanel.text = "Attractie is gereed om te draaien"
            self.attr_popup.line_color = (32/255, 32/255, 32/255, 100/255) 
            
            self.btn_check.state = 'down'
            self.btn_check.text = "Check Voltooid"
            self.btn_check.background_color = (102/255, 204/255, 0/255, 150/255)
            self.btn_check.color = (233/255, 233/255, 251/255, 255/255)
            self.btn_check.outline_color = (32/255, 32/255, 32/255)

            self.btn_malfunction.background_color = (255/255, 0/255, 0/255, 255/255)
            self.btn_malfunction.color = (255/255, 255/255, 255/255, 255/255)
        
        # Update layout main popup attraction to attraction status malfunction

        if Path('Database/Lists/Malfunction/' + self.attraction.string + '.txt').is_file():
            self.attr_infopanel.text = malfunction_info
            self.attr_popup.line_color = (255/255, 0/255, 0/255, 150/255)
            
            self.btn_malfunction.state = 'down'
            self.btn_malfunction.background_color = (255/255, 0/255, 0/255, 150/255)
            self.btn_malfunction.color = (169/255, 169/255, 169/255, 255/255)
            
            self.btn_check.state = 'down'
            self.btn_check.text = "Storing"
            self.btn_check.background_color = (102/255, 204/255, 0/255, 150/255)
            self.btn_check.color = (233/255, 233/255, 251/255, 255/255)
            self.btn_check.outline_color= (32/255, 32/255, 32/255)
        
        # Update layout maintance buttons when they haven been ticked off

        def check_maintance(check_date, button):
        
            if check_date == "Checked":
                button.background_color = (0/255, 255/255, 0/255, 255/255)
            else:
                button.background_color = (255/255, 0/255, 0/255, 255/255)
        
        check_maintance(check_date1, self.btn_maintance1)
        check_maintance(check_date2, self.btn_maintance2)
        check_maintance(check_date3, self.btn_maintance3)
        check_maintance(check_date4, self.btn_maintance4)
    
    # Reset layout main popup attraction and update statuses in mainscreen to attraction status 
    # off if attraction is in morningcheck which is not finished when closing the popup 

    def close_update(self):

        if Path('Database/Lists/Morningcheck/' + self.attraction.string + '.txt').is_file():
            self.attraction.transfer_list(Attraction.off)
        
        App.get_running_app().root.update_statuses()

# Class popup maintance

class PopupscreenMaintance(BoxLayout):

    attr_name = StringProperty("None")
    attr_date1 = StringProperty("None")
    attr_date2 = StringProperty("None")
    attr_date3 = StringProperty("None")
    attr_date4 = StringProperty("None")
    
    def __init__(self, attraction):

        super(PopupscreenMaintance, self).__init__()

        with open(attraction.adm_maintance.maintance_1, "r") as a:
            try:
                maintance_date1 = a.read().splitlines()[0] 
            except IndexError:
                maintance_date1 = ""
        with open(attraction.adm_maintance.maintance_2, "r") as b:
            try:
                maintance_date2 = b.read().splitlines()[0] 
            except IndexError:
                maintance_date2 = ""
        with open(attraction.adm_maintance.maintance_3, "r") as c:
            try:
                maintance_date3 = c.read().splitlines()[0] 
            except IndexError:
                maintance_date3 = ""
        with open(attraction.adm_maintance.maintance_4, "r") as d:
            try:
                maintance_date4 = d.read().splitlines()[0] 
            except IndexError:
                maintance_date4 = ""

        self.attraction = attraction 
        self.attr_name = attraction.name

        self.attr_date1 = maintance_date1
        self.attr_date2 = maintance_date2
        self.attr_date3 = maintance_date3
        self.attr_date4 = maintance_date4
         
# Class popup inspection

class PopupscreenInspection(BoxLayout):

    attr_name = StringProperty("None")
    attr_last = StringProperty("None")
    attr_next = StringProperty("None")
    
    def __init__(self, attraction):

        super(PopupscreenInspection, self).__init__()

        with open(attraction.adm_maintance.last_inspection, "r") as i:
            try:
                inspection_date1 = i.read().splitlines()[0] 

            except IndexError:
                inspection_date1 = ""

        with open(attraction.adm_maintance.next_inspection, "r") as j:
            try:
                inspection_date2 = j.read().splitlines()[0] 
                
            except IndexError:
                inspection_date2 = ""

        self.attraction = attraction  
        self.attr_name = attraction.name
        self.attr_last = inspection_date1
        self.attr_next = inspection_date2

# Class popup inlogscreen

class PopupscreenInlog(BoxLayout):

    attr_name = StringProperty("None")
    input_username = ObjectProperty("None")
    input_password = ObjectProperty("None")
    
    
    def __init__(self, attraction, popup):
        super(PopupscreenInlog, self).__init__()
        self.attraction = attraction

        self.attr_name = attraction.name
        self.popup = popup
    
    # Function to check if password and username are valid

    def confirm(self):
                                       
        username = (self.input_username.text).strip()
        password = (self.input_password.text).strip()

        if username in users_used and password == passwords_used[users_used.index(username)]:

            App.get_running_app().root.popup_attraction.popup_inlog.dismiss()    
            self.popup.open()
        
        else:
            pass

class PopupscreenPassword(BoxLayout):

    attr_name = StringProperty("None")
    input_username = ObjectProperty("None")
    input_password = ObjectProperty("None")
    
    
    def __init__(self, attraction, date, path, button):
        super(PopupscreenPassword, self).__init__()
        self.attraction = attraction

        self.attr_name = attraction.name
        self.date = date
        self.path = path
        self.button = button
    
    # Function to check if password and username are valid

    def confirm(self):
                                       
        username = (self.input_username.text).strip()
        password = (self.input_password.text).strip()

        if username in users_used and password == passwords_used[users_used.index(username)]:

            App.get_running_app().root.popup_attraction.popup_password.dismiss()    
            App.get_running_app().root.popup_attraction.content.tickoff_maintance(self.date, self.path, self.button)
        
        else:
            pass

# Class popup to malfunction attraction

class PopupscreenMalfunction1(Popup):

    def __init__(self, attraction):
        super(PopupscreenMalfunction1, self).__init__()
        self.attraction = attraction

# Class with content of popup to malfunction attraction (needed to get info why 
# attraction is on malfunction)

class PopupMalfunction1Content(BoxLayout):

    attr_name = StringProperty("None")
    attr_malfunction_info = ObjectProperty("None")

    malfunction_choise1 =  ObjectProperty("None")
    malfunction_choise2 =  ObjectProperty("None")
    malfunction_choise3 = ObjectProperty("None")
    
    def __init__(self, attraction):

        super(PopupMalfunction1Content, self).__init__()
        self.attraction = attraction  
        self.attr_name = attraction.name

# Class popup to put attraction back on running after malfunction

class PopupscreenMalfunction2(BoxLayout):

    attr_name = StringProperty("None")
    
    def __init__(self, attraction):

        super(PopupscreenMalfunction2, self).__init__()
        self.attraction = attraction  
        self.attr_name = attraction.name

# Class to create Hoover-events 

class HoverBehavior(object):

    hovered = BooleanProperty(False)
    border_point= ObjectProperty(None)
    def __init__(self, **kwargs):
        self.register_event_type('on_enter')
        self.register_event_type('on_leave')
        Window.bind(mouse_pos=self.on_mouse_pos)
        super(HoverBehavior, self).__init__(**kwargs)

    def on_mouse_pos(self, *args):
        if not self.get_root_window():
            return 
        pos = args[1]
        
        inside = self.collide_point(*self.to_widget(*pos))
        if self.hovered == inside:
            
            return
        self.border_point = pos
        self.hovered = inside
        if inside:
            self.dispatch('on_enter')
        else:
            self.dispatch('on_leave')

    def on_enter(self):
        pass

    def on_leave(self):
        pass

# Create Buttonclass with hoover-events

class AttractionButton(HoverBehavior, Button):
    pass

Factory.register('HoverBehavior', HoverBehavior)
      
# Class main app

class DashboardApp(App):

    def build(self):

        m = Mainscreen()

        Clock.schedule_interval(m.clock, 1)
        Clock.schedule_interval(m.closed_open, 1)
        m.check_newday()
        m.malfunction_unknown()
        m.update_statuses()

        return m

if __name__ == '__main__':
    DashboardApp().run()

  

  

  