from time import *
present = time()
ctime(present)
present = ctime().split()
dt_today = present[1] + present[2] + present[4]
time_now = present[3][0:5]

class AlarmRinger():
    
    def __init__(self, timeStamps):
        while(True):
            present = ctime().split()
            dt_today = present[1] + present[2] + present[4]
            time_now = present[3][0:5]
            for i in timeStamps:
                if time_now == i[0] and dt_today == i[1]:
                    print("Alarm")
                    sleep(30)
                    print(i[2])
            sleep(50)
                

print(dt_today)
print(time_now)
timestamps = [["14:09", "Aug92022", "text1"], ["14:24","Aug92022", "text2"]]

bot = AlarmRinger(timestamps)
#896d9b313708907e9fb81231b93b8b10fec99cc4
