from classes import *

# Hoover colors

hover_color = (183/255, 221/255, 29/255, 255/255)
hover_outline = (37/255, 123/255, 58/255, 255/255)

# Number of days before warning that test or maintance is upcoming

warn_test = 14
warn_maintance = 14

# users

user1 = 'user'
user2 = ''
user3 = ''
user4 = ''
user5 = ''
user6 = ''
user7 = ''
user8 = ''
user9 = ''
user10 = ''

users = [user1, user2, user3, user4, user5, user6, user7, user8, user9, user10]
users_used = []

for user in users:
    if user != '':
        users_used.append(user)

# passwords

password1 = '0000'
password2 = ''
password3 = ''
password4 = ''
password5 = ''
password6 = ''
password7 = ''
password8 = ''
password9 = ''
password10 = ''

passwords = [password1, password2, password3, password4, password5, password6, password7, password8, password9, password10]
passwords_used = []

for password in passwords:
    if password != '':
        passwords_used.append(password)

# Variables to adjust openinghours

# monday
monday_open = 9
monday_closed = 18

# tuesday
tuesday_open = "closed"
tuesday_closed = "closed"

# wednesday
wednesday_open = 9
wednesday_closed = 18

# thursday
thursday_open = 9
thursday_closed = 18

# friday
friday_open = 9
friday_closed = 18

# saturday
saturday_open = 9
saturday_closed = 18

# sunday
sunday_open = 9
sunday_closed = 18

# openinghours objecs

Monday = OpeningHours(monday_open, monday_closed)
Tuesday = OpeningHours(tuesday_open, tuesday_closed)
Wednesday = OpeningHours(wednesday_open, wednesday_closed)
Thursday = OpeningHours(thursday_open, thursday_closed)
Friday = OpeningHours(friday_open, friday_closed)
Saturday = OpeningHours(saturday_open, saturday_closed)
Sunday = OpeningHours(sunday_open, sunday_closed)

# manufacturer objects

vekoma = Manufacturer("Vekoma", "+31 (0)475 40 92 22", "info@Vekoma.nl")
gerstlauer = Manufacturer("Gerstlauer Amasument Rides", "+49 8281 9968-0", 
                          "info(@)gerstlauer-rides.de")
zierer = Manufacturer("Zierer", "+49 991 9106-0", "info@zierer.com")
reverchon = Manufacturer("Reverchon", "+33 1 60 74 94 00", "sales@reverchon-attraction.com")
barcachoc = Manufacturer("Barca-Choc", "+46 36 168325", "info@barcachoc.se")
mackrides = Manufacturer("MACK Rides", "+49 7681 20000", "info@mack-rides.com")
metallbauemmeln = Manufacturer("Metallbau Emmeln", "+49(0)5932/7255-0", 
                               "info@metallbau-emmeln.de")
kumbak = Manufacturer("Kumbak", "+31 (0)49 558 31 00", "info@kumbak.nl")
wooddesign = Manufacturer("Wooddesign", "+31 (0)73 657 05 05", "rides@wooddesign.nl")
hussparkattractions = Manufacturer("Huss Park Attractions", "49 (0)421 499 00-0",
                                   "sales@hussrides.com")
krekel = Manufacturer("Krekel", "+31 (0)68 657 14 65", "info@krekel.com")
schwarzkopf = Manufacturer("Schwarzkopf", "+41 7321 67900", "info@schwarzkopf.de")
bumpercars = Manufacturer("Bumper Cars", "+31 (0)74 243 44 33", "info@bumpercars.nl")
kmg = Manufacturer("KMG", "+31 (0)54 529 45 45", "info@kmg.nl")
vanegdom = Manufacturer("Van Egdom", "31 (0)30 666 21 04", "info@vanegdom.com")
hajump = Manufacturer("HaJump", "+32 56 52 06 27", "info@hajump.be")
eliplay = Manufacturer("ELI Play", "+31 (0)613 249 848", "info@eliplay.com")
donkergroen = Manufacturer("DonkerGroen", "0515 72 65 25", "info@donkergroen.nl")

# maintance objects

