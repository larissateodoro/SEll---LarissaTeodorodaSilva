#Módulo data e hora

import datetime
import pytz


# d = datetime.date(2016, 7, 24)
#print(d)

tday = datetime.date.today()
print(tday.weekday())
print(tday.isoweekday())

# weekday() - Segunda é 0 e domingo 6
# print(tday)

# isoweekday() - Segunda é 1 e domingo 7
# print(tday)


tdelta = datetime.timedelta(days=7)
print(tday + tdelta)

# date2 = date1 + timedelta
# timedelta = date1 + date2

bday = datetime.date(2016, 9, 24)
till_bday = bday - tday
print(till_bday.days)

t = datetime.time(9, 30, 45, 100000)
print(t.hour)

dt = datetime.datetime(2016, 7, 24, 12, 30, 45, 100000)
tdelta = datetime.timedelta(days=7)
print(dt+tdelta)

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.today()
dt_utcnow = datetime.datetime.today()

# print(dt_today)
# print(dt_now)
# print(dt_utcnow)

dt = datetime.datetime(2016, 7, 24, 12, 30, 45, tzinfo=pytz.UTC)
# print(dt)

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
# print(dt_utcnow)


dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
print(dt_mtn)

dt_mtn = datetime.datetime.now()

mtn_tz = pytz.timezone('US/Mountain')
dt_mtn = mtn_tz.localize(dt_mtn)
print(dt_mtn)

dt_east = dt_mtn.astimezone(pytz.timezone('US/Eastern'))
print(dt_east)

#print(dt_mtn.strftime('%B %d, %Y'))

dt_str = 'July 26, 2016'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)