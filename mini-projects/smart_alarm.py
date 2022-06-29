# Alarm

import datetime
import winsound


print(datetime.datetime.today().strftime("%H"))  # soat
print(datetime.datetime.today().strftime("%M"))  # minut
hour = int(input("Enter a Hour: "))
minute = int(input("Enter a Minute: "))
while True:
    if hour == int(datetime.datetime.today().strftime("%H")) and minute == int(datetime.datetime.today().strftime("%M")):
        print("Alarm Raised")
        winsound.PlaySound('alarm.wav', winsound.SND_FILENAME)
        break
    else:
        print("Alarm Not Raised")
        break


# freq = 100
# dur = 50

# loop iterates 5 times i.e, 5 beeps will be produced.
# for i in range(0, 5):
#     winsound.Beep(freq, dur)
#     freq += 100
#     dur += 50
