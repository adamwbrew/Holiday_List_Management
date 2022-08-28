from datetime import datetime, date
import json
import csv
from bs4 import BeautifulSoup
import requests
from dataclasses import dataclass
from config import weather_api_key_2


# -------------------------------------------
# Modify the holiday class to 
# 1. Only accept Datetime objects for date.
# 2. You may need to add additional functions
# 3. You may drop the init if you are using @dataclasses
# --------------------------------------------
@dataclass
class Holiday:
    name : str
    date: date      
    
    def __str__ (self):
        # String output
        # Holiday output when printed.
        return f"{self.name.title()} ({self.date})"
    
    def __gt__(self, other):
        return self.date > other.date

    def __ge__(self, other):
        return self.date >= other.date

    def __lt__(self, other):
        return self.date < other.date

    def __lt__(self, other):
        return self.date <= other.date
           
# -------------------------------------------
# The HolidayList class acts as a wrapper and container
# For the list of holidays
# Each method has pseudo-code instructions
# --------------------------------------------
@dataclass
class HolidayList:
    innerHolidays : list = None

    def sort(self):
        return self.innerHolidays.sort()
   
    def addHoliday(self): 
        # Make sure holidayObj is an Holiday Object by checking the type
        # Use innerHolidays.append(holidayObj) to add holiday
        # print to the user that you added a holiday
        month_max_day = {'01':'31', '02':'28', '03':'31', '04':'30', '05':'31', '06':'30', '07':'31', '08':'31', '09':'30', '10':'31', '11':'30', '12':'31'}
        holiday_str = input("Holiday: ")
        while(True):
            date_str = input("Date: ")
            date_list = str(date_str).split('-')
            if(len(date_list) != 3): print("\nError:\nInvalid date format [Format: Year-Month-Day Ex: 2020-02-02]. Try again.\n"); continue
            year_str = date_list[0]; month_str = date_list[1]; day_str = date_list[2]
            if(year_str.isdigit() == False): print("\nError:\nInvalid date, letter found in year [Format: Year-Month-Day Ex: 2020-02-02]. Try again.\n"); continue
            elif(2024 < int(year_str) or int(year_str) < 2020): print("\nError:\nInvalid date, year not in range [2020-2024], [Format: Year-Month-Day Ex: 2020-02-02]. Try again.\n"); continue
            elif(month_str.isdigit() == False): print("\nError:\nInvalid date, letter found in month [Format: Year-Month-Day Ex: 2020-02-02]. Try again.\n"); continue
            elif(12 < int(month_str) or int(month_str) < 1): print("\nError:\nInvalid date, month not in range [01-12], [Format: Year-Month-Day Ex: 2020-02-02]. Try again.\n"); continue
            elif(day_str.isdigit() == False): print("\nError:\nInvalid date, letter found in day [Format: Year-Month-Day Ex: 2020-02-02]. Try again.\n"); continue
            month_str = str(int(month_str)).zfill(2)
            if(year_str in ['2020', '2024'] and month_str == '02'):
                max_day = int(month_max_day[month_str]) + 1
            else:
                max_day = int(month_max_day[month_str])
            if(max_day < int(day_str) or int(day_str) < 1): print(f"\nError:\nInvalid date, day not in range [01-{max_day}], [Format: Year-Month-Day Ex: 2020-02-02]. Try again.\n"); continue
            else: break
        date_formatted = (datetime.strptime(date_str, '%Y-%m-%d')).date()
        holiday_str = holiday_str.strip()
        no_append = 0
        if(self.innerHolidays != None):
            for holiday in self.innerHolidays:
                if(holiday.name.lower() == holiday_str.lower() and holiday.date == date_formatted):
                    print("\nError:\nThe holiday entered is already in the holiday list.\n"); no_append+= 1; break
            if(no_append == 0): 
                holiday = Holiday(holiday_str.title(), date_formatted)
                self.innerHolidays.append(holiday)
                print(f"\nSuccess:\n{holiday} has been added to holiday list.")
        else:
            holiday = Holiday(holiday_str.title(), date_formatted)
            self.innerHolidays = [holiday]
            print(f"\nSuccess:\n{holiday} has been added to holiday list.")
        return self.innerHolidays

    def findHoliday(self): 
        # Find Holiday in innerHolidays
        # Return Holiday
        month_max_day = {'01':'31', '02':'28', '03':'31', '04':'30', '05':'31', '06':'30', '07':'31', '08':'31', '09':'30', '10':'31', '11':'30', '12':'31'}
        while(True):
            holiday_str = input("Holiday: ")
            while(True):
                date_str = input("Date: ")
                date_list = str(date_str).split('-')
                if(len(date_list) != 3): print("\nError:\nInvalid date format [Format: Year-Month-Day Ex: 2020-02-02]. Try again.\n"); continue
                year_str = date_list[0]; month_str = date_list[1]; day_str = date_list[2]
                if(year_str.isdigit() == False): print("\nError:\nInvalid date, letter found in year [Format: Year-Month-Day Ex: 2020-02-02]. Try again.\n"); continue
                elif(2024 < int(year_str) or int(year_str) < 2020): print("\nError:\nInvalid date, year not in range [2020-2024], [Format: Year-Month-Day Ex: 2020-02-02]. Try again.\n"); continue
                elif(month_str.isdigit() == False): print("\nError:\nInvalid date, letter found in month [Format: Year-Month-Day Ex: 2020-02-02]. Try again.\n"); continue
                elif(12 < int(month_str) or int(month_str) < 1): print("\nError:\nInvalid date, month not in range [01-12], [Format: Year-Month-Day Ex: 2020-02-02]. Try again.\n"); continue
                elif(day_str.isdigit() == False): print("\nError:\nInvalid date, letter found in day [Format: Year-Month-Day Ex: 2020-02-02]. Try again.\n"); continue
                month_str = str(int(month_str)).zfill(2)
                if(year_str in ['2020', '2024'] and month_str == '02'):
                    max_day = int(month_max_day[month_str]) + 1
                else:
                    max_day = int(month_max_day[month_str])
                if(max_day < int(day_str) or int(day_str) < 1): print(f"\nError:\nInvalid date, day not in range [01-{max_day}], [Format: Year-Month-Day Ex: 2020-02-02]. Try again.\n"); continue
                else: break
            date_formatted = (datetime.strptime(date_str, '%Y-%m-%d')).date()
            holiday_str = holiday_str.strip().lower()
            found = 0
            for holiday in self.innerHolidays:
                if(holiday.name.lower() == holiday_str and holiday.date == date_formatted):
                    found += 1; break
            if(found == 0): print(f"\nError:\n{holiday_str.title()} ({date_formatted}) not found. Try again.\n")
            else: break
        return holiday_str, date_formatted

    def removeHoliday(self, holiday_found, date_found): 
        # Find Holiday in innerHolidays by searching the name and date combination.
        # remove the Holiday from innerHolidays
        # inform user you deleted the holiday
        for i, holiday in enumerate(self.innerHolidays):
            if(holiday.name.lower() == holiday_found.lower() and holiday.date == date_found):
                self.innerHolidays.pop(i)
                print(f"\nSuccess:\n{holiday_found.title()} ({date_found}) has been removed from the holiday list.")
                break
        return self.innerHolidays

    def read_json(self, file_name): 
        # Read in things from json file location
        # Use addHoliday function to add holidays to inner list.
        with open(f"./{file_name}", 'r') as holiday_json:
            json_response = json.load(holiday_json)
        mini_holiday_list = json_response["holidays"]
        for holiday in mini_holiday_list:
            holiday_date = (datetime.strptime(holiday["date"], '%Y-%m-%d')).date()
            if(self.innerHolidays != None):
                append_list = 0
                for used_holiday in self.innerHolidays:
                    if(holiday["name"].lower() == used_holiday.name.lower() and holiday_date == used_holiday.date): append_list += 1; break
                if(append_list == 0):
                    self.innerHolidays.append(Holiday(holiday["name"].title(), holiday_date))
            else: 
                self.innerHolidays =[Holiday(holiday["name"].title(), holiday_date)]
        return self.innerHolidays

    def save_to_json_or_csv(self, file_name): 
        # Write out json file to selected file.
        while(True):
            desicion = input("Are you sure you want to save your changes? [y/n]: ")
            if(desicion.lower() != 'y'and desicion.lower() != 'n'): print("\nError:\nInvalid input. You must enter 'y' for yes or 'n' for no. Try again.\n"); continue
            else: break
        if(desicion == 'n'): print("\nCanceled:\nHoliday list file save canceled.\n")
        else:
            while(True):
                choice = input("Would you like to save changes to a CSV or JSON file? [csv/json]: ")
                if(choice.lower() != 'json' and choice.lower() != 'csv'): print("\nError:\nInvalid input. You must enter 'json' for a JSON file or 'csv' for a CSV file. Try again.\n"); continue
                else: break
            if(choice == 'json'):
                file_name = file_name + '.json'
                with open(f"./{file_name}", 'w') as j_file:
                    holidays = [{"holiday":holiday.name.title(), "date":holiday.date.isoformat()} for holiday in self.innerHolidays]
                    json.dump(holidays, j_file, indent=2)
            else:
                file_name = file_name + '.csv'
                with open(f"./{file_name}", 'w', newline='') as c_file:
                    write = csv.writer(c_file)
                    write.writerow(["Holiday", "Date"])
                    write.writerows([[holiday.name.title(), holiday.date] for holiday in self.innerHolidays])
            print("\nSuccess:\nYour changes have been saved.")
        return self.innerHolidays, desicion

    def scrapeHolidays(self): 
        # Scrape Holidays from https://www.timeanddate.com/holidays/us/ 
        # Remember, 2 previous years, current year, and 2  years into the future. You can scrape multiple years by adding year to the timeanddate URL. For example https://www.timeanddate.com/holidays/us/2022
        # Check to see if name and date of holiday is in innerHolidays array
        # Add non-duplicates to innerHolidays
        # Handle any exceptions. 
        month_dict = {"Jan":'1', "Feb":'2', "Mar":'3', "Apr":'4', "May":'5', "Jun":'6', "Jul":'7', "Aug":'8', "Sep":'9', "Oct":'10', "Nov":'11', "Dec":'12'}
        years = ["2020", "2021", "2022", "2023", "2024"]
        holiday_list = self.innerHolidays
        for year in years:
            holiday_list_duplicate_check = []
            url = f"https://www.timeanddate.com/holidays/us/{year}?hol=43122559"
            html_response = BeautifulSoup((requests.get(url)).text, "html.parser")
            rows = html_response.find("section", attrs={"class" : "table-data__table"}).find("table", attrs={"id" : "holidays-table"}).find("tbody").find_all("tr")
            for row in rows:
                if(row["id"][:3] == "hol"): continue
                else:
                    date_month_day = row.find("th").text.split(' ')
                    date_string = year + '-' + month_dict[date_month_day[0]] + '-' + date_month_day[1]
                    date_formatted = (datetime.strptime(date_string, '%Y-%m-%d')).date()
                    row_description = row.find_all("td")[1].text
                    row_type = row.find_all("td")[2].text
                    if(row_type.split(' ')[-1] == 'observance'): continue
                    else:
                        row_description = row_description.strip()
                        if(row_description not in holiday_list_duplicate_check):
                            holiday_list_duplicate_check.append(row_description)
                            holiday_list.append(Holiday(row_description.title(), date_formatted))
        self.innerHolidays = holiday_list
        return self.innerHolidays

    def numHolidays(self): 
        # Return the total number of holidays in innerHolidays
        return len(self.innerHolidays)
    
    def filter_holidays_by_week(self):
        # Use a Lambda function to filter by week number and save this as holidays, use the filter on innerHolidays
        # Week number is part of the the Datetime object
        # Cast filter results as list
        # return your holidays
        years = ["2020", "2021", "2022", "2023", "2024"]
        while(True):
            year_choice = input("Which Year: ")
            if(year_choice.isdigit() == False): print("\nError:\nNon-integer entity entered. Please enter an integer. Try again.\n"); continue
            elif(year_choice not in years): print(f"\nError:\nYear not in year range [{years[0]}-{years[-1]}]. Please enter a valid year. Try again.\n"); continue
            else: year_choice = int(year_choice); break
        while(True):
            week_choice = input("Which week? #[1-52, Leave blank for the current week]: ")
            if(week_choice.strip() == ''): break
            elif(week_choice.isdigit() == False): print("\nError:\nNon-integer entity entered. Please enter an integer. Try again.\n"); continue
            week_choice = int(week_choice)
            if(1 > week_choice or 52 < week_choice): print(f"\nError:\nWeek not in week range [1-52]. Please enter a valid week. Try again.\n"); continue
            else: break
        if(str(week_choice).strip() == ''):
            filtered_holiday_list = ['current', f"{date.today().isocalendar()[1]}", f"{year_choice}"]
        else:
            filtered_holiday_list = list(filter(lambda x : int(x.date.year) == year_choice and int(x.date.isocalendar()[1]) == week_choice, self.innerHolidays))
        return filtered_holiday_list

    def displayHolidaysInWeek(self, weather = None): 
        # Use your filter_holidays_by_week to get list of holidays within a week as a parameter
        # Output formated holidays in the week. 
        # * Remember to use the holiday __str__ method.
        if(self.innerHolidays == []):
            print("\nThere are no holidays in this week.")
        elif(weather != None):
            for i, holiday in enumerate(self.innerHolidays):
                if(weather[i][1] != ''):
                    print(f"{holiday} - {weather[i][0]} ({weather[i][1]})")
                else:
                    print(f"{holiday} - {weather[i][0]}")
        else:
            print()
            for i, holiday in enumerate(self.innerHolidays):
                print(holiday)

    def getWeather(self, weekNum, year): 
        # Convert weekNum to range between two days
        # Use Try / Except to catch problems
        # Query API for weather in that week range
        # Format weather information and return weather string.
        weather_for_week = []
        for day in range(1,7):
            start = date.fromisocalendar(int(year), int(weekNum), day)
            url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/New%20York/{start}/{start}?unitGroup=us&key={weather_api_key_2}&contentType=json"
            html_response = BeautifulSoup((requests.get(url)).text, "html.parser")
            conditions = json.loads(str(html_response))["days"][0]["conditions"].strip()
            description = json.loads(str(html_response))["days"][0]["description"].strip()
            weather_for_week.append([conditions, description])
        return weather_for_week

    def viewCurrentWeek(self, weather_year): 
        # Use the Datetime Module to look up current week and year
        # Use your filter_holidays_by_week function to get the list of holidays 
        # for the current week/year
        # Use your displayHolidaysInWeek function to display the holidays in the week
        # Ask user if they want to get the weather
        # If yes, use your getWeather function and display results
        while(True):
            desicion = input("Would you like to see this week's weather? [y/n]: ")
            if(desicion.lower() != 'y'and desicion.lower() != 'n'): print("\nError:\nInvalid input. You must enter 'y' for yes or 'n' for no. Try again.\n"); continue
            else:break
        week_holiday_list = list(filter(lambda x : int(x.date.year) == int(weather_year) and int(x.date.isocalendar()[1]) == date.today().isocalendar()[1], self.innerHolidays))
        return week_holiday_list, desicion


