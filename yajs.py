#!/usr/bin/env python3

from sys import argv
from os import mkdir, makedirs, listdir
from os.path import exists, join
from time import localtime, strftime, sleep
from pathlib import Path
import subprocess

def path_creation(path):
    if exists(path) == True:
        return True
    else:
        makedirs(path)
        path_creation(path)

def year_month_day(date):
    year = date.split(",")[1].replace(" ", "")
    day = date.split(",")[0].split(" ")[1]
    month = date.split(",")[0].split(" ")[0]
    return [year, month, day]

def arg_new():
    udate = argv[2]
    date = year_month_day(argv[2])

    if len(argv) == 4:
        title = argv[3]
    else:
        title = ""


    date_path = str(Path.home()) + "/Documents/yajs/" + "/".join(date)
    path_creation(date_path)
    right_now = strftime("%H-%M", localtime())
    if title != "":
        specific_path = date_path + "/" + right_now + " - " + title + ".org"
    else:
        specific_path = date_path + "/" + right_now + ".org"
    open(specific_path, 'w').write("* " + udate + " " + right_now + " : \n")
    subprocess.call(["emacs", specific_path])

def arg_open():
    date = year_month_day(argv[2])
    date_path = str(Path.home()) + "/Documents/yajs/" + "/".join(date)
    incrementer = 0
    for i in listdir(date_path):
        print(str(incrementer + 1) + ". " + i)
        incrementer+=1

    choice_n = int(input("Open: "))-1
    choice = listdir(date_path)[choice_n]
    print()
    for i in list(open(date_path + "/" + choice).read()):
        print(i, end="")
        sleep(0.004)

def main():
    if argv[1] == "new": arg_new()
    if argv[1] == "open": arg_open()


if __name__ == "__main__":
    main()
