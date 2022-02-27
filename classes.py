import datetime
import os
from pathlib import Path

class OpeningHours():

    def __init__(self, open, closed):

        self.open = open
        self.closed = closed

class Manufacturer():

    def __init__(self, name, phonenumber, email):
        self.name = name
        self.phonenumber = phonenumber
        self.email = email

class Administration():
    
    def __init__(self, attractionstring, maintance_1, maintance_2, maintance_3, maintance_4, 
                 rapport_1, rapport_2, rapport_3, rapport_4, last_inspection, next_inspection):
        
        self.attractionstring = attractionstring
        
        self.maintance_1 = maintance_1
        self.maintance_2 = maintance_2
        self.maintance_3 = maintance_3
        self.maintance_4 = maintance_4

        self.rapport_1 = rapport_1
        self.rapport_2 = rapport_2
        self.rapport_3 = rapport_3
        self.rapport_4 = rapport_4

        self.last_inspection = last_inspection
        self.next_inspection = next_inspection
    
    # Function to administrate maintance date

    def change_maintancedate(self, path, input):

        with open(path, "r") as e:
            try:
                date = e.read().splitlines()[0]
            except IndexError:
                date = ""
        
        if input != date:

            with open(path, "w") as f:
                f.write(input)
                f.write('\n')

                if input != "":
                    f.write("Planned")

                else:
                    pass
                    
    # Function to administrate inspection date
    
    def change_inspectiondate(self, path, input):

        with open(path, "w") as f:
                f.write(input)
    
    # Function to administrate if maintance has been completed

    def check_date(self, path, date):

        with open(path, "w") as f:
            f.write(date)
            f.write('\n')
            f.write("Checked")
    
    # Function to administrate malfunction info

    def write_malfunction(self, input):

        with open('Database/Lists/Malfunction/' + self.attractionstring + '.txt', "w") as f:
            f.write("Oorzaak Storing")
            f.write('\n')
            f.write('\n')
            f.write(input)

class Attraction():

    malfunction = 'Malfunction/'
    off = 'Off/'
    morningcheck = 'Morningcheck/'
    running = 'Running/'

    def __init__(self, string, name, type, image, RAS_number, date_of_construction, manufacturer, 
                 adm_maintance, validity_rapport, durance_maintance, durance_morningcheck):
        
        self.string = string
        self.name = name
        self.type = type
        self.image = image
        self.RAS_number = RAS_number
        self.date_of_construction = date_of_construction
        self.manufacturer = manufacturer
        self.adm_maintance = adm_maintance
        self.validity_rapport = validity_rapport
        self.durance_maintance = durance_maintance
        self.durance_morningcheck = durance_morningcheck

    # Function to transer attraction in database to a different list

    def transfer_list(self, path):

        date_now = datetime.datetime.now()
        date_now = date_now.strftime("%d") + "/" + date_now.strftime("%m") + "/" + date_now.strftime("%Y")

        if Path('Database/Lists/Malfunction/' + self.string + '.txt').is_file():
            os.remove('Database/Lists/Malfunction/' + self.string + '.txt')
        
        if Path('Database/Lists/Off/' + self.string + '.txt').is_file():
            os.remove('Database/Lists/Off/' + self.string + '.txt')

        if Path('Database/Lists/Morningcheck/' + self.string + '.txt').is_file():
            os.remove('Database/Lists/Morningcheck/' + self.string + '.txt')
        
        if Path('Database/Lists/Running/' + self.string + '.txt').is_file():
            os.remove('Database/Lists/Running/' + self.string + '.txt')
    
        with open('Database/Lists/' + path + self.string + '.txt', "w") as f:

            if path == self.running:
                f.write(self.string)
                f.write('\n')
                f.write(str(date_now))
            
            else:
                f.write("")

class Rollercoaster(Attraction):

    def __init__(self, string, name, type, image, RAS_number, date_of_construction, manufacturer,
                 adm_maintance, validity_rapport, durance_maintance, durance_morningcheck, 
                 train_capacity, number_of_trains, capacity_total, capacity_hour, track_length,
                 max_speed, trip_duration, max_height, min_length, safety_device, powerconsumption, 
                 max_gforce, inversions, onride_photo):
        
        super().__init__(string, name, type, image, RAS_number, date_of_construction, manufacturer, 
                         adm_maintance, validity_rapport, durance_maintance, durance_morningcheck)
        
        self.train_capacity = train_capacity
        self.number_of_trains =number_of_trains
        self.capacity_total = capacity_total
        self.capacity_hour = capacity_hour
        self.track_length = track_length
        self.max_speed = max_speed
        self.trip_duration = trip_duration
        self.max_height = max_height
        self.min_length = min_length
        self.safety_device = safety_device
        self.powerconsumption = powerconsumption
        self.max_gforce = max_gforce
        self.inversions = inversions
        self.onride_photo = onride_photo

