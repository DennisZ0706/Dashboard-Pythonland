# Project

## The App

Application build for the technical service of Pythonland, intended for getting information and properties from all attractions and for administering, planning and monitoring inspections, maintenance and morning checks.

Application shows an interactive map of the park on which all attractions are depicted. And next to this map, all attractions are shown separately in a status bar with their own status and possible warning signals. 

Above the map, all totals are shown for each status an attraction can achieve and the total number of attractions that are present at the theme park.

By clicking on the image on the map, or clicking on the status bar of the attraction besides the map, a pop-up of the relevant attraction appears on which all information and data of this attraction is displayed and can be changed.

## Libraries used

* kivy
* os
* time
* datetime
* webbrowser
* pathlib

---

## Learned skills

* Basics of Object Orientated Programming
* Build classes and use inheritance  
* Building a GUI with kivy
* Use kv files for coding layout 
* Work with different modules
* Working with popups 
* Compare dates with eachother
* Work with HoverBehavior in kivy

<br>

* Work with CV files
* Making use-cases
* Making a gantt chart
* Making a GUI design
* Making a moscow analysis
* Basics of MS-project
* Keep track of progress with trelloo

---

## How it works

**Status attraction** 

There are 4 different statuses an attraction can achieve. An attraction can be turned off (orange), on morning check (yellow), on running (green), or on malfunction (red). 

Every day a morning check must be carried out on each attraction before it is allowed to start. This can be registered and tracked using the application. 
A morning check can be started in the pop-up of the relevant attraction with the button "Start Check". The attraction's status will change from orange to yellow and the timer will begin to count down. When the minimum time required for the morning check of the attraction has expired and the timer reaches zero, the morning check can be completed with the same button. The text of the button will change to "Voltooi Check" when this is possible and the status of the attraction will change to green, after which the attraction can be started.

Each attraction can be manually set to red status to indicate that an attraction is on malfunction and cannot be started. The big red button in the pop-up with text "Storing" serves this purpose.

**Warning Signals**

In addition to the status of an attraction, a warning signal can also be shown in the status bar of the attraction. 

There are warning signals for maintenance and for the inspection status of the attraction. Inspection warnings are indicated by a check mark and service warnings are indicated by a wrench. 

A green check mark or a green wrench means that an inspection or maintenance is taking place at that time. An orange check mark or an orange wrench means that a new planned inspection or maintenance is coming. 
And a red check mark or a red wrench means that an inspection or service has been missed or has not been registered, or that a new date has not yet been planned.

**Information**

Globally, information in the pop-up can be divided into 4 parts. 

At the top is the general information. Then comes a block with information about the inspection. In this block the validity period of an inspection report of the attraction is shown. The third block mainly contains information regarding maintenance. This shows how long a major maintenance and a morning check of the attraction takes.
The fourth block mainly shows specific characteristics of the attraction.

**Inspection**

Dates related to the inspection certificate of the attraction can be entered in the pop-up of the attraction by clicking on the "Keuring" button. Here can be entered  when the last inspection has taken place and when a next inspection is scheduled.

**Maintane**

Each attraction needs maintenance 4 times a year. These dates can also be entered in a pop-up. 

This can be done using the "onderhoud" button. When the attraction has undergone maintenance and the minimum duration in days prescribed for the relevant attraction has expired, the maintenance can be checked in the pop-up. A report of the maintenance can then be requested in the pop-up by clicking on the "Rapport" button next to the relevant maintenance.

---

## Preview

![screenshot_mainscreen](Showcase/screenshot_mainscreen.png?raw=true "Mainscreen")<br>
Mainscree

![screenshot_popup](Showcase/screenshot_popup.png?raw=true "Popup attraction")<br>
Popup attraction

![screenshot_login](Showcase/screenshot_login.png?raw=true "Login to make changes")<br>
Login to make changes

![screenshot_maintance](Showcase/screenshot_maintance.png?raw=true "Plan maintance")<br>
Plan maintance

![screenshot_morningcheck](Showcase/screenshot_morningcheck.png?raw=true "Attraction on morningcheck")<br>
Attraction on morningcheck

![screenshot_malfunction](Showcase/screenshot_malfunction.png?raw=true "Attraction on malfunction")<br>
Attraction on malfunction