maintance_adm1 = Administration( 'Attraction1',
                                 'Database/Attractions/attraction_1/maintance/maintance_1.txt',
                                 'Database/Attractions/attraction_1/maintance/maintance_2.txt',
                                 'Database/Attractions/attraction_1/maintance/maintance_3.txt',
                                 'Database/Attractions/attraction_1/maintance/maintance_4.txt',
                                 'Database/Attractions/attraction_1/maintance/rapport_1/',
                                 'Database/Attractions/attraction_1/maintance/rapport_2',
                                 'Database/Attractions/attraction_1/maintance/rapport_3',
                                 'Database/Attractions/attraction_1/maintance/rapport_4',
                                 'Database/Attractions/attraction_1/inspection/last_inspection.txt',
                                 'Database/Attractions/attraction_1/inspection/next_inspection.txt')

maintance_adm2 = Administration( 'Attraction2',
                                 'Database/Attractions/attraction_2/maintance/maintance_1.txt',
                                 'Database/Attractions/attraction_2/maintance/maintance_2.txt',
                                 'Database/Attractions/attraction_2/maintance/maintance_3.txt',
                                 'Database/Attractions/attraction_2/maintance/maintance_4.txt',
                                 'Database/Attractions/attraction_2/maintance/rapport_1',
                                 'Database/Attractions/attraction_2/maintance/rapport_2',
                                 'Database/Attractions/attraction_2/maintance/rapport_3',
                                 'Database/Attractions/attraction_2/maintance/rapport_4',
                                 'Database/Attractions/attraction_2/inspection/last_inspection.txt',
                                 'Database/Attractions/attraction_2/inspection/next_inspection.txt')

maintance_adm3 = Administration( 'Attraction3',
                                 'Database/Attractions/attraction_3/maintance/maintance_1.txt',
                                 'Database/Attractions/attraction_3/maintance/maintance_2.txt',
                                 'Database/Attractions/attraction_3/maintance/maintance_3.txt',
                                 'Database/Attractions/attraction_3/maintance/maintance_4.txt',
                                 'Database/Attractions/attraction_3/maintance/rapport_1',
                                 'Database/Attractions/attraction_3/maintance/rapport_2',
                                 'Database/Attractions/attraction_3/maintance/rapport_3',
                                 'Database/Attractions/attraction_3/maintance/rapport_4',
                                 'Database/Attractions/attraction_3/inspection/last_inspection.txt',
                                 'Database/Attractions/attraction_3/inspection/next_inspection.txt')

maintance_adm4 = Administration( 'Attraction4',
                                 'Database/Attractions/attraction_4/maintance/maintance_1.txt',
                                 'Database/Attractions/attraction_4/maintance/maintance_2.txt',
                                 'Database/Attractions/attraction_4/maintance/maintance_3.txt',
                                 'Database/Attractions/attraction_4/maintance/maintance_4.txt',
                                 'Database/Attractions/attraction_4/maintance/rapport_1',
                                 'Database/Attractions/attraction_4/maintance/rapport_2',
                                 'Database/Attractions/attraction_4/maintance/rapport_3',
                                 'Database/Attractions/attraction_4/maintance/rapport_4',
                                 'Database/Attractions/attraction_4/inspection/last_inspection.txt',
                                 'Database/Attractions/attraction_4/inspection/next_inspection.txt')

maintance_adm5 = Administration( 'Attraction5',
                                 'Database/Attractions/attraction_5/maintance/maintance_1.txt',
                                 'Database/Attractions/attraction_5/maintance/maintance_2.txt',
                                 'Database/Attractions/attraction_5/maintance/maintance_3.txt',
                                 'Database/Attractions/attraction_5/maintance/maintance_4.txt',
                                 'Database/Attractions/attraction_5/maintance/rapport_1',
                                 'Database/Attractions/attraction_5/maintance/rapport_2',
                                 'Database/Attractions/attraction_5/maintance/rapport_3',
                                 'Database/Attractions/attraction_5/maintance/rapport_4',
                                 'Database/Attractions/attraction_5/inspection/last_inspection.txt',
                                 'Database/Attractions/attraction_5/inspection/next_inspection.txt')

maintance_adm6 = Administration( 'Attraction6',
                                 'Database/Attractions/attraction_6/maintance/maintance_1.txt',
                                 'Database/Attractions/attraction_6/maintance/maintance_2.txt',
                                 'Database/Attractions/attraction_6/maintance/maintance_3.txt',
                                 'Database/Attractions/attraction_6/maintance/maintance_4.txt',
                                 'Database/Attractions/attraction_6/maintance/rapport_1',
                                 'Database/Attractions/attraction_6/maintance/rapport_2',
                                 'Database/Attractions/attraction_6/maintance/rapport_3',
                                 'Database/Attractions/attraction_6/maintance/rapport_4',
                                 'Database/Attractions/attraction_6/inspection/last_inspection.txt',
                                 'Database/Attractions/attraction_6/inspection/next_inspection.txt')

