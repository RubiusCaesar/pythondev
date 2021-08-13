# Goals:
# 1. Create dates using year, month, and day as arguments
# 2. Create a date using datetime.now()
# 3. Parse a date from a string using strptime
# 4. Render a date as a string using strftime (inverse of goal 3)

# Datetime represents an object storing information about time.
# GOAL 1. datetime comes installed with python. We are importing the datetime object from the datetime module below.
from datetime import time
from datetime import date
from datetime import datetime

# GOAL 2. We create a new datetime object and store it in the variable birthday.
# The object is given three ints, year, month and day, which are sent to the class constructor and create an instance of datetime which we store in our variable.
# If we wanted we could pass additional arguments to include the time as well.
birthday = datetime(2000, 5, 2)
print(birthday)
# The datetime weekday() function finds the day of the week for a specific date.
# The return value follows standard index prodedure, with 0 representing Monday, and 6 representing Sunday
print(birthday.weekday())

# GOAL 3. datetime.now() is a datetime method that returns a datetime instance for the current time, down to the milisecond.
# Useful if we want to determine the exact time some line of code is ran
right_now = datetime.now()
print(right_now)
# datetime objects allow us to easily find the distance between two points in time.
# While we can only subtract datetime objects, this allows to to accurately and easily determine the amount of time between two points
# When we run an operation like this we get a timedelta object which represents the change(delta) in time. Attribute structure is exactly like nomral datetime objects
time_passed = datetime(2018, 1, 1) - datetime(2017, 1, 1)
time_since_birth = datetime.now() - birthday
print(time_since_birth)

# GOAL 4. The strptime() methods allows us to parse a string into a datetime object. The p stands for parse.
# The method takes two arguements, the first being the string which we wish to parse into a datetime object, and the second,
# a format string to tell python where each value of the datetime instance is in the string. Formatting characters (expressed as %char)
# for this method can be found on the python docs.
parsed_date = datetime.strptime('Jan 15, 2018', '%b %d, %Y')
print(parsed_date)

# GOAL 5. The strftime method allows us to turn specific parts of a datetime instance and turn them into a string. Essentially the inverse of the strptime() method
# It works very similar to the strptime() method, and also requires two arguments, a datetime object to pull information from, and a formatting string.
date_string = datetime.strftime(datetime.now(), '%b %d, %Y')
print(date_string)

# BONUS INFO:
# In addition to just the datetime object, there are individual classes within the datetime module that allows users to create objects
# that store just date information or just the time information. These classes are called date and time respectively.
today = date.today()
print(today)
# The two functions below may prove useful. The isocalendar function returns a named tuple object with three components: year, week, and weekday.
# The isoweekday function works the exact same as the weekday function, except that it measures the days from 1-7 not 0-6
print(today.isocalendar())
print(today.isoweekday())

right_now = time(11, 47, 0)
print(right_now)
# Both classes have several unique methods as well as those featured in the datetime object.
# As mentioned previously the module also includes timedelta objects, which measure change in time, but also tzinfo and timezone classes.
# These classes store useful information about time zones and allow programmers felxibility with time display.
