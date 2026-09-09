import time
import winsound  # Windows only, use 'playsound' for cross-platform

alarm_time = input("Set alarm (HH:MM): ")

while True:
    current = time.strftime("%H:%M")
    if current == alarm_time:
        print("Wake up!")
        # winsound.Beep(1000, 5000)  # Uncomment for sound
        break
    time.sleep(30)