maintance_adm7 = Administration( 'Attraction7',
                                 'Database/Attractions/attraction_7/maintance/maintance_1.txt',
                                 'Database/Attractions/attraction_7/maintance/maintance_2.txt',
                                 'Database/Attractions/attraction_7/maintance/maintance_3.txt',
                                 'Database/Attractions/attraction_7/maintance/maintance_4.txt',
                                 'Database/Attractions/attraction_7/maintance/rapport_1',
                                 'Database/Attractions/attraction_7/maintance/rapport_2',
                                 'Database/Attractions/attraction_7/maintance/rapport_3',
                                 'Database/Attractions/attraction_7/maintance/rapport_4',
                                 'Database/Attractions/attraction_7/inspection/last_inspection.txt',
                                 'Database/Attractions/attraction_7/inspection/next_inspection.txt')

maintance_adm8 = Administration( 'Attraction8',
                                 'Database/Attractions/attraction_8/maintance/maintance_1.txt',
                                 'Database/Attractions/attraction_8/maintance/maintance_2.txt',
                                 'Database/Attractions/attraction_8/maintance/maintance_3.txt',
                                 'Database/Attractions/attraction_8/maintance/maintance_4.txt',
                                 'Database/Attractions/attraction_8/maintance/rapport_1',
                                 'Database/Attractions/attraction_8/maintance/rapport_2',
                                 'Database/Attractions/attraction_8/maintance/rapport_3',
                                 'Database/Attractions/attraction_8/maintance/rapport_4',
                                 'Database/Attractions/attraction_8/inspection/last_inspection.txt',
                                 'Database/Attractions/attraction_8/inspection/next_inspection.txt')

maintance_adm9 = Administration( 'Attraction9',
                                 'Database/Attractions/attraction_9/maintance/maintance_1.txt',
                                 'Database/Attractions/attraction_9/maintance/maintance_2.txt',
                                 'Database/Attractions/attraction_9/maintance/maintance_3.txt',
                                 'Database/Attractions/attraction_9/maintance/maintance_4.txt',
                                 'Database/Attractions/attraction_9/maintance/rapport_1',
                                 'Database/Attractions/attraction_9/maintance/rapport_2',
                                 'Database/Attractions/attraction_9/maintance/rapport_3',
                                 'Database/Attractions/attraction_9/maintance/rapport_4',
                                 'Database/Attractions/attraction_9/inspection/last_inspection.txt',
                                 'Database/Attractions/attraction_9/inspection/next_inspection.txt')

maintance_adm10 = Administration('Attraction10',
                                 'Database/Attractions/attraction_10/maintance/maintance_1.txt',
                                 'Database/Attractions/attraction_10/maintance/maintance_2.txt',
                                 'Database/Attractions/attraction_10/maintance/maintance_3.txt',
                                 'Database/Attractions/attraction_10/maintance/maintance_4.txt',
                                 'Database/Attractions/attraction_10/maintance/rapport_1',
                                 'Database/Attractions/attraction_10/maintance/rapport_2',
                                 'Database/Attractions/attraction_10/maintance/rapport_3',
                                 'Database/Attractions/attraction_10/maintance/rapport_4',
                                 'Database/Attractions/attraction_10/inspection/last_inspection.txt',
                                 'Database/Attractions/attraction_10/inspection/next_inspection.txt')

maintance_adm11 = Administration('Attraction11',
                                 'Database/Attractions/attraction_11/maintance/maintance_1.txt',
                                 'Database/Attractions/attraction_11/maintance/maintance_2.txt',
                                 'Database/Attractions/attraction_11/maintance/maintance_3.txt',
                                 'Database/Attractions/attraction_11/maintance/maintance_4.txt',
                                 'Database/Attractions/attraction_11/maintance/rapport_1',
                                 'Database/Attractions/attraction_11/maintance/rapport_2',
                                 'Database/Attractions/attraction_11/maintance/rapport_3',
                                 'Database/Attractions/attraction_11/maintance/rapport_4',
                                 'Database/Attractions/attraction_11/inspection/last_inspection.txt',
                                 'Database/Attractions/attraction_11/inspection/next_inspection.txt')

