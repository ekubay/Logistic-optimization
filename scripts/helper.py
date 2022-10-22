import pandas as pd

from datetime import datetime
import holidays
from geopy import distance

# is weekdend or not function
def isWeekend(df_date_str):
    datetime_object = datetime.strptime(df_date_str, '%Y-%m-%d %H:%M:%S')
    # print(datetime_object.weekday())
    if datetime_object.weekday() < 5:
         return 0
    else:  
        return 1

# holyday derivation
def isHoliday(df):
    ng_holidays = holidays.country_holidays('NG')
    try:
        dt = datetime.strptime(df, '%Y-%m-%d %H:%M:%S').date()
        if dt in ng_holidays:
            return 1
        else: return 0
    except Exception as e:
        return 0