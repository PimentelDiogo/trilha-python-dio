from datetime import datetime
import pytz
#pip install pytz
data = datetime.now(pytz.timezone("Europe/Oslo"))
data2 = datetime.now(pytz.timezone("America/Sao_Paulo"))

print(data.astimezone(pytz.utc))  # converts to UTC timezone
print(data2.strftime("%Y-%m-%d %H:%M:%S"))  # formats output as YYYY-MM-DD HH:MM:SS

print(data)
print(data2)