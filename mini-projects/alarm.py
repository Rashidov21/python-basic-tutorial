# pip install schedule
# https://pypi.org/project/schedule/
import schedule
# siz ko'rsatgan vaqtda siz ko'rsatgan funksiyani ishga tushirib beradi
import time
import winsound

hour = int(input("Enter a Hour :"))
minute = int(input("Enter a Minute: "))


def alarm():
    winsound.PlaySound('alarm.wav', winsound.SND_FILENAME)


schedule.every().day.at(f"{hour}:{minute}").do(alarm)
# schedule.every(10).seconds.do(alarm)
while True:
    schedule.run_pending()
    time.sleep(1)
