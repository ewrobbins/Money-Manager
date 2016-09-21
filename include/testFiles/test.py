import datetime

today = datetime.datetime.today()
print datetime.date(today.year, today.month, today.day).strftime('%Y%m%d')