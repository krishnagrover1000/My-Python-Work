#%%
#This Imports A Module Of A Calender
import calendar 
# %%
#This Function Prints Out The Letters Of The Week By The Lenth In The Parentahese
print(calendar.weekheader(3))
print()
#%%
#This Function Prints Out Zero Because For Python First Weekday is Monday And Number 0
print(calendar.firstweekday())
print()
#%%
#This Function Prints Out the Normal Calender Format (Year, Month Number, Weekheader)
print(calendar.month(2020, 9, w=3 ))
print()
# %%
#This Function Prints Out The Array Of The Days In One Week (Year, Month)
print(calendar.monthcalendar(2020, 9))
print()
# %%
#This Function Prints Out The Whole Year Calendar With The Given Year (Year)
print(calendar.calendar(2020))
print()
# %%
#This Function Prints Out Day of Week With Given Parameters (Year, Month, Day)
day_of_week = calendar.weekday(2020, 9, 27)
print(day_of_week)
print()

# %%
#This Function Prints Out A Boolean To The Given Parameters If Its A Leap Year (Year)
is_leap = calendar.isleap(2020)
print(is_leap)
print()
# %%
#This Function Prints Out The How many Leap Years Are In the Range Of Parameters (Year, Year)
how_many_leap_years = calendar.leapdays(2020,2040)
print(how_many_leap_years)
print()


# %%