class WaterRide(Attraction):

    def __init__(self, string, name, type, image, RAS_number, date_of_construction, manufacturer, 
                 adm_maintance, validity_rapport, durance_maintance, durance_morningcheck, 
                 boat_capacity,number_of_boats, capacity_total, capacity_hour, track_length, 
                 max_speed, trip_duration, max_height, min_length, powerconsumption, onride_photo):
        
        super().__init__(string, name, type, image, RAS_number, date_of_construction, manufacturer, 
                         adm_maintance, validity_rapport, durance_maintance, durance_morningcheck)
        
        self.boat_capacity = boat_capacity
        self.number_of_boats = number_of_boats
        self.capacity_total = capacity_total
        self.capacity_hour = capacity_hour
        self.track_length = track_length
        self.max_speed = max_speed
        self.trip_duration = trip_duration
        self.max_height = max_height
        self.min_length = min_length
        self.powerconsumption = powerconsumption
        self.onride_photo = onride_photo

class Transport(Attraction):

    def __init__(self, string, name, type, image, RAS_number, date_of_construction, manufacturer, 
                 adm_maintance, validity_rapport, durance_maintance, durance_morningcheck, 
                 wagon_capacity, number_of_wagons, capacity_total, capacity_hour, track_length, 
                 max_speed, trip_duration,  max_height, min_length, powerconsumption, onride_photo):
        
        super().__init__(string, name, type, image, RAS_number, date_of_construction, manufacturer, 
                         adm_maintance, validity_rapport, durance_maintance, durance_morningcheck)
        
        self.wagon_capacity = wagon_capacity
        self.number_of_wagons = number_of_wagons
        self.capacity_total = capacity_total
        self.capacity_hour = capacity_hour
        self.track_length = track_length
        self.max_speed = max_speed
        self.trip_duration = trip_duration
        self.max_height = max_height
        self.min_length = min_length
        self.powerconsumption = powerconsumption
        self.onride_photo = onride_photo

class Carrousel(Attraction):

    def __init__(self, string, name, type, image, RAS_number, date_of_construction, manufacturer, 
                 adm_maintance, validity_rapport, durance_maintance, durance_morningcheck, 
                 cabin_capacity, number_of_cabins, capacity_total, capacity_hour, track_length, 
                 max_speed, trip_duration, max_height, min_length, safety_device, powerconsumption,
                 onride_photo):
        
        super().__init__(string, name, type, image, RAS_number, date_of_construction, manufacturer, 
                         adm_maintance, validity_rapport, durance_maintance, durance_morningcheck)
        
        self.cabin_capacity = cabin_capacity
        self.number_of_cabins = number_of_cabins
        self.capacity_total = capacity_total
        self.capacity_hour = capacity_hour
        self.track_length = track_length
        self.max_speed = max_speed
        self.trip_duration = trip_duration
        self.max_height = max_height
        self.min_length = min_length
        self.safety_device = safety_device
        self.powerconsumption = powerconsumption
        self.onride_photo = onride_photo

class SpinPuke(Attraction):

    def __init__(self, string, name, type, image, RAS_number, date_of_construction, manufacturer, 
                 adm_maintance, validity_rapport, durance_maintance, durance_morningcheck, 
                 cabin_capacity, number_of_cabins, capacity_total, capacity_hour, track_length, 
                 max_speed, trip_duration, max_height, min_length, safety_device, powerconsumption,
                 onride_photo):
        
        super().__init__(string, name, type, image, RAS_number, date_of_construction, manufacturer, 
                         adm_maintance, validity_rapport, durance_maintance, durance_morningcheck)
        
        self.cabin_capacity = cabin_capacity
        self.number_of_cabins = number_of_cabins
        self.capacity_total = capacity_total
        self.capacity_hour = capacity_hour
        self.track_length = track_length
        self.max_speed = max_speed
        self.trip_duration = trip_duration
        self.max_height = max_height
        self.min_length = min_length
        self.safety_device = safety_device
        self.powerconsumption = powerconsumption
        self.onride_photo = onride_photo

class Playground(Attraction):

    def __init__(self, string, name, type, image, RAS_number, date_of_construction, manufacturer, 
                 adm_maintance, validity_rapport, durance_maintance, durance_morningcheck, 
                 play_equipment_capacity, number_of_play_equipment, capacity_total, max_height, 
                 min_length):
        
        super().__init__(string, name, type, image, RAS_number, date_of_construction, manufacturer, 
                         adm_maintance, validity_rapport, durance_maintance, durance_morningcheck)
        
        self.play_equipment_capacity = play_equipment_capacity
        self.number_of_play_equipment = number_of_play_equipment
        self.capacity_total = capacity_total
        self.max_height = max_height
        self.min_length = min_length








