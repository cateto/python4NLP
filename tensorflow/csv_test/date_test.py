import datetime
start_date = datetime.date(2021,6,1)
end_date = datetime.date(2021,6,30)
delta = datetime.timedelta(days=1)

while start_date <= end_date:
    print(start_date)
    start_date += delta