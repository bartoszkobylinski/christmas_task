from datetime import datetime
from dateutil import relativedelta
from craiyon import Craiyon

def counting_time(current_date):
    christmas = [f"20{x}-12-24 00:00:00" for x in range(23,34)]
    current_date = current_date + ' 00:00:00'
    current_date = datetime.strptime(current_date, "%Y-%m-%d %H:%M:%S")
    for christmas_day in christmas:
        christmas_day = datetime.strptime(christmas_day, "%Y-%m-%d %H:%M:%S")
        r = relativedelta.relativedelta(christmas_day, current_date)
        print(f"until day {christmas_day} is: {type(r.years)} years, {r.months} months, {r.weeks} weeks and {r.days} days")

counting_time('2022-12-26')

my_birthday= datetime(1982,5,17,8,0,0)
NOW = datetime.today()
a = relativedelta.relativedelta(NOW, my_birthday)
print(a.days, a.years, a.months, a.weeks)

generator = Craiyon() # Instantiates the api wrapper
result = generator.generate("Photorealistic image of santa claus whith presents and candles")
result.save_images() # Saves the generated images to 'current working directory/generated', you can also provide a custom path


