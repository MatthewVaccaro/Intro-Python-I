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

now = datetime.now()
year = now.year
month = now.month
returned_cal = []

## --> A better way of accomplishing the same thing without having to use sys <-- ##
# inputDate = input("Enter Date --- Example: 2,12 ").split(',')
# # No Input
# if len(inputDate[0]) == 0:
#   print(" 😔 No values Given 😔")
#   print((calendar.month_name[month], year))
#   monthMatrix = calendar.monthcalendar(year, month)
#   for weeks in monthMatrix:
#     print(weeks)
# # One Input ( No year )
# elif len(inputDate) == 1:
#   print('{}, {}'.format(calendar.month_name[int(inputDate[0])], year))
#   monthMatrix = calendar.monthcalendar(year, int(inputDate[0]))
#   for weeks in monthMatrix:
#     print(weeks)
# # Two inputs(Month & Year)
# elif len(inputDate) == 2:
#   print('{}, {}'.format(calendar.month_name[int(inputDate[0])], int(inputDate[1])))
#   monthMatrix = calendar.monthcalendar(int(inputDate[1]), int(inputDate[0]))
#   for weeks in monthMatrix:
#     print(weeks)
# # Entered more then 2 digits
# else:
#   print("Incorrect Information Added")

if len(sys.argv) > 3:
    print("Please enter month and date arguments only")
if len(sys.argv) == 3:
    month = int(sys.argv[1])
    year = int(sys.argv[2])
elif len(sys.argv) == 2:
    month = int(sys.argv[1])

cal_values = calendar.monthcalendar(year, month)
display_month = calendar.month_name[month]

print("{} {}".format(display_month,year ))
for week in cal_values:
    print(week)