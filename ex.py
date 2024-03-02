from datetime import datetime

today = '2006-04-01'



obj = datetime.strptime(today, r'%Y-%m-%d')
ts = int(obj.timestamp())

print(ts)