maintance_adm12 = Administration('Attraction12',
                                 'Database/Attractions/attraction_12/maintance/maintance_1.txt',
                                 'Database/Attractions/attraction_12/maintance/maintance_2.txt',
                                 'Database/Attractions/attraction_12/maintance/maintance_3.txt',
                                 'Database/Attractions/attraction_12/maintance/maintance_4.txt',
                                 'Database/Attractions/attraction_12/maintance/rapport_1',
                                 'Database/Attractions/attraction_12/maintance/rapport_2',
                                 'Database/Attractions/attraction_12/maintance/rapport_3',
                                 'Database/Attractions/attraction_12/maintance/rapport_4',
                                 'Database/Attractions/attraction_12/inspection/last_inspection.txt',
                                 'Database/Attractions/attraction_12/inspection/next_inspection.txt')

maintance_adm13 = Administration( 'Attraction13',
                                 'Database/Attractions/attraction_13/maintance/maintance_1.txt',
                                 'Database/Attractions/attraction_13/maintance/maintance_2.txt',
                                 'Database/Attractions/attraction_13/maintance/maintance_3.txt',
                                 'Database/Attractions/attraction_13/maintance/maintance_4.txt',
                                 'Database/Attractions/attraction_13/maintance/rapport_1',
                                 'Database/Attractions/attraction_13/maintance/rapport_2',
                                 'Database/Attractions/attraction_13/maintance/rapport_3',
                                 'Database/Attractions/attraction_13/maintance/rapport_4',
                                 'Database/Attractions/attraction_13/inspection/last_inspection.txt',
                                 'Database/Attractions/attraction_13/inspection/next_inspection.txt')

maintance_adm14 = Administration( 'Attraction14',
                                 'Database/Attractions/attraction_14/maintance/maintance_1.txt',
                                 'Database/Attractions/attraction_14/maintance/maintance_2.txt',
                                 'Database/Attractions/attraction_14/maintance/maintance_3.txt',
                                 'Database/Attractions/attraction_14/maintance/maintance_4.txt',
                                 'Database/Attractions/attraction_14/maintance/rapport_1',
                                 'Database/Attractions/attraction_14/maintance/rapport_2',
                                 'Database/Attractions/attraction_14/maintance/rapport_3',
                                 'Database/Attractions/attraction_14/maintance/rapport_4',
                                 'Database/Attractions/attraction_14/inspection/last_inspection.txt',
                                 'Database/Attractions/attraction_14/inspection/next_inspection.txt')

maintance_adm15 = Administration( 'Attraction15',
                                 'Database/Attractions/attraction_15/maintance/maintance_1.txt',
                                 'Database/Attractions/attraction_15/maintance/maintance_2.txt',
                                 'Database/Attractions/attraction_15/maintance/maintance_3.txt',
                                 'Database/Attractions/attraction_15/maintance/maintance_4.txt',
                                 'Database/Attractions/attraction_15/maintance/rapport_1',
                                 'Database/Attractions/attraction_15/maintance/rapport_2',
                                 'Database/Attractions/attraction_15/maintance/rapport_3',
                                 'Database/Attractions/attraction_15/maintance/rapport_4',
                                 'Database/Attractions/attraction_15/inspection/last_inspection.txt',
                                 'Database/Attractions/attraction_15/inspection/next_inspection.txt')

maintance_adm16 = Administration( 'Attraction16',
                                 'Database/Attractions/attraction_16/maintance/maintance_1.txt',
                                 'Database/Attractions/attraction_16/maintance/maintance_2.txt',
                                 'Database/Attractions/attraction_16/maintance/maintance_3.txt',
                                 'Database/Attractions/attraction_16/maintance/maintance_4.txt',
                                 'Database/Attractions/attraction_16/maintance/rapport_1',
                                 'Database/Attractions/attraction_16/maintance/rapport_2',
                                 'Database/Attractions/attraction_16/maintance/rapport_3',
                                 'Database/Attractions/attraction_16/maintance/rapport_4',
                                 'Database/Attractions/attraction_16/inspection/last_inspection.txt',
                                 'Database/Attractions/attraction_16/inspection/next_inspection.txt')

