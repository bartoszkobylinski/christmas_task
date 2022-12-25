from datetime import datetime
from dateutil import relativedelta

def counting_time(current_date):
    christmas = [f"20{x}-12-24 00:00:00" for x in range(23,34)]
    print(christmas)
    current_date = current_date + ' 00:00:00'
    
    current_date = datetime.strptime(current_date, "%Y-%m-%d %H:%M:%S")
    print(current_date)
    for christmas_day in christmas:
        christmas_day = datetime.strptime(christmas_day, "%Y-%m-%d %H:%M:%S")
        time_delta = christmas_day - current_date
        print(f"time_delat is : {time_delta}")
        r = relativedelta.relativedelta(christmas_day, current_date)
        total_months = r.years * 12 + r.months 
        total_days = r.days
        
        print(total_months)
        print(total_days)

counting_time('2022-03-24')
