#!/usr/bin/env python3

"""
_____.___.           __
\__  |   |____      |__| ______
 /   |   \__  \     |  |/  ___/
 \____   |/ __ \_   |  |\___ \
 / ______(____  /\__|  /____  >
 \/           \/\______|    \/  by XiKuuKy

Yet Another Journal Software
"""
help_text = """
No argument supplied. Try:

    yajs open <date> - open an entry
    yajs new <date> <title - optional>
    yajs day_view <date>

<date> format - \"<month> <day>, <year>\"
"""
from sys import argv, exit
from os import mkdir, makedirs, listdir
from os.path import exists, join
from time import localtime, strftime, sleep
from pathlib import Path
import subprocess

# takes a path as an input and checks for the paths existence, if it doesn't exist it will create it
def path_creation(path):
    if exists(path) == True:
        return True
    else:
        makedirs(path)
        path_creation(path) # recursive function!!

# takes a date formated as "<month> <day>, <year>" and returns a list of [year, month, day]
def year_month_day(date):
    year = date.split(",")[1].replace(" ", "")
    day = date.split(",")[0].split(" ")[1]
    month = date.split(",")[0].split(" ")[0]
    return [year, month, day]

# creates a new entry
def arg_new():
    udate = argv[2] # get the user suplied date from the 3 positional argument
    date = year_month_day(argv[2]) # convert it to a list

    if len(argv) == 4: # check for a title
        title = argv[3] # if there is title use it
    else:
        title = "" # else: empty title


    date_path = str(Path.home()) + "/Documents/yajs/" + "/".join(date) # set as the Doc/year/month/day path
    path_creation(date_path) # create the path if it doesn't exist
    right_now = strftime("%H-%M", localtime()) # get the current time from the computer's time
    if title != "": # if there is a title, add it to the file name and the title of the document
        specific_path = date_path + "/" + right_now + " - " + title + ".org"
        open(specific_path, 'w').write("* " + udate + " " + right_now + " : " + title + "\n")
    else: # else, don't
        specific_path = date_path + "/" + right_now + ".org"
        open(specific_path, 'w').write("* " + udate + " " + right_now + " : \n")
    subprocess.call(["emacs", specific_path]) # ask emacs to open our file pretty please

def arg_open():
    date = year_month_day(argv[2]) # get our user date again and convert it right away
    date_path = str(Path.home()) + "/Documents/yajs/" + "/".join(date) # get the path Doc/year/month/day/
    incrementer = 0 # incrementer for the following for loop to number the options
    for i in listdir(date_path): # get the names of all the files in the directory of that day
        print(str(incrementer + 1) + ". " + i.replace(".org", "")) # print the name of the file minus the .org extension
        incrementer+=1 # increment ya!

    choice_n = int(input("Open: "))-1 # ask the user for their choice
    choice = listdir(date_path)[choice_n] # select their choice
    print()
    for i in list(open(date_path + "/" + choice).read()): # index each character in a file
        print(i, end="") # print each character (looks cooler than just printing the file all at once)
        sleep(0.004) # wait a moment, we're in no rush!

def arg_day_view():
    date = year_month_day(argv[2]) # get the date in format again
    date_path = str(Path.home()) + "/Documents/yajs/" + "/".join(date) # get the path for said date
    for i in listdir(date_path): # get a list of every file in the day's directory
        print(open(date_path+"/"+i).read()) # print the contents of everyday in the day's directory

def main():
    if len(argv) < 2:
        print(help_text)
        exit()
    if argv[1] == "new": arg_new()
    if argv[1] == "open": arg_open()
    if argv[1] == "day_view": arg_day_view()


if __name__ == "__main__":
    main()