maintance_adm17 = Administration( 'Attraction17',
                                 'Database/Attractions/attraction_17/maintance/maintance_1.txt',
                                 'Database/Attractions/attraction_17/maintance/maintance_2.txt',
                                 'Database/Attractions/attraction_17/maintance/maintance_3.txt',
                                 'Database/Attractions/attraction_17/maintance/maintance_4.txt',
                                 'Database/Attractions/attraction_17/maintance/rapport_1',
                                 'Database/Attractions/attraction_17/maintance/rapport_2',
                                 'Database/Attractions/attraction_17/maintance/rapport_3',
                                 'Database/Attractions/attraction_17/maintance/rapport_4',
                                 'Database/Attractions/attraction_17/inspection/last_inspection.txt',
                                 'Database/Attractions/attraction_17/inspection/next_inspection.txt')

maintance_adm18 = Administration('Attraction18',
                                 'Database/Attractions/attraction_18/maintance/maintance_1.txt',
                                 'Database/Attractions/attraction_18/maintance/maintance_2.txt',
                                 'Database/Attractions/attraction_18/maintance/maintance_3.txt',
                                 'Database/Attractions/attraction_18/maintance/maintance_4.txt',
                                 'Database/Attractions/attraction_18/maintance/rapport_1',
                                 'Database/Attractions/attraction_18/maintance/rapport_2',
                                 'Database/Attractions/attraction_18/maintance/rapport_3',
                                 'Database/Attractions/attraction_18/maintance/rapport_4',
                                 'Database/Attractions/attraction_18/inspection/last_inspection.txt',
                                 'Database/Attractions/attraction_18/inspection/next_inspection.txt')

maintance_adm19 = Administration( 'Attraction19',
                                 'Database/Attractions/attraction_19/maintance/maintance_1.txt',
                                 'Database/Attractions/attraction_19/maintance/maintance_2.txt',
                                 'Database/Attractions/attraction_19/maintance/maintance_3.txt',
                                 'Database/Attractions/attraction_19/maintance/maintance_4.txt',
                                 'Database/Attractions/attraction_19/maintance/rapport_1',
                                 'Database/Attractions/attraction_19/maintance/rapport_2',
                                 'Database/Attractions/attraction_19/maintance/rapport_3',
                                 'Database/Attractions/attraction_19/maintance/rapport_4',
                                 'Database/Attractions/attraction_19/inspection/last_inspection.txt',
                                 'Database/Attractions/attraction_19/inspection/next_inspection.txt')

maintance_adm20 = Administration('Attraction20',
                                 'Database/Attractions/attraction_20/maintance/maintance_1.txt',
                                 'Database/Attractions/attraction_20/maintance/maintance_2.txt',
                                 'Database/Attractions/attraction_20/maintance/maintance_3.txt',
                                 'Database/Attractions/attraction_20/maintance/maintance_4.txt',
                                 'Database/Attractions/attraction_20/maintance/rapport_1',
                                 'Database/Attractions/attraction_20/maintance/rapport_2',
                                 'Database/Attractions/attraction_20/maintance/rapport_3',
                                 'Database/Attractions/attraction_20/maintance/rapport_4',
                                 'Database/Attractions/attraction_20/inspection/last_inspection.txt',
                                 'Database/Attractions/attraction_20/inspection/next_inspection.txt')

maintance_adm21 = Administration('Attraction21',
                                 'Database/Attractions/attraction_21/maintance/maintance_1.txt',
                                 'Database/Attractions/attraction_21/maintance/maintance_2.txt',
                                 'Database/Attractions/attraction_21/maintance/maintance_3.txt',
                                 'Database/Attractions/attraction_21/maintance/maintance_4.txt',
                                 'Database/Attractions/attraction_21/maintance/rapport_1',
                                 'Database/Attractions/attraction_21/maintance/rapport_2',
                                 'Database/Attractions/attraction_21/maintance/rapport_3',
                                 'Database/Attractions/attraction_21/maintance/rapport_4',
                                 'Database/Attractions/attraction_21/inspection/last_inspection.txt',
                                 'Database/Attractions/attraction_21/inspection/next_inspection.txt')

