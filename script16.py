import datetime
today=datetime.date.today()
print(today.strftime("%d/%m/%Y"))
#dd/mm/yyyy(time module)
Aday=datetime.date(2017,12,16)
print(Aday.strftime("%d/%m/%Y"))
#someday in format str
today=today-datetime.timedelta(days=1)
print(today.strftime("%d/%m/%Y"))
#Date replace
today=today.replace(day=today.day+1)
print(today.strftime("%d/%m/%Y"))

