# Holiday List Management
This repository encompasses a program the creates a Holiday Management System that has multiple feature seen below. The holidays are put together in a list format for easy access and forted by date. Holidays in list come from a holiday api seen below from a span of years (2020-2024). Weather can also be found and displayed from a weather api seen below with instructions on how to access this in the View featue below. 

## Features

### Add Holiday
User can add a holiday by inputting holiday name and date with error handling around date formatting.


### Remove Holiday
User can remove holiday by inputting holiday name and date with error handling around date formatting.


### Save Holiday List
User can save list of holidays to either CSV format or JSON format based on prefrence. File name outputted will be either 'holiday_list.csv' or 'holiday_list.json' based on user file prefrence. 

### View Holiday List
User can view all holidays and date in a distinct week based on specified year and week number. If week number in not specified (left blank), current week's holidays for specified year will be displayed. Also if no week specified, user will be asked if they would like to view weather for the holidays in the current week or not. If weather is displayed, weather shown with be relative to New York City weather. 

### Exit Holiday Management
User can exit the holiday management system with added concerns if user changed holiday list without saving list.

## File Navagation

### holiday_list_code.py
Run this python file to activate the holiday management system. From here the user can access all the features listed above. 

### holidays_json.json
This ia a json file that is read into the list of holidays management system. 

### README.md
General decription guide for Github.

### Plans
Directory that entails image of flowchart of general guide as to how flow holiday_list_code.py was constructed. Actual code is more detailed, but this was my first idea of how to move about the main menu for the holiday management system. 

### text_readins
Directory that entails .txt files with titles for features above. These files are read in by the function read_file() in the holiday_list_code.py python file.

## API Resources

### [Holiday API](https://www.timeanddate.com/holidays/us/?hol=43122559)

### [Weather API](https://www.visualcrossing.com/weather/weather-data-services/New%20%20York?v=api)