maintance_adm22 = Administration('Attraction22',
                                 'Database/Attractions/attraction_22/maintance/maintance_1.txt',
                                 'Database/Attractions/attraction_22/maintance/maintance_2.txt',
                                 'Database/Attractions/attraction_22/maintance/maintance_3.txt',
                                 'Database/Attractions/attraction_22/maintance/maintance_4.txt',
                                 'Database/Attractions/attraction_22/maintance/rapport_1',
                                 'Database/Attractions/attraction_22/maintance/rapport_2',
                                 'Database/Attractions/attraction_22/maintance/rapport_3',
                                 'Database/Attractions/attraction_22/maintance/rapport_4',
                                 'Database/Attractions/attraction_22/inspection/last_inspection.txt',
                                 'Database/Attractions/attraction_22/inspection/next_inspection.txt')

maintance_adm23 = Administration('Attraction23',
                                 'Database/Attractions/attraction_23/maintance/maintance_1.txt',
                                 'Database/Attractions/attraction_23/maintance/maintance_2.txt',
                                 'Database/Attractions/attraction_23/maintance/maintance_3.txt',
                                 'Database/Attractions/attraction_23/maintance/maintance_4.txt',
                                 'Database/Attractions/attraction_23/maintance/rapport_1',
                                 'Database/Attractions/attraction_23/maintance/rapport_2',
                                 'Database/Attractions/attraction_23/maintance/rapport_3',
                                 'Database/Attractions/attraction_23/maintance/rapport_4',
                                 'Database/Attractions/attraction_23/inspection/last_inspection.txt',
                                 'Database/Attractions/attraction_23/inspection/next_inspection.txt')

maintance_adm24 = Administration('Attraction24',
                                 'Database/Attractions/attraction_24/maintance/maintance_1.txt',
                                 'Database/Attractions/attraction_24/maintance/maintance_2.txt',
                                 'Database/Attractions/attraction_24/maintance/maintance_3.txt',
                                 'Database/Attractions/attraction_24/maintance/maintance_4.txt',
                                 'Database/Attractions/attraction_24/maintance/rapport_1',
                                 'Database/Attractions/attraction_24/maintance/rapport_2',
                                 'Database/Attractions/attraction_24/maintance/rapport_3',
                                 'Database/Attractions/attraction_24/maintance/rapport_4',
                                 'Database/Attractions/attraction_24/inspection/last_inspection.txt',
                                 'Database/Attractions/attraction_24/inspection/next_inspection.txt')

maintance_adm25 = Administration('Attraction25',
                                 'Database/Attractions/attraction_25/maintance/maintance_1.txt',
                                 'Database/Attractions/attraction_25/maintance/maintance_2.txt',
                                 'Database/Attractions/attraction_25/maintance/maintance_3.txt',
                                 'Database/Attractions/attraction_25/maintance/maintance_4.txt',
                                 'Database/Attractions/attraction_25/maintance/rapport_1',
                                 'Database/Attractions/attraction_25/maintance/rapport_2',
                                 'Database/Attractions/attraction_25/maintance/rapport_3',
                                 'Database/Attractions/attraction_25/maintance/rapport_4',
                                 'Database/Attractions/attraction_25/inspection/last_inspection.txt',
                                 'Database/Attractions/attraction_25/inspection/next_inspection.txt')


maintance_adm26 = Administration('Attraction26',
                                 'Database/Attractions/attraction_26/maintance/maintance_1.txt',
                                 'Database/Attractions/attraction_26/maintance/maintance_2.txt',
                                 'Database/Attractions/attraction_26/maintance/maintance_3.txt',
                                 'Database/Attractions/attraction_26/maintance/maintance_4.txt',
                                 'Database/Attractions/attraction_26/maintance/rapport_1',
                                 'Database/Attractions/attraction_26/maintance/rapport_2',
                                 'Database/Attractions/attraction_26/maintance/rapport_3',
                                 'Database/Attractions/attraction_26/maintance/rapport_4',
                                 'Database/Attractions/attraction_26/inspection/last_inspection.txt',
                                 'Database/Attractions/attraction_26/inspection/next_inspection.txt')

maintance_adm27 = Administration('Attraction27',
                                 'Database/Attractions/attraction_27/maintance/maintance_1.txt',
                                 'Database/Attractions/attraction_27/maintance/maintance_2.txt',
                                 'Database/Attractions/attraction_27/maintance/maintance_3.txt',
                                 'Database/Attractions/attraction_27/maintance/maintance_4.txt',
                                 'Database/Attractions/attraction_27/maintance/rapport_1',
                                 'Database/Attractions/attraction_27/maintance/rapport_2',
                                 'Database/Attractions/attraction_27/maintance/rapport_3',
                                 'Database/Attractions/attraction_27/maintance/rapport_4',
                                 'Database/Attractions/attraction_27/inspection/last_inspection.txt',
                                 'Database/Attractions/attraction_27/inspection/next_inspection.txt')

