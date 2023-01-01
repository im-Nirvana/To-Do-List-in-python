# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 19:57:37 2022

@author: sini1002
"""
### Header Files or libraries to be imported

import csv
import pandas as pd
import datetime
from datetime import date


#### To do list App
def Home():
    print("Welcome to To Do List Program")
    print("1. Add a new task")
    print("2. Edit an existing task")
    print("3. Mark a task as complete")
    print("4. Delete an existing task")
    print("5. Set a reminder")
    

    
def Add_task():
    
    print("Add a task here")
#### Opening or creating a file
    with open("C:/Users/sini1002/Documents/Python Scripts/To Do List/To do list.csv", "a", newline="") as file:
        myfile = csv.writer(file)
        
## Writing the columns headers
       # myfile.writerow(["TaskNo.", "TaskName", "TargetDate", "TaskDate", "PercentageAch" ])

### Getting the no of tasks to be addded
        noOfTask = int(input("Enter the no. of task you want to enter : ")) 

### USing for loop to add tasks
        for i in range(noOfTask):
            Tno = int(input("Enter Task No. : "))
            Tnam = input("Enter the task name : ")
            userDate = input("Enter a date in YYYY-MM-DD format : ")
            year, month, day = map(int, userDate.split('-'))
            TargetDate = datetime.date(year, month, day)
            TaskDate = date.today()
            PerAch = int(input("Enetr Percentage of Task achieve by now (in numbers): "))
            ###myFile.writerow([edu, course, institute, year, marks])
            myfile.writerow([Tno, Tnam, TargetDate, TaskDate, PerAch])
            

            
        
    
    
    
    
def Edit_task():
    print("Edit a task here")
    
    
    
def cmp_task():
    print("Mark as Complete a task here")
    
    
def Del_task():
    print("Delete a task here")
    
    
def set_rem():
    print("Set Reminder")




    
# Main program
if __name__ == '__main__':
    Home()
    ch = int(input("Enter your Choice : "))
    
    if ch in(1,2,3,4,5):
        
        if ch == 1:
            Add_task()
            
        elif ch == 2:
            Edit_task()
            
        elif ch == 3:
            cmp_task()
            
        elif ch == 4:
            Del_task()
            
        elif ch == 5:
            set_rem()
            
    else :
        print("Invalid Input")
    