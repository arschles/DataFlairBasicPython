import time
import datetime

class AlarmClock:
    def __init__(self):
        pass

    def set_alarm(self, user_time):
        while True:
            time.sleep(1)
            current_time = datetime.datetime.now()
            now = current_time.strftime("%H:%M:%S")
            print(user_time['time'])
            print(now)
            if now == user_time['time']:
                print("Time to Wake Up")
                break

if __name__ == "__main__":
    print("AlarmClock")