maintance_adm28 = Administration('Attraction28',
                                 'Database/Attractions/attraction_28/maintance/maintance_1.txt',
                                 'Database/Attractions/attraction_28/maintance/maintance_2.txt',
                                 'Database/Attractions/attraction_28/maintance/maintance_3.txt',
                                 'Database/Attractions/attraction_28/maintance/maintance_4.txt',
                                 'Database/Attractions/attraction_28/maintance/rapport_1',
                                 'Database/Attractions/attraction_28/maintance/rapport_2',
                                 'Database/Attractions/attraction_28/maintance/rapport_3',
                                 'Database/Attractions/attraction_28/maintance/rapport_4',
                                 'Database/Attractions/attraction_28/inspection/last_inspection.txt',
                                 'Database/Attractions/attraction_28/inspection/next_inspection.txt')

maintance_adm29 = Administration('Attraction29',
                                 'Database/Attractions/attraction_29/maintance/maintance_1.txt',
                                 'Database/Attractions/attraction_29/maintance/maintance_2.txt',
                                 'Database/Attractions/attraction_29/maintance/maintance_3.txt',
                                 'Database/Attractions/attraction_29/maintance/maintance_4.txt',
                                 'Database/Attractions/attraction_29/maintance/rapport_1',
                                 'Database/Attractions/attraction_29/maintance/rapport_2',
                                 'Database/Attractions/attraction_29/maintance/rapport_3',
                                 'Database/Attractions/attraction_29/maintance/rapport_4',
                                 'Database/Attractions/attraction_29/inspection/last_inspection.txt',
                                 'Database/Attractions/attraction_29/inspection/next_inspection.txt')

maintance_adm30 = Administration('Attraction30',
                                 'Database/Attractions/attraction_30/maintance/maintance_1.txt',
                                 'Database/Attractions/attraction_30/maintance/maintance_2.txt',
                                 'Database/Attractions/attraction_30/maintance/maintance_3.txt',
                                 'Database/Attractions/attraction_30/maintance/maintance_4.txt',
                                 'Database/Attractions/attraction_30/maintance/rapport_1',
                                 'Database/Attractions/attraction_30/maintance/rapport_2',
                                 'Database/Attractions/attraction_30/maintance/rapport_3',
                                 'Database/Attractions/attraction_30/maintance/rapport_4',
                                 'Database/Attractions/attraction_30/inspection/last_inspection.txt',
                                 'Database/Attractions/attraction_30/inspection/next_inspection.txt')

maintance_adm31 = Administration('Attraction31',
                                 'Database/Attractions/attraction_31/maintance/maintance_1.txt',
                                 'Database/Attractions/attraction_31/maintance/maintance_2.txt',
                                 'Database/Attractions/attraction_31/maintance/maintance_3.txt',
                                 'Database/Attractions/attraction_31/maintance/maintance_4.txt',
                                 'Database/Attractions/attraction_31/maintance/rapport_1',
                                 'Database/Attractions/attraction_31/maintance/rapport_2',
                                 'Database/Attractions/attraction_31/maintance/rapport_3',
                                 'Database/Attractions/attraction_31/maintance/rapport_4',
                                 'Database/Attractions/attraction_31/inspection/last_inspection.txt',
                                 'Database/Attractions/attraction_31/inspection/next_inspection.txt')

maintance_adm32 = Administration('Attraction32',
                                 'Database/Attractions/attraction_32/maintance/maintance_1.txt',
                                 'Database/Attractions/attraction_32/maintance/maintance_2.txt',
                                 'Database/Attractions/attraction_32/maintance/maintance_3.txt',
                                 'Database/Attractions/attraction_32/maintance/maintance_4.txt',
                                 'Database/Attractions/attraction_32/maintance/rapport_1',
                                 'Database/Attractions/attraction_32/maintance/rapport_2',
                                 'Database/Attractions/attraction_32/maintance/rapport_3',
                                 'Database/Attractions/attraction_32/maintance/rapport_4',
                                 'Database/Attractions/attraction_32/inspection/last_inspection.txt',
                                 'Database/Attractions/attraction_32/inspection/next_inspection.txt')


