"""A vaccination calculator."""

__author__ = "730246800"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...

population = int(input("Population: "))
dosesAdmin = int(input("Doses administered: "))
dosesDay = int(input("Doses per day: "))
target = int(input("Target percent vaccinated: "))




finalTarget =  (population * target ) / 100 

finalDosesAdmin = dosesAdmin / 2 

finalTarget = finalTarget - finalDosesAdmin

finalDosesperDay = dosesDay / 2

finalTarget = round(finalTarget / finalDosesperDay)


finalDay = datetime.today() + timedelta(finalTarget)
finalDay = finalDay.strftime("%B %d, %Y")


print("We will reach " + str(target) + "% vaccination in "
 + str(finalTarget) + " days, which falls on " + 
  finalDay + ".") 