def read_file(file_name):
    with open(f"./text_readins/{file_name}", 'r') as file:
        file_output = file.readlines()
        file_output = [file_line.strip() for file_line in file_output]
        for line in file_output:
            print(line)


def main(): 
    # Large Pseudo Code steps
    # -------------------------------------
    # 1. Initialize HolidayList Object
    # 2. Load JSON file via HolidayList read_json function
    # 3. Scrape additional holidays using your HolidayList scrapeHolidays function.
    # 3. Create while loop for user to keep adding or working with the Calender
    # 4. Display User Menu (Print the menu)
    # 5. Take user input for their action based on Menu and check the user input for errors
    # 6. Run appropriate method from the HolidayList object depending on what the user input is
    # 7. Ask the User if they would like to Continue, if not, end the while loop, ending the program.  If they do wish to continue, keep the program going. 
    read_file("Title.txt")
    holidays = HolidayList()
    holidays.read_json("holidays_json.json")
    holidays.scrapeHolidays()
    holidays.sort()
    print(f"There are {holidays.numHolidays()} holidays stored in the system.")
    run = 0; change = 0; save = 0
    while(run == 0):
        while(True):
            read_file("Main_Menu.txt")
            selection = input("\nPlease choose which menu option you'd like preform by selecting the associated number. [1-5]: ")
            if(selection not in ['1', '2', '3', '4', '5']): print("\nError:\nInvalid input. Input not in menu number options. [1-5]\n")
            else:break

        if(selection == '1'): # -------------------------------------------------   Add   -----------------------------------------------------------
            read_file("Add.txt")
            holidays.addHoliday()
            holidays.sort()
            change = 1

        elif(selection == '2'): # ----------------------------------------------   Remove   ----------------------------------------------------------
            read_file("Remove.txt")
            holiday_found, date_found = holidays.findHoliday()
            holidays.removeHoliday(holiday_found, date_found)
            change = 1

        elif(selection == '3'): # -----------------------------------------------   Save   -----------------------------------------------------------
            read_file("Save.txt")
            holidays, choice = holidays.save_to_json_or_csv("holiday_list")
            holidays = HolidayList(holidays)
            if(choice =='y'): save = 1; change = 0

        elif(selection == '4'): # -----------------------------------------------   View   ----------------------------------------------------------
            read_file("View.txt")
            filitered_holidays = HolidayList(holidays.filter_holidays_by_week())
            if(filitered_holidays.innerHolidays != []):
                if(filitered_holidays.innerHolidays[0] == 'current'):
                    weather_week = filitered_holidays.innerHolidays[1]
                    weather_year = filitered_holidays.innerHolidays[2]
                    week_holidays, weather_choice = holidays.viewCurrentWeek(weather_year)
                    week_holidays = HolidayList(week_holidays)
                    if(weather_choice == 'y'):
                        weather_of_week = week_holidays.getWeather(weather_week, weather_year)
                        week_holidays.displayHolidaysInWeek(weather_of_week)
                    else:
                        week_holidays.displayHolidaysInWeek()
                else:
                    filitered_holidays.displayHolidaysInWeek()
            else:
                filitered_holidays.displayHolidaysInWeek()

        else: # -----------------------------------------------------------------   Exit   -----------------------------------------------------------
            read_file("Exit.txt")
            while(True):
                if(change == 1 and save == 0):
                    desicion = input("Are you sure you want to exit? \nYour changes will be lost. \n[y/n]: ")
                else:
                    desicion = input("Are you sure you want to exit? [y/n]: ")
                if(desicion.lower() != 'y'and desicion.lower() != 'n'): print("\nError:\nInvalid input. You must enter 'y' for yes or 'n' for no. Try again.\n"); continue
                else:break
            if(desicion == 'n'):continue
            else: print("\nGoodbye!\n"); run+=1


if __name__ == "__main__":
    main();


# Additional Hints:
# ---------------------------------------------
# You may need additional helper functions both in and out of the classes, add functions as you need to.
#
# No one function should be more then 50 lines of code, if you need more then 50 lines of code
# excluding comments, break the function into multiple functions.
#
# You can store your raw menu text, and other blocks of texts as raw text files 
# and use placeholder values with the format option.
# Example:
# In the file test.txt is "My name is {fname}, I'm {age}"
# Then you later can read the file into a string "filetxt"
# and substitute the placeholders 
# for example: filetxt.format(fname = "John", age = 36)
# This will make your code far more readable, by seperating text from code.
