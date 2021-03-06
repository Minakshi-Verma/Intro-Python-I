"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

l = len(sys.argv)

if l ==1:
  #User didn't specify any input
    month = datetime.now().month
    year = datetime.now().year
elif l == 2:
    #User didn't specify year
    month = int(sys.argv[1])
    year = datetime.now().year
elif l == 3:
    month = int(sys.argv[1])
    year = int(sys.argv[2]) 
else:
    #User provided faulty input
    print("usage: calendar.py [month] [year]")
    sys.exit[1] 

cal = calendar.TextCalendar() 

cal.prmonth(year, month)




# import sys
# import calendar
# from datetime import datetime

# # print(dir(datetime))
# # print(dir(calendar))
# # print(calendar.calendar())

# # tday = datetime.today()
# # print(tday)
# # print(calendar,datetime.now())

# # yy = int(input("[Enter year]: "))
# # mm = int(input("[Enter month]: "))
# # args = [yy, mm]

# # for arg in args:
#     # if no input is supplied, print current month
# if len(sys.argv)==0:   
#     print(datetime(datetime.today().year,datetime.today().month, 1))
#     #if one input value is provided(month), display input month calendar
# if len(sys.argv)==1:
#     mm = int(input("[Enter month]: "))
#     yy= 2020
# print(calendar.month(yy,mm))
#     #if 2 inputs are provided, render the calendar for that month and day
# if len(sys.argv)==2:
#     yy = int(input("[Enter year]: "))
#     mm = int(input("[Enter month]: "))
# print(calendar.month(yy,mm)) 
# # else:
# #     print("input are required")
# #     # break


# user_input = sys.argv
# month =user_input[1]
# year =user_input[2]
# print(month, year)
# print(user_input)


# currentMonth = datetime.now().month //display the current month number(not name)
# currentSecond= datetime.now().second
# currentMinute = datetime.now().minute
# currentHour = datetime.now().hour
# currentDay = datetime.now().day
# currentYear = datetime.now().year

# To display current month name in calendar
# print(datetime.now().strftime('%B')