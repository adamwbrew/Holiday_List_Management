from datetime import datetime, date
import json
import csv
from bs4 import BeautifulSoup
import requests
from dataclasses import dataclass
from config import weather_api_key_2


@dataclass
class Holiday:
    """
    |
    | Holiday.name - string - name of holiday
    | Holiday.date - datetime.date - date of holiday
    |
    """
    name : str
    date: date      
    
    def __str__ (self):
        # String output
        # Holiday output when printed.
        return f"{self.name.title()} ({self.date})"
    
    def __gt__(self, other):
        # greater than method
        return self.date > other.date

    def __ge__(self, other):
        # greater than or equal to method
        return self.date >= other.date

    def __lt__(self, other):
        # less than method
        return self.date < other.date

    def __le__(self, other):
        # less than or equal to method
        return self.date <= other.date
           

@dataclass
class HolidayList:
    """
    |
    | Holiday.innerHoliday - list - list of holidays where each element is a Holiday() class
    |
    """
    innerHolidays : list = None

    def sort(self):
        # sorts holiday list based on Holiday() class magic methods
        return self.innerHolidays.sort()
   
    def addHoliday(self): 
        # Ask user for holiday information with error handling
        # than creates holiday using Holiday() class,
        # appends to innerHolidays, and
        # prints to the user that you added a holiday
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
        # Finds Holiday in innerHolidays
        # Returns Holiday
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
        # Finds Holiday in innerHolidays by searching the name and date combination.
        # Then removes the Holiday from innerHolidays
        # and informs user you deleted the holiday
        for i, holiday in enumerate(self.innerHolidays):
            if(holiday.name.lower() == holiday_found.lower() and holiday.date == date_found):
                self.innerHolidays.pop(i)
                print(f"\nSuccess:\n{holiday_found.title()} ({date_found}) has been removed from the holiday list.")
                break
        return self.innerHolidays

    def read_json(self, file_name): 
        # Read in things from json file location
        # and adds holidays to innerHoliday
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
        # Asks user if they would like to save
        # innerHolidays to either a JSON or CSV file,
        # and notifies user the information has been saved.
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
        # Scrape Holidays from https://www.timeanddate.com/holidays/us/?hol=43122559
        # and adds them to innerHolidays.
        # Holidays are added from a span of years (2020 - 2024).
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
        # filters innerHoliday by year and week number.
        # if week left blank a special output will be returned
        # so that current week can later be displayed.
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
        # Displays innerHolidays.
        # If no holidays in innerHolidays special print will occur.
        # If weather parameter not None, weather will be displayed with associated holidays.
        # other wise innerHolidays will be displayed based on Holiday class __str__ method.
        if(self.innerHolidays == []):
            print("\nThere are no holidays in this week.")
        elif(weather != None):
            print()
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
        # Returns week/year weather results
        # Weather results based on New York City weather
        # Scrapes Weather from https://www.visualcrossing.com/weather/weather-data-services/New%20%20York?v=api
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
        # Ask user if they want to get the weather.
        # If yes, use your getWeather function and display results.
        # Uses lambda function to find holidays based on current week and year
        while(True):
            desicion = input("Would you like to see this week's weather? [y/n]: ")
            if(desicion.lower() != 'y'and desicion.lower() != 'n'): print("\nError:\nInvalid input. You must enter 'y' for yes or 'n' for no. Try again.\n"); continue
            else:break
        week_holiday_list = list(filter(lambda x : int(x.date.year) == int(weather_year) and int(x.date.isocalendar()[1]) == date.today().isocalendar()[1], self.innerHolidays))
        return week_holiday_list, desicion


def read_file(file_name):
    # reads .txt files from text_readins
    with open(f"./text_readins/{file_name}", 'r') as file:
        file_output = file.readlines()
        file_output = [file_line.strip() for file_line in file_output]
        for line in file_output:
            print(line)


def main(): 
    # Main user functionality with 5 main features:
    #   1: Add Holiday
    #   2: Remove Holiday
    #   3: Save Holiday List
    #   4: View Holiday List
    #   5: Exit Holiday Management System
    # Functionality takes place in while loop 
    # for inifinte looping if needed for user
    read_file("Title.txt")
    holidays = HolidayList()
    holidays.read_json("holidays_json.json"); holidays.scrapeHolidays()
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
            read_file("Add.txt"); holidays.addHoliday(); holidays.sort()
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
                    weather_week = filitered_holidays.innerHolidays[1]; weather_year = filitered_holidays.innerHolidays[2]
                    week_holidays, weather_choice = holidays.viewCurrentWeek(weather_year)
                    week_holidays = HolidayList(week_holidays)
                    if(weather_choice == 'y'):
                        weather_of_week = week_holidays.getWeather(weather_week, weather_year)
                        week_holidays.displayHolidaysInWeek(weather_of_week)
                    else: week_holidays.displayHolidaysInWeek()
                else: filitered_holidays.displayHolidaysInWeek()
            else: filitered_holidays.displayHolidaysInWeek()
        else: # -----------------------------------------------------------------   Exit   -----------------------------------------------------------
            read_file("Exit.txt")
            while(True):
                if(change == 1 and save == 0): desicion = input("Are you sure you want to exit? \nYour changes will be lost. \n[y/n]: ")
                else: desicion = input("Are you sure you want to exit? [y/n]: ")
                if(desicion.lower() != 'y'and desicion.lower() != 'n'): print("\nError:\nInvalid input. You must enter 'y' for yes or 'n' for no. Try again.\n"); continue
                else:break
            if(desicion == 'n'):continue
            else: print("\nGoodbye!"); run+=1

if __name__ == "__main__":
    main();