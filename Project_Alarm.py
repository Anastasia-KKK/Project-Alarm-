from datetime import datetime
from playsound import playsound

def validate_time(alarm_time): 
    if len(alarm_time) != 8: 
        return "Неверный формат будильника, попробуй снова"
    else:
        if int(alarm_time[0:2]) > 23: 
            return "Неверный формат часов, попробуй снова"
        elif int(alarm_time[3:5]) > 59: 
            return "Неверный формат минут, попробуй снова"
        elif int(alarm_time[6:8]) > 59: 
            return "Неверный формат секунд, попробуй снова"
        else:
            return "ok"
while True:
    alarm_time = input("Введи время будильника в формате HH:MM:SS \n Время будильника: ") 
    validate = validate_time(alarm_time) 
    if validate != "ok":
        print(validate)
    else:
        print(f"Будильник установлен на {alarm_time}...")
        break  
alarm_hour = int(alarm_time[0:2])
alarm_min = int(alarm_time[3:5])
alarm_sec = int(alarm_time[6:8])

while True:
    now = datetime.now() 
    current_hour = now.hour 
    current_min = now.minute
    current_sec = now.second 

    if alarm_hour == current_hour and alarm_min == current_min and alarm_sec == current_sec:
        print("Подъем!")
        playsound('D:\\Python\\.vscode\\ProjectAlarm\\1700916607_1700853777_1700550446_2681_r5_3mp4rt_3mp578266_457634.mp3')
